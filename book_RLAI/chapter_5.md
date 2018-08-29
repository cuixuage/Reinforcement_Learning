**Monte Carlo Methods**
无模型的蒙特卡洛学习方法   Model free
idea:未知转移概率矩阵,未知state-value函数  == 通过模拟计算得到(有限的情节任务)
Monte Carlo使用模拟解决Markov Decision Process

**5.1 MC Prediction**
MC基于抽样数据计算结果
e.g.游戏类都适合：完全信息博弈游戏，像围棋、国际象棋。非完全信息博弈游戏：21点、麻将等等
```
在Episode中的模拟得到value
first-visit MC  
every-visit MC  在一个Episode中,Q(s,a)出现多次如何评估？(平稳性/非平稳性Reward)
平稳性:  均值  V(St) = average(Returns(St))
非平稳性: 1/k换成折扣因子α  Vk+1 = Vk + α*(Gk - Vk) α越大越重视眼前Reward  Gk当前的收获  Vk每次遇到S的平均价值
```

**5.2 MC Estimation of action-value**
**5.3 MC Control** 
在episode之后,返回值用作政策评估,再通过遍历所有state进行政策改善

**5.4 MC Control without Exploring Starts**
如何获得充足的经验是无模型强化学习的核心所在
解决思路1：
探索的初始化  每个state都有可能作为初始状态

**5.5 off-policy Prediction & important Sampling**
一些概念性问题:
https://www.cnblogs.com/steven-yang/p/6507015.html
```
on-policy method - 评估和优化的策略和模拟的策略是同一个。
off-policy method - 评估和优化的策略和模拟的策略是不同的两个。有时候，模拟数据来源于其它处，比如：已有的数据，或者人工模拟等等。
target policy - 目标策略。off policy method中，需要优化的策略。
behavior policy - 行为策略。off policy method中，模拟数据来源的策略。
```

**5.6 Incremental Implementation**
**5.7 off-policy MC Control**
**总结**
Monte Carlo使用模拟解决Markov Decision Process
知乎   https://zhuanlan.zhihu.com/p/28107168
blackJack游戏:
给定玩家固定策略,比如只要手中两张牌之和大于20,就继续要牌。(得到庄家手中牌面，玩家手中牌面的table) 
==>  求解此固定策略的优劣  =》计算此策略的avg value

on-policy 和 off-policy
https://zhuanlan.zhihu.com/p/25743759
off-policy保证充分的探索性 ==> 要求behaior policy覆盖target policy

重要性采样(important Sampling)
http://blog.sina.com.cn/s/blog_60b44d6a0101l45z.html
