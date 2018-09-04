**TD思想中的Sarsa实现**
https://zhuanlan.zhihu.com/p/28133594  

*Sarsa是on-policy的  action初始拥有自己的策略d  我们需要优化策略π*  

*初始情况*  
1.终止点Reward=1,否则Reward=-1  
2.Sarsa需要维护Q(s,a)即state-value函数。在状态S下采取动作A能获取对应value  

*目的*  
Agent遵循着某一个策略选择Action,得到Env的反馈信息(Reward+S'变化),来优化策略  

*公式*  
1.γ=0.9  
2.α=0.1  
3.V(St) <==  V(St) + α * {Rt+1 + γ*V(St+1) -V(st)}  
*其中VSt+1 通过e-greedy策略选择 MaxQ*  
3.1. VSt+1区别DP的转移概率  
3.2. e-greedy优化 == 随着迭代次数的增加,随机Action的概率越来越小  

*trick*  
1.Q表  字典套字典 key:state value:{key:action value:State-action的价值}  
2.区别 QLearning计算VSt 不使用随机action 完全依赖Max Q
Qlearning  V(St) <==  V(St) + α * {Rt+1 + γ*Max(V(St+1,a)) -V(st)}  
