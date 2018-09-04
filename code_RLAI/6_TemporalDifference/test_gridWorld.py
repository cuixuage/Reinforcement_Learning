#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/9/4 0004 下午 14:50
# @Author   : cuixuange
# @FileName : test_gridWorld.py
# @Contact  : cuixuange1995@gmail.com

from gridworld import GridWorldEnv
from gym import spaces

env = GridWorldEnv(n_width=12,          # 水平方向格子数量
                   n_height = 4,        # 垂直方向格子数量
                   u_size = 60,         # 可以根据喜好调整大小
                   default_reward = -1, # 默认格子的即时奖励值
                   default_type = 0)    # 默认的格子都是可以进入的
env.action_space = spaces.Discrete(4)   # 设置行为空间数量
# 格子世界环境类默认使用0表示左，1：右，2：上，3:下，4,5,6,7为斜向行走
# 具体可参考_step内的定义
# 格子世界的观测空间不需要额外设置，会自动根据传输的格子数量计算得到
env.start = (0,0)
env.ends = [(11,0)]
# 悬崖的格子的即时奖励设为-100
# 这个例子中没有不可进入的格子，所以不需要对格子类型进行修改。示例中悬崖格子是终止状态
for i in range(10):
    env.rewards.append((i+1,0,-100))
    env.ends.append((i+1,0))
# 特殊类型的格子设置类似于即时奖励设置，比如我们将坐标为（5,1）和（5,2）的两个格子设为不可进入，可以添加如下代码
env.types = [(5,1,1),(5,2,1)]
# 最后为了使这些设置在实际生效，调用刷新设置方法
env.refresh_setting()
env.reset()

env.render()
input("press any key to continue...")