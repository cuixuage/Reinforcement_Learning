**policy gradient Methods**
Model Free的策略梯度  直接策略搜索
值函数:策略评估+策略改善 ==》值函数最优，策略就是最优的的 ==》value-based method
策略搜索: 对于策略π进行参数化表示  π(a|s,θ)==》policy-based method


**13.1 Policy Approximation**
https://zhuanlan.zhihu.com/p/28348110
先验知识:
likeliHood ratios似然比  似然系数
函数在某个变量θ处的梯度等于该处函数值与该函数的对数函数在此处梯度的乘积，
dlog(y) = dy / y
1.原来J(θ)求导后为:
source Function
2.连续行为
行为的具体数值以μ(s)为均值,x为标准差的高斯分布中随机采样:
▽θlogπθ(s,a) = (α-μ(s))φ(s) / (x^2)

**13.2 The Policy gradient Theorem**
J(θ)是策略目标函数,再计算其梯度,沿着梯度上升的方向寻找局部最大值
J(θ) = d(s) * πθ(S,a)R(S,a)
其中d(s)是状态S满足的分布函数
结论:
J(θ)的梯度 = E期望(策略函数的对数的梯度  * 即时奖励)
连续问题:
将 即时奖励替换为Q

**13.3 Monte Carlo Policy gradient**
更新参数θ  
e.g. Puck世界
收敛速度缓慢  迭代次数长  较大的virance

**13.4 REINFORCE with baseline**
baseline(s)只和状态有关 与行为无关 从而不改变J(θ) ==》降低Variance
B(s) advantage function便利函数
1.一般将baseline设置为 值函数的预估值V(s,w)
idea:当个体采取行为a离开s状态时，究竟比该状态s总体平均价值要好多少

**13.5 Actor-Critic Methods**
1. Critic：参数化行为价值函数Qw(s, a)
2. Actor：按照Critic部分得到的价值引导策略函数参数θ的更新
3.critic==策略评估==由参数θ确定的πθ的表现如何
方法== MC,TD,TD(λ)
连续状态空间的Qw(s,a) = φ(s,a)TW
其中critic通过TD(0)更新w  actor更新θ

==》需要精心设计的Qw(s,a)
满足条件 https://zhuanlan.zhihu.com/p/28348110

**13.6 Policy Gradient for Continuing Problems**
**13.7 Policy parameterization for continuous Actions**

**summary**
1.policy-based & value-based优缺点？
https://zhuanlan.zhihu.com/p/28348110
高维度+连续状态空间使用基于策略的学习更加高效；policy-based有较高变异性variance
