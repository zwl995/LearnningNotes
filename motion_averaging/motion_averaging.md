<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# Motion Averaging

<u>**注(重要)**: Motion Averating 必然涉及到`旋转 (rotation)`，关于`旋转`的一些性质及运算请见 [Rotation](rotation.md)</u>

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

## 1. Motion Averaging 进化史

给定 $N$ 张图片，全局运动可以用 $N-1$ 个运动模型描述。两个相机之间的相对运动关系可以通过对极几何估计`本质矩阵(Essential Matrix)`，再进行矩阵分解(对本质矩阵的奇异值分解)得到。由公式(4)，我们可以通过相对相机运动来估计全局相机运动模型。如果每对图片之间都有足够的重叠，那么我们可以得到 $\frac{N(N-1)}{2}$ 对约束(虽然实际上不可能存在这么多对，但一般也存在远多于 $N$ 的约束)。

现在，问题描述可以简化为，对于给定的 $\{M_{ij}\}$ 对相对运动模型，如何估计 $N$ 个相机运动模型 $\{ M_1, M_2, ..., M_N\}$.

### 1.1 线性拟合模型
令$\hat{M}_{ij}$ 是所估计的 $i$ 到 $j$ 的相对运动，由之前的介绍，我们有
$$
\hat{M}_{ij}M_i - M_j = 0, \forall i \not= j
$$
我们可以重写为
$$
\left[
\begin{array}{}
\cdots\ \hat{M}_{ij}\ \cdots\ -I\ \cdots
\end{array}
\right]
\left[
    \begin{array}{c}
        \vdots\\
        M_i\\
        \vdots\\
        M_j\\
        \vdots
    \end{array}
\right]=0
$$
直观地，我们可以通过最小二乘来估计与$\{M_{ij}\}$拟合的最好的$\{M_i\}$。因此，<u>每对独立的相对运动的估计$M_{ij}$的误差通过这样一种方式被**平均 (averaged out)**</u>了。

#### 估计旋转

#### 估计平移

### 1.2 Rotation Averaging 在李代数上的线性模型求解

关于旋转的一些性质已经在 [三维重建中的旋转(Rotation)](rotation.md) 里提及，包括李代数等。
现在由公式 (4.a)，我们重新考虑我们要求解的问题。给定参考系和一系列相对旋转 $R_{ij}$，我们希望求解 $R_{global} = {R_1, ..., R_N}$。我们希望最小化代价函数:
$$
arg\ min\ \sum_{(i,j)\in \varepsilon} d^2(R_{ij}, R_jR_i^{-1}) \tag{}
$$
现在我们考虑使用李代数来进行优化, $R_{ij} = exp([\boldsymbol{w_{ij}}]_{\times}), R_i = exp([\boldsymbol{w_{i}}]_{\times})$，其中 $\boldsymbol{w_{ij}}$ 和 $\boldsymbol{w_{i}}$ 分别为 $R_{ij}$ 和 $R_i$ 对应的李代数。 

假设只考虑其中一对关系 $R_{ij} = R_jR_i^{-1}$。由 BCH 公式： $BCH(x, y) = x + y + \frac{1}{2}[x, y] + \frac{1}{12}[x - y, [x, y]] + o(|(x, y)|^4)$，若只采用BCH公式的一阶估计 $BCH(x, y) \approx x + y$，则

$$
\boldsymbol{w_{ij}} = BCH(\boldsymbol{w_{j}}, -\boldsymbol{w_{i}}) = \boldsymbol{w_{j}} - \boldsymbol{w_{i}}
$$

## References