## 旋转
旋转在三维重建中是比较重要的，这里主要对旋转的性质及应用做一些总结。

### 1. 旋转矩阵
设某个<u>单位正交基</u> $(e_1, e_2, e_3)$ 经过一次旋转变成了 $(e_1^{'}, e_2^{'}, e_3^{'})$ 。那么，对于同一个向量 $\bold{a}$ (注意该向量并没有随着坐标系的旋转而发生运动)，它在两个坐标系下的坐标为 $(a_1, a_2, a_3)^T$ 和 $(a_1^{'}, a_2^{'}, a_3^{'})^T$。由坐标的定义，有：
$$
\left[
    \begin{array}{ccc}
    e_1 & e_2 & e_3
    \end{array}
\right]
\left[
    \begin{array}{c}
    a_1\\a_2\\a_3
    \end{array}
\right]=
\left[
    \begin{array}{ccc}
    e_1^{'} & e_2^{'} & e_3^{'}
    \end{array}
\right]
\left[
    \begin{array}{c}
    a_1^{'}\\a_2^{'}\\a_3^{'}
    \end{array}
\right] \tag{1}
$$
为描述两个坐标之间的关系，(1)左右两边同时乘以$(e_1^T, e_2^T, e_3^T)^T$，则有
$$
\left[
    \begin{array}{c}
    a_1\\a_2\\a_3
    \end{array}
\right]=
\left[
    \begin{array}{ccc}
    e_1^{T}e_1{'} & e_1^Te_2^{'} & e_1^Te_3^{'}\\
    e_2^{T}e_1^{'} & e_2^Te_2^{'} & e_1^Te_3^{'}\\
    e_3^{T}e_1^{'} & e_3^Te_2^{'} & e_3^Te_3^{'}
    \end{array}
\right]
\left[
    \begin{array}{c}
    a_1^{'}\\a_2^{'}\\a_3^{'}
    \end{array}
\right] = R\bold{a^{'}} \tag{2}
$$
其中 $R$ 即为旋转矩阵。旋转矩阵的集合定义为:
$$
SO(n) = \{R \in \mathbb{R}^{n\times n} | RR^T = I, det(R) = I \} \tag{3}
$$
由于旋转矩阵是正交阵，它的逆(即转置)描述了一个相反的旋转，则有$\bold{a^{'}} = R^{-1}\bold{a}=R^T\bold{a}$。显然，$R^T$刻画了一个相反的旋转。


### 2. 李群和李代数 (Lie Group and Lie Algebra)
这里我们只描述旋转空间上的`李群`和`李代数`。
李群是指具有连续光滑性质的群。$SO(n)$在实数空间上是连续的。我们能够直观想象一个刚体能够连续地在空间中运动，所以他们都是李群。每个李群都有与之对应的李代数，李代数描述了李群的局部性质。旋转空间上的李群已经在公式(3)中做了描述。

#### 2.1 旋转空间上的李代数推导
设 $R$ 为某个相机的旋转，随时间连续变化，即 $R$ 为关于时间 $t$ 的函数 $R(t)$。由于 $R$ 为正交阵，则有
$$
R(t)R(t)^T = I \tag{4}
$$
等式两边对 $t$ 求导，则有 $\frac{\delta R(t)}{\delta t} R(t)^T + R(t)\frac{\delta R(t)^T}{\delta t} = 0$。整理可得，
$$
\frac{\delta R(t)}{\delta t} R(t)^T = -R(t)\frac{\delta R(t)^T}{\delta t} = -(\frac{\delta R(t)}{\delta t} R(t)^T)^T \tag{5}
$$
由(5)可以看出 $\frac{\delta R(t)}{\delta t} R(t)^T$ 是一个`反对称矩阵` (反对称矩阵的定义: $A = -A^T$)。
而对于`反对称矩阵`，我们总能找到一个三维向量 $\bold{w}$ 与之对应。一般地，$[\bold{w}]_{\times}$ 表示向量到反对称阵的变换。因此，我们有
$$
\frac{\delta R(t)}{\delta t} R^T = [\bold{w}]_{\times} \tag{6}
$$
对公式(6), 左右两边同时右乘$R(t)$可得
$$
\frac{\delta R(t)}{\delta t} = [\bold{w}]_{\times} R(t) \tag{7}
$$
公式(7)是一个形如 $\frac{\mathrm{d}y}{\mathrm{d}x} = ay$ 的常微分方程，对方程两边同时去倒数，则有 $\frac{\mathrm{d}x}{\mathrm{d}y} = \frac{1}{ay}$。显然，$\mathrm{d}x = \frac{1}{y}\mathrm{d}y$ 的解为 $x = ln\ ay$，进一步可得 $y = e^{ax}$。将公式(7)代入，可得
$$
R(t) = e^{[\bold{w}]_{\times}t} \tag{8}
$$
#### 2.2 李代数 $\mathfrak{so}(3)$
李群 $SO(3)$ 对应的李代数是定义在 $R(3)$ 上的向量，记为 $\bold{w}$。每个 $\bold{w}$ 都可以生成一个反对称矩阵 $\Phi$ : 
$$
\Phi = [\bold{w}]_{\times} =
\left[
    \begin{array}{ccc}
    0 & -w_3 & w_2\\
    w_3 & 0 & -w_1\\
    -w_2 & w_1 & 0
    \end{array}
\right]
\in \mathbb{R}^{3\times 3}
$$
一般说，$\mathfrak{so}(3)$的元素是三维向量或者三维反对称矩阵，不加区别:
$$
\mathfrak{so}(3) = \{\bold{w} \in R^3, \Phi = [\bold{w}]_{\times} \in \mathbb{R}^{3\times 3}\} \tag{9}
$$
至此，我们知道 $\mathfrak{so}(3)$ 是一个由三维向量组成的集合，每个向量对应到一个反对称矩阵，可以表达旋转矩阵的倒数。它与 $\mathfrak{so}(3)$ 的关系通过`指数映射 (exponential mapping)`给定:
$$
R = exp([\bold{w}]_{\times}) \tag{10}
$$

#### 2.3 推导 $\mathfrak{so}(3)$ 上的指数映射

由 公式 (10) 可知，它是一个矩阵的指数。在李群和李代数中，称为`指数映射 (exponential mapping)`。
我们知道指数函数的`幂级数`为 
$$
exp(x) = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$
同样地，对于 $\mathfrak{so}(3)$ 中的任意元素 $[\bold{w}]_{\times}$，它的指数映射为
$$
exp([\bold{w}]_{\times}) = \sum_{n=0}^{\infty} \frac{([\bold{w}]_{\times})^n}{n!} \tag{11}
$$
令 $\bold{w} = \theta \bold{a}$，其中$\theta$ 为方向，$\bold{a}$ 为长度为1的方向向量。对于 $[\bold{a}]_{\times}$，有两个性质：
- $[\bold{a}]_{\times}[\bold{a}]_{\times} = \bold{a}\bold{a}^T - I$
- $[\bold{a}]_{\times}[\bold{a}]_{\times}[\bold{a}]_{\times} = -[\bold{a}]_{\times}$

利用这两个性质，指数映射可以写为:
$$
exp([\bold{w}]_{\times}) = exp(\theta [\bold{a}]_{\times})
= \sum_{n=0}^{\infty} \frac{(\theta [\bold{a}]_{\times})^n}{n!}\\
= I + \theta [\bold{a}]_{\times} + \frac{1}{2!} \theta^2 [\bold{a}]_{\times}[\bold{a}]_{\times} + \frac{1}{3!}\theta^3[\bold{a}]_{\times}[\bold{a}]_{\times}[\bold{a}]_{\times} + \frac{1}{4}\theta^4([\bold{a}]_{\times})^4 + \cdots\\
= \bold{a}\bold{a}^T - [\bold{a}]_{\times}[\bold{a}]_{\times} + \frac{1}{2!}\theta^2[\bold{a}]_{\times}[\bold{a}]_{\times} + \frac{1}{3!}\theta^3[\bold{a}]_{\times}[\bold{a}]_{\times}[\bold{a}]_{\times} + \frac{1}{4!}\theta^4([\bold{a}]_{\times})^4 + \cdots\\
= \bold{a}\bold{a}^T - [\bold{a}]_{\times}[\bold{a}]_{\times} + \theta[\bold{a}]_{\times} + \frac{1}{2!}\theta^2[\bold{a}]_{\times}[\bold{a}]_{\times} - \frac{1}{2!}\theta^3[\bold{a}]_{\times} - \frac{1}{4!}\theta^4([\bold{a}]_{\times})^2 + \cdots\\
= \bold{a}\bold{a}^T + (\theta - \frac{1}{3!}\theta^3 + \frac{1}{5!}\theta^5 - \cdots)[\bold{a}]_{\times} - (1 - \frac{1}{2!}\theta^2 + \frac{1}{4!}\theta^4 - \cdots)[\bold{a}]_{\times}[\bold{a}]_{\times}\\
=[\bold{a}]_{\times}[\bold{a}]_{\times} + I + [\bold{a}]_{\times}sin\theta - [\bold{a}]_{\times}[\bold{a}]_{\times} cos\theta\\
= (1 - cos\theta)[\bold{a}]_{\times}[\bold{a}]_{\times} + I + [\bold{a}]_{\times} sin\theta\\
= (1-cos\theta)(\bold{a}\bold{a}^T - I) + I + [\bold{a}]_{\times}sin\theta\\
= cos\theta\ I + (1 - cos\theta)\bold{a}\bold{a}^T + [\bold{a}]_{\times}sin\theta
\tag{12}
$$
公式 (12) 就是`罗德里格斯公式`，<u>指数映射即罗德里格斯公式</u>！

同样，我们可以定义`对数映射`，把 $SO(3)$ 中的元素对应到 $\mathfrak{so}(3)$ 中 :
$$
\bold{[w]}_{\times} = ln(R)^{V} = (\sum_{n=0}^{\infty} \frac{(-1)^n}{n+1} (R - I)^{n+1} )^{V} \tag{13}
$$
不过，一般不会按照泰勒展开计算对数映射，而是通过旋转矩阵恢复李代数：
令转轴为 $\bold{n}$，转角为 $\theta$，
(1) 计算转角 $\theta$。对于转角 $\theta$，由罗德里格斯公式，有
$$
tr(R) = cos\theta\ tr(I) + (1-cos\theta)tr(\bold{n}\bold{n}^T) + sin\theta\ tr([\bold{n}]_{\times})\\
= 3cos\theta + (1-cos\theta) = 1 + 2cos\theta
$$
，因此，$\theta = arc\ cos\frac{tr(R) - 1}{2}$。
(2) 计算转轴 $\bold{n}$，由于旋转轴上的向量在旋转后不发生改变，有 $R\bold{n} = \bold{n}$。因此，转轴 $\bold{n}$ 是矩阵 $R$ 特征值为1对应的特征向量。求解次方程，再归一化，就得到了转轴。最后，李代数可以写为 $\bold{w} = \theta\bold{n}$。

### 3. 四元数 (Quanternion)
四元数是Hamilton找到的一种扩展的复数，拥有一个实部和三个虚部，可表示为 : 
$$
\bold{q} = (c, \bold{v}) = (q_0, q_1, q_2, q_3) = q_0 + q_1\bold{i} + q_2\bold{j} + q_3\bold{k} \tag{14}
$$
这三个虚部满足以下关系:
$$
i^2 = j^2 = k^2 = -1\\
ij = k,\ ji = -k,\\
jk = i,\ kj = -i,\\
ki = j,\ ik = -j.
$$

#### 3.1 四元数的运算
设 $\bold{q} = (c_1, \bold{v}_1), q_2 = (c_2, \bold{v}_2)$，则
$$
\bold{q}_1 \pm \bold{q}_2 = (c_1 \pm c_2,\ \bold{v}_1 \pm \bold{v}_2)\\
\bold{q}_1 \cdot \bold{q}_2 = (c_1c_2 - \bold{v}_1^T\bold{v}_2,\ c_1\bold{v}_2 + c_2\bold{v}_1 + \bold{v}_1 \times \bold{v}_2)\\
||\bold{q}|| = \sqrt{q_0^2 + q_1^2 + q_2^2 + q_3^2},\ 
\bold{q}^{-1} = \frac{1}{||q||^2} (c,\ -\bold{v})\\
||\bold{q}_1 \cdot \bold{q}_2|| = ||\bold{q_1}|| \cdot ||\bold{q_2}||
$$

#### 3.2 四元数表示旋转
假设旋转绕单位向量 $\bold{n} = (n_x, x_y, n_z)^T$ 进行了角度为 $\theta$ 的旋转，则该旋转的四元数定义为:
$$
\bold{q} = (cos\frac{\theta}{2},\ n_xsin\frac{\theta}{2},\ n_ysin\frac{\theta}{2},\ n_zsin\frac{\theta}{2})^T \tag{15}
$$
令 $\theta = \theta + 2\pi$，则 $\bold{q} = (-cos\frac{\theta}{2}, -n_x\sin\frac{\theta}{2}, -n_ysin\frac{\theta}{2}, -n_zsin\frac{\theta}{2})^T = -\bold{q}$。即 **$\bold{q}$ 和 $-\bold{q}$ 表示同一个旋转**。

令 $\bold{v} = (n_x, n_y, n_z)$，$\bold{w} = \theta\bold{v}$，则 $R = exp([\bold{w}]_{\times})$。

### 4. 旋转矩阵、角轴表示法、四元数之间的转换

#### 4.1 旋转矩阵与四元数
##### 四元数到旋转矩阵的转换
通过 3.2 节，即可通过四元数计算得到旋转矩阵。

##### 旋转矩阵到四元数的转换
令旋转矩阵为
$$
R = 
\left[
    \begin{array}{ccc}
        R_{11} & R_{12} & R_{13}\\
        R_{21} & R_{22} & R_{23}\\
        R_{31} & R_{32} & R_{33}
    \end{array}
\right]
$$
则旋转矩阵到四元数的转换如下:
$q_0 = \frac{\sqrt{tr(R) + 1}}{2},\ q_1 = \frac{R_{23} - R_{32}}{4q_0},\ q_2 = \frac{R_{31} - R_{13}}{4q_0},\ q_3 = \frac{R_{12} - R{21}}{4q_0}$

#### 4.2 四元数与角轴表示法
##### 四元数到角轴表示法的转换
采用 3.2 节的符号表示，很容易得到 
$$
\theta = 2arc cos\ q_0,\\
(n_x, n_y, n_z)^T = \frac{1}{sin\frac{\theta}{2}} (q_1, q_2, q_3)^T = \frac{1}{||\bold{n}||} (q_1, q_2, q_3)^T
$$

##### 角轴表示法到四元数的转换
通过 3.2 节即可得到。

#### 4.3 旋转矩阵与角轴表示法的转换

##### 角轴表示法到旋转矩阵
很显然，通过指数映射，使用罗德里格斯公式就可以将角轴表示法变换到旋转矩阵

##### 旋转矩阵到角轴表示法
一般会先将旋转矩阵转换到四元数，再通过四元数转换到角轴表示法。

### 5. 罗德里格斯旋转公式 (Rodrigues' rotation formula)
和罗德里格斯公式不同(李代数到李群的指数映射)，`罗德里格斯旋转公式`是用于对向量进行旋转的，即<u>给定空间中的一个三维点(具体形式是一个三维向量)，如何通过轴角表示法对三维点进行旋转</u>。这个公式也被扩展用于计算指数映射，也就是罗德里格斯公式。罗德里格斯旋转公式可以通过以下公式计算得到:
$$
\bold{v}_{rot} = \bold{v}cos\theta + (\bold{k}\times \bold{v})sin\theta + \bold{k}(\bold{k} \cdot \bold{v})(1-cos\theta) \tag{16}
$$

#### 5.1 对三维点进行旋转
实际中，使用轴角表示法对三维点进行旋转会分两种情况：
- $||\bold{w}||$ 相比0较大时。这个时候可以通过`罗德里格斯旋转公式`计算
- $||\bold{w}||$ 相比0较小时。根据罗德里格斯公式，
$$
R = cos||\bold{w}||I + \frac{[\bold{w}]_{\times}}{||\bold{w}||} sin(||\bold{w}||) + \frac{[\bold{w}]_{\times}^2}{||\bold{w}||^2}(1 - cos(||\bold{w}||)) 
$$
当$\bold{w}$较小时，$cos(||\bold{w}||) \approx 1, sin(||\bold{w}||) \approx ||\bold{w}||$。因此，$R \approx I + [\bold{w}]_{\times}$。于是，$R\bold{p} = \bold{p} + [\bold{w}]_{\times} \bold{p}$

*注： 对于李代数 $\bold{w} = \theta \bold{n}$，其中$\bold{n}$为单位转轴，因此 $||\bold{n}||^2 = 1$，于是$||\bold{w}||^2 = \theta^2 ||\bold{n}||^2 = \theta^2$。因此，有 $\theta = ||\bold{w}||$*。

#### 5.2 Ceres中的实现
```cpp
template<typename T> inline
void AngleAxisRotatePoint(const T angle_axis[3], const T pt[3], T result[3]) {
  const T theta2 = DotProduct(angle_axis, angle_axis);
  if (theta2 > T(std::numeric_limits<double>::epsilon())) {
    // Away from zero, use the rodriguez formula
    //
    //   result = pt costheta +
    //            (w x pt) * sintheta +
    //            w (w . pt) (1 - costheta)
    //
    // We want to be careful to only evaluate the square root if the
    // norm of the angle_axis vector is greater than zero. Otherwise
    // we get a division by zero.
    //
    const T theta = sqrt(theta2);
    const T costheta = cos(theta);
    const T sintheta = sin(theta);
    const T theta_inverse = T(1.0) / theta;

    const T w[3] = { angle_axis[0] * theta_inverse,
                     angle_axis[1] * theta_inverse,
                     angle_axis[2] * theta_inverse };

    // Explicitly inlined evaluation of the cross product for
    // performance reasons.
    const T w_cross_pt[3] = { w[1] * pt[2] - w[2] * pt[1],
                              w[2] * pt[0] - w[0] * pt[2],
                              w[0] * pt[1] - w[1] * pt[0] };
    const T tmp =
        (w[0] * pt[0] + w[1] * pt[1] + w[2] * pt[2]) * (T(1.0) - costheta);

    result[0] = pt[0] * costheta + w_cross_pt[0] * sintheta + w[0] * tmp;
    result[1] = pt[1] * costheta + w_cross_pt[1] * sintheta + w[1] * tmp;
    result[2] = pt[2] * costheta + w_cross_pt[2] * sintheta + w[2] * tmp;
  } else {
    // Near zero, the first order Taylor approximation of the rotation
    // matrix R corresponding to a vector w and angle theta is
    //
    //   R = I + hat(w) * sin(theta)
    //
    // But sintheta ~ theta and theta * w = angle_axis, which gives us
    //
    //  R = I + hat(w)
    //
    // and actually performing multiplication with the point pt, gives us
    // R * pt = pt + w x pt.
    //
    // Switching to the Taylor expansion near zero provides meaningful
    // derivatives when evaluated using Jets.
    //
    // Explicitly inlined evaluation of the cross product for
    // performance reasons.
    const T w_cross_pt[3] = { angle_axis[1] * pt[2] - angle_axis[2] * pt[1],
                              angle_axis[2] * pt[0] - angle_axis[0] * pt[2],
                              angle_axis[0] * pt[1] - angle_axis[1] * pt[0] };

    result[0] = pt[0] + w_cross_pt[0];
    result[1] = pt[1] + w_cross_pt[1];
    result[2] = pt[2] + w_cross_pt[2];
  }
}
```

### 6. $SO(3)$ 上的距离测量 (Distance Measure)

##### (1) Bi-invariant distance
如果对于所有的 $S$ 和 $R_i$，我们有 : 
$$
d(SR_1, SR_2) = d(R_1, R_2) = d(R_1S, R_2S) \tag{17}
$$
那么这样的一个距离测量称为 `Bi-invariant`.

##### (2) Angular Distance (Geodesic Distance)

定义 R 和 S 之间的 `angular distance` 为旋转 $SR^T$ 的角度，并且处于区间 $[0, \pi]$ 里。因此，
$$
d(S, R) = d(SR^T, I) = ||log(SR^T)||_2 \tag{18}
$$
距离测量函数 $d(S, R)$ 和 $SR^T$ 的旋转角度相等。需要注意，我们可能会等价地写为 $R^TS$，$RS^T$，$S^TR$，因为这些都表示同一个旋转。

##### (3) Chordal Distance
旋转 $R$ 和 $S$ 之间的 `chordal distance` 定义为:
$$
d_{chord}(S, R) = ||S-R||_F \tag{19}
$$
其中，$||\cdot||_F$ 表示矩阵的 `Frobenius 范数`。

`chordal distance` 和 `angular distance` 之间可以通过罗德里格斯公式关联起来:
$$
exp(\theta \bold{v}) = I + sin\theta\ [\bold{v}]_{\times} + (1-cos\theta)([\bold{v}]_{\times})^2
$$
具体来讲，令 $SR^T = exp(\theta \bold{v})$，由于 $[\bold{v}]_{\times}$ 和 $([\bold{v}]_{\times})^2$正交，且 $||[\bold{v}]_{\times}||^2_F = ||([\bold{v}]_{\times})^2||^2_F = 2$，因此，我们有
$$
d_{chord}(S, R)^2 = ||S - R||^2 = ||SR^T - I||^2 = 2(sin^2\theta + (1-cos\theta)^2) = 8sin^2\frac{\theta}{2}
$$
因此，
$$
d_{chord}(S, R) = 2\sqrt{2} sin\frac{\theta}{2} \tag{20}
$$


### 7. 扰动模型对旋转求导

设左扰动 $\nabla R$ 对应的李代数为 $\bold{a}$。对 $\bold{a}$ 求导，有
$$
\frac{\delta(R\bold{p})}{\delta \bold{a}} = {\lim_{\bold{a} \to 0}} \frac{exp([\bold{a}]_{\times}) exp([\bold{a}]_{\times})\bold{p} - exp([\bold{a}]_{\times})\bold{p}}{\bold{a}} \\
= {\lim_{\bold{a} \to 0}} \frac{(1 + [\bold{a}]_{\times}) exp([\bold{a}]_{\times})\bold{p} - exp([\bold{a}]_{\times})\bold{p}}{\bold{a}}\\
= {\lim_{\bold{a} \to 0}} \frac{[\bold{a}]_{\times}R\bold{p}}{\bold{a}} = {\lim_{\bold{a} \to 0}} \frac{-[R\bold{p}]_{\times}\bold{a}}{\bold{a}} = -[R\bold{p}]_{\times}
$$

### References

- [1] 视觉SLAM十四讲 从理论到实践
- [2] https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula
- [3] https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation
- [4] Hartley, Richard, Trumpf, et al. Rotation Averaging[J]. International Journal of Computer Vision, 2013, 103(3):267-305.