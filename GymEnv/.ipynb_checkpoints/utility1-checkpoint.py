'''''
用户数为5
'''''
import math
import numpy as np
from .utility2 import load_execl, people_num, delta_t
people_num = people_num
delta_t = delta_t
RAC = 18
QAC = 2.25
Ceq = 0.525
Rqq = 18

# 系统模型
class ABC:
    def __init__(self):
        self.load_system_parameter()
        self.inside_now_temperature = np.array(self.inside_init_temperature).reshape(len(self.inside_init_temperature[0]),1)
        self.price = 0.0
    # 导入并温度初始值、不参与调控的功率、室外温度、光伏发电功率
    def load_system_parameter(self):
        self.inside_init_temperature = load_execl(r'~/Heating_distribution/GymEnv/source/Init_Temperature.xlsx')#行向量:不同用户的初始室内温度
        self.other_power = load_execl(r'~/Heating_distribution/GymEnv/source/Other_Power.xlsx', people_num)#二维矩阵:第一维为用户，第二维为不同时刻的不参与调控功率值
        self.outside_temperature = load_execl(r'~/Heating_distribution/GymEnv/source/Outside_Temperature.xlsx') #行向量：不同时刻的室外温度值，所有用户的都一样
        self.photovoltaics = load_execl(r'~/Heating_distribution/GymEnv/source/Photovoltaics.xlsx') #行向量，不同时刻光伏发电功率值，所有用户都一样
    # 计算室内温度
    def com_inside_temperature(self, action, t):#需要根据action的形状得到tmp3
        coefficient = -delta_t/(Rqq*Ceq)
        tmp1 = self.inside_now_temperature * math.exp(coefficient)
        tmp2 = np.array(self.outside_temperature[0][int(t/delta_t)]) * (1 - math.exp(coefficient))
        tmp3 = action * QAC * RAC * (1-math.exp(coefficient))
        self.inside_now_temperature = tmp1 + tmp2 + tmp3
    # 计算电价
    def com_price(self, t):
        if 0.0<t<7.0 or 22.0<t<24.0:
            self.price = 0.3
        elif 7<t<11 or 14<t<18:
            self.price = 0.5
        else:
            self.price = 0.8
    # 计算每一时刻,所有用户取暖+不参与调控-光伏的功率值
    def com_H_O_P(self, action, t):
        self.H_O_P = 0
        for i in range(people_num):
            tmp = action[i]*QAC + self.other_power[i][int(t/delta_t)] - self.photovoltaics[0][int(t/delta_t)]
            self.H_O_P += tmp
    # 一步仿真
    def sim_step(self, t, action):
        self.com_inside_temperature(action, t)
        self.com_price(t)
        self.com_H_O_P(action, t)
    def reset_abc(self):
        self.inside_now_temperature = np.array(self.inside_init_temperature).reshape(people_num, 1)
# 测试
if __name__ == '__main__':
    test = ABC()
    test.load_system_parameter()