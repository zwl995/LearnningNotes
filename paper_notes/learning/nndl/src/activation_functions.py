import numpy as np

class ActivationFunction(object):
  def __init__(self) -> None:
      super().__init__()

  def evaluate(self, z):
    pass

  def derivative(self, z):
    print("PASS")
    pass


class Sigmoid(ActivationFunction):
  def __init__(self):
    ActivationFunction.__init__(self)

  def evaluate(self, z):
    return 1.0 / (1.0 + np.exp(-z))

  def derivative(self, z):
    act_sum = self.evaluate(z)
    return act_sum * (1 - act_sum)