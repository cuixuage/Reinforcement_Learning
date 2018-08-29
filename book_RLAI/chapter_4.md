**Dynamic Programming**
动态规划求解MDP

**4.1 policy Prediction**
策略  状态到行为的映射

**4.2 policy Improvement**
最优策略
问题:  表格计算K=3的值  怎么计算出来的？
 P87  计算K=3是  序号为1的表格
注意:
边界外的Vk自身(意味着原地不动)
-2.4 = 0.25 * (-1 + 1.0 * 0) + 0.25 * (-1 + 1.0 * -2.0) + 
0.25 * (-1 + 1.0 * -2.0) + 0.25 * (-1 + 1.0 * -1.7) 
**4.3 Policy Iteration**
**4.4 Value Iteration**
虽然不需要策略的参与   但是仍然需要知道迭代的价值函数+转移概率

**4.5 Asynchronous DP**
异步

**4.6 Generalized Policy Iteration**
广义的策略迭代   GPI 
两个方面:
1.如何得到策略Value
2.如何通过价值反过来获得最优策略
GPI 核心:循环交互 = 迭代value function,迭代policy improment

**总结**
zhihu： https://zhuanlan.zhihu.com/p/25580624
1.不断迭代计算值函数  每一轮状态不断更新(no discount)  如何计算？算不对
2.最后通过max value来选择最优策略

==》策略迭代算法 P87
问题:  一定要等待值函数收敛完毕  才进行策略的improvment？
值函数迭代法

**David Silver总结**
https://zhuanlan.zhihu.com/p/28084955
1.同步反向迭代  Vk采用第K+1次的状态  不可能实现 
 =》 异步反向迭代 第K+1次采用当前K的状态价值更新自我状态
状态s的价值等于前一次迭代该状态的即时奖励  与所有s的下一个可能状态s' 的价值与其概率乘积的和
**Vk+1 = 每一个动作的可能性π(a|s) * {Rk + γ * P * Vk}**

2.策略迭代:  e.g. 连锁汽车租赁
固定一个策略开始value迭代,迭代一定程度后,进行policy改善,直到最终收敛

思考:
很多时候价值更新的收敛速度**远慢于**策略更新,如何解决？
设置条件,提前终止迭代
