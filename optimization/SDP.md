# Semidefinite Positive Programming

## 1. 半正定规划 (SDP)


## 2. Row by Row methods for Semidefinite Programming

通过 Row by Row (RBR) 的方法来解决半正定规划 (SDP) 的问题

### 2.1 一些符号
- $S^n$: $n\times n$　的对称阵
- $S_+^n$: $n\times n$　的对称半正定矩阵
- $S_{++}^n$: $n\times n$　的对称正定矩阵

令 $A \in \mathbb{R}^{n\times n}$，$\alpha, \beta$　为给定的索引集合
- $A(i, j)$ 或 $A_{i,j}$: A 的第 $i$ 行第 $j$ 列元素
- $\alpha$ 的 cardinality表示为 $|\alpha|$，它的补 (complemente) 为 $\alpha^c=\{1,2,\cdots,n\}\backslash \alpha$
- $A_{i^c, i^c}$: 移除 $A$ 的第 $i$ 行和第 $i$ 列之后保留下来的子矩阵
- $A_{i^c, i}$: 不包含矩阵元素 $A_{i,i}$ 的第 $i$ 列
- $\langle C, X \rangle$: 矩阵 $C$ 和 矩阵 $X$ 的内积，$\langle C, X \rangle = \sum_{j,k}^N C_{j,k}X_{j,k}$
- $tr(X) = \sum_{i=1}^nX_{ii}$
- $[x;y]$: 将 $x\in \mathbb{R}^p$ 堆叠在 $y\in \mathbb{R}^q$ 得到的向量

### 2.2 Schur Complement
令 $X\in S^n$ 划分为

$$
X = \left[
    \begin{array}{cc}
    \xi & y^T\\
    y & B
    \end{array}
\right] \tag{1}
$$

其中，$\xi \in R$，$y\in R^{n-1}$，$B\in S^{n-1}$ 并且 $B$ 为非奇异矩阵。矩阵 $X$ 可以分解为

$$
X = 
\left[
    \begin{array}{cc}
    \xi & y^TB^{-1}\\
    \boldsymbol{0} & I
    \end{array}
\right] 
\left[
    \begin{array}{cc}
    \xi-y^TB^{-1}y & 0\\
    0 & B
    \end{array}
\right]
\left[
    \begin{array}{cc}
    1 & 0\\
    B^{-1} & I
    \end{array}
\right]  \tag{2}
$$

正定性约束 $X\succeq 0$ 等价于

$$
X \succ 0 \Longleftrightarrow B \succ 0\ 且\ (X/B) = \xi - y^TB^{-1}y > 0 \tag{3}
$$

其中，$(X/B)$ 为 $X$　对应于 $B$ 的 `Schur Complement`。如果矩阵 $B$ 是奇异阵，则 $X$ 对应于 $B$ 的 `generalized Schur Complement` 为

$$
(X/B) = \xi - y^TB^{\dagger}y \tag{4}
$$

其中，$B^{\dagger}$ 是 $B$ 的 `Moore-Penrose 伪逆`。公式 (3) 由以下定理得到:
**定理 1**: 令 $X \in S^n$　为划分成 公式 (1) 的对称阵，其中 $\xi$ 是标量并且 $B \in S^{n-1}$。$X$ 对应于 $B$ 的 generalized schur complement 定义为 $(X/B) = \xi - y^TB^{\dagger}y$，则以下定理成立:
(1) 如果 $B$ 非奇异，那么 $X \succ 0$ 成立当且仅当 $B \succ 0$ 且 $(X/B) > 0$
(2) 如果 $B$　非奇异，那么 $X \succeq 0$ 成立当且仅当 $B \succ 0$ 且 $(X/B) \ge 0$
(3) $X \succeq 0$ 当且仅当 $B \succeq 0, (X/B) \ge 0$ 且 $y \in \mathcal{R}(B)$，其中 $\mathcal{R}(B)$ 是 $B$ 的 range space

### 2.3 RBR 方法推导
考虑如下半正定规划 (SDP) 问题:

$$
\min_{X\in S^n}\qquad \langle C, X \rangle \qquad \qquad \\
s.t.\quad \mathcal{A}(X) = \boldsymbol{b},\quad X \succeq 0 \tag{5}
$$

其中，$C,A^{(i)} \in S^n$，未知矩阵 $X\in S^n_+$，线性映射 $\mathcal{A}(\centerdot): S^n \rightarrow \mathbb{R}^m$ 定义为

$$
\mathcal{A}(X) = \left[
    \begin{array}{c}
        \langle A^{(1)}, X \rangle\\
        \cdots\\
        \langle A^{(m)}, X \rangle
    \end{array}
\right]
$$

给定一个严格的可行解 $X^k \succ 0$，对 (5) 中的问题，我们可以构造一个二阶锥规划(second-order cone programming, SOCP)的限制: 固定 $(n-1)\times (n-1)$ 的子矩阵 $B=X_{1^c,1^c}^k$ 中的 $\frac{n(n-1)}{2}$ 个变量，令 $\xi = X_{1,1}, y = X_{1^c, 1}$，对应的，$X = \left[
    \begin{array}{cc}
    \xi & y^T\\
    y & B
    \end{array}
\right] = \left[
    \begin{array}{cc}
    \xi & y^T\\
    y & X_{1^c,1^c}^k
    \end{array}
\right]
$

由定理 1，$X \succeq 0$　等价于 $\xi-y^TB^{-1}y \ge 0$，因此，SDP　问题 (5) 变成

$$
\min_{[\xi;y]\in \mathbb{R}^n}\quad \tilde{c}^T[\xi;y] \qquad \\
s.t.\qquad \tilde{A}[\xi;y] = \tilde{b},\\
\qquad\qquad\qquad \xi-y^TB^{-1}y \ge 0 \tag{6}
$$

其中，

$$
\tilde{c} = \left(\begin{array}{c}C_{i,i}\\2C_{i^c,i}\end{array}\right), 
\tilde{A} = \left[\begin{array}{cc}A_{i,i}^{(1)} & 2A_{i,i^c}^{(1)}\\\cdots&\cdots\\A_{i,i}^{(m)} & 2A_{i,i^c}^{(m)}\end{array}\right], 
\tilde{b} = \left[
    \begin{array}{c}
        b_1 - \langle A_{i^c, i^c}^{(1)}, B \rangle \\
        \cdots \\
        b_m - \langle A_{i^c,i^c}^{(m)}, B \rangle
    \end{array}
\right] \tag{7}
$$

令 $B=LL^T$ 为 $B$ 的 Cholesky 分解，引入新的变量 $z=l^{-1}y$，因此，$y^TB^{-1}y = y^T{LL^T}^{-1}y = y^TL^{-T}L^{-1}y=(L^{-1}y)^T(L^{-1}y) = (L^{-1}y)^T(L^{-1}y) = z^Tz = ||z||_2^2$。所以，Schur Complement 约束等价于同时满足线性约束 $Lz=y$ 和 `rotated second-order cone constraint` $||z||_2^2 \le \xi$。除此之外，解 $X$ 的正定性可以通过将 Schur Complement 右边的 $0$ 替换为 $\nu > 0$ 来维持。因此，子问题 (5) 可以替换为

$$
\min_{[\xi;y]\in \mathbb{R}^n}\quad \tilde{c}^T[\xi;y] \qquad \\
s.t.\qquad \tilde{A}[\xi;y] = \tilde{b},\\
\qquad\qquad\qquad \xi-y^TB^{-1}y \ge \nu \tag{8}
$$

显然，如果对于任意的 $i = 1,\cdots, n$，将$X^k$ 中的除第 $i$ 行和第 $i$ 列之外的所有元素固定，只有第 $i$ 行/列中的元素当做未知量，我们可以构造相似的问题。因此，有以下推论:

**推论 1**: 对于任意的 $i \in \{1,\cdots, n\}$，$X_{i^c,i^c}$ 的 Schur Complement $(X/X_{i^c,i^c}) = X_{i,i} - X_{i^c,i}^TX_{i^c,i^c}^{\dagger}X_{i^c,i}$，存在一个 $X$ 行和列的 permutation matrix $P$，能把 $X_{i^c, i^c}$ 放置在 $X$ 的右下角，留下在 $X$ 中的 $X_{i^c, i}$ 和 $X_{i, i^c}$ 保持相同的递增顺序，也即 $P^TXP = \left[\begin{array}{cc}X_{i,i}&X_{i^c,i}^T\\X_{i^c,i}& X_{i^c,i^c}\end{array}\right]$。因此，$X$ 对应于 $X_{i^c, i^c}$ 的 Schur Complement 为 $((P^TXP)/X_{i^c,i^c})$。

#### 2.3.1 求解 (5) 的 RBR 方法

令初始的可行解 $X^k=X^1$ 为正定矩阵，其中 $k$ 表示算法的第 $k$ 次迭代。对于 $X\in \mathbb{R}^n$，在 $n$ 次内部循环中，我们通过求解子问题 (8) 更新 $X$ 的行和列。从第 $i$ 行到第 $n$ 列的这个过程称做一个 `cycle`。在第 $k$ 次 cycle 的第一步，我们固定 $B=X_{i^c,i^c}^k$，并且求解子问题 (8)，得到的解为 $[\xi;y]$，因此我们将 $X$ 更新为 $X_{i^c,i} = y, X_{i, i^c} = y^T, X_{i,i} = \xi$。在第 $i$ 行和第 $i$ 列更新完成之后，第 $k$ 个循环结束。之后，我们通过 $X^{k+1} = X^k$ 更新变量的值。这个过程一直重复直到目标函数的值的减少量小于 tolerance $\epsilon$。算法总结如下:

![RBR_SDP](img/RBR_SDP.png)

## 3. Block Coordinate Descent for Semidefinite Programming with Block Diagnal Constraints

现在考虑带对角约束的SDP问题:

$$
minimize\ \langle A, X \rangle \qquad \\
s.t.\ X_{ii} = 1, \forall i \in [n], \\
X \succeq 0 \qquad\quad \tag{CVX-SDP}
$$

我们可以用RBR [1] 的方法求解这个问题。由于 $X$ 的对角元素被固定为1，令 $B = X_{i^c,i^c}^k$ 为第 $k$ 次迭代中消去 $X$ 的第 $i$ 行和 $i$ 列得到的矩阵，则 (CVX-SDP) 的子问题为

$$
\min_{y\in \mathbb{R}^{n-1}}\ c^Ty \qquad\qquad \\
s.t.\ 1-y^TB^{\dag}y \geq \nu \tag{9}
$$

但是，对于(CVX-SDP)问题，存在更为高效的解法。[4,5,6,9] 用矩阵低秩分解的方法进行求解。令 $y = [y_1, y_2, \dots, y_n]$，则问题变为

$$
minimize\ \langle A, y^Ty \rangle \qquad \\
s.t.\ ||y_i|| = 1, for\ i \in [n], \tag{NONCVX-SDP}
$$

## 4. ADMM for Semidefinite Programming

## References

[1] Z. Wen, D. Goldfarb, S. Ma, and K. Scheinberg. Row by
row methods for semidefinite programming. Technical report, Columbia University, 2009. 7

[2] Wen Z, Goldfarb D, Yin W. Alternating direction augmented Lagrangian methods for semidefinite programming[J]. Mathematical Programming Computation, 2010, 2(3-4): 203-230.

[3] Zheng Y, Fantuzzi G, Papachristodoulou A, et al. Fast ADMM for semidefinite programs with chordal sparsity[C]//2017 American Control Conference (ACC). IEEE, 2017: 3335-3340.

[4] Wang P W, Chang W C, Kolter J Z. The mixing method: coordinate descent for low-rank semidefinite programming[J]. arXiv preprint arXiv:1706.00476, 2017.

[5] Erdogdu M A, Ozdaglar A, Parrilo P A, et al. Convergence Rate of Block-Coordinate Maximization Burer-Monteiro Method for Solving Large SDPs[J]. arXiv preprint arXiv:1807.04428, 2018.

[6] Tian Y, Khosoussi K, How J P. Block-Coordinate Minimization for Large SDPs with Block-Diagonal Constraints[J]. arXiv preprint arXiv:1903.00597, 2019.

[7] Nutini J, Laradji I, Schmidt M. Let's Make Block Coordinate Descent Go Fast: Faster Greedy Rules, Message-Passing, Active-Set Complexity, and Superlinear Convergence[J]. arXiv preprint arXiv:1712.08859, 2017.

[8] Tu S, Wang J. Practical first order methods for large scale semidefinite programming[R]. Technical report, University of California, Berkeley, 2014.

[9] Boumal N, Voroninski V, Bandeira A. The non-convex Burer-Monteiro approach works on smooth semidefinite programs[C]//Advances in Neural Information Processing Systems. 2016: 2757-2765.

[10] Cifuentes D. Burer-Monteiro guarantees for general semidefinite programs[J]. arXiv preprint arXiv:1904.07147, 2019.