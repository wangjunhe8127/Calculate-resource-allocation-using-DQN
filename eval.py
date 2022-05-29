import gym
from stable_baselines3 import DQN
import os
import numpy as np
import torch as th
import random
from PARAMS_SN import TARGET
from train import fixed_seed
import GymEnv
#导入环境
env = gym.make("Assign-v0")
#导入训练好的参数模型
model = DQN.load('%s.pkl'%repr(TARGET))
fixed_seed(1)#固定随机种子
#得到初始状态
state = env.reset().astype(float)
done = False
action_set = []
#开始运行
while not done:
    action,_ = model.predict(state,deterministic=True)
    action_set.append(action)
    state,reward,done,_ = env.step(action)
    state = state.astype(float)
#输出剩余容量
print('剩余容量:',env.abc.reset_data)
#输出动作列表
print('动作列表:',action_set)
#输出成本
print('成本:',env.abc.test_r2)
#记录剩余容量和动作
with open('reset.txt', 'a+') as f:
    for i in range(10):
        f.write(str(env.abc.reset_data[i]))
        f.write('\r\n')
with open('action.txt', 'a+') as f:
    for i in range(15):
        f.write(str(action_set[i]))
        f.write('\r\n')
            