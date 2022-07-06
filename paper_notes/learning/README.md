# Papers in Deep Learning

## Papers to Read

### 1. Backbone/Classical NN architectures

- [x] [**IEEE 1998** | **LeNet**] [GradientBased Learning Applied to Document Recognition](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf)

- [ ] [**ECCV 2014** | **SPP-Net**] [Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition](https://arxiv.org/pdf/1406.4729.pdf)

- [x] [**CVPR 2015** | **GoogleNet**] [Going deeper with convolutions](https://arxiv.org/pdf/1409.4842.pdf)

- [x] [**ICLR 2015** | **VGG**] [VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION](https://arxiv.org/pdf/1409.1556.pdf) ([**[Reading Note](backbones/VGG.md) | [Implementation(Up-to-date)]()**])

- [x] [**CVPR 2016** | **ResNet**] [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf) ([**[Reading Note](backbones/resnet.md) | [Implementation](backbones/src/resnet.py)**])

- [x] [**ECCV 2016** | **Follow-up of ResNet**] [Identity mappings in deep residual networks](https://arxiv.org/pdf/1603.05027.pdf)

- [x] [**BMVC 2016** | **[Github](https://github.com/szagoruyko/wide-residual-networks/tree/master/pretrained)**] [Wide Residual Networks](https://arxiv.org/pdf/1605.07146.pdf)

- [ ] [**CVPR 2017** | **ResNeXt**] [Aggregated residual transformations for deep neural networks]()

- [x] [**CVPR 2018**] [Squeeze-and-Excitation Networks](https://www.robots.ox.ac.uk/~vgg/publications/2018/Hu18/hu18.pdf)

- [ ] [**2016**] [Layer normalization]()


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

- [x] [**Neural Computation 1997** | **LSTM**] [Long short-term memory](http://www.bioinf.at/publications/older/2604.pdf)

- [x] [**EMNLP 2014** | **GRU**] [Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](https://arxiv.org/pdf/1406.1078.pdf)

- [x] [**EMNLP 2014** | **GRU**] [On the Properties of Neural Machine Translation: Encoder–Decoder Approaches](https://arxiv.org/pdf/1409.1259.pdf)

- [x] [**CoRR 2014** | **GRU**] [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](https://arxiv.org/pdf/1412.3555.pdf)

#### 1.4 Data Augmentation

- [ ] [**arXiv 2017** | **[Github](https://github.com/uoguelph-mlrg/Cutout)**] [Improved Regularization of Convolutional Neural Networks with Cutout](https://arxiv.org/pdf/1708.04552.pdf)

- [ ] [**ICLR 2018** | **[Github](https://github.com/facebookresearch/mixup-cifar10)**] [mixup: Beyond Empirical Risk Minimization](https://arxiv.org/pdf/1710.09412.pdf)


### 2. Attention & Transformers

***I will write a note of transformer later...***

- [ ] [**ICLR 2017** | **[Github](https://github.com/ExplorerFreda/Structured-Self-Attentive-Sentence-Embedding)**] [A Structured Self-attentive Sentence Embedding](https://arxiv.org/pdf/1703.03130.pdf)

- [x] [**NeuIPS 2017** | **[Github](https://github.com/jadore801120/attention-is-all-you-need-pytorch)**] [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)

- [ ] [**ICLR 2021** | **[Github](https://github.com/google-research/vision_transformer)**] [An Image Is Worth 16X16 Words: Transformers For Image Recognition At Scale](https://arxiv.org/pdf/2010.11929.pdf)

- [ ] [**ICCV 2021 Best Paper** | **[Github](https://github.com/microsoft/Swin-Transformer)**] [Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/pdf/2103.14030.pdf)

- [ ] [**CVPR 2022** | **[Github](https://github.com/microsoft/unilm)**] [DeepNet: Scaling Transformers to 1,000 Layers](https://arxiv.org/pdf/2203.00555.pdf)



### 3. Deep Structure from Motion

***[My Review of Deep Structure from Motion Literatures](deep_sfm/review.ipynb)***

#### 3.1 Multi View methods

- [x] [**ICCV 2015** | **[Github](https://github.com/youngguncho/PoseNet-Pytorch)**] [PoseNet: A Convolutional Network for Real-Time 6-DOF Camera Relocalization](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Kendall_PoseNet_A_Convolutional_ICCV_2015_paper.pdf)

- [x] [**CVPR 2017** | **[Github](https://github.com/lmb-freiburg/demon)**] [DeMoN: Depth and Motion Network for Learning Monocular Stereo](https://arxiv.org/pdf/1612.02401.pdf)

- [ ] [**CVPR 2018** | **[Github](https://github.com/silviutroscot/CodeSLAM)**] [CodeSLAM - Learning a Compact, Optimisable Representation for Dense Visual SLAM](https://arxiv.org/pdf/1804.00874.pdf)

- [x] [**ECCV 2018** | **[Github](https://github.com/r0nn13/learn2rec)**] [LS-Net: Learning to Solve Nonlinear Least Squares for Monocular Stereo](https://arxiv.org/pdf/1809.02966.pdf)

- [x] [**ICLR 2019** | **[Github](https://github.com/frobelbest/BANet)**] [BA-NET: DENSE BUNDLE ADJUSTMENT NETWORKS](https://arxiv.org/pdf/1806.04807.pdf)

- [x] [**ICML 2020** | **[Github](https://github.com/princeton-vl/DeepV2D)**] [Deepv2d: Video to depth with differentiable structure from motion](https://arxiv.org/pdf/1812.04605.pdf)

- [x] [**CVPR 2020** | **[Github](https://github.com/B1ueber2y/TrianFlow)**] [Towards Better Generalization: Joint Depth-Pose Learning without PoseNet](https://arxiv.org/pdf/2004.01314.pdf)

- [x] [**ECCV 2020 oral** | **[Github](https://github.com/weixk2015/DeepSFM)**] [DeepSFM: Structure From Motion Via Deep Bundle Adjustment](https://arxiv.org/pdf/1912.09697.pdf)

- [ ] [**ECCV 2020** | **[Github](https://github.com/princeton-vl/RAFT)**] [RAFT: Recurrent All Pairs Field Transforms for Optical Flow](https://arxiv.org/pdf/2003.12039.pdf)

- [ ] [**ICRA 2020** | **[Github](https://github.com/Huangying-Zhan/DF-VO)**] [Visual odometry revisited: What should be learnt](https://arxiv.org/pdf/1909.09803.pdf)

- [x] [**CVPR 2021** | **[Github](https://github.com/jytime/Deep-SfM-Revisited)**] [Deep Two-View Structure-from-Motion Revisited](https://arxiv.org/pdf/2104.00556.pdf)

- [x] [**arXiv 2021** | **[Github](https://github.com/aliyun/dro-sfm)**] [DRO: Deep Recurrent Optimizer for Structure-from-Motion](https://arxiv.org/pdf/2103.13201.pdf) [**[Reading Note](deep_sfm/dro.md)**]

- [ ] [**ECCV 2020** | **[Github](https://github.com/svip-lab/Indoor-SfMLearner)**] [Patch-match and Plane-regularization for Unsupervised Indoor Depth Estimation](https://arxiv.org/pdf/2007.07696.pdf)

- [x] [**ECCV 2020** | **[Github](https://github.com/mihaidusmanu/local-feature-refinement)** | **[Video](https://youtube.com/watch?v=zBbIFxMGs3A)**] [Multi-View Optimization of Local Feature Geometry](https://arxiv.org/pdf/2003.08348.pdf)

- [x] [**ECCV 2020** | **[Github](https://github.com/pulak09/NeuRoRA)**] [NeuRoRA: Neural Robust Rotation Averaging](https://arxiv.org/pdf/1912.04485.pdf)

- [x] [**3DV 2021** | **[Github](https://github.com/yewzijian/MultiReg)**] [Learning Iterative Robust Transformation Synchronization](https://arxiv.org/pdf/2111.00728.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/sfu-gruvi-3dv/msp_rot_avg)**] [End-to-End Rotation Averaging with Multi-Source Propagation](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_End-to-End_Rotation_Averaging_With_Multi-Source_Propagation_CVPR_2021_paper.pdf)

- [x] [**ICCV 2021 Best Student Paper** | **[Github](https://github.com/cvg/pixel-perfect-sfm)**] [Pixel-Perfect Structure-from-Motion](https://arxiv.org/pdf/2108.08291.pdf)

- [ ] [**3DV 2021** | **[Github](https://github.com/JingwenWang95/DSP-SLAM)**] [DSP-SLAM: Object Oriented SLAM with Deep Shape Priors](https://arxiv.org/pdf/2108.09481.pdf)

- [ ] [**NeurlIPS 2021** | **[Github](https://github.com/AljazBozic/TransformerFusion)**] [TransformerFusion: Monocular RGB Scene Reconstruction using Transformers](https://arxiv.org/pdf/2107.02191.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/zju3dv/NeuralRecon)**] [NeuralRecon: Real-Time Coherent 3D Reconstruction from Monocular Video](https://arxiv.org/pdf/2104.00681.pdf)

- [x] [**CVPR 2022** | **[Github](https://github.com/facebookresearch/banmo)**] [BANMo: Building Animatable 3D Neural Models from Many Casual Videos](https://arxiv.org/pdf/2112.12761.pdf)

- [ ] [**CVPR 2022** | **[Github](https://github.com/cvg/nice-slam)**] [NICE-SLAM: Neural Implicit Scalable Encoding for SLAM](https://arxiv.org/pdf/2112.12130.pdf)

- [x] [**CVPR 2022** | **[Github](https://github.com/amazon-research/small-baseline-camera-tracking)**] [Depth-Guided Structure-from-Motion for Movies and TV Shows](https://assets.amazon.science/b4/43/86551d474ac19789eb1635cc2795/depth-guidedsparse-structure-from-motion-for-movies-and-tv-shows.pdf)

- [x] [**RAL 2022** | **[Github](https://github.com/utiasSTARS/tightly-coupled-SfM)**] [On the Coupling of Depth and Egomotion Networks for Self-Supervised Structure from Motion]()

- [x] [**CVPR 2022** | **[Github](https://github.com/sfu-gruvi-3dv/RAGO)**] [RAGO: Recurrent Graph Optimizer For Multiple Rotation Averaging](https://github.com/sfu-gruvi-3dv/RAGO/blob/main/paper/04166.pdf)

#### 3.2 Single View

- [ ] [**CVPR 2015** | **[Github](https://github.com/comeonyang/Depth-Estimation-DCNF)**] [Deep Convolutional Neural Fields for Depth Estimation from a Single Image](https://arxiv.org/pdf/1502.07411.pdf)

- [ ] [**ICCV 2015**] [Predicting Depth, Surface Normals and Semantic Labels with a Common Multi-Scale Convolutional Architecture](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Eigen_Predicting_Depth_Surface_ICCV_2015_paper.pdf)

- [ ] [**CVPR 2017 oral** | **[Github](https://github.com/tinghuiz/SfMLearner)**] [Unsupervised Learning of Depth and Ego-Motion from Video](https://arxiv.org/pdf/1704.07813.pdf)

- [ ] [**CVPR 2018** | **[Github](https://github.com/MightyChaos/LKVOLearner)**] [Learning Depth From Monocular Videos Using Direct Methods](https://openaccess.thecvf.com/content_cvpr_2018/papers/Wang_Learning_Depth_From_CVPR_2018_paper.pdf)

- [ ] [**CVPR 2018** | **[Github](https://github.com/zhengqili/MegaDepth)**] [MegaDepth: Learning Single-View Depth Prediction from Internet Photos](https://openaccess.thecvf.com/content_cvpr_2018/papers/Li_MegaDepth_Learning_Single-View_CVPR_2018_paper.pdf)

- [ ] [**CVPR 2018** | **[Github](https://github.com/yzcjtr/GeoNet)**] [GeoNet: Unsupervised Learning of Dense Depth, Optical Flow and Camera Pose](https://arxiv.org/pdf/1803.02276.pdf)

- [ ] [**ICCV 2019** | **[Github](https://github.com/google-research/google-research/blob/master/dual_pixels/README.md)**] [Learning single camera depth estimation using dual pixels](https://openaccess.thecvf.com/content_ICCV_2019/papers/Garg_Learning_Single_Camera_Depth_Estimation_Using_Dual-Pixels_ICCV_2019_paper.pdf)

- [ ] [**ICCV 2019** | **[Github](https://github.com/nianticlabs/monodepth2)**] [Digging into Self-Supervised Monocular Depth Prediction](https://arxiv.org/pdf/1806.01260.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/nianticlabs/manydepth)**] [The Temporal Opportunist: Self-Supervised Multi-Frame Monocular Depth]()

#### 3.3 Optimization in 3D Vision

- [x] [**CVPR 2021** | **[Github](https://github.com/hjwdzh/DeepLM)**] [DeepLM: Large-scale Nonlinear Least Squares on Deep Learning Frameworks using Stochastic Domain Decomposition](https://openaccess.thecvf.com/content/CVPR2021/papers/Huang_DeepLM_Large-Scale_Nonlinear_Least_Squares_on_Deep_Learning_Frameworks_Using_CVPR_2021_paper.pdf)

- [ ] [**ICML 2021** | **[Github](https://github.com/johannesbrust/SNLLS)**] [Nonlinear Least Squares for Large-Scale Machine Learning using Stochastic Jacobian Estimates](https://arxiv.org/pdf/2107.05598.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/princeton-vl/lietorch)**] [Tangent Space Backpropagation for 3D Transformation Groups](https://openaccess.thecvf.com/content/CVPR2021/papers/Teed_Tangent_Space_Backpropagation_for_3D_Transformation_Groups_CVPR_2021_paper.pdf)


### 4. Deep Multi-View Stereo

- [ ] [**CVPR 2017** | **[Github](https://github.com/kelkelcheng/GC-Net-Tensorflow)**] [End-to-end learning of geometry and context for deep stereo regression](https://openaccess.thecvf.com/content_ICCV_2017/papers/Kendall_End-To-End_Learning_of_ICCV_2017_paper.pdf)

- [x] [**ECCV 2018** | **[Github](https://github.com/YoYo000/MVSNet)**] [MVSNet: Depth Inference for Unstructured Multi-view Stereo](https://arxiv.org/pdf/1804.02505.pdf)

- [x] [**CVPR 2018** | **[Github](https://github.com/phuang17/DeepMVS)**] [DeepMVS: Learning Multi-view Stereopsis](https://arxiv.org/pdf/1804.00650.pdf)

- [x] [**CVPR 2019** | **[Github](https://github.com/YoYo000/MVSNet)**] [Recurrent MVSNet for High-resolution Multi-view Stereo Depth Inference](https://arxiv.org/pdf/1902.10556.pdf)

- [x] [**CVPR 2019** | **[Github](https://github.com/callmeray/PointMVSNet)**] [Point-based Multi-view Stereo Network](https://arxiv.org/pdf/1908.04422.pdf)

- [ ] [**ICLR 2019** | **[Github](https://github.com/sunghoonim/DPSNet)**] [Dpsnet: End-to-end deep plane sweep stereo](https://openreview.net/pdf?id=ryeYHi0ctQ)

- [ ] [**CVPR 2020** | **[Github](https://github.com/alibaba/cascade-stereo)**] [Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching](https://arxiv.org/pdf/1912.06378.pdf)

- [ ] [**CVPR 2022** | **[Github](https://github.com/prstrive/UniMVSNet)**] [Rethinking Depth Estimation for Multi-View Stereo: A Unified Representation](https://arxiv.org/pdf/2201.01501.pdf)

- [ ] [**CVPR 2022** | **[Github](https://github.com/FangjinhuaWang/IterMVS)**] [IterMVS: Iterative Probability Estimation for Efficient Multi-View Stereo](https://arxiv.org/pdf/2112.05126.pdf)

- [x] [**arXiv 2022** | **[Github](https://github.com/JeffWang987/MVSTER)**] [MVSTER: Epipolar Transformer for Efficient Multi-View Stereo](https://arxiv.org/pdf/2204.07346.pdf)

### 5. Implicit Surface Reconstruction / View Synthesis

- [x] [**ECCV 2020** | **[Github](https://github.com/bmild/nerf)**] [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/pdf/2003.08934.pdf) [**[Reading Notes(coming soon)]()**]

- [x] [**CVPR 2021** | **[Github](https://github.com/sxyu/pixel-nerf)**] [pixelNeRF: Neural Radiance Fields from One or Few Images](https://arxiv.org/pdf/2012.02190.pdf)

- [x] [**ICCV 2021** | **[Github](https://github.com/google/nerfies)**] [Nerfies: Deformable Neural Radiance Fields](https://arxiv.org/pdf/2011.12948.pdf)

- [x] [**ICCV 2021** | **[Github](https://github.com/google/mipnerf)**] [Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields](https://openaccess.thecvf.com/content/ICCV2021/papers/Barron_Mip-NeRF_A_Multiscale_Representation_for_Anti-Aliasing_Neural_Radiance_Fields_ICCV_2021_paper.pdf)

- [ ] [**ICCV 2021 oral** | **[Github](https://github.com/google-research/google-research/tree/master/snerg)**] [Baking Neural Radiance Fields for Real-Time View Synthesis](https://openaccess.thecvf.com/content/ICCV2021/papers/Hedman_Baking_Neural_Radiance_Fields_for_Real-Time_View_Synthesis_ICCV_2021_paper.pdf)

- [ ] [**CVPR 2022 oral** | **[Github](https://jonbarron.info/mipnerf360/)**] [Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](https://arxiv.org/pdf/2111.12077.pdf)

- [ ] [**CVPR 2022 oral** | **[Github](https://bmild.github.io/rawnerf/index.html)**] [NeRF in the Dark: High Dynamic Range View Synthesis from Noisy Raw Images](https://arxiv.org/pdf/2111.13679.pdf)

- [ ] [**CVPR 2022 oral** | **[Github](https://dorverbin.github.io/refnerf/index.html)**] [Ref-NeRF: Structured View-Dependent Appearance for Neural Radiance Fields](https://arxiv.org/pdf/2112.03907.pdf)

- [ ] [**CVPR 2022 oral** | **[Github](https://github.com/google-research/google-research/tree/master/regnerf)**] [RegNeRF: Regularizing Neural Radiance Fields for View Synthesis from Sparse Inputs](https://drive.google.com/file/d/1S_NnmhypZjyMfwqcHg-YbWSSYNWdqqlo/view)

- [ ] [**CVPR 2022** | **[Github](https://github.com/limacv/Deblur-NeRF)**] [Deblur-NeRF: Neural Radiance Fields from Blurry Images](https://arxiv.org/pdf/2111.14292.pdf)

- [ ] [**CVPR 2022 oral** | **[Github](https://github.com/computational-imaging/bacon)**] [BACON: Band-limited Coordinate Networks for Multiscale Scene Representation](https://arxiv.org/pdf/2112.04645.pdf)

- [ ] [**CVPR 2022** | **[Github](https://github.com/liuyuan-pal/NeuRay)**] [Neural Rays for Occlusion-aware Image-based Rendering](https://arxiv.org/pdf/2107.13421.pdf)

- [ ] [**arXiv 2022** | **[Github](https://github.com/apchenstu/TensoRF)**] [TensoRF: Tensorial Radiance Fields](https://arxiv.org/pdf/2203.09517.pdf)

#### 5.0 Survey/Overview

- [ ] [**EG 2022**] [Neural fields in visual computing and beyond](https://arxiv.org/pdf/2111.11426.pdf)

- [ ] [**EG 2022**] [Advances in Neural Rendering]()

#### 5.1 Fourier Features

- [x] [**NeurIPS 2020** | **[Github](https://github.com/tancik/fourier-feature-networks)**] [Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains](https://arxiv.org/pdf/2006.10739.pdf)

- [ ] [**WACV 2022** | **[Github]()**] [Seeing Implicit Neural Representations as Fourier Series](https://openaccess.thecvf.com/content/WACV2022/papers/Benbarka_Seeing_Implicit_Neural_Representations_As_Fourier_Series_WACV_2022_paper.pdf)

- [ ] [**arXiv 2022**] [Generalised Implicit Neural Representations](https://arxiv.org/pdf/2205.15674.pdf)

#### 5.2 Pose Estimation

- [x] [**IROS 2021** | **[Github](https://github.com/yenchenlin/iNeRF-public)**] [iNeRF: Inverting Neural Radiance Fields for Pose Estimation](https://arxiv.org/pdf/2012.05877.pdf)

- [x] [**arXiv 2021** | **[Github](https://github.com/ActiveVisionLab/nerfmm)**] [NeRF−−: Neural Radiance Fields Without Known Camera Parameters](https://arxiv.org/pdf/2102.07064.pdf)

- [x] [**ICCV 2021 oral** | **[Github](https://github.com/chenhsuanlin/bundle-adjusting-NeRF)**] [BARF: Bundle-Adjusting Neural Radiance Fields](https://chenhsuanlin.bitbucket.io/bundle-adjusting-NeRF/paper.pdf)

- [x] [**ICCV 2021 oral** | **[Github](https://github.com/MQ66/gnerf)**] [GNeRF: GAN-based Neural Radiance Field without Posed Camera](https://arxiv.org/pdf/2103.15606.pdf)

#### 5.3 Depth Supervised NeRF

- [x] [**ICCV 2021** | **[Github](https://github.com/weiyithu/NerfingMVS)**] [NerfingMVS: Guided Optimization of Neural Radiance Fields for Indoor Multi-view Stereo](https://arxiv.org/pdf/2109.01129.pdf)

- [x] [**CVPR 2022** | **[Github](https://github.com/barbararoessle/dense_depth_priors_nerf)**] [Dense Depth Priors for Neural Radiance Fields from Sparse Input Views](https://arxiv.org/pdf/2112.03288.pdf)

- [x] [**CVPR 2022** | **[Github](https://github.com/dunbar12138/DSNeRF)**] [Depth-supervised NeRF: Fewer Views and Faster Training for Free](https://arxiv.org/pdf/2107.02791.pdf)

#### 5.4 Dynamic NeRF

- [x] [**CVPR 2021** | **[Github](https://github.com/princeton-computational-imaging/neural-scene-graphs)**] [Neural Scene Graphs for Dynamic Scenes](http://light.princeton.edu/neural-scene-graphs)

#### 5.5 Unified Representation

- [x] [**ICCV 2021 oral** | **[Github](https://github.com/autonomousvision/unisurf)**] [UNISURF: Unifying Neural Implicit Surfaces and Radiance Fields for Multi-View Reconstruction](http://www.cvlibs.net/publications/Oechsle2021ICCV.pdf)

- [x] [**NeurIPS 2021**] [H-NeRF: Neural Radiance Fields for Rendering and Temporal Reconstruction of Humans in Motion](https://openreview.net/pdf?id=s-NI4H4e3Rf)

#### 5.6 Large Scale NeRF

- [x] [**ICCV 2021** | **[Github](https://github.com/creiser/kilonerf)**] [KiloNeRF: Speeding up Neural Radiance Fields with Thousands of Tiny MLPs](https://arxiv.org/abs/2103.13744.pdf)

- [ ] [**arXiv 2021** | **[Github](https://github.com/city-super/citynerf)**] [CityNeRF: Building NeRF at City Scale](https://arxiv.org/pdf/2112.05504.pdf)

- [x] [**CVPR 2022** | **[Official Site](http://waymo.com/research/block-nerf)**] [Block-NeRF: Scalable Large Scene Neural View Synthesis](https://arxiv.org/pdf/2202.05263.pdf)

- [ ] [**CVPR 2022** | **[Github](https://github.com/cmusatyalab/mega-nerf)**] [Mega-NeRF: Scalable Construction of Large-Scale NeRFs for Virtual Fly-Throughs](https://arxiv.org/pdf/2112.10703.pdf)

#### 5.7 MVS Enhanced NeRF

- [x] [**ICCV 2021** | **[Github](https://github.com/apchenstu/mvsnerf)**] [MVSNeRF: Fast Generalizable Radiance Field Reconstruction from Multi-View Stereo](https://arxiv.org/pdf/2103.15595.pdf)

- [x] [**CVPR 2022** | **[Github](https://github.com/Xharlie/pointnerf)**] [Point-NeRF: Point-based Neural Radiance Fields](https://arxiv.org/pdf/2201.08845.pdf)

- [ ] [**arXiv 2022** | **[Github](https://github.com/princeton-vl/SNP)**] [View Synthesis with Sculpted Neural Points](https://arxiv.org/pdf/2205.05869.pdf)