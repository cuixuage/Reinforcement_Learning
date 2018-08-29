**Planning and Learning with Table**
向前搜索   采样
**8.1 models and Planning**
distribution model --返回所有可能的Action以及其概率
sample model-- 根据概率返回一种行为
样本模型的数学公式:  R,S' = model(S,A)
planning model==动态规划 启发式查询 都是通过模型获取价值信息
learning model==MC TD方法  都是通过experience来获得价值信息

**8.2 Dyna:Learning**
idea：
通过experience直接优化policy&model,同时model又可以间接地优化policy

伪代码  P186
```
// n==0 就是Q-learning公式
loop repeat n times:
S <= random state
A <= random Action in State
R,S' <= model(S,A)
Q(S,A) <= Q(S,A) + α{R + γ*Max_a Q(S',a)-Q(S,A)}
```
可以带来性能上的提高
e.g. P187

**8.3 Prioritized Sweeping**
优化交换
只进行评估前后误差大于seita的策略价值
用作性能优化

其他章节是对于上面章节中的组件进行了分析  我就没看了

**8.11 Monte Carlo Tree Search**
1.MC Search
a.从St模拟K个Episodes(有一个特定的策略模拟,这也是主要缺点--可能并不是最优的)
b.使用a步骤的平均Reward评估当前动作的行为价值Q(St,a)
c.Max Q(St,a)作为实际采取的动作at

2.MC Tree Search
https://zhuanlan.zhihu.com/p/28423255   图形化解释
Value越大的action  越优先选择best-first(被选择的概率越大)
==》其搜索树将越来越深，那些能够引导个体获胜的搜索树内的节点将会被充分的探索，其节点代表的状态价值也越来越有说服力



**summary**
知乎model-based的优缺点   https://zhuanlan.zhihu.com/p/28423255

MC Tree http://www.cnblogs.com/steven-yang/p/5993205.html
