from typing import ParamSpecArgs
import torch
from torch import device, nn
from d2l import torch as d2l

batch_size, num_steps = 32, 35
train_iter, vocab = d2l.load_data_time_machine(batch_size, num_steps)


def get_lstm_params(vocab_size, num_hiddens, device):
  num_inputs = num_outputs = vocab_size
  
  def normal(shape):
    return torch.randn(size=shape, device=device)
  
  def three():
    return (normal((num_inputs, num_hiddens)),
            normal((num_hiddens, num_hiddens)),
            torch.zeros(num_hiddens, device=device))

  W_xi, W_hi, b_i = three() # input gate
  W_xf, W_hf, b_f = three() # forget gate
  W_xo, W_ho, b_o = three() # output gate
  W_xc, W_hc, b_c = three() # candidate memory unit
  
  # output parameters.
  W_hq = normal((num_hiddens, num_outputs))
  b_q = torch.zeros(num_outputs, device=device)

  params = [W_xi, W_hi, b_i, W_xf, W_hf, b_f, W_xo, b_o, W_xc, W_hc, b_c, W_hq, b_q]
  for param in params:
    param.requires_grad_(True)
  return params


def init_lstm_state(batch_size, num_hiddens, device):
  return (torch.zeros((batch_size, num_hiddens), device=device),
          torch.zeros((batch_size, num_hiddens), device=device))


def lstm(inputs, state, params):
  [W_xi, W_hi, b_i, W_xf, W_hf, b_f, W_xo, W_ho, b_o, W_xc, W_hc, b_c,
   W_hq, b_q] = params
  (H, C) = state
  outputs = []
  for X in inputs:
    I = torch.sigmoid((X * W_xi) + (H * W_hi) + b_i)
    F = torch.sigmoid((X * W_xf) + (H * W_hf) + b_f)
    O = torch.sigmoid((X * W_xo) + (H * W_ho) + b_o)
    C_tilde = torch.tanh((X * W_xc) + (H * W_hc) + b_c)
    C = F * C + I * C_tilde
    H = O * torch.tanh(C)
    Y = H * W_hq + b_q
    outputs.append(Y)
  return torch.cat(outputs, dim=0), (H, C)


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
