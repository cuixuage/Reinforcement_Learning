**目标:balancing exploration(探索) exploitation(贪心利用)**

读书笔记参考:
https://www.cnblogs.com/steven-yang/p/6476034.html

**2.2 action-value method**  
Qt(a) = avg(时间t以前所有动作A=a的Reward)平均值  
At = Max(Qt(a))当前时间所有可能action的最大Q的策略  
==》扩展: 小概率的(0.1)的exploration     "-greedy

**2.3 the 10-armed test**
给出10个动作的Q,比较greedy的收敛情况以及exploreation
结论:
如果Reward之间的方差较大,0.1左右的随机Greedy效果更有效
greedy的exploreation只有1/3的动作覆盖率
考虑非平衡性(Action的Reward可能在将来出现不断变化)的问题

**2.4 增量的Q实现**
P53  增量公式推导
P54  伪代码
和QL 思想真的很像啊
Q(A) <= Q(A) + 1/N(A) * {R - Q(A)} 在旧的Q加上 步长*和目标之间的偏差

**2.5 NonStationary Problem**
==>相当于带权值的增量实现
非平稳性的Reward =》需要更多依赖于最近的Reward
Q(N+1) = Q(N) + α{R(N) - Q(N)} 
//2.4的step size设计成  0,1之间的参数alpha
公式不断展开 P54 ==》α越大,对于之前的依赖也就越少

**2.6 optimistic Initial Values**
当我们把Q(1)设计值较大时(Reward的均值较小)  哪怕是对于最贪心的Greedy算法都会大大增加exploration
P56 figure
但是对于非平稳性的reward用处不大

**2.7 Upper-Confidence-Bound Action Selection**
UCB 上限置信度的动作选择
随机Greedy exploration更加随机性，那么UCB方法使得exploration更加倾向于探索没有频繁出现的state

公式P58
最终Reward优于传统的随机exploration,缺点:对于nonstatic + large state space问题不太适用

**2.8 Gradient Bandit Algorithms没看懂**
公式推导P59
随机梯度上升
结论: Ht(a)对于当前时间的动作偏好程度  (之前的奖励大于baseline越多,偏好程度越大)

**2.9 associative search**
关联搜索  任务之间关联性问题(简述章节)

**2.10 Summary**
e-greedy 随机的exploration
UCB 依赖于前期时间内的动作频繁程度提高Q或者降低Q,是一种确定性的exploration
Gradient-algorithm 根据前期的动作倾向完成当前动作
(和依赖Reward的本质区别有吗？？  似乎一样的)

结论:
UCB的方法一般来说效果更好
