# import random
# from random import randint
# import numpy as np
# import itertools
# from collections import defaultdict
# import gym
# import json
# # import sys
# # # sys.path.insert(0,'/Users/sherylpaul/Desktop/MARL EGT/gym_gridworld/')
# # print(sys.path)
# from stable_baselines3 import PPO
# # from stable_baselines.common.policies import MlpPolicy
# # from stable_baselines import PPO2
# from envs3.classic_control import *
# import tensorflow as tf
# import torch as th
# import datetime
# a = datetime.datetime.now().replace(microsecond=0)
# env = gym.make('GridWorldEGT-v0')
# env_test = gym.make('GridWorldTest-v0')


# # n_observations = env.n_states
# # n_actions = env.n_actions
# #  model = PPO2(MlpPolicy, env, verbose=1)
# # policy_kwargs = dict(act_fun=tf.nn.tanh, net_arch=[4, 16])
# # Create the agent
# # policy_kwargs = dict(activation_fn=th.nn.ReLU, net_arch=[4, 16])
# # Create the agent
# model = PPO("MlpPolicy", env, learning_rate=0.0005, verbose=1)


# model.learn(total_timesteps=100000)
# obs = env_test.reset()

# action_list = dict()
# action_list = {'0': 'up','1': 'right','2': 'down','3': 'left','4': 'stay' }
# rewards_per_episode = []
# failed = 0
# number_of_agents = 2
# episode_length = []
# # observations = [[] for i in number_of_agents]
# print("observation", obs, "type", type(obs))
# for i in range(100):

#   episode_reward = 0
#   print("Round", i)
#   flagger = 1
#   epi_length = 0

#   while flagger:
#     action_list = []
#     for j in range(len(obs)):
#       action, _states = model.predict([obs[j],[0,0]], deterministic = False)
#       action_list.append(action[0])
#     # action = [1]
#     obs, rewards, done, info = env_test.step(action_list)
#     # print("reward", rewards)
#     key = str(action)
#     epi_length += 1
#     if done:
#       obs = env_test.reset()
#       flagger = 0
#   rewards_per_episode.append(episode_reward)
#   episode_length.append(epi_length)
#   # if episode_reward <= -200:
#   #   failed += 1
#   #   obs = env.reset()
# # print(rewards_per_episode)
# # print(sum(rewards_per_episode))
# # print(episode_length)
# # print(sum(episode_length))
# # print(failed)
# # from envs3.classic_control.grid_world import average_path_per_round
# # print("Average path per round", average_path_per_round)
# # avg_path_length = round(float(sum(episode_length)/len(episode_length)),2)
# # avg_collision_value = round(float(collision_value/sum(episode_length)),2)

# # b = datetime.datetime.now().replace(microsecond=0)
# # print("Average path length", avg_path_length,'\n', "Average collision value", avg_collision_value, '\n', "Time taken", b-a)
# # try:
# #     ppo_results = json.load(open("ppo_learning_results.json"))
# # except:
# #     ppo_results = dict()
# # number_of_agents = 1
# # key = map_name.split('_')[0]+","+ str(number_of_agents)
# # b = datetime.datetime.now().replace(microsecond=0)
# # print("Computation time", b-a)
# # time_taken = str(b-a)
# # ppo_results[key] = [avg_path_length, avg_collision_value, time_taken]
# # with open("ppo_learning_results.json", "w") as outfile:
# #     json.dump(ppo_results, outfile)


#   # if done:
#   #     obs = env.reset()
# #   env.render()
# from envs3.classic_control.grid_world_test import failed_count, reached_count
# print("Failed", failed_count, "Reached", reached_count)

import random
from random import randint
import numpy as np
import itertools
from collections import defaultdict
import gym
import json
# import sys
# # sys.path.insert(0,'/Users/sherylpaul/Desktop/MARL EGT/gym_gridworld/')
# print(sys.path)
from stable_baselines3 import PPO
# from stable_baselines.common.policies import MlpPolicy
# from stable_baselines import PPO2
from envs3.classic_control import *
import tensorflow as tf
import torch as th
import datetime
a = datetime.datetime.now().replace(microsecond=0)
env = gym.make('GridWorldTest-v0')


model = PPO("MlpPolicy", env, learning_rate=0.0005, verbose=1)


model.learn(total_timesteps=100)
obs = env.reset()
action_list = dict()
action_list = {'0': 'up','1': 'right','2': 'down','3': 'left','4': 'stay' }
rewards_per_episode = []
failed = 0
number_of_agents = 2
episode_length = []
for i in range(100):
  episode_reward = 0
  print("Round", i)
  flagger = 1
  epi_length = 0
  while flagger:
    action, _states = model.predict(obs, deterministic = False)
    # action = [1]
    obs, rewards, done, info = env.step(action)
    # print("reward", rewards)
    key = str(action)
    epi_length += 1
    if done:
      obs = env.reset()
      flagger = 0
  rewards_per_episode.append(episode_reward)
  episode_length.append(epi_length)

print(rewards_per_episode)
print(sum(rewards_per_episode))
print(episode_length)
print(sum(episode_length))
print(failed)
