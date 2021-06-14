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
\right]=0 \tag{5}
$$
直观地，我们可以通过最小二乘来估计与$\{M_{ij}\}$拟合的最好的$\{M_i\}$。因此，<u>每对独立的相对运动的估计$M_{ij}$的误差通过这样一种方式被**平均 (averaged out)**</u>了。

#### 估计旋转

#### 估计平移

### 1.2 Rotation Averaging 在李代数上的线性模型求解

关于旋转的一些性质已经在 [三维重建中的旋转(Rotation)](rotation.md) 里提及，包括李代数等。
现在由公式 (4.a)，我们重新考虑我们要求解的问题。给定参考系和一系列相对旋转 $R_{ij}$，我们希望求解 $R_{global} = {R_1, ..., R_N}$。我们希望最小化代价函数:
$$
arg\ min\ \sum_{(i,j)\in \varepsilon} d^2(R_{ij}, R_jR_i^{-1}) \tag{6}
$$
现在我们考虑使用李代数来进行优化, $R_{ij} = exp([\boldsymbol{w_{ij}}]_{\times}), R_i = exp([\boldsymbol{w_{i}}]_{\times})$，其中 $\boldsymbol{w_{ij}}$ 和 $\boldsymbol{w_{i}}$ 分别为 $R_{ij}$ 和 $R_i$ 对应的李代数。 

假设只考虑其中一对关系 $R_{ij} = R_jR_i^{-1}$。由 BCH 公式： $BCH(x, y) = x + y + \frac{1}{2}[x, y] + \frac{1}{12}[x - y, [x, y]] + o(|(x, y)|^4)$，若只采用BCH公式的一阶估计 $BCH(x, y) \approx x + y$，则

$$
\boldsymbol{w_{ij}} = BCH(\boldsymbol{w_{j}}, -\boldsymbol{w_{i}}) = \boldsymbol{w_{j}} - \boldsymbol{w_{i}}
$$

令全局坐标系下旋转的李代数表示为 $\boldsymbol{\omega}_{global} = [\boldsymbol{\omega}_1, \cdots, \boldsymbol{\omega}_N]^T$，那么我们有
$$
\boldsymbol{w_{ij}} = \boldsymbol{w_{j}} - \boldsymbol{w_{i}} = 
\left[
\begin{array}{cccc}
\cdots & -I & \cdots & I & \cdots
\end{array}
\right]
\boldsymbol{w_{global}}
= A_{ij}\boldsymbol{w_{global}} \tag{7}
$$
在 $A_{ij}$ 中，$I$ 和 $_I$ 为在 $i$ 和 $j$ 处的 $3\times 3$ 的块矩阵。把所有的相对运动关系拼合起来，我们有
$$
A\boldsymbol{w_{global}} = \boldsymbol{w_{rel}} \tag{8}
$$

其中 $\boldsymbol{w_{rel}}$ 是把所有 $\boldsymbol{w_{ij}}$ 拼接起来的向量，$A$ 是把所有 $A_{ij}$ 堆叠在一起的矩阵。方程(8)可以通过以下算法求解:
```cpp
// Algorithm1: Lie-Algebraic Relative Rotation Averaging
// Input: {R_{ij1}, ..., R_{ijk}} (relative rotations)'
// Output: R_{global} = {R_1, ..., R_N} (absolute rotations)
// Initialization: R_{global} to an initial guess
while (||delta_w_rel|| < epsilon) {
    delta_R_ij = R_j.inverse() * R_ij * R_i; // step (1)
    delta_w_ij = log(delta_R_ij);            // step (2)
    Solve(A * delta_w_global) = delta_w_rel; // step (3)
    for (int k = 0; k < N; k++) {
       R_k = R_k * exp(delta_w_k);           // step (4)
    }
}
```
在算法1中，观测值 $R_{ij}$ 和使用 $R_jR_i^{-1}$计算的估计值之间的误差在李代数上被average了。求解完 step (3) 之后，每个全局的旋转 $R_k$ 都通过指数映射更新了 (step (4)里)。需要注意的是：在实践中会将其中的一个旋转设为单位阵来移除 gauge freedom。
之后的有些做法会在使用最小二乘最小化 step (3) 的 $l_2$-范数，但是最小二乘是不鲁棒的，有时即使仅存在一个outlier，都有可能给出非常不正确的结果。而 outlier 在三维重建中是普遍存在的。对于 relative rotation averaging来说，$l_1$ 范数比 $l_2$ 范数更为鲁棒，因此 step (3) 将在 $l_1$-范数下最小化。


#### 1.2.1 $l_1$ Rotation Averaging
由于李代数是一个向量空间，因此对于李代数上的 rotation averaging，我们可以类比为线性方程组的鲁棒估计。

考虑非齐次线性方程组 $A\boldsymbol{x} = \boldsymbol{b}$，其中 $\boldsymbol{x} \in \mathbb{R}^n, \boldsymbol{b} \in \mathbb{R}^m$，并且 $m > n$。这个方程的求解难度由于噪声和外点的存在发生了改变，比如 $\boldsymbol{b} = A\boldsymbol{x} + \boldsymbol{e} $。在压缩感知方向的一些研究表明，在外点存在的情况下，$\boldsymbol{x}$ 可以通过以下公式高效精确地求解：
$$
arg\ min\ ||A\boldsymbol{x} - \boldsymbol{b}||_{l_1} \tag{9}
$$ 

如果我们考虑相对运动的观测值存在外点的情况下，我们有 $\triangle w_{rel} = A\triangle w_{global} + \boldsymbol{e}$ 。在算法1中，step (3) 使用公式(9)求解，这个算法被称为 <u>$l_1$ Robust Rotation Averaging (`L1RA`) 算法</u>。需要注意的是，$A$ 的每行只有 $\{-1, +1\}$ 两个非零元素，因此矩阵 $A$ 非常稀疏。

#### 1.2.2 鲁棒最小二乘和 IRLS Rotation Averaging
尽管1.2.1中的 `L1RA`算法可以在存在外点的情况下鲁棒地求解，我们仍然可以把鲁棒rotation averaging问题当成最小二乘估计下的鲁棒回归(robust regression)或M-估计(M-estimator)。

##### 鲁棒最小二乘和 IRLS 问题
常规的最小二乘对其中噪声符合高斯分布的观测值来说是一个合适的选择，然而在对应点中有外点时，需要更鲁棒的最小二乘。这种情况下，最好用M-估计(M-estimator)，它对残差施加一个鲁棒惩罚函数 $\rho (r) $ (也称为 `loss function`)
$$
E_{RLS(\triangle \boldsymbol{x})} = \sum_{i} \rho(||\boldsymbol{r}_i||) \tag{10}
$$
来代替它们的平方
$$
E_{LS(\triangle \boldsymbol{x})} = \sum_{i} ||\boldsymbol{r}_i||_2^2 \tag{11}
$$
公式(10)对$\boldsymbol{x}$求偏导，则有
$$
\sum_{i} \frac{\partial \rho (||\boldsymbol{r}_i||)}{\partial ||\boldsymbol{r_i}||} \cdot\frac{\partial ||\boldsymbol{r}_i||}{\partial \boldsymbol{x}}\\
= \sum_i \frac{\partial \rho (||\boldsymbol{r}_i||)}{\partial ||\boldsymbol{r_i}|| \cdot ||\boldsymbol{r}_i||} \cdot \boldsymbol{r}_i^T \frac{\partial ||\boldsymbol{r}_i||}{\partial \boldsymbol{x}}\\
= \sum_i \frac{\Psi (||\boldsymbol{r}_i||)}{||\boldsymbol{r}_i||} \cdot \boldsymbol{r}_i^T \frac{\partial ||\boldsymbol{r}_i||}{\partial \boldsymbol{x}} \ \ \ \ \ \ \ \\
= \sum_i w(||\boldsymbol{r}_i||) \cdot \boldsymbol{r}_i^T \frac{\partial ||\boldsymbol{r}_i||}{\partial \boldsymbol{x}} = 0 \ \ \tag{12}
$$

其中 $\Psi (||\boldsymbol{r}_i||) = \frac{\partial \rho (||\boldsymbol{r}_i||)}{\partial ||\boldsymbol{r_i}||}$，称为`影响函数 (influence function)`，$w(r) = \frac{\Psi(r)}{r}$ 称为`加权函数(weight function)`。可以看出用公式(12)求解 (10)的极小值等于最小化`迭代重加权最小二乘 (Iteratively Reweighted Least Squares, IRLS)问题`
$$
E_{IRLS} = \sum_i w(||\boldsymbol{r}_i||)||\boldsymbol{r}_i||^2 \tag{13}
$$
其中 $w(||\boldsymbol{r}_i||)$ 起着局部加权作用。IRLS 算法在计算影响函数 $w(||\boldsymbol{r}_i||)$ 和求解得到的加权最小二乘问题(固定的 $w$ 值) 之间交替。M-estimator 一定能够减少外点的影响，但是在一些情况中，从太多外点起步的话会使得 IRLS(或者其他梯度下降算法) 不能收敛到全局最优。

#### IRLS Rotation Averaging
现在考虑使用 IRLS 算法来求解 Rotation Averaging 问题，令残差为$\boldsymbol{e} = A\boldsymbol{x} - \boldsymbol{b}$，我们希望最小化鲁棒代价函数
$$
E_{RLS} = \sum_i \rho(||\boldsymbol{e}_i||) \tag{14}
$$
这里，loss function 选则 Huber-like loss function: $\rho(x) = \frac{x^2}{x^2 + \sigma^2}$。因此，
$$
min\ E_{RLS} = min\ \sum_i \rho(||\boldsymbol{e}_i||) = min\ \sum_i \frac{\boldsymbol{e}_i^2}{\boldsymbol{e}_i^2 + \sigma^2} \tag{15}
$$
公式(15)对 $\boldsymbol{x}$ 求偏导，有
$$
\frac{\partial E_{RLS}}{\partial \boldsymbol{x}} = \frac{\partial E_{RLS}}{\partial \bold{e}} \cdot \frac{\partial \boldsymbol{e}}{\partial \boldsymbol{x}} \qquad \qquad \qquad \qquad \ \\
= \frac{2||\boldsymbol{e}_i||(||\boldsymbol{e}_i||^2 + \sigma^2) - 2||\boldsymbol{e}_i||\cdot ||\boldsymbol{e}_i||^2}{(||\boldsymbol{e}_i||^2 + \sigma^2)^2} \cdot A^T\\
= \frac{2||\boldsymbol{e}_i||\sigma^2}{(||\boldsymbol{e}_i||^2 + \sigma^2)^2} \cdot A^T \qquad \qquad \qquad \qquad \quad \\
= \frac{2(A\boldsymbol{x}-b)\sigma^2 A^T}{(||\boldsymbol{e}_i||^2 + \sigma^2)^2} \qquad \qquad \qquad \qquad \qquad \\
= 2 \cdot \frac{A^T \sigma^2A\boldsymbol{x}- A^T\sigma^2b}{(||\boldsymbol{e}_i||^2 + \sigma^2)^2} = 0 \qquad \qquad \qquad\  \tag{16}
$$

因此，有
$$
A^T\Phi(\boldsymbol{e})A\boldsymbol{x} - A^T\Phi(\boldsymbol{e}) \boldsymbol{b} = 0\ \Rightarrow \\
A^T\Phi(\boldsymbol{e})A\boldsymbol{x} = A^T\Phi(\boldsymbol{e}) \boldsymbol{b} \tag{17}
$$
其中，$\Phi(\boldsymbol{e})$ 是对角阵并且 $\Phi(i, i) = \frac{\sigma^2}{(\boldsymbol{e}_i^2 + \sigma^2)^2}$ 。
由公式 (13), RLS 问题可以转变为求解 IRLS 问题： $min\ (A\boldsymbol{x} - \boldsymbol{b})^T\Phi(A\boldsymbol{x} - \boldsymbol{b})$，由公式 (17) 知，其最优点为 $$\boldsymbol{x} = (A^T \Phi A)^{-1} A^T \Phi \boldsymbol{b} \tag{18}$$ 。在 IRLS 中，我们先固定$\boldsymbol{x}$，然后计算 $\Phi$；接着固定 $\Phi$ (由公式 (18) 计算得到)。通过这样一个交替的方式直到收敛。IRLS 算法见算法2.

```cpp
// Alogrithm2: Iteratively Reweighted Least Squares (IRLS)
// set x to initial guess
while (||x - x_prev|| < epsilon) {
    x_prev = x;                                             // step (1)
    e = A * x - b;                                          // step (2)
    Phi = Phi(e);                                           // step (3)
    x = (A.tranpose() * Phi * A).inverse() * A * Phi * b;   // step (4)
}
```
前面提到，如果没有一个好的初值的话，`IRLS` 算法很有可能不能收敛到全局最优，而由于 `L1RA` 算法对于 $R_{gobal}$ 来说足够提供一个好的初值，因此 `L1RA` 算法的输出可以作为 `IRLS` 算法的输入。到这里，我们可以直到，整个使用 $l_1$-范数求解 Rotion Averaging 问题的算法(L1-IRLS)可以分为两步: (1) `L1RA`算法求解 $R_{global}$ 的初值；（2）$R_{global}$ 的初值作为 `IRLS` 的输入，使用算法2求解得到最终的 $R_{global}$ 。

### 1.3 Robust Relative Rotation Averaging
对于 Robust Rotation Averaging 问题
$$
arg\ min\ \sum_{(ij)\in \epsilon} \rho(d(R_{ij}, R_jR_i^{-1})) \tag{19}
$$
重新考虑我们需要最小化的代价函数，我们选择 `geodesic distance` (也称为 `angular distance`)。接下来，我们将推导在此代价函数下的 IRLS 算法。
令 $\boldsymbol{\omega}(R)$ 为 $R$ 的角轴表示，$\triangle R_{ij} = R_j^{-1}R_{ij}R_i$ 表示相对运动的观测值 $R_{ij}$ 和当前的估计值 $R_jR_i^{-1}$ 之间的误差, 则
$$
arg\ min\ \sum_{(ij)\in \epsilon} \rho(d(R_{ij}, R_jR_i^{-1})) \\
= arg\ min\ \sum_{(ij)\in \epsilon} \rho(||\boldsymbol{\omega}(R_j^{-1}R_{ij}R_i)||)) \\
= arg\ min\ \sum_{(ij)\in \epsilon} \rho(||\boldsymbol{\omega}(\triangle R_{ij})||)) \tag{20}
$$

设当前估计值 $R_v = \{R_1, \cdots, R_N\}$，当前迭代中 $R_v$ 的增量为 $\{\triangle R_1, \cdots, \triangle R_N\}$，更新之后新的估计值为 $\{R_1\triangle R_1, \cdots, R_N\triangle R_N\}$。因此，在一个给定的迭代中，我们的目标是最小化
$$
arg\ min\ \sum_{(ij)\in \epsilon} \rho(||\boldsymbol{\omega}(\triangle R_j^{-1} \triangle R_{ij} \triangle R_i)||)) \tag{21}
$$

令全局旋转的更新值 $\triangle R_i$ 对应的角轴表示记为 $\triangle \boldsymbol{\omega}_i$。将所有的这些向量连接成一个 $3N \times 1$ 的向量 $\triangle \boldsymbol{\Omega}_{\nu} = [\omega_1^T, \cdots, \triangle \omega_N^T]^T$。同样地，对每个残差 $\triangle R_{ij}$，对应的角轴表示记为 $\triangle \omega_{ij}$，把所有的这些向量连接成一个 $3 \times M$ 的向量 $\triangle \boldsymbol{\Omega}_{\epsilon}$。公式 (20) 便转化成寻找 $\boldsymbol{\Omega}_{\nu}$ 来最小化如下函数:
$$
F(\boldsymbol{\Omega}_{\nu}) = \sum_{(i,j) \in \epsilon} \rho(||\boldsymbol{\omega}(R(-\triangle\omega_j)R(\triangle \omega_{ij}) R(\triangle \omega_i))||) \\
= \sum_{(i,j) \in \epsilon} \rho(||\boldsymbol{r}_{ij}(\triangle \Omega_{\nu})||) \qquad \qquad \qquad \tag{22}
$$
其中 $R(\omega)$ 是李代数到旋转矩阵的指数映射，$$\boldsymbol{r}_{ij}(\triangle \Omega_{\nu}) = \boldsymbol{\omega}(R(-\triangle\omega_j)R(\triangle \omega_{ij}) R(\triangle \omega_i)) \tag{23}$$
接着，我们把公式 (10) 到 公式 (12) 的推导过程再做一遍:
$$
\nabla F(\triangle \boldsymbol{\Omega}_{\nu}) = \sum_{(i,j) \in \epsilon} \nabla \rho (||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||) \qquad \qquad \qquad \qquad \qquad \quad \qquad\qquad \\
= \sum_{(i,j) \in \epsilon} \frac{\partial \rho(||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||)}{\partial ||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||} \cdot \frac{\partial ||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||}{\partial (\triangle \boldsymbol{\Omega}_{\nu})} \qquad \quad \\
= \sum_{(i,j) \in \epsilon} \psi (||\boldsymbol{r}_{ij} (\triangle \boldsymbol{\Omega}_{\nu})||) \cdot \nabla (||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||) \qquad \quad \tag{24}
$$
其中，$\psi(r) = \frac{\partial \rho(r)}{\partial r}$为`影响函数 (influence function)`。
为了推导出形如 (13) 一样最小二乘表示，令 $\phi(||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||) = \frac{\psi (||\boldsymbol{r}_{ij} (\triangle \boldsymbol{\Omega}_{\nu})||)}{||\boldsymbol{r}_{ij} (\triangle \boldsymbol{\Omega}_{\nu})||}$。因此，有
$$
\nabla F(\triangle \boldsymbol{\Omega}_{\nu}) \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad  \\ 
= \frac{1}{2} \sum_{(i,j) \in \epsilon} \phi (||\boldsymbol{r}_{ij} (\triangle \boldsymbol{\Omega}_{\nu})||) \cdot 2||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})|| \cdot \nabla (||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||) \\
= \frac{1}{2} \sum_{(i,j) \in \epsilon} \phi (||\boldsymbol{r}_{ij} (\triangle \boldsymbol{\Omega}_{\nu})||) \cdot \nabla (||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||^2) \qquad \qquad \qquad \tag{25}
$$
由于我们使用 IRLS 优化，因此，在每一步迭代中，$\phi (||\boldsymbol{r}_{ij} (\triangle \boldsymbol{\Omega}_{\nu})||)$ 可以看作常量，并且令 $\phi (||\boldsymbol{r}_{ij} (\triangle \boldsymbol{\Omega}_{\nu})||) = \phi (||\boldsymbol{r}_{ij} (0)||) = \phi_{ij}$。因此，问题 (25) 很容易转化为求解以下最小二乘问题
$$
min\ \sum_{(i,j) \in \epsilon} \phi_{ij}\ ||\boldsymbol{r}_{ij}(\triangle \boldsymbol{\Omega}_{\nu})||^2 \tag{26}
$$
在每一步迭代中，我们在最开始的时候计算一次 $\phi_{ij} = \phi (||\boldsymbol{r}_{ij} (0)||)$。因此，relative rotation averaging 问题就转化成了一个`迭代重加权最小二乘问题`。

可以证明，非线性问题 (26) 的 Gauss-Newton 优化等价于线性最小二乘的最小化问题: $(\sqrt{\Phi}A \triangle \boldsymbol{\Omega}_{\nu} + \sqrt{\Phi} \triangle \boldsymbol{\Omega}_{\epsilon})^2$。因此，类比于 (18)，我们的更新步骤可以写为 
$$
\triangle \Omega_{\nu} = -(A^T \Phi A)^{-1} A^T\Phi\triangle \Omega_{\epsilon} \tag{27}
$$

现在，我们可以总结一下该方法: <u>我们从一个我们需要迭代求解的非线性代价函数开始(公式 (19))，然后考虑每步迭代过程中的更新方式，从而引出公式(9)的最小化问题。通过将公式 (9) 的导数设为0，问题可以转化为一个 `IRLS` 问题。最后，该非线性问题可以通过 `IRLS` 的线性最小二乘形式求解，也即公式 (27)</u>。该求解 Robust Relative Rotatio Averaging 的问题在算法3中总结。

```cpp
// Algorithm 3: Relative Rotation Averaging with iteratively reweighted lease squares
// Input: Set of relative rotation measurements {R_ij} for ij \in \varepsilon，tolerance \epsilon,
//        maximum iterations N_max
// Output: Set of absolute rotations R_v = {R_1, ..., R_N}
// Initialization: Set R_v = {R_1, ..., R_N} to an initial guess. Set iteration number k = 1
while (delta_Omega_nu > epsilon && k < N_max) {
    delta_omega_ij = omega(R_j.inverse() * R_ij * R_i);
    // Collect delta_omega_ij into delta_Omega_epsilon;
    phi_ij = phi(r_ij(0)); // r_ij is defined in equation (23)
    delta_Omega_nu = -(A.transpose() * Phi * A).inverse() * A.transpose() * Phi * delta_Omega_epsilon;
    for (int i = 0; i < N; i++) R[i] = R[i] * R(delta_omega_i);
    k += 1;
}
```

和 1.2 节一样，`IRLS` 算法要求一个较好的初值，因此，需要像 1.2 节中那样，使用算法1求解初值，再将初值作为算法3的输入进行求解即可。

## References

- Govindu V M . Combining two-view constraints for motion estimation[C]// Computer Vision and Pattern Recognition, 2001. CVPR 2001. Proceedings of the 2001 IEEE Computer Society Conference on. IEEE, 2001.

- Govindu V M . Lie-Algebraic Averaging for Globally Consistent Motion Estimation[C]// null. IEEE Computer Society, 2004.

- Chatterjee A , Govindu V M . Efficient and Robust Large-Scale Rotation Averaging[C]// 2013 IEEE International Conference on Computer Vision (ICCV). IEEE Computer Society, 2013.

- Chatterjee A, Govindu V. Robust Relative Rotation Averaging[J]. IEEE Transactions on Pattern Analysis & Machine Intelligence, 2017, PP(99):1-1.