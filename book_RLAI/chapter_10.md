**On-policy Control with Approximation**
**策略的行动状态价值**
Q(S,A)的近似值Q(S,A,W)

**10.1 Episode Semi-gradient Control**
e.g. 半梯度的one-step Sarsa  伪代码P266
state-action的状态的价值的近似
*动作离散* 的example:---小车上山    
解释: https://zhuanlan.zhihu.com/p/28223841  通过小车的位置和速度决定当前的价值

**10.2 semi-gradient n-step sarsa**
跳过  不是特别明白
感觉不重要

**10.3 Average Reward for Continuing Tasks**
discount γ 对于连续性任务的近似计算有一定的问题(chapter11)
*连续性任务*中引入了平均奖赏
*略过 不是很明白*

**10.4 deprecating the discount Set**
弃用折扣因子

**10.5 Differential Semi-gradient n-step Sarsa**
*略过了 没看*

**summary**

第11章关于 off-policy的值函数近似  这也是当前前沿研究
看第六章第七章

off-policy的近似方法的研究现在处于领域的前沿。主要有两个方向：

使用重要样本的方法，扭曲样本的分布成为目标策略的分布。这样就可以使用半梯度递减方法收敛。
开发一个真正的梯度递减方法，这个方法不依赖于任何分布。
https://www.cnblogs.com/steven-yang/p/6536742.html
