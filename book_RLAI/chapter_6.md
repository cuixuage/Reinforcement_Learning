**Temporal-Difference Learning**
(单步 one-step)时序差分学习   无模型Model-Free RL
理解如何结合  DP+MC == 在当前episode尚未结束,就进行估计当前值函数 

**6.1 TD Prediction**
先验知识:
bootstraping  自举算法  DP=当前state value依赖于t+1时刻
V(St) = Eπ{Rt+1 + γV(St+1)}
MC 是经验平均avg:
V(St) = V(St) + α(Gt - V(St))  
1. exit model可以通过动作集,计算出S的所有后继S'的状态
2. model-free MC估计=episode_avg
3. MC Gt是状态S自身 直到终止状态的所有返回值

结合以上两者:
TD  (one-step单步)
V(St+1)也是估计值(如何计算出来的呢？？)
V(St) <==  V(St) + α * {Rt+1 + γ*V(St+1) -V(st)}

**6.3 Optimality TD**
1.TD均方误差 < MC(模拟avg)均方误差
2.step-size不是非常小的话,TD可能在某一区间震荡而不收敛

**6.4 Sarsa: On-policy TD Control**
公式 P151
例如:e-greedy 对于State有固定的政策选择Action
行动策略,评估策略  都是E-greedy

**6.5 QLearnign: off-policy TD Control**
公式P153
1.行动策略是 E-greedy
目标策略是 贪婪策略(选择max value的S')
2.Qlearning Maximizaiton Bias

**6.7 Double QLearning**
目的: 解决Qlearning Maximizaiton Bias问题  example P156
P158  公式


**总结**
TD n-step https://zhuanlan.zhihu.com/p/25913410

MC TD对比:
https://zhuanlan.zhihu.com/p/28107168
