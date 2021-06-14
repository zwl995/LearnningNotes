# Structure from Motion

## 问题

(1) 相机姿态的优化方式

以rotation averaging为例：

1）文章的section 4.2中提到：“In the first iteration of local motion averaging, we follow the traditional motion averaging pipeline revisited in Section 3 to reconstruct camera rotations or translations of each partition.”这句话很明白, 加上后文的理解，其实他们就是在有了很多个partition之后，每个partition先做local incremental SfM，然后local motion averaging的第一次优化时，用传统的motion averaging方法优化相机姿态。

2）接着，“From the second iteration, we optimize the intra-camera poses while fixing all the inter-camera poses and similarity transformations.” 

 这里的intra-camera就是partition内部的相机，inter-camera是“the cameras that connecting multiple sub-graphs.”，可以把inter-camera理解为边界处的相机，这些相机连接着其他子图。也就是他们先固定边界处的相机和相似变换参数，在local motion averaging第二次优化的时候，只优化每个partition中所有非边界处的相机。结合Section 4.4 中local rotation averaging中的内容，误差项分为L_intra和L_betw，L_intra比较好理解，但是L_betw的公式（8）这里：R_i^k(Q^k)^T将partition中非边界处的相机在局部坐标系中的旋转变换到全局坐标系，但是边界处的相机R_j没有进行变换，这说明R_j已经位于全局坐标系了。这里这样做的intuition不明白，为什么要分成边界处和非边界处的相机进行优化？还有，1）的时候不是已经用local motion averaging优化了一遍吗？如果只做1）但是不做2）会和两个都做有什么区别？




3）“In the global motion averaging, the inter-camera poses and similarity transformations asocitated with each partition are optimized by the inter-relative-poses with all the intra-camera poses fixed in their local coordinate frames.”. 这次固定非边界处的相机姿态，优化相似变换和边界处的相机姿态。


整个相机姿态的优化方式就让我很困惑：如果做了global motion averaging的话，local motion averaging还有必要吗？只做global不做local的差别在哪？为什么要进行边界和非边界处的相机这样的划分方式来进行优化(初步理解是边界处的相机需要收到其他partition的约束)。


- （2）一些小问题.
Section 4.3中Global rotation averaging中的最后一句话：“We set the rotation of any one camera R_i = I_(3x3) to fix the gauge freedom”，以及Section 4.5节Global translation averaging最后一句话：“We fix the gauge freedom by setting the position of any one camera c_i = 0_(3x1) and the scale of any one similarity transformation alpha^k = 1”

这两句话都没太明白。


（3）这篇文章做大规模SfM的时候，相似变换之后使用了motion averaging, 但是也没对比使用motion averaging前后的差别。

我那篇投CVPR 2019的文章中，给strong reject的reviewer说我的方法速度块的原因是我graph merging之后并没有考虑loop closure的约束进行优化，否则会有drift出现。

猜想这篇文章这么做也是为了解决drift的问题，因为motion averaging本来就能解决这一问题。但是都没有实验对比。

## References

[1] Zhu S , Zhang R , Zhou L , et al. Very Large-Scale Global SfM by Distributed Motion Averaging[C]// 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, 2018.