from .utility1 import people_num, delta_t
from numpy import mean
#记得查看各奖励函数区间
class Reward():
    def __init__(self):
        self.H_O_P = []
    def com_rewards(self,inside_T, H_O_P, price):
        tmp1 = self.reward_1(inside_T)
        tmp2 = self.reward_2(H_O_P, price)
        tmp3 = self.reward_3(H_O_P)
        res = tmp1 + tmp2 + tmp3
        self.H_O_P.append(H_O_P)
        return res
    # 计算舒适度奖励
    def reward_1(self,inside_T):
        res = 0.0
        for i in range(people_num):
            tmp = inside_T[i] - 22.0 if inside_T[i] < 28.0 else 28.0-inside_T[i]
            tmp = 0 if tmp > 0 else tmp
            res += tmp
#         print(inside_T)
#         print('1:',res/10)
        return res/10
    # 计算电费
    def reward_2(self,H_O_P, price):
        res = -price * H_O_P * delta_t
#         print('2:',res*2)
        return res/15
    # 计算功率平稳奖励
    def reward_3(self,H_O_P):
        if self.H_O_P == []:
            return 0
        tmp1 = -abs(H_O_P - mean(self.H_O_P))
        tmp2 = -abs(H_O_P - self.H_O_P[-1])
        res = 0.4*tmp1 + 0.6*tmp2
        print(H_O_P)
        return res/2.2
    def reset(self):
        self.H_O_P = []
