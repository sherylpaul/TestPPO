import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import os
import pickle
# from gym.envs.classic_control.rendering import SimpleImageViewer
import random
import xlrd
from xlwt.Style import *
from xlrd import open_workbook
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
STAY = 4
failed_count = 0
reached_count = 0

map = []
start_area = []
goal_area = []
obstacle_area = []
number_of_agents = 1
transition_probability = dict()
map_values = dict()
average_path_per_round = 0
collision_value = 0

info = dict()

def is_legal(state,chosen_action):
    # print("state is", state, type(state), "action is", action)
    global map
    global rows
    x = state[0]
    y = state[1]
    # print("Received in is legal", chosen_action)
    action = chosen_action
    try:
        if action == UP :
            if y>= (cols-1):
                return 0
            else:
                if map[x][y+1] == 'E' or map[x][y+1] == 'S' or map[x][y+1] == 'G':

                    return 1
                elif map[x][y+1] == '0'or map[x+1][y] == 'O':

                    return 2
            return 3
        elif action == DOWN :
            if y<=0 :
                return 0
            else:
                if map[x][y-1] == 'E' or map[x][y-1] == 'S'or map[x][y-1] == 'G':
                    return 1
                elif map[x][y-1] == '0'or map[x+1][y] == 'O':
                    return 2
            return 4
        elif action == LEFT :

            if x<=0 :
                return 0
            else:
                if map[x-1][y] == 'E'or map[x-1][y] == 'S'or map[x-1][y] == 'G':
                    return 1
                elif map[x-1][y] == '0' or map[x+1][y] == 'O':

                    return 2
            return 5
        elif action == RIGHT :
            if x>= (rows-1) :
                return 0
            else:
                if map[x+1][y] == 'E' or map[x+1][y] == 'S' or map[x+1][y] == 'G':
                    return 1
                elif map[x+1][y] == '0' or map[x+1][y] == 'O':
                    return 2
            # print("map right", map[x+1][y])
            return 6
        elif action == STAY:
            return 1

    except Exception as e:
        print("Exception", action, x,y, map[x][y], e)
        return 0



class GridWorldTest(gym.Env):
    metadata = {'render.modes': ['console']}
    def __init__(self):
        global map
        global map_values
        global start_area
        global goal_area
        global rows
        global obstacle_area
        global collision_value
        global map_name
        global cols
        global average_path_per_round
        #enter map name as 50x50_map or 100x100_map
        map_name = "50x50_map"
        pickle_file = "/Users/sherylpaul/Desktop/MARL EGT/gym_gridworld_upload/envs3/classic_control/" + map_name +".pkl"
        with open(pickle_file, 'rb') as f:
            map = pickle.load(f)
            start_area = pickle.load(f)
            obstacle_area = pickle.load(f)
            goal_area = pickle.load(f)
        rows = cols = len(map)
        print("Len", len(map), len(start_area), len(goal_area), len(obstacle_area))
        # book = xlrd.open_workbook("/Users/sherylpaul/Desktop/MARL EGT/gym_gridworld/envs3/classic_control/Excel_100x100_map.xls", formatting_info = True)
        # sheets = book.sheet_names()
        # print ("sheets are:", sheets)
        # map_name = "100x100_map.txt"

        # map = []
        # start_area = []
        # goal_area = []
        # obstacle_area = []
        # number_of_agents = 1
        # transition_probability = dict()
        # for index, sh in enumerate(sheets):
        #     sheet = book.sheet_by_index(index)
        #     print("Sheet:", sheet.name)
        #     rows, cols = sheet.nrows, sheet.ncols

        #     all_colours = []
        #     for row in range(1,rows):
        #         line = []
        #         for col in range(cols):
        #             # print("row, col is:", row+1, col+1,)
        #             xfx = sheet.cell_xf_index(row, col)
        #             xf = book.xf_list[xfx]
        #             bgx = xf.background.pattern_colour_index
        #             # print(bgx)
        #             all_colours.append(bgx)
        #             transition_probability[str([row-1,col])] = {'up':0.2, 'down':0.2, 'left':0.2, 'right':0.2, 'stay':0.2}
        #             # if 15<=row<=25 and 9<=col<=12:
        #             #     print("Background of goal",bgx)
        #             # if 17<=row<=25 and 3<=col<=5:
        #             #     print("Background of obst",bgx)
        #             if bgx == 13 or bgx == 12:
        #                 line.append('S')
        #                 start_area.append([row-1,col])
        #             elif bgx == 16:
        #                 line.append('0')
        #                 obstacle_area.append([row-1,col])
        #             elif bgx == 14:
        #                 line.append('G')
        #                 goal_area.append([row-1,col])
        #             else:
        #                 line.append('E')
        #         map.append(line)
        # # f = open("/Users/sherylpaul/Desktop/MARL EGT/gym_gridworld/envs3/classic_control/200x200_map.txt", "r")
        # # map_name = "200x200_map.txt"
        # # for line in f:
        # #     columns = len(line)
        # #     map.append(list(line.rstrip()))
        # # for x in range(len(map)):
        # #     for y in range(len(map[x])):
        # #         if map[x][y] == 'S':
        # #             start_area.append([x,y])
        # #         if map[x][y] == 'G':
        # #             goal_area.append([x,y])
        # #         if map[x][y] == '0' or map[x][y] == 'O' or x == 0 or y == 0 or x >= (len(map)-2) or y >= (len(map)-2):
        # #             obstacle_area.append([x,y])

        # # min_distance_to_goal = dict()
        # rows = len(map)
        # cols = len(map[0])

        # print("Rows, columns", len(map),len(map[0]))
        # print("Length of start area, goal area, obstacle area", len(start_area), len(goal_area),len(obstacle_area))
        # new_colours = set(all_colours)
        # print(new_colours)
        # for i in new_colours:
        #     print("Colour", i, "Occurences", all_colours.count(i))
        # for x in range(rows):
        #     for y in range(columns):
        #         int_state_temp = int(x)*rows + int(y)
        #         print("State", x, y, int_state_temp)
        #         safety_value = 0
        #         for i in range(-1,1):
        #             for j in range(-1,1):
        #                 if i== 0 and j== 0:
        #                     safety_value+=0
        #                 else:
        #                     if (x+i)<0 or (x+i)>=rows or (y+j)<0 or (y+j)>=columns or map[x+i][y+j] == '0' :
        #                         safety_value += round(float(-1/(abs(i)+abs(j))),2)
        #                     else:
        #                         safety_value += round(float(1/(abs(i)+abs(j))),2)
        #                 distances_to_goals = []
        #                 for k in goal_area:
        #                     distances_to_goals.append(int(abs(k[0]-x)+abs(k[1]-y)))
        #         # ("X and Y", x, y, distances_to_goals)
        #         min_distance = min(distances_to_goals)
        #         min_distance_to_goal[tuple([x,y])] = min_distance
        #         if min_distance == 0:
        #             min_distance = 1
        #         map_values[tuple([x,y])] = round(safety_value + float(rows/min_distance),2)

        self.n_agents = 1
        self.n_states = rows*cols
        print("number of states", self.n_states)
        self.n_actions = 5
        self.action_space = spaces.Discrete(5)


        print("Action space", self.action_space)
        self.observation_space = gym.spaces.Box(low=0, high=1000, shape = (2,))
        print("observation space", self.observation_space)
        # self.observation_space = gym.spaces.Discrete(1)
        self.state = []

        self.state = random.choice(start_area).copy()
        self.path = []
        self.collision_value = 0
        self.reward = 0
        print("Start area", self.state)

    def step(self, action):
        global info
        global rows
        global collision_value
        global cols
        global average_path_per_round
        global reached_count
        global failed_count
        # print("Entering step", self.state, action)


        if self.state in goal_area or len(self.path)>=200 or self.done == True:
            if len(self.path)>=200:
                self.reward += -1
                print("FAILED")
                failed_count += 1
            # print("Length of path", len(self.path))

            self.done = True
            average_path_per_round += len(self.path)


        else:
            # print("In step State", self.state, "action", action)
            flag = is_legal(self.state,action)
            # print("FLAG ", flag)
            # average_reward = min(self.reward)
            if flag == 0 or flag == 2:
                self.collision_value -= 1
                # print("Appending", len(self.path))
                self.path.append(self.state)



            else:
                self.reward, self.state, self.collision_value = self.take_action(action)


        return self.state, self.reward, self.done, info

    def reset(self):
        global start_area
        self.done = False
        self.state = random.choice(start_area).copy()
        # print("New start area", self.state)
        self.path = []
        self.collision_value = 0
        self.reward = 0

        try:
            return self.state
        except Exception as e:
            print("Exception", e)


    def render(self, mode='console'):
        '''
            render the state
        '''
        if mode != 'console':
          raise NotImplementedError()
        global map
        global map_values
        global start_area
        global goal_area

        row  = self.state[0]// self.size
        col  = self.state[1] % self.size

        for r in range(len(map)):
            for c in range(len(map[0])):
                if r == row and c == col:
                    print("X",end='')
                else:
                    print(map[r][c],end='')
            print('')

    def take_action(self, action):
        global reached_count

        if is_legal(self.state, action) == 1:
            self.reward += -1
            self.path.append(self.state.copy())
            if action == UP:
                directions = [0,1]
                self.state[0] = self.state[0]+directions[0]
                self.state[1] = self.state[1]+directions[1]
            if action == DOWN:
                directions = [0,-1]
                self.state[0] = self.state[0]+directions[0]
                self.state[1] = self.state[1]+directions[1]
            if action == LEFT:
                directions = [-1,0]
                self.state[0] = self.state[0]+directions[0]
                self.state[1] = self.state[1]+directions[1]
            if action == RIGHT:
                directions = [1,0]
                self.state[0] = self.state[0]+directions[0]
                self.state[1] = self.state[1]+directions[1]



            if self.state in goal_area:
                print("REACHED", len(self.path))
                reached_count += 1
                for k in range(len(self.path)):
                    dist_to_obstacle = []
                    for j in obstacle_area:
                        dist_to_obstacle.append(int(abs(j[0]-int(self.path[k][0]))+abs(j[1]-int(self.path[k][1]))))
                    self.collision_value += min(dist_to_obstacle)
                self.reward += 100







        # average_reward = float(sum(self.reward)/self.n_agents)
        return self.reward, self.state, self.collision_value
