# Papers in Deep Learning

## Papers to Read

- [ ] **Transformer** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia
Polosukhin. Attention is all you need. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan

- [ ] **Adam** Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization, 2014


- [ ] [**CVPR 2021** | **[Github](https://github.com/hjwdzh/DeepLM)**] [DeepLM: Large-scale Nonlinear Least Squares on Deep Learning Frameworks
using Stochastic Domain Decomposition](https://openaccess.thecvf.com/content/CVPR2021/papers/Huang_DeepLM_Large-Scale_Nonlinear_Least_Squares_on_Deep_Learning_Frameworks_Using_CVPR_2021_paper.pdf)

- [ ] [**ICCV 2021 Best Student Paper** | **[Github](https://github.com/cvg/pixel-perfect-sfm)**] [Pixel-Perfect Structure-from-Motion](https://arxiv.org/pdf/2108.08291.pdf)

- [ ] [**3DV 2021** | **[Github](https://github.com/JingwenWang95/DSP-SLAM)**] [DSP-SLAM: Object Oriented SLAM with Deep Shape Priors](https://arxiv.org/pdf/2108.09481.pdf)


## Weekly Papers
----------------------------------------------------

- [x] [**ICCV 2021** | **[Github](https://github.com/ChrisWu1997/DeepCAD)**] [DeepCAD: A Deep Generative Network for Computer-Aided Design Models](https://arxiv.org/pdf/2105.09492.pdf)


> This paper presents a deep generative method that outputs the sequence of operations used in CAD tools. DeepCAD considers the most commonly used CAD operations, and unifies them into a common structure that encodes the operation types, parameters and sequential orders. It uses a Transformer-based autoencoder to embed the CAD model into a latent space, and decodes the latent vector into a CAD command sequence. This work also generates a large amount of CAD models by Onshape to train their autoencoder. (The CAD model has two levels of representation: one is the user-interaction level, one the the boundary representation(Brep).)
In DeepCAD, a CAD model is described by a sequence of curve commands interleave with extrusion commands. To overcome the issue that CAD commands differ from the natural language, DeepCAD represents each command into a 16-dimensional vectors, and also fixed the total number of commands in every CAD model. It also unified continuous and discrete parameters by quantizing the continuous parameters, which can improve the generation quality. Leveraging the representation of CAD commands, the autoencoder takes as input a CAD command sequence, and projects commands into the embedding space, then feds the embeddings into an encoder to output a latent vector. At last, DeepCAD used the latent-GAN to automatically generate editable CAD models. The proposed method is benchmarked based on the Command Accuracy (ACCcmd) and Parameter Accuracy (ACCparam). 
The experiments also show the effectiveness the data representation. However, this method performs not good on CAD models that require long commands to describe.

Q: Why failed when command sequences becomes quite long?
A: Not enough training data for long sequences.
