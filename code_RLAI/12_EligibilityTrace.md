**Sarsa(λ)实践**  
Model-Free

*先验知识*  
https://zhuanlan.zhihu.com/p/28108498  
1.资格迹定义的来源公式 chapter12  
2.定义  
E0(s,a)=0  
Et(s,a) = γ * λ * Et-1(s,a) + 1  其中(St=s,At=a)  
3.引入资格迹的Q值更新公式:
Q(s,a) = Q(s,a) + α * {Rt+1 + γ*Q(S',a') -Q(s,a)} * Et(s,a)  

它体现的是一个结果和某一个state-actin之间的因果关系。得到刺果的最近以及最频繁出现的state-action认为影响此结果的权重高  

*背景*
windy gridWorld 的引入资格迹Sarsaλ算法

*目的*
Agent遵循着某一个策略选择Action,得到Env的反馈信息(Reward+S'变化),来优化策略 

*伪代码*
https://zhuanlan.zhihu.com/p/28180443  
```python
Repeat episode{
    E(s,a)=0  //For all S,all A
    while not done{
        take action A,observe R,S’
        根据on-policy得到 S' A'
        计算δ
        E(s,a) += 1         //经历的越多 对应E值越大
        
        //更新all s, all a----trick1
        //同时在  近期发生γ 或者频繁发生λ   的Q(S,A)变化更加明显一些
        for(整体state-value空间){
            for(Agent的action-space 比如上下左右){
                //更新Q
                //更新E
            }
        }
    }
    //一次episode结束
}
```

**trick**
1.Q表E表  字典套字典 key:state value:{key:action value:State-action的价值}  
https://zhuanlan.zhihu.com/p/28108498  
解释为什么不选择只更新agent经历过的Q表E表  

2.*参数lamda更新E时候的作用*  
2.1 初始状态E(s0,a0)=1,后续的Q值没有发生变化。E值变化就是对路径有记忆
2.2 直到终止状态,遇到非0的Reward：更新之前经历过的所有Q,越近的+越频繁的Q值变化更加明显

3.每次episode清空E表  https://zhuanlan.zhihu.com/p/28108498  

**三个参数**
经过试验得出
# lamda越大=动作越频繁的Q变化越大
# gama越大,越重视下一步Q(s',a')
# alpha越小,越重视上一步Q(s,a)经验
