# Convex Optimization

## 1. (伪凸函数) Pseudoconvex function
A pseudoconvex function is a function that behaves like a convex function with respect to finding its local minima, but need not actually be convex. Informally, a differentiable function is pseudoconvex if it is increasing in any direction where it has a positive directional derivative.
### 定义
Formally, a real-valued differentiable function $f$ defined on a (nonempty) convex open set $X$ in the finite-dimensional Euclidean space Rn is said to be pseudoconvex if, for all $x, y \in X$ such that $\nabla f(x)\cdot (y-x)\geq 0 \nabla f(x)\cdot(y-x) \ge 0$, we have $f(y)\geq f(x) f(y)\ge f(x)$. Here $\nabla ƒ$ is the gradient of $ƒ$, defined by
$\nabla f=\left({\frac {\partial f}{\partial x_{1}}},\dots ,{\frac {\partial f}{\partial x_{n}}}\right)$.

### 属性
Every convex function is pseudoconvex, but the converse is not true. For example, the function $ƒ(x) = x + x^3$ is pseudoconvex but not convex. Any pseudoconvex function is quasiconvex, but the converse is not true since the function $ƒ(x) = x^3$ is quasiconvex but not pseudoconvex. Pseudoconvexity is primarily of interest because a point $x^*$ is a local minimum of a pseudoconvex function ƒ if and only if it is a stationary point of ƒ, which is to say that the gradient of ƒ vanishes at $x^*$:

$\nabla f(x^{*})=0$.

### 扩展到不可微函数
The notion of pseudoconvexity can be generalized to nondifferentiable functions as follows. Given any function $f : X → R$ we can define the upper Dini derivative of $f$ by

$$
f^+(x,u) = \limsup_{h\to 0^+} \frac{f(x+hu) - f(x)}{h}
$$
where $u$ is any unit vector. The function is said to be pseudoconvex if it is increasing in any direction where the upper Dini derivative is positive. More precisely, this is characterized in terms of the subdifferential $\delta f$ as follows:

For all $x, y \in X$, if there exists an $x^* \in \delta ƒ(x)$ such that $\langle x^*, y - x \rangle \ge 0 $, then $ƒ(x) ≤ ƒ(z)$ for all $z$ on the line segment adjoining $x$ and $y$.