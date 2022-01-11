# Papers in Deep Learning

## Papers to Read

- [ ] **Transformer** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia
Polosukhin. Attention is all you need. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan

- [ ] **Adam** Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization, 2014

- [ ] [**CVPR 2016**] [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf)

- [ ] [**ECCV 2020** | **[Github](https://github.com/princeton-vl/RAFT)**] [RAFT: Recurrent All Pairs Field Transforms for Optical Flow](https://arxiv.org/pdf/2003.12039.pdf)

- [ ] [**ICML 2020** | **[Github](https://github.com/princeton-vl/DeepV2D)**] [Deepv2d: Video to depth with differentiable structure from motion](https://arxiv.org/pdf/1812.04605.pdf)

- [ ] [**CVPR 2017** | **[Github](https://github.com/lmb-freiburg/demon)**] [DeMoN: Depth and Motion Network for Learning Monocular Stereo](https://arxiv.org/pdf/1612.02401.pdf)

- [ ] [**ICLR 2019** | **[Github](https://github.com/frobelbest/BANet)**] [BA-NET: DENSE BUNDLE ADJUSTMENT NETWORKS](https://arxiv.org/pdf/1806.04807.pdf)

- [ ] [**ECCV 2020 oral** | **[Github](https://github.com/weixk2015/DeepSFM)**] [DeepSFM: Structure From Motion Via Deep Bundle Adjustment](https://arxiv.org/pdf/1912.09697.pdf)

- [x] [**arXiv 2021** | **[Github](https://github.com/aliyun/dro-sfm)**] [DRO: Deep Recurrent Optimizer for Structure-from-Motion](https://arxiv.org/pdf/2103.13201.pdf)

> This work deals with the image depth and pose estimation problem by recurrent neural network. The neural optimizer optimizes the image depth and image pose alternatively. At first, DRO uses ResNet-16 to extract the feature maps, the cost is defined so as to minimize the alignment errors between the predicted feature maps. Then, the small update w.r.t. depth $\Delta \mathbf{D}_i$ and pose $\Delta \mathbf{P}_i$ is computed by the ***gated recurrent unit (See RAFT)*** , which are used for alternatively updating the image depth and pose. DRO also used two different loss functions for supervised training and unsupervised training. DRO is superior to ***DeepV2D (See ICML 2020 Deng et, al)*** in memory occupation and computation efficiency.

- [ ] [**ECCV 2020** | **[Github](https://github.com/svip-lab/Indoor-SfMLearner)**] [Patch-match and Plane-regularization for Unsupervised Indoor Depth Estimation](https://arxiv.org/pdf/2007.07696.pdf)

- [x] [**CVPR 2021** | **[Github](https://github.com/hjwdzh/DeepLM)**] [DeepLM: Large-scale Nonlinear Least Squares on Deep Learning Frameworks using Stochastic Domain Decomposition](https://openaccess.thecvf.com/content/CVPR2021/papers/Huang_DeepLM_Large-Scale_Nonlinear_Least_Squares_on_Deep_Learning_Frameworks_Using_CVPR_2021_paper.pdf)

> This paper is not actually using neural network to do the LM method. Instead, it used a method that can gather derivatives for all 
variables to a full jacobian efficiently, which can be analogized with the backpropagation. The main contribution of this work comes 
from this efficient jacobian collection method, which I would rather say it's more an backend architecture than a neural network. Besides, 
the stochastic domain decomposition method seems simply adopted the stochastic clustering method in STBA.

- [ ] [**ICML 2021** | **[Github](https://github.com/johannesbrust/SNLLS)**] [Nonlinear Least Squares for Large-Scale Machine Learning using Stochastic Jacobian Estimates](https://arxiv.org/pdf/2107.05598.pdf)

- [ ] [**CVPR 2021** | **[Github](https://github.com/princeton-vl/lietorch)**] [Tangent Space Backpropagation for 3D Transformation Groups](https://openaccess.thecvf.com/content/CVPR2021/papers/Teed_Tangent_Space_Backpropagation_for_3D_Transformation_Groups_CVPR_2021_paper.pdf)

- [ ] [**ICCV 2021 Best Student Paper** | **[Github](https://github.com/cvg/pixel-perfect-sfm)**] [Pixel-Perfect Structure-from-Motion](https://arxiv.org/pdf/2108.08291.pdf)

- [ ] [**3DV 2021** | **[Github](https://github.com/JingwenWang95/DSP-SLAM)**] [DSP-SLAM: Object Oriented SLAM with Deep Shape Priors](https://arxiv.org/pdf/2108.09481.pdf)

- [ ] [**arXiv 2021** | **[Github]()**] [Gradient-SDF: A Semi-Implicit Surface Representation for 3D Reconstruction](https://arxiv.org/pdf/2111.13652.pdf)

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


Last week I read some deep learning materials and some papers.