**目标: 有限的马尔科夫决策过程**
**解决大部分的强化学习框架MDP Markov Decision Processes**

**3.1 agent-environment interface**
介绍agent和env之间的交互过程:  St +At 得到Rt+1   P70
实际应用中哪些被认为是env  哪些被认为是agent P74
状态转移矩阵 或者 转换矩阵以及Reward的初始设计

**3.2 Goals and Rewards**
Goals = 最大化的Rewards
Reward = 想要使机器人最终达到的状态(比如棋牌类的获胜) 而不是how to achieved

**3.3  Returns and Episodes(剧情)**
discount rate折扣因子γ
γ->1  越加有远见,将来的reward也很重要
γ->0  越近视,只关心current reward
example Pole-Balancing 木杆平衡问题  P78

**3.4 unified Notation for Episodic and continuing Task**
剧情和连续任务的统一表示法  没啥好说的

**3.5 Policies and values functions**
π  策略,状态到动作的映射==》对于状态S不同Action有着不同的P概率
basic idea: 
Gt = Rt+1 + γGt+1    (当前Goal只需要得到下一步的Goal' * discount γ)
注:
1.state-value funciton(最优策略等价于最优状态值函数)  state-action funtion(在某一状态下 采用某一动作的q)
2.某一时间t的value不是固定的,但是它的期望是可计算的(S'不同action的Reward *γ)
3.V(S_t+1) = E(G_t+1)  t+1时的G期望 == Value
**3.6 最优化policy**
关键:
state-value funciton(最优策略等价于最优状态值函数)
bellman最优方程  求γ*Max_q(s',a')
**3.7optimality and approximation 最优性和近似性**
**3.8总结**
 还没看。。
 
 **3.9  MDP 知乎**
 参考读书笔记1:
 https://zhuanlan.zhihu.com/p/25498081
 注意下S各个状态的初始计算？？   解线性方程组
 注意下关于强化学习的分类
 
 参考读书笔记2:
 https://www.cnblogs.com/steven-yang/p/6480666.html
