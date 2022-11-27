import numpy as np
import random
import math
import matplotlib.pyplot as plt


def create_grid():
  grid = np.random.randint(2, size=(12, 12))
  for i, g in enumerate(grid):
     for j, gr in enumerate(grid[i]):
         if j == 0 or j == 11 or i == 0 or i == 11:
            grid[i][j] = 5
  return grid


class Robby:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.rewards = 0
        self.collection = 0

    def current_sensor(self, grid):
        return grid[self.x][self.y]

    def north_sensor(self, grid):
        return grid[self.x][self.y + 1]

    def south_sensor(self, grid):
        return grid[self.x][self.y - 1]

    def east_sensor(self, grid):
        return grid[self.x + 1][self.y]

    def west_sensor(self, grid):
        return grid[self.x - 1][self.y]

    def pick_up(self, grid):
        if grid[self.x][self.y] == 1:
            grid[self.x][self.y] = 0
            return True
        else:
            return False

    def move_north(self, grid):
        if self.north_sensor(grid) == 5:
            return False
        self.y += 1
        return True

    def move_south(self, grid):
        if self.south_sensor(grid) == 5:
            return False
        self.y -= 1
        return True

    def move_east(self, grid):
        if self.east_sensor(grid) == 5:
            return False
        self.x += 1
        return True

    def move_west(self, grid):
        if self.west_sensor(grid) == 5:
            return False
        self.x -= 1
        return True

    def choose_next_action(self, q_matrix, current_state):
        possible_actions = list()
        PU = q_matrix[current_state][0]
        possible_actions.append(PU)
        N = q_matrix[current_state][1]
        possible_actions.append(N)
        S = q_matrix[current_state][2]
        possible_actions.append(S)
        E = q_matrix[current_state][3]
        possible_actions.append(E)
        W = q_matrix[current_state][4]
        possible_actions.append(W)
        max_action = max(possible_actions)
        if max_action == PU:
            action = 0
        if max_action == N:
            action = 1
        elif max_action == S:
            action = 2
        elif max_action == E:
            action = 3
        elif max_action == W:
            action = 4
        return action

    def action_selection(self,q_matrix, current_state, epsilon):
        if random.randint(1, 100) <= (100 * epsilon):
            action = random.randint(0, 4)
        else:
            action = self.choose_next_action(q_matrix, current_state)
        return action

    def action_performed(self, action, grid):
        if action == 0:
            success = self.pick_up(grid)
            if success:
                self.collection += 1
                reward = 10
            else:
                reward = -1
        elif action == 1:
            success = self.move_north(grid)
            if success:
                reward = 0
            else:
                reward = -5
        elif action == 2:
            success = self.move_south(grid)
            if success:
                reward = 0
            else:
                reward = -5
        elif action == 3:
            success = self.move_east(grid)
            if success:
                reward = 0
            else:
                reward = -5
        elif action == 4:
            success = self.move_west(grid)
            if success:
                reward = 0
            else:
                reward = -5
        return reward

    def convert_state(self, grid):
        state = (self.current_sensor(grid), self.north_sensor(grid), self.south_sensor(grid), self.east_sensor(grid),
                 self.west_sensor(grid))
        return state

    def train_episode(self, grid, q_matrix, epsilon):
        m_steps = 200
        learning_rate = 0.2
        discount_factor = 0.9
        step_count = 0

        while step_count < m_steps:
            current_state = self.convert_state(grid)
            if current_state not in q_matrix:
                q_matrix[current_state] = np.zeros(5)
            action = self.action_selection(q_matrix,current_state, epsilon)
            reward = self.action_performed(action, grid)
            self.rewards += reward

            next_state = self.convert_state(grid)
            if next_state not in q_matrix:
                q_matrix[next_state] = np.zeros(5)

            q_matrix[current_state][action] = q_matrix[current_state][action] + learning_rate * (
                    reward + discount_factor * max(q_matrix[next_state]) - q_matrix[current_state][action])
            step_count += 1

    def train_robby(self, q_matrix):
        episodes = 5000
        epsilon = 0.1
        episode_count = 0
        reward_list = list()

        while episode_count < episodes:
            grid = create_grid()
            self.x = random.randint(1, 10)
            self.y = random.randint(1, 10)
            self.collection = 0
            self.rewards = 0
            self.train_episode(grid, q_matrix, epsilon)
            print("Total can collected: ", self.collection)
            print("Total reward received: ", self.rewards)
            point_lost = (self.collection * 10) - self.rewards
            print("Point lost: ", point_lost)
            print("Iteration: ", episode_count)
            episode_count += 1
            if ((episodes - episode_count) % 50) == 0:
                epsilon -= 0.001
                reward_list.append(self.rewards)
        print("Average reward for training: ", (sum(reward_list) / (episodes / 50)))
        plt.plot(reward_list)
        train_fig = plt.figure()
        plt.show()

    def test_episode(self, grid, q_matrix, epsilon):
        m_steps = 200
        step_count = 0
        while step_count < m_steps:
            current_state = self.convert_state(grid)
            action = self.action_selection(q_matrix, current_state, epsilon)
            reward = self.action_performed(action, grid)
            self.rewards += reward
            step_count += 1

    def test_robby(self, q_matrix):
        episodes = 1000
        epsilon = 0.1
        episode_count = 0
        reward_list = list()

        while episode_count < episodes:
            grid = create_grid()
            self.x = random.randint(1, 10)
            self.y = random.randint(1, 10)
            self.collection = 0
            self.rewards = 0
            self.test_episode(grid, q_matrix, epsilon)
            reward_list.append(self.rewards)
            episode_count += 1
        print("Average reward for test: ", (sum(reward_list) / episodes))
        plt.plot(reward_list)
        test_fig = plt.figure()
        plt.show()


Q_matrix = {}
Robot = Robby()
Robot.train_robby(Q_matrix)
Robby.test_robby(Q_matrix)




