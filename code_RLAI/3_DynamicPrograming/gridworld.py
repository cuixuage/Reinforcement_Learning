#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/9/4 0004 上午 8:03
# @Author   : cuixuange
# @FileName : gridworld.py
# @Contact  : cuixuange1995@gmail.com

# 全局变量
states = [i for i in range(16)]
values = [0 for _ in range(16)]
actions = ["n", "e", "s", "w"]
ds_actions = {"n": -4, "e": 1, "s": 4, "w": -1}
gamma = 0.95  # 100次左右收敛


# gama = 1.00  # 150次左右收敛


# 根据当前的S,A确定下一步状态
def nextState(s, a):
    next_state = s
    if (s % 4 == 0 and a == "w") or (s < 4 and a == "n") or \
            ((s + 1) % 4 == 0 and a == "e") or (s > 11 and a == "s"):
        pass
    else:
        ds = ds_actions[a]
        next_state = s + ds
    return next_state


def rewardOf(s):
    return 0 if s in [0, 15] else -1


def isTerminateState(s):
    return s in [0, 15]


# 获取某一状态下一步的可能状态空间
def getSuccessors(s):
    successors = []
    if isTerminateState(s):
        return successors
    for a in actions:
        next_state = nextState(s, a)
        # if s != next_state:
        successors.append(next_state)
    return successors


# 根据后续状态更新某一状态价值
def updateValue(s):
    sucessors = getSuccessors(s)
    newValue = 0  # values[s]
    num = 4  # len(successors)
    reward = rewardOf(s)
    # 公式 概率*（R + gama*下一步价值）
    # TODO：  state更新
    for next_state in sucessors:
        newValue += 1.00 / num * (reward + gamma * values[next_state])
    return newValue


def printValue(v):
    for i in range(16):
        print('{0:>6.2f}'.format(v[i]), end=" ")
        if (i + 1) % 4 == 0:
            print("")
    print()


# 进行一次迭代
def performOneIteration():
    newValues = [0 for _ in range(16)]
    for s in states:
        newValues[s] = updateValue(s)
    global values
    values = newValues
    printValue(values)


# 在150次左右收敛
def main():
    print("hello")
    max_iterate_times = 160
    cur_iterate_times = 0
    while cur_iterate_times <= max_iterate_times:
        print("Iterate No.{0}".format(cur_iterate_times))
        performOneIteration()
        cur_iterate_times += 1
    printValue(values)


if __name__ == '__main__':
    main()
