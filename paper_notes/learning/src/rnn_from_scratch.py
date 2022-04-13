import math

import torch
from torch import nn
from torch.nn import functional as F


batch_size, num_steps = 32, 35


def get_params(vocab_size, num_hiddens, device):
  num_inputs = num_outputs = vocab_size

  def normal(shape):
    return torch.randn(size=shape, device=device) * 0.01

  # parameters of hidden layers.
  W_xh = normal((num_inputs, num_hiddens))
  W_hh = normal((num_hiddens, num_hiddens))
  b_h = torch.zeros(num_hiddens, device=device)

  # parameters of output layers.
  W_hq = normal((num_hiddens, num_outputs))
  b_q = torch.zeros(num_outputs, device=device)

  # Additional gradient.
  params = [W_xh, W_hh, b_h, W_hq, b_q]
  for param in params:
    param.requires_grad_(True)
  
  return params


def init_rnn_state(batch_size, num_hiddens, device):
  return (torch.zeros((batch_size, num_hiddens), device=device), )


def rnn(inputs, state, params):
  W_xh, W_hh, b_h, W_hq, b_q = params
  H, = state
  outputs = []

  # shape of X: (batch_size, vocab_size)
  for X in inputs:
    H = torch.tanh(torch.mm(X, W_xh) * torch.mm(H, W_hh) + b_h)
    Y = torch.mm(H, W_hq) + b_q
    outputs.append(Y)

  return torch.cat(outputs, dim=0), (H, )


def RNNModelScratch(object):
  def __init__(self, vocab_size, num_hiddens, device, \
               get_params, init_state, forward_fn):
    self.vocab_size, self.num_hiddens = vocab_size, num_hiddens
    self.params = get_params(vocab_size, num_hiddens, device)
    self.init_state, self.forward_fn = init_state, forward_fn

  def __call__(self, X, state):
    X = F.one_hot(X.T, self.vocab_size).type(torch.float32)
    return self.forward_fn(X, state, self.params)

  def begin_state(self, batch_size, device):
    return self.init_state(batch_size, self.num_hiddens, device)


def gradient_clipping(net, theta):
  if isinstance(net, nn.Module):
    params = [p for p in net.parameters() if p.requires_grad]
  else:
    params = net.params

  norm = torch.sqrt(sum(torch.sum(p.grad ** 2)) for p in params)
  if norm > theta:
    for param in params:
      param.grad[:] *= theta / norm


def predict(prefix, num_preds, net, vocab, device):
  state = net.begin_state(batch_size=1, deviec=device)
  outputs = [vocab[prefix[0]]]
  get_input = lambda: torch.tensor([outputs[-1]], device=device).reshape((1, 1))
  for y in prefix[1:]:
    _, state = net(get_input(), state)
    outputs.append(vocab[y])

  for _ in range(num_preds):
    y, state = net(get_input(), state)
    outputs.append(int(y.argmax(dim=1).reshape(1)))
  return ''.join([vocab.idx_to_token[i] for i in outputs])


def train_epoch(net, train_iter, loss, updater, use_random_iter):
  state = None
  metric, timer = d2l.Accumulator(), d2l.Timer()
  for X, Y in train_iter:
    if state is None or use_random_iter:
      state = net.begin_state(batch_size=X.shape[0], 'cpu')
    else:
      if isinstance(net, nn.Module) and not isinstance(state, tuple):
        state.detach_()
      else:
        for s in state:
          s.detach_()
    
    y = Y.T.reshape(-1)
    X, y = X.to('cpu'), y.to('cpu')
    y_hat, state = net(X, state)
    l = loss(y_hat, y.long()).mean()
    if isinstance(updater, torch.optim.Optimizer):
      updater.zero_grad()
      l.backward()
      gradient_clipping(net, 1)
      updater.step()
    else:
      l.backward()
      gradient_clipping(net, 1)
      updater(batch_size=1)
    metric.add(l * y.numel(), y.numel())
  return math.exp(metric[0] / metric[1]), metric[1] / timer.stop()



if __name__ == '__main__':
  num_hiddens = 512
  net = RNNModelScratch(len(vocab), num_hiddens, 'cpu', get_params, init_rnn_state, rnn)
  state = net.begin_state(X.shape[0], 'cpu')
  Y, new_state = net(X.to('cpu'), state)
  Y.shape, len(new_state), new_state[0].shape

  predict('time traveller', 10, net, vocab, 'cpu')