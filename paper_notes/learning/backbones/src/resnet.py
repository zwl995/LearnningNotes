from inspect import stack
from turtle import forward
from numpy import append
import torch
from torch import nn


class ShallowResidualBlock(nn.Module):
  def __init__(self, in_channels, out_channels, use_conv1D=False, strides=1) -> None:
    super(ShallowResidualBlock, self).__init__()
    if use_conv1D:
      self.conv1D = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=strides)
    else:
      self.conv1D = None
    self.conv1 = nn.Conv2d(in_channels, out_channels, 3, stride=strides)
    self.conv2 = nn.Conv2d(out_channels, out_channels, 3)
    
    self.bn1 = nn.BatchNorm2d(out_channels)
    self.bn2 = nn.BatchNorm2d(out_channels)
    self.relu = nn.ReLU()

  def forward(self, X):
    Fx = self.relu(self.bn1(self.conv1(X)))
    Fx =           self.bn2(self.conv2(Fx))

    if self.conv1D != None:
      X = self.conv1D(X)

    return self.relu(Fx + X)


class DeepResidualBlock(nn.Module):
  def __init__(self, in_channels, out_channels, use_conv1D=False, strides=1) -> None:
    super(DeepResidualBlock, self).__init__()
    self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=strides)
    self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3)
    self.conv3 = nn.Conv2d(out_channels, 4 * out_channels, kernel_size=1)

    if use_conv1D == True:
      self.conv1D = nn.Conv2d(in_channels, 4 * out_channels, kernel_size=1, stride=strides)
    else:
      self.conv1D = None

    self.relu = nn.ReLU()
    self.batch_norm1 = nn.BatchNorm2d(out_channels)
    self.batch_norm2 = nn.BatchNorm2d(out_channels)
    self.batch_norm3 = nn.BatchNorm2d(4 * out_channels)

  def forward(self, X):
    Fx = self.relu(self.batch_norm1(self.conv1(X)))
    Fx = self.relu(self.batch_norm2(self.conv2(Fx)))
    Fx =           self.batch_norm3(self.conv3(Fx))
    
    if self.conv1D != None:
      X = self.conv1D(X)

    return self.relu(Fx + X)


def resnet_block(in_channels, out_channels, num_residuals, net_type='shallow', first_block=False):
  blocks = []
  for i in range(num_residuals):
    if i == 0 and not first_block:
      # For each residual block, if it is not the first block in ResNet but it
      # is the first residual block, we should use a 1*1 convolution layer to 
      # match the size such that 'x.shape = Fx.shape', and the feature map is
      # also downsampled; otherwise, the shape of x is the same as the shape of
      # Fx.
      if net_type == 'shallow':
        blocks.append(ShallowResidualBlock(in_channels, out_channels, True, strides=2))
      else:
        blocks(append(DeepResidualBlock(in_channels, out_channels, True, strides=2)))
    else:
      if net_type == 'shallow':
        blocks.append(ShallowResidualBlock(out_channels, out_channels))
      else:
        blocks.append(DeepResidualBlock(out_channels, out_channels))

  return blocks


class ShallowResNet(nn.Module):
  def __init__(self, in_channels=3, out_channels=10, depth=18) -> None:
    super(ShallowResNet, self).__init__()
    if depth == 18:
      res_block_nums=[2, 2, 2, 2]
    elif depth == 34:
      res_block_nums=[2, 2, 2, 2]
    else:
      print("Depth must be 18 or 34 for a shallow resnet!")
      return None
        
    self.block1 = nn.Sequential([nn.Conv2d(in_channels, 64, kernel_size=7, stride=2, padding=3),
                                 nn.BatchNorm2d(64),
                                 nn.ReLU(),
                                 nn.MaxPool2d(kernel_size=3, stride=2, padding=1)])
    self.res_block1 = nn.Sequential(*resnet_block(64, 64, res_block_nums[0], 'shallow', True))
    self.res_block2 = nn.Sequential(*resnet_block(64, 128,  'shallow', res_block_nums[1]))
    self.res_block3 = nn.Sequential(*resnet_block(128, 256, 'shallow', res_block_nums[2]))
    self.res_block4 = nn.Sequential(*resnet_block(256, 512, 'shallow', res_block_nums[3]))

    self.global_avg_pool = nn.AdaptiveAvgPool2d((1, 1))
    self.flatten = nn.Fatten(start_dim=1, end_dim=-1)
    self.fc = nn.Linear(512, out_channels)


  def forward(self, X):
    X = self.block1(X)
    X = self.res_block1(X)
    X = self.res_block2(X)
    X = self.res_block3(X)
    X = self.res_block4(X)
    X = self.flatten(self.global_avg_pool(X))
    X = self.fc(X)
    return X


class DeepResNet(nn.Module):
  def __init__(self, in_channels, out_channels, depth=50) -> None:
    super(DeepResNet, self).__init__()
    if depth == 50:
      res_block_nums = [3, 4, 6, 3]
    elif depth == 101:
      res_block_nums = [3, 4, 23, 3]
    elif depth == 152:
      res_block_nums = [3, 8, 36, 3]
    else:
      print("Depth must be 50 or 101 or 152 for a deep resnet!")
      return None

    self.block1 = nn.Sequential([nn.Conv2d(in_channels, 64, kernel_size=7, stride=2, padding=3),
                                 nn.BatchNorm2d(64),
                                 nn.ReLU(),
                                 nn.MaxPool2d(kernel_size=3, stride=2, padding=1)])
    self.res_block1 = nn.Sequential(*resnet_block( 64, 64, res_block_nums[0], 'deep', True))
    self.res_block2 = nn.Sequential(*resnet_block( 64, 128, 'deep', res_block_nums[1]))
    self.res_block3 = nn.Sequential(*resnet_block(128, 256, 'deep', res_block_nums[2]))
    self.res_block4 = nn.Sequential(*resnet_block(256, 512, 'deep', res_block_nums[3]))

    self.global_avg_pool = nn.AdaptiveAvgPool2d((1, 1))
    self.flatten = nn.Fatten(start_dim=1, end_dim=-1)
    self.fc = nn.Linear(4 * 512, out_channels)


  def forward(self, X):
    X = self.block1(X)
    X = self.res_block1(X)
    X = self.res_block2(X)
    X = self.res_block3(X)
    X = self.res_block4(X)
    X = self.flatten(self.global_avg_pool(X))
    X = self.fc(X)
    return X