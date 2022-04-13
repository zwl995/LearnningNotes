from turtle import forward
import torch
from torch import batch_norm, nn
from torch.nn import functional as F

batch_size, num_steps = 32, 35
train_iter, vocab = d2l.load_data_time_machine(batch_size, num_steps)

num_hiddens = 256
rnn_layer = nn.RNN(len(vocab), num_hiddens)

state = torch.zeros((1, batch_size, num_hiddens))
X = torch.rand(size=(num_steps, batch_size, len(vocab)))
Y, state_new = rnn_layer(X, state)


class RNNModel(nn.Module):
  def __init__(self, rnn_layer, vocab_size, **kwargs) -> None:
    super(RNNModel, self).__init__(**kwargs)
    self.rnn = rnn_layer
    self.vocab_size = vocab_size
    self.num_hiddens = self.rnn_hidden_size
    # 如果 RNN 是双向的, num_directions 应该是 2, 否则应该是 1
    if not self.rnn.bidirectional:
      self.num_directions = 1
      self.linear = nn.Linear(self.num_hiddens, self.vocab_size)
    else:
      self.num_directions = 2
      self.linear = nn.Linear(self.num_hiddens * 2, self.vocab_size)

  def forward(self, inputs, state):
    X = F.one_hot(inputs.T.long(), self.vocab_size)
    X = X.to(torch.float32)
    Y, state = self.rnn(X, state)
    # 全连接层首先将Y的形状改为(时间步数*批量大小, 隐藏单元数)
    # 它的输出形状是 (时间步数*批量大小, 词表大小)
    output = self.linear(Y.reshape((-1, Y.shape[-1])))
    return output, state

  def begin_state(self, device, batch_size=1):
    if not isinstance(self.rnn, nn.LSTM):
      return torch.zeros((self.num_directions * self.rnn.num_layers,
                          batch_size, self.num_hiddens), device=device)
    else:
      return (torch.zeros((self.num_directions * self.rnn.num_layers,
                           batch_size, self.num_hiddens), device=device),
                           torch.zeros((self.num_directions * self.rnn.num_layers,
                           batch_size, self.num_hiddens), device=device))


net = RNNModel(rnn_layer, vocab_size=len(vocab))