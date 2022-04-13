import collections
from lib2to3.pgen2 import token
from operator import index
import re
from d2l import torch as d2l


def read_time_machine():
  with open(d2l.download('time_machine'), 'r') as f:
    lines = f.readlines()
  return [re.sub('[^A-Za-z]+', ' ', line).strip().lower() for line in lines]


def tokenize(lines, token='word'):
  if token == 'word':
    return [line.split() for line in lines]
  elif token == 'char':
    return [list(line) for line in lines]
  else:
    print("Error: unknown token type: " + token)


class Vocab(object):
  def __init__(self, tokens=None, min_freq=0, reserved_tokens=None) -> None:
    if tokens is None:
      tokens = []
    if reserved_tokens is None:
      reserved_tokens = []
    # Sort according to the frequency.
    counter = count_corpus(tokens)
    self._token_freqs = sorted(counter.items(), key=lambda x: x[1],
                               reverse=True)
    # Index of unknown token is 0
    self.idx_to_token = ['<unk>'] + reserved_tokens
    self.token_to_idx = {token: idx for idx, token in enumerate(self.idx_to_token)}
    self.idx_to_token, self.token_to_idx = [], dict()
    for token, freq in self._token_freqs:
      if freq < min_freq:
        break
      if token not in self.token_to_idx:
        self.idx_to_token.append(token)
        self.token_to_idx[token] = len(self.idx_to_token) - 1

  def __len__(self):
    return len(self.idx_to_token)

  def __getitem__(self, tokens):
    if not isinstance(tokens, (list, tuple)):
      return self.token_to_idx.get(tokens, self.unk)
    return [self.__getitem__(token) for token in tokens]

  def to_tokens(self, indices):
    if not isinstance(indices, (list, tuple)):
      return self.idx_to_token[indices]
    return [self.idx_to_token[index] for index in indices]

  @property
  def unk(self):
    return 0

  @property
  def token_freqs(self):
    return self._token_freqs

def count_corpus(tokens):
  if len(tokens) == 0 or isinstance(tokens[0], list):
    tokens = [token for line in tokens for token in line]
  return collections.Counter(tokens)


def load_corpus_time_machine(max_tokens=-1):
  lines = read_time_machine()
  tokens = tokenize(lines, 'char')
  vocab = Vocab(tokens)
  corpus = [vocab[token] for line in tokens for token in line]
  if max_tokens > 0:
    corpus = corpus[:max_tokens]
  return corpus, vocab


d2l.DATA_HUB['time_machine'] = (d2l.DATA_URL + 'timemachine.txt',
                                '090b5e7e70c295757f55df93cb0a180b9691891a')

lines = read_time_machine()
print(f'# 文本总行数: {len(lines)}')
print(lines[0])
print(lines[10])

tokens = tokenize(lines)
# for i in range(11):
#   print(tokens[i])

# vocab = Vocab(tokens)
# print(list(vocab.token_to_idx.items()))[:10]
corpus, vocab = load_corpus_time_machine()
print(len(corpus))
print(len(vocab))

