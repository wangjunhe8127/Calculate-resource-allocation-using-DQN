import numpy as np

from PARAMS import equipment, func
import random
import copy
#系统类
class system():
    def __init__(self):
        random.seed(0)#固定函数选取顺序
        data = np.array(equipment,dtype=float).reshape(10, 3)#导入设备信息
#         random.shuffle(func)#函数顺序先打乱
        shuffle_func = np.array(func,dtype=float).reshape(15,2)#导入排序后的函数信息
        shuffle_fun=np.argsort(-shuffle_func)
        self.data =data[:,0]#设别容量
        self.ability =data[:,1]#设备能力
        self.trans_time =data[:,2]#设备传输时间
        self.func_data = shuffle_func[:,0]#函数数据量
        self.func_time = shuffle_func[:,1]#函数时间容忍度
        self.now_comsum_time = 0#当前消耗时间
        self.test_r2 = 0#记录回合成本
        self.reset_data = copy.deepcopy(self.data)#剩余容量
        #分配一次后更新所有设备信息
    def assign_step(self,action,number):
        #计算消耗时间
        self.now_comsum_time = self.func_data[number]/self.ability[action] + self.trans_time[action]
        #更新剩余容量
        self.reset_data[action] = self.reset_data[action]-self.func_data[number]
        #获取回合奖励
        reward= self.assign_reward(action,number)
        return reward
        #定义获取回合奖励函数
    def assign_reward(self,action,number):
        #消耗时间惩罚
        r1 = -self.now_comsum_time+self.func_time[number] if self.now_comsum_time>self.func_time[number] else 0
        #成本惩罚
        r2 = (-0.3*self.data[action]-0.7*self.ability[action])/25#调节系数
        #剩余容量负数惩罚
        r3 = -2 if self.reset_data[action]<0 else 0
        #记录当前回合成本
        self.test_r2 = self.test_r2+r2
        print(r1,r3)
        reward = r1+r2+r3
        return reward 
        #将参数恢复到初始值
    def reset(self):
        self.now_comsum_time = 0
        self.reset_data = copy.deepcopy(self.data)
        self.use_num = np.array([0.0]*10,dtype=int).reshape(10,1)
if __name__ == '__main__':
    abc = system()
    print(abc.func_data)