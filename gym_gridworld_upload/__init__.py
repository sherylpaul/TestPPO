import gym
import numpy as np
from gym.envs.registration import register

register(
    id='GridWorldEGT-v0',
    entry_point='envs3.classic_control.grid_world:GridWorldEGT',
)
register(
    id='GridWorldTest-v0',
    entry_point='envs3.classic_control.grid_world_test:GridWorldTest',
)