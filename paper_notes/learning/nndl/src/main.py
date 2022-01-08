from numpy import test
from mnist_loader import load_data
from network import Network
from network import NetworkConfig

def mnist_data_to_list(mnist_data):
  images = mnist_data[0]
  labels = mnist_data[1]

  mnist_data_list = []
  for img, label in zip(images, labels):
    datum = (img, label)
    mnist_data_list.append(datum)

  return mnist_data_list

if __name__ == '__main__':
  training_data, validation_data, test_data = load_data()
  training_data_list = mnist_data_to_list(training_data)
  test_data_list = mnist_data_to_list(test_data)

  num_epochs = 30
  config = NetworkConfig(batch_size=50, learning_rate=0.8, \
                         activation_func_type="Sigmoid", \
                         loss_func_type = "MeanSquareLoss")
                        #  loss_func_type = "CrossEntropyLoss")

  network = Network([784, 100, 10], config)
  network.load()
  network.run(training_data_list, num_epochs, test_data_list)
  network.save_network()
  # network.run(training_data_list, num_epochs)
