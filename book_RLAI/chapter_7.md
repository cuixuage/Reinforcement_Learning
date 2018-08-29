


**P174 n-step tree backup algorithm**
这部分的公式没有细看




**n-step Bootstraping**

**7.1 prediction**
example P167
大规模的随机行走

T(λ)向前 向后观点
**7.2 sarsa control**

**7.3 off-policy Learning**
重要性采样
**7.5 off-policy without importantce Sampling**

**总结**
频率启发 frequency Heuristic 将原因归因于频率出现最高的状态
就近启发 recency Heuristic 将原因归因于就近的几次状态

λ收获:
任意n步的reward添加权重 (1-λ)*λ^(n-1)
所以所有步数的权重为  1-λ   (1-λ)*λ  。。。。。所有权重加起来的和为1
λ取值区间为[0,1]，当λ=1时对应的就是MC算法
