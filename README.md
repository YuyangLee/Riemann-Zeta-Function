# Riemann-Zeta Function

> This is Yuyang's codebase for his course project for Numerical Analysis and Algorithms (40250443-0, Fall 2022) at THU.

## 安装依赖

安装必要依赖：

```bash
pip install numpy gmpy tqdm   # Tested on Python 3.9 with Ubuntu 22.04 LTS
```

> 运行 `viz.py` 还需要安装 `matplotlib`, `seaborn`。

## 运行求解器

所有求解程序的默认参数均已设置好，**直接执行而不指定任何参数即可完成报告所述案例的计算**。

### 问题 1：Basel 级数求和

通过计算 $\zeta(8)$ （或 $\zeta(2)$）求解问题 $\pi$。

```shell
python 0_basel.py --precision PRECISION : 精度 m，默认为 20
                  --zeta2               : 使用 zeta(2) 求解；否则使用 zeta(8)，默认为 False
```

### 问题 2：方程求根

从初始值 $x = x_0$ 开始，用 Newton 法求解问题 $\zeta(x) = a$

```shell
python 1_root_newton.py [--precision PRECISION] : 精度 m，默认为 4
                        [--a A]                 : 指定 a，默认为 1.5
                        [--x_0 X_0]             : 指定 x_0，默认为 2.5
```

### 问题 3：数值积分

求解

$$
I = \int_0^\infty \frac{t^{x-1}}{e^t - 1} \mathrm{d}t
$$

通过直接计算积分求解：

```shell
python 2_integral.py [--precision PRECISION]     : 精度 m，默认为 4
                     [--x X]                     : 指定 x，默认为 3.5
                     [--N_subdivide N_SUBDIVIDE] : 指定复化积分公式的内分点数，默认为 1，即采用复化梯形公式
```

通过计算 $I(x) = \zeta(x) \Gamma(x)$ 求解：

```shell
python 2_integral_gamma.py [--precision PRECISION]     : 精度 m，默认为 4
                           [--x X]                     : 指定 x，默认为 3.5
                           [--N_subdivide N_SUBDIVIDE] : 指定复化积分公式的内分点数，默认为 1，即采用符合梯形公式
```

### 问题 4：微分方程数值求解

已知

$$
y'(x) = \zeta(y), y(x_0) = y_0
$$

求解 $y(x)$


```shell
python 3_diff_eq.py [--precision PRECISION] : 精度 m，默认为 4
                    [--x_0 X_0]             : 指定 x_0，默认为 2.0
                    [--y_0 Y_0]             : 指定 y_0，默认为 2.0
                    [--x X]                 : 指定 x，默认为 4.0
```
