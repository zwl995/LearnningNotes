import numpy as np

class LossFunction(object):
  def __init__(self) -> None:
      super().__init__()

  def evaluate(self, x, y):
    pass

  def derivative(self, x, y):
    pass

  def delta(self, x, y, activation_func):
    pass


class MeanSquareLoss(LossFunction):
  def __init__(self) -> None:
    LossFunction.__init__(self)

  def evaluate(self, x, y):
    return np.square(x - y)

  def derivative(self, x, y):
    return x - y

  def delta(self, x, y, activation_func):
    return self.derivative(activation_func.evaluate(x), y) * activation_func.derivative(x)


class CrossEntropyLoss(LossFunction):
  def __init__(self) -> None:
    LossFunction.__init__(self)

  def evaluate(self, x, y):
    return -y * np.log(x) + (1 - y) * np.log(1 - x)

  def derivative(self, x, y):
    return (x - y) / (x * (1 - x))

  def delta(self, x, y, activation_func):
    return activation_func.evaluate(x) - y