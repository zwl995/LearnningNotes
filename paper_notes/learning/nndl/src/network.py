import random
import numpy as np

from loss_functions import MeanSquareLoss
from loss_functions import CrossEntropyLoss
from activation_functions import Sigmoid
from mnist_loader import load_data


class NetworkConfig(object):
  def __init__(self, batch_size, learning_rate, loss_func_type="", activation_func_type="") -> None:
    super().__init__()
    self.learning_rate = learning_rate
    self.loss_func_type = loss_func_type
    self.activation_func_type = activation_func_type
    self.batch_size = batch_size


class Network(object):
  def __init__(self, sizes, config) -> None:
    self._num_layers = len(sizes)
    self._sizes = sizes
    self._weights = [np.random.randn(y, x) / np.sqrt(x) for x, y in zip(sizes[ : -1], sizes[1 : ])]
    self._biases = [np.random.randn(x, 1) for x in sizes[1 : ]]
    self.learning_rate = config.learning_rate
    self.batch_size = config.batch_size
    self.activation_func = Sigmoid()
    if config.loss_func_type == 'MeanSquareLoss':
      print("Using MeanSquareLoss")
      self.loss_func = MeanSquareLoss()
    else:
      print("Using CrossEntropyLoss")
      self.loss_func = CrossEntropyLoss()

  def save_network(self) -> None:
    for index in range(self._num_layers - 1):
      np.savetxt('weight'+str(index), self._weights[index])
      np.savetxt('bias'+str(index), self._biases[index])
  
  def load(self):
    for index in range(self._num_layers - 1):
      self._weights[index] = np.loadtxt('weight'+str(index)).reshape(\
        self._weights[index].shape)
      self._biases[index] = np.loadtxt('bias'+str(index)).reshape(\
        self._biases[index].shape)

  def run(self, training_data, epochs, test_data=None):
    self.__stochastic_gradient_descent(training_data, epochs, test_data)

  def __training_feedforward(self, input):
    activation_output = [np.zeros((x, 1)) for x in self._sizes]
    weighted_sum = [np.zeros((x, 1)) for x in self._sizes[1 : ]]

    activation_output[0] = input
    i = 0

    for weight, bias in zip(self._weights[:], self._biases[:]):
      weighted_sum[i] = (weight.dot(activation_output[i])).reshape(bias.shape) + bias
      activation_output[i + 1]= self.activation_func.evaluate(weighted_sum[i])
      i += 1
    return weighted_sum, activation_output

  def __test_feedforward(self, a):
    for weight, bias in zip(self._weights, self._biases):
      a = self.activation_func.evaluate(weight.dot(a).reshape(bias.shape) + bias)

    return a

  def __backpropagation(self, z, a, y, nabla_b, nabla_w):
    residuals = [np.zeros((x, 1)) for x in self._sizes[1 : ]]

    # residuals[self._num_layers - 2] = \
    #   self.loss_func.derivative(a[self._num_layers - 1], y) * \
    #     self.activation_func.derivative(z[self._num_layers - 2])
    delta = \
      self.loss_func.delta(z[self._num_layers - 2], y, self.activation_func)
    # print("res: {0}".format(residuals[self._num_layers - 2]))

    i = self._num_layers - 2
    for weight, bias in zip(self._weights[::-1], self._biases[::-1]):
      # if i - 1 >= 0:
      #   residuals[i - 1] = (weight.T).dot(residuals[i]) * self.activation_func.derivative(z[i - 1])
      # Only for MeanSquareLoss
      # nabla_w[i] += residuals[i].dot(a[i].reshape(1, a[i].size))
      # nabla_b[i] += residuals[i]

      nabla_w[i] += delta.dot(a[i].reshape(1, a[i].size))
      nabla_b[i] += delta
      if i - 1 >= 0:
        delta = weight.transpose().dot(delta) * \
                           self.activation_func.derivative(z[i - 1])
      i -= 1

    # return nabla_w, nabla_b

  def __update_mini_batch(self, mini_batch):
    nabla_b = [np.zeros((bias.shape)) for bias in self._biases]
    nabla_w = [np.zeros((weight.shape)) for weight in self._weights]

    for x, y in mini_batch:
      z, a = self.__training_feedforward(x)
      self.__backpropagation(z, a, y, nabla_b, nabla_w)
      # print(nabla_b)

    m = len(mini_batch)
    self._weights = [weight - self.learning_rate / m * dw for weight, dw in zip(self._weights, nabla_w)]
    self._biases = [bias - self.learning_rate / m * db for bias, db in zip(self._biases, nabla_b)]

  def __stochastic_gradient_descent(self, training_data, epochs, test_data=None):
    num_training_data = len(training_data)
    print("line 102: num training data: {0}".format(num_training_data))

    if test_data:
      num_test = len(test_data)

    for count_epoch in range(epochs):
      random.shuffle(training_data)
      mini_batches = [training_data[index : index + self.batch_size] \
                      for index in range(0, num_training_data, self.batch_size)]

      for mini_batch in mini_batches:
        self.__update_mini_batch(mini_batch)

      if test_data:
        print("Epoch {0}: {1} / {2}".format(
          count_epoch, self.__evaluate(test_data), num_test))
      else:
        print("Epoch {0} complete".format(count_epoch))

  def __evaluate(self, test_data):
    predicts = [(np.argmax(self.__test_feedforward(x)), y) for (x, y) in test_data]
    return sum(int(x == y) for (x, y) in predicts)