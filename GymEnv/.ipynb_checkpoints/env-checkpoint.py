import gym
import math
import numpy as np
from .utility import system
gym.logger.set_level(40)
class Env(gym.Env):
    # 初始化参数
    def __init__(self):
        self.abc = system()
        #状态空间12维
        self.observation_space = gym.spaces.Box(low=-10, high=10, shape=(12,1))
        #动作空间10维，每次输出一个
        self.action_space = gym.spaces.Discrete(10)
        # 当前步长
        self.number = 0
    def get_state(self):
        tmp1 = np.array(self.abc.reset_data).reshape(10,1)
        tmp2 = np.array([self.abc.func_data[self.number],self.abc.func_data[self.number]*8]).reshape(2,1)
        state = np.vstack((tmp1,tmp2))
        return state/10
    # 主程序
    def step(self, action):
        #分配一次，并得到奖励
        reward = self.abc.assign_step(action,self.number)
        #更新状态
        state = self.get_state()
        #一个回合分配结束
        if self.number == 14:
            done = True
        else: 
            done = False
            self.number = self.number + 1
        return state, reward, done, {}
    # 重置环境
    def reset(self):
        self.number = 0
        self.abc.reset()
        return self.get_state()