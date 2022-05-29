import gym
import numpy as np
import torch as th
import GymEnv
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
import random
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor
from PARAMS_SN import TARGET
from PARAMS import DQN_PARAMS
import os
#定义固定随机数种子函数
def fixed_seed(i):
    random.seed(i)
    os.environ['PYTHONHASHSEED'] = str(i)  # 为了禁止hash随机化，使得实验可复现
    np.random.seed(i)
    th.manual_seed(i)
    th.cuda.manual_seed(i)
    th.cuda.manual_seed_all(i)  # if you are using multi-GPU.
    th.backends.cudnn.benchmark = False
    th.backends.cudnn.deterministic = True
if __name__=='__main__':
    fixed_seed(0)#固定随机种子
    params = DQN_PARAMS()#导入参数
    env = make_vec_env("Assign-v0", n_envs=30,seed = 0)#导入环境
    #模型参数设置
    model = DQN(
        "MlpPolicy", 
        env=env, 
        learning_rate=5e-4,
        gamma=0.99,
        batch_size=300,
        buffer_size=20000,
        learning_starts=0,
        target_update_interval=300,
        policy_kwargs={"net_arch" : params['yes']},
        verbose=0,
        tensorboard_log="../tf-logs/")
    #开始学习
    model.learn(
        total_timesteps=20*10**5,
        n_eval_episodes=60,)
    #学习完成后保存模型
    model.save('%s.pkl'%repr(TARGET))