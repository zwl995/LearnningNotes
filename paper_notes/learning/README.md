# Papers in Deep Learning

## Papers to Read

### 1. Backbone/Classical NN architectures

- [x] [**IEEE 1998** | **LeNet**] [GradientBased Learning Applied to Document Recognition](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf)

- [ ] [**ECCV 2014** | **SPP-Net**] [Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition](https://arxiv.org/pdf/1406.4729.pdf)

- [ ] [**CVPR 2015** | **GoogleNet**] [Going deeper with convolutions](https://arxiv.org/pdf/1409.4842.pdf)

- [x] [**ICLR 2015** | **VGG**] [VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION](https://arxiv.org/pdf/1409.1556.pdf) ([**[Reading Note](backbones/VGG.md) | [Implementation(Up-to-date)]()**])

- [x] [**CVPR 2016** | **ResNet**] [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf) ([**[Reading Note](backbones/resnet.md) | [Implementation](backbones/src/resnet.py)**])

- [ ] [**ECCV 2016** | **Follow-up of ResNet**] [Identity mappings in deep residual networks](https://arxiv.org/pdf/1603.05027.pdf)

- [ ] [**2016**] [Layer normalization]()

- [ ] [**NeuIPS 2017** | **Transformer**] [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)

- [ ] [**ICCV 2021 Best Paper** | **[Github](https://github.com/microsoft/Swin-Transformer)**] [Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/pdf/2103.14030.pdf)

- [ ] [**CVPR 2022** | **[Github](https://github.com/microsoft/unilm)**] [DeepNet: Scaling Transformers to 1,000 Layers](https://arxiv.org/pdf/2203.00555.pdf)

- [ ] [**ECCV 2020** | **[Github](https://github.com/princeton-vl/RAFT)**] [RAFT: Recurrent All Pairs Field Transforms for Optical Flow](https://arxiv.org/pdf/2003.12039.pdf)

#### 1.1. Vanishing/Exploding gradients

[My Notes on What is Gradients Vanishing/Exploding & How to Solve it?](backbones/vanish_explode_gradients.md)

- [ ] [**TNN 1994**] [learning long-term dependencies with gradient descent is difficult](http://www.comp.hkbu.edu.hk/~markus/teaching/comp7650/tnn-94-gradient.pdf)

- [x] [**AISTATS 2010**] [Understanding the difficulty of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf)

- [x] [**ICML 2015**] [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167.pdf) [[Reading Note](backbones/batch_norm.ipynb)]

#### 1.2 Optimization techniques
[Loss Functions](backbones/loss_funcs.md)

- [ ] [**JMLR 2011** | **AdaGrad**] [Adaptive subgradient methods for online learning and stochastic optimization](https://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf)

- [ ] [**COURSERA Neural networks for machine learning, 2012** | **RMSProp**] [rmsprop: Divide the gradient by a running average of its recent magnitude](https://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)

- [ ] [**ICML 2013** | **Momentum**] [On the importance of initialization and momentum in deep learning](http://proceedings.mlr.press/v28/sutskever13.pdf)

- [ ] [**JMLR 2014** | **Dropout**] [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~rsalakhu/papers/srivastava14a.pdf)

- [ ] [**ICLR 2015** | **Adam**] [Adam: A method for stochastic optimization](https://arxiv.org/pdf/1412.6980.pdf)

#### 1.3 Recurrent Neural Network

- [ ] [**Neural Computation 1997** | **LSTM**] [Long short-term memory](http://www.bioinf.at/publications/older/2604.pdf)

- [ ] [**EMNLP 2014** | **GRU**] [On the Properties of Neural Machine Translation: Encoder–Decoder Approaches](https://arxiv.org/pdf/1409.1259.pdf)

- [ ] [**CoRR 2014** | **GRU**] [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](https://arxiv.org/pdf/1412.3555.pdf)

### 2. Optimization in 3D Vision

- [x] [**CVPR 2021** | **[Github](https://github.com/hjwdzh/DeepLM)**] [DeepLM: Large-scale Nonlinear Least Squares on Deep Learning Frameworks using Stochastic Domain Decomposition](https://openaccess.thecvf.com/content/CVPR2021/papers/Huang_DeepLM_Large-Scale_Nonlinear_Least_Squares_on_Deep_Learning_Frameworks_Using_CVPR_2021_paper.pdf)

- [ ] [**ICML 2021** | **[Github](https://github.com/johannesbrust/SNLLS)**] [Nonlinear Least Squares for Large-Scale Machine Learning using Stochastic Jacobian Estimates](https://arxiv.org/pdf/2107.05598.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/princeton-vl/lietorch)**] [Tangent Space Backpropagation for 3D Transformation Groups](https://openaccess.thecvf.com/content/CVPR2021/papers/Teed_Tangent_Space_Backpropagation_for_3D_Transformation_Groups_CVPR_2021_paper.pdf)


### 3. Deep Structure from Motion

***Should write a detailed review later.***

#### 3.1 Multi View methods

- [x] [**CVPR 2017** | **[Github](https://github.com/lmb-freiburg/demon)**] [DeMoN: Depth and Motion Network for Learning Monocular Stereo](https://arxiv.org/pdf/1612.02401.pdf)

- [x] [**ICLR 2019** | **[Github](https://github.com/frobelbest/BANet)**] [BA-NET: DENSE BUNDLE ADJUSTMENT NETWORKS](https://arxiv.org/pdf/1806.04807.pdf)

- [x] [**ICML 2020** | **[Github](https://github.com/princeton-vl/DeepV2D)**] [Deepv2d: Video to depth with differentiable structure from motion](https://arxiv.org/pdf/1812.04605.pdf)

- [x] [**ECCV 2020 oral** | **[Github](https://github.com/weixk2015/DeepSFM)**] [DeepSFM: Structure From Motion Via Deep Bundle Adjustment](https://arxiv.org/pdf/1912.09697.pdf)

- [x] [**CVPR 2021** | **[Github](https://github.com/jytime/Deep-SfM-Revisited)**] [Deep Two-View Structure-from-Motion Revisited](https://arxiv.org/pdf/2104.00556.pdf)

- [x] [**arXiv 2021** | **[Github](https://github.com/aliyun/dro-sfm)**] [DRO: Deep Recurrent Optimizer for Structure-from-Motion](https://arxiv.org/pdf/2103.13201.pdf) [**[Reading Note](deep_sfm/dro.md)**]

- [ ] [**ECCV 2020** | **[Github](https://github.com/svip-lab/Indoor-SfMLearner)**] [Patch-match and Plane-regularization for Unsupervised Indoor Depth Estimation](https://arxiv.org/pdf/2007.07696.pdf)

- [x] [**ECCV 2020** | **[Github](https://github.com/mihaidusmanu/local-feature-refinement)** | **[Video](https://youtube.com/watch?v=zBbIFxMGs3A)**] [Multi-View Optimization of Local Feature Geometry](https://arxiv.org/pdf/2003.08348.pdf)

- [x] [**ICCV 2021 Best Student Paper** | **[Github](https://github.com/cvg/pixel-perfect-sfm)**] [Pixel-Perfect Structure-from-Motion](https://arxiv.org/pdf/2108.08291.pdf)

- [ ] [**3DV 2021** | **[Github](https://github.com/JingwenWang95/DSP-SLAM)**] [DSP-SLAM: Object Oriented SLAM with Deep Shape Priors](https://arxiv.org/pdf/2108.09481.pdf)

- [ ] [**NeurlIPS 2021** | **[Github](https://github.com/AljazBozic/TransformerFusion)**] [TransformerFusion: Monocular RGB Scene Reconstruction using Transformers](https://arxiv.org/pdf/2107.02191.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/zju3dv/NeuralRecon)**] [NeuralRecon: Real-Time Coherent 3D Reconstruction from Monocular Video](https://arxiv.org/pdf/2104.00681.pdf)

- [ ] [**CVPR 2022** | **[Github](https://github.com/facebookresearch/banmo)**] [BANMo: Building Animatable 3D Neural Models from Many Casual Videos](https://arxiv.org/pdf/2112.12761.pdf)

#### 3.2 Single View

***Up-to-date***

### 4. Deep Multi-View Stereo

- [ ] [**ECCV 2018** | **[Github](https://github.com/YoYo000/MVSNet)**] [MVSNet: Depth Inference for Unstructured Multi-view Stereo](https://arxiv.org/pdf/1804.02505.pdf)

- [ ] [**CVPR 2019** | **[Github](https://github.com/YoYo000/MVSNet)**] [Recurrent MVSNet for High-resolution Multi-view Stereo Depth Inference](https://arxiv.org/pdf/1902.10556.pdf)

- [ ] [**CVPR 2020** | **[Github](https://github.com/alibaba/cascade-stereo)**] [Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching](https://arxiv.org/pdf/1912.06378.pdf)

### 5. Implicit Surface Reconstruction / View Synthesis

- [x] [**ECCV 2020** | **[Github](https://github.com/bmild/nerf)**] [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/pdf/2003.08934.pdf) [**[Reading Notes(coming soon)]()** | **[Implementation(coming soon)]()**]

- [ ] [**arXiv 2021** | **[Github]()**] [Gradient-SDF: A Semi-Implicit Surface Representation for 3D Reconstruction](https://arxiv.org/pdf/2111.13652.pdf)

- [x] [**CVPR 2021** | **[Github](https://github.com/princeton-computational-imaging/neural-scene-graphs)**] [Neural Scene Graphs for Dynamic Scenes](http://light.princeton.edu/neural-scene-graphs)

- [x] [**ICCV 2021 oral** | **[Github](https://github.com/autonomousvision/unisurf)**] [UNISURF: Unifying Neural Implicit Surfaces and Radiance Fields for Multi-View Reconstruction](http://www.cvlibs.net/publications/Oechsle2021ICCV.pdf)

- [ ] [**ICCV 2021 oral** | **[Github](https://github.com/google-research/google-research/tree/master/snerg)**] [Baking Neural Radiance Fields for Real-Time View Synthesis](https://openaccess.thecvf.com/content/ICCV2021/papers/Hedman_Baking_Neural_Radiance_Fields_for_Real-Time_View_Synthesis_ICCV_2021_paper.pdf)

- [ ] [**arXiv 2021** | **[Github](https://github.com/city-super/citynerf)**] [CityNeRF: Building NeRF at City Scale](https://arxiv.org/pdf/2112.05504.pdf)

- [ ] [**arXiv 2022** | **[Official Site](http://waymo.com/research/block-nerf)**] [Block-NeRF: Scalable Large Scene Neural View Synthesis](https://arxiv.org/pdf/2202.05263.pdf)

