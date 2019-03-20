<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# Motion Averaging

首先来推几个公式: 假设已知两个相机在全局坐标系下的运动，那么这两个相机之间的相对运动是怎样的关系呢？

已知点$P$在世界坐标系中的坐标，记为$P_0$。对于两个不同的相机$i$和$j$，对应于全局坐标系中的旋转和平移分别为$R_i, t_i, R_j, t_j$。将点$P_0$分别投影到相机i和j的坐标系，那么：
$$
P_i = R_iP_0 + t_j\ (1.a) \\ 
P_j = R_jP_0 + t_j\ (1.b)
$$
由公式(1.a)我们可以得到
$$P_0 = R_i^{-1}(P_i - t_i)\ (2) $$
将公式(2)代入(1.b)中，有
$$
P_j = R_j(R_i^{-1}(P_i - t_i)) + t_j\\
\ = R_jR_i^{-1}P_i + (t_j - R_jR_i^{-1}t_i)\ (3)
$$
由公式(3)我们可以得到相机$i$到相机$j$的相对运动关系:
$$
R_{ij} = R_jR_i^{-1} = R_jR_i^{T}\ (4.a)\\
t_{ij} = t_j - R_jR_i^{-1}t_i = t_j - R_{ij}t_i\ (4.b)
$$
这里需要注意的是 ***$R_{ij}$ 和 $t_{ij}$是相机 $i$ 相对于 $j$ 的运动***，很多论文在提及相机$i$和相机$j$之间的相对运动关系时会用**between**，但是实际上是有方向的。

所有的motion averaging方法都是基于公式(4)进行的。

## Very Large-Scale Global SfM by Distributed Motion Averaging



## References