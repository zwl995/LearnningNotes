# Structure from Motion Papers

## 1. Incremental Structure from Motion
- [x] [[3DV 2013] Towards Linear-time Incremental Structure from Motion](http://ccwu.me/vsfm/vsfm.pdf)

第一次提出 ```Retriangulate``` 的概念来尝试解决incremental SfM中的drift.
由于初始的相机姿态和经过BA之后的姿态可能都不够准，一些正确的匹配在triangulate的时候失败了。而这些正确匹配的累计丢失是造成
drift的一个主因。

为了解决这个问题，```VSFM```提出对失败的匹配进行 ```re-triangulate(RT)```。```RT```的时候，需要选择相机对。

怎么识别不好的相机姿态: 两个相机之间的公共三维点和匹配点数目的比例太低。这样的相机对被称为```under-recontructed```。
为了使得相机姿态更稳定，需要对这些```under-reconstructed```的相机进行re-triangulate。为了得到更多的点，冲投影误差的阈值加大。
从上到下为```Without RT```、```With RT``` :
![](img/retriangulate.png)

---------------------------------------------------------------------------------------------------
- [x] [[CVPR 2016] Structure-from-Motion Revisited](https://demuc.de/papers/schoenberger2016sfm.pdf)


---------------------------------------------------------------------------------------------------
- [x] [[3DV 2017] Batched Incremental Structure-from-Motion](ir.ia.ac.cn/bitstream/173211/19771/1/HainanCui_3DV2017.pdf)

主要贡献点在于```batched camera registration```和```batched tracks selection```。

(1) 不同于COLMAP，在对相机进行注册的时候不再考虑使用next view selection的策略，而是把有足够多2D-3D点对的相机批量式(batched)进行注册。
这样做的原因是: incremental SfM的误差是累积的，更早注册的相机要比后注册的相机姿态更为准确。

(2) batched tracks selection的意思是，在每个相机注册的步骤，不再考虑所有的track，而是仅把track的一部分进行选择并且优化。
对于大规模重建了来说，track通常是冗余的并且对于BA来说既耗内存也耗时间。为了保证下一个相机注册的成功率，track的选择有三个原则:
- 包含已标定的相机，来优化它们的姿态
- 包含将要在下一个步骤中进行标定的相机
- 更长的track应该优先选择

在进行增量重建的过程中，不使用匹配点而使用track。原因:
- track的长度通常比较长，使用track能够在相机注册的时候得到更多的候选。
- track构建的时候，很多错误的匹配已经被筛选出来了。
- track是feature match的集合，相比feature match来说更可信。

流程如下：

![pipeline](img/pipeline.png)

#### 1. Batched Seed Selection

初始对的选取原则：
(1) 能看到尽可能多的相机
(2) 宽基线

##### 细节
在构造```Epipolar Graph```的时候，先用初始的```EG```中的相对相机姿态通过```rotation averaging(RA)```计算出global的相机姿态。然后通过计算$$acos(||R_{ij} - R_jR_i^T||_F)$$ 来将误差大的边删除，然后相对旋转通过 $$R_{ij}=R_jR_i^T$$重新计算得到。然后，对于EG中的每条边，通过 $\rho_{ij} = min(n_i, n_j)$ 来表示与至相邻的相机密度, 其中$n_i$是相机$i$在EG中相邻相机的个数。最后，得到以 $\rho_{ij}$ 的大小为优先级的候选```seeds```.

#### 2. Batched Camera Registration
所有能够看到大于12个三维点的相机都考虑为候选标定相机，然后```RANSAC + P3P```计算初始相机姿态，最后加```bundle adjustment```优化。这时固定三维点和内参，只对外参进行优化。

#### 3. Tracks Triangulation and Selection

使用track作为输入，每次选两个相机，使用```RANSAC + Triangulation```来计算三维点。一个较为稳定的三维点应满足:
- 投影回图像平面的两条射线的家教应该大于 $2^{\degree}$
- 满足cheirality约束(在相机前方，具有正的深度值)

为了提高效率，不使用所有的track，而是找track的子集，这些track需要对每个相机至少包含 $K$ 次

#### 4. Batched Bundle Adjustment

#### 5. Iterative Re-triangulation and Re-selection
#### 结果
![](img/result1.png)
![](img/result2.png)
![](img/result3.png)

--------------------------------------------------------------------------------------------------

## 2. Global Structure from Motion

## 3. Hierarchical Structure from Motion

## 4. Hybrid Structure from Motion
- [x] [[ACCV 2014] Divide and Conquer: Efficient Large-Scale Structure from Motion Using Graph Partitioning]()

- [x] [[arXiv 2017] Parallel Structure from Motion from Local Increment to Global Averaging](https://arxiv.org/pdf/1702.08601.pdf)

- [x] [[CVPR 2018] Very Large-scale Global SfM by Distributed Motion Averaging](https://www.cs.sfu.ca/~pingtan/Papers/cvpr18sfm.pdf)