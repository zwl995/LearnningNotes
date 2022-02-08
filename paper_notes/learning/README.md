# Papers in Deep Learning

## Papers to Read

### 1. Backbone/Classical NN architectures

- [ ] **Transformer** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia
Polosukhin. Attention is all you need. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan

- [ ] [**IEEE 1998** | **LeNet**] [GradientBased Learning Applied to Document Recognition](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf)

- [ ] [**ECCV 2014** | **SPP-Net**] [Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition](https://arxiv.org/pdf/1406.4729.pdf)

- [x] [**ICLR 2015** | **VGG**] [VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION](https://arxiv.org/pdf/1409.1556.pdf)
> This paper is really helpful in understanding how deep convolution neural network helps to increase the classification performance, especially in terms of the depth of neural network and data augmentation when training. **Should write a detailed notes later.**

- [ ] [**CVPR 2016** | **ResNet**] [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf)

- [ ] [**NeuIPS 2017**] | **Transformer**] [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)

- [ ] [**ECCV 2020** | **[Github](https://github.com/bmild/nerf)**] [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/pdf/2003.08934.pdf)

- [ ] [**ECCV 2020** | **[Github](https://github.com/princeton-vl/RAFT)**] [RAFT: Recurrent All Pairs Field Transforms for Optical Flow](https://arxiv.org/pdf/2003.12039.pdf)

### 2. Optimizers

- [ ] [**ICLR 2015** | **Adam**] [Adam: A method for stochastic optimization](https://arxiv.org/pdf/1412.6980.pdf)

- [x] [**CVPR 2021** | **[Github](https://github.com/hjwdzh/DeepLM)**] [DeepLM: Large-scale Nonlinear Least Squares on Deep Learning Frameworks using Stochastic Domain Decomposition](https://openaccess.thecvf.com/content/CVPR2021/papers/Huang_DeepLM_Large-Scale_Nonlinear_Least_Squares_on_Deep_Learning_Frameworks_Using_CVPR_2021_paper.pdf)

> This paper is not actually using neural network to do the LM method. Instead, it used a method that can gather derivatives for all 
variables to a full jacobian efficiently, which can be analogized with the backpropagation. The main contribution of this work comes 
from this efficient jacobian collection method, which I would rather say it's more an backend architecture than a neural network. Besides, 
the stochastic domain decomposition method seems simply adopted the stochastic clustering method in STBA.

- [ ] [**ICML 2021** | **[Github](https://github.com/johannesbrust/SNLLS)**] [Nonlinear Least Squares for Large-Scale Machine Learning using Stochastic Jacobian Estimates](https://arxiv.org/pdf/2107.05598.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/princeton-vl/lietorch)**] [Tangent Space Backpropagation for 3D Transformation Groups](https://openaccess.thecvf.com/content/CVPR2021/papers/Teed_Tangent_Space_Backpropagation_for_3D_Transformation_Groups_CVPR_2021_paper.pdf)


### 3. Deep SfM Methods

***Should write a detailed review later.***

- [x] [**CVPR 2017** | **[Github](https://github.com/lmb-freiburg/demon)**] [DeMoN: Depth and Motion Network for Learning Monocular Stereo](https://arxiv.org/pdf/1612.02401.pdf)

- [x] [**ICLR 2019** | **[Github](https://github.com/frobelbest/BANet)**] [BA-NET: DENSE BUNDLE ADJUSTMENT NETWORKS](https://arxiv.org/pdf/1806.04807.pdf)
> The key ideas of `BANet` is to use represent depth map as a linear combination of depth maps at different scales, and to use a `BALayer` to predict the damping factor of the classical LM algorithm, which makes $\mathcal{X}$ differentiable to feature maps.

- [ ] [**ICML 2020** | **[Github](https://github.com/princeton-vl/DeepV2D)**] [Deepv2d: Video to depth with differentiable structure from motion](https://arxiv.org/pdf/1812.04605.pdf)

- [x] [**ECCV 2020 oral** | **[Github](https://github.com/weixk2015/DeepSFM)**] [DeepSFM: Structure From Motion Via Deep Bundle Adjustment](https://arxiv.org/pdf/1912.09697.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/jytime/Deep-SfM-Revisited)**] [Deep Two-View Structure-from-Motion Revisited](https://arxiv.org/pdf/2104.00556.pdf)

- [x] [**arXiv 2021** | **[Github](https://github.com/aliyun/dro-sfm)**] [DRO: Deep Recurrent Optimizer for Structure-from-Motion](https://arxiv.org/pdf/2103.13201.pdf)

> This work deals with the image depth and pose estimation problem by recurrent neural network. The neural optimizer optimizes the image depth and image pose alternatively. At first, DRO uses ResNet-16 to extract the feature maps, the cost is defined so as to minimize the alignment errors between the predicted feature maps. Then, the small update w.r.t. depth $\Delta \mathbf{D}_i$ and pose $\Delta \mathbf{P}_i$ is computed by the ***gated recurrent unit (See RAFT)*** , which are used for alternatively updating the image depth and pose. DRO also used two different loss functions for supervised training and unsupervised training. DRO is superior to ***DeepV2D (See ICML 2020 Deng et, al)*** in memory occupation and computation efficiency.

- [ ] [**ECCV 2020** | **[Github](https://github.com/svip-lab/Indoor-SfMLearner)**] [Patch-match and Plane-regularization for Unsupervised Indoor Depth Estimation](https://arxiv.org/pdf/2007.07696.pdf)

- [ ] [**ECCV 2020** | **[Github](https://github.com/mihaidusmanu/local-feature-refinement)** | **[Video](https://youtube.com/watch?v=zBbIFxMGs3A)**] [Multi-View Optimization of Local Feature Geometry](https://arxiv.org/pdf/2003.08348.pdf)

- [ ] [**ICCV 2021 Best Student Paper** | **[Github](https://github.com/cvg/pixel-perfect-sfm)**] [Pixel-Perfect Structure-from-Motion](https://arxiv.org/pdf/2108.08291.pdf)

- [ ] [**3DV 2021** | **[Github](https://github.com/JingwenWang95/DSP-SLAM)**] [DSP-SLAM: Object Oriented SLAM with Deep Shape Priors](https://arxiv.org/pdf/2108.09481.pdf)


### 4. Implicit Surface Reconstruction / View Synthesis

- [ ] [**arXiv 2021** | **[Github]()**] [Gradient-SDF: A Semi-Implicit Surface Representation for 3D Reconstruction](https://arxiv.org/pdf/2111.13652.pdf)

- [x] [**ICCV 2021 oral** | **[Github](https://github.com/autonomousvision/unisurf)**] [UNISURF: Unifying Neural Implicit Surfaces and Radiance Fields for Multi-View Reconstruction](http://www.cvlibs.net/publications/Oechsle2021ICCV.pdf)

- [ ] [**ICCV 2021 oral** | **[Github](https://github.com/google-research/google-research/tree/master/snerg)**] [Baking Neural Radiance Fields for Real-Time View Synthesis](https://openaccess.thecvf.com/content/ICCV2021/papers/Hedman_Baking_Neural_Radiance_Fields_for_Real-Time_View_Synthesis_ICCV_2021_paper.pdf)

- [ ] [**arXiv 2021** | **[Github](https://github.com/city-super/citynerf)**] [CityNeRF: Building NeRF at City Scale](https://arxiv.org/pdf/2112.05504.pdf)


## Weekly Papers
----------------------------------------------------

- [x] [**ICCV 2021** | **[Github](https://github.com/ChrisWu1997/DeepCAD)**] [DeepCAD: A Deep Generative Network for Computer-Aided Design Models](https://arxiv.org/pdf/2105.09492.pdf)


> This paper presents a deep generative method that outputs the sequence of operations used in CAD tools. DeepCAD considers the most commonly used CAD operations, and unifies them into a common structure that encodes the operation types, parameters and sequential orders. It uses a Transformer-based autoencoder to embed the CAD model into a latent space, and decodes the latent vector into a CAD command sequence. This work also generates a large amount of CAD models by Onshape to train their autoencoder. (The CAD model has two levels of representation: one is the user-interaction level, one the the boundary representation(Brep).)
In DeepCAD, a CAD model is described by a sequence of curve commands interleave with extrusion commands. To overcome the issue that CAD commands differ from the natural language, DeepCAD represents each command into a 16-dimensional vectors, and also fixed the total number of commands in every CAD model. It also unified continuous and discrete parameters by quantizing the continuous parameters, which can improve the generation quality. Leveraging the representation of CAD commands, the autoencoder takes as input a CAD command sequence, and projects commands into the embedding space, then feds the embeddings into an encoder to output a latent vector. At last, DeepCAD used the latent-GAN to automatically generate editable CAD models. The proposed method is benchmarked based on the Command Accuracy (ACCcmd) and Parameter Accuracy (ACCparam). 
The experiments also show the effectiveness the data representation. However, this method performs not good on CAD models that require long commands to describe.

Q: Why failed when command sequences becomes quite long?
A: Not enough training data for long sequences.

- [x] [**CVPR 2021** | **[Github]()**] [uncertainty guided collaborative training for weakly supervised temporal action detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_Uncertainty_Guided_Collaborative_Training_for_Weakly_Supervised_Temporal_Action_Detection_CVPR_2021_paper.pdf)

> This paper deals with the temporal action detection problem. The work proposed an ***Uncertainty Guided Collaborative Training(UGCT)*** strategy that enables the online generation of pseudo ground truth labels and an uncertainty aware learning module that can mitigate the noise in the generated pseudo labels. In the pseudo ground truth generation module, the pseudo labels are generated by a teacher model. The RGB stream and FLOW stream work collaboratively that can learn from each other, as the teacher model in the RGB stream provides pseudo labels for the FLOW stream and the teacher model in the FLOW stream provides pseudo labels for the RGB stream. In the uncertainty prediction module, the uncertainty about the pseudo label is predicted. And this module is removed after training.


- [x] [**ICCV 2021 oral** | **[Github](https://github.com/autonomousvision/unisurf)**] [UNISURF: Unifying Neural Implicit Surfaces and Radiance Fields for Multi-View Reconstruction](http://www.cvlibs.net/publications/Oechsle2021ICCV.pdf)

> This work deals with the neural implicit rendering problem.
The rendering technique of ***neural implicit multi-view reconstruction*** has two mainstream catagories: *surface rendering technique* and *volume rendering technique*. Surface rendering technique can estimate surface geometry accurately, while requires per-pixel object masks and appropriate network initialization, which is limited to small scenes. Volume rendering techniques like NeRF require no input masks, while can only extract surface as level sets of the underlying volume density, which are usually non-smooth and contain artifacts.
UNISURF proposed an unified formulation which combines both the advantages of surface rendering and volume rendering, enabling the reconstruction of accurate geometry from multi-view images without masks. And it adopted a $l_1$ reconstruction loss with a $l_2$ surface regularization term. During optimization, the sampling interval for drawing samples during volume rendering is monotonically decreased. UNISURF is evaluated on the DTU, blended MVS datasets and SceneNet dataset, and achieves state-of-the-art. However, this work is limited on solid and non-transparent surfaces. Besides, the overexposed and texture-less areas can also limit UNISURF's performance, and the reconstructions are less accurate at rarely visible regions in the images. (My question: can this method adapts to larger areas, i.e, city-scale aerial images?)

- [x] [**ECCV 2020**] [Unsupervised Shape and Pose Disentanglement
for 3D Meshes](https://arxiv.org/pdf/2007.11341.pdf)

> The paper addresses the problem of unsupervised disentanglement of
pose and shape for 3D meshes. It used an auto-encoder neural network to auto-encode a mesh in *pose* code and *shape* code. Built upon the cross-consistency and self-consistency. To achieve the cross-consistency constraints, this work generates pairs of different shapes with the exact same pose on the fly during training with our disentangling network. The self-consistency is achieved by generating a proxy mesh $\tilde{X}^t$ with the pose of mesh $X^s_1$ and the shape of mesh $X_t$ within the training loop from two meshes with different shapes and poses $X^s_1$ and $X^t$. An effective disentanglement should recover the original pose code from the proxy mesh. Accordingly, the cross-consistency loss and self-consistency loss are proposed to train the network. At last, this work used the *as-rigid-as-possible Deformation* algorithm to deform $X^t$ to match the pose of the network prediction $\tilde{X}^t$ while preserving the original shape as much as possible. Their model is straightforward to train and it generalizes well across various datasets.
The limitation is that they have no control over specific parts of the mesh with their pose code. And also the interpolation of large torso rotations squeezes the meshes.

- [x] [**NeurIPS 2021** | **[Github](https://github.com/TorchSSL/TorchSSL)**] [FlexMatch: Boosting Semi-Supervised Learning with Curriculum Pseudo Labeling]()

> This paper deals with the semi-supervised learning(SSL) problem. The main contribution of this work is to propose the Curriculum Pseudo Labeling(CPL) approach, which takes into account the learning status of each class for semi-supervised learning. As modern SSL algorithms such as Pseudo-Labeling and Unsupervised Data Augmentation(UDA) rely on a fixed threshold to compute the unsupervised loss, and can only handle all classes equally without considering the different learning difficulties, this work used a initial threshold which can be dynamically adjusted during training. when apply the CPL module into FixMatch, the called FlexMatch method converges faster than FixMatch and achieves SOTA performances on most SSL image classification benchmarks. Specifically, FixMatch uses consistency regularization and data augmentation to improve the training performance, where the unsupervised loss needs a pre-defined threshold. The intuition of Curriculum Pseudo Labeling is that, when the threshold is high, the learning effect of a class can be reflected by the number of samples whose predictions fall into this class and above the threshold. Based on the intuition, CPL proposed a new loss, where the threshold of a well-learned class is raised higher to selectively pick up higher-quality samples as learning proceeds. Besides, more techniques such as threshold warm-up and nonlinear mapping are proposed to improve the performance.