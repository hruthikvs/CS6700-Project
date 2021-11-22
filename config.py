import os
import aicrowd_gym
import gym_bellman
import numpy as np
from tqdm import tqdm


config = {"acrobot": [0, 0], "taxi": [0, 0], "kbca": [0, 0], "kbcb": [0, 0], "kbcc": [0, 0]}


env = aicrowd_gym.make("Taxi-v3")
config['taxi'] = [env.observation_space.n,env.action_space.n]
print(config)

