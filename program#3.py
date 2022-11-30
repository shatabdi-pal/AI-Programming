import math
import random
import numpy as np
import statistics as st
import matplotlib.pyplot as plt


def create_grid():
    grid = np.random.randint(2, size=(10, 10))
    for i, g in enumerate(grid):
        for j, gr in enumerate(grid[i]):
            if j == 0 or j == 9 or i == 0 or i == 9:
                grid[i][j] = 5
    return grid


class Robby:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.rewards = 0
        self.collection = 0

    def current_sensor(self, grid):
        if (0 <= self.x <= 9) and (0 <= self.y <= 9):
            return grid[self.x][self.y]

    def north_sensor(self, grid):
        if (0 <= self.x <= 9) and (0 <= self.y < 9):
            return grid[self.x][self.y + 1]

    def south_sensor(self, grid):
        if (0 <= self.x <= 9) and (0 < self.y < 9):
            return grid[self.x][self.y - 1]

    def east_sensor(self, grid):
        if (0 <= self.x < 9) and (0 <= self.y <= 9):
            return grid[self.x + 1][self.y]

    def west_sensor(self, grid):
        if (0 < self.x < 9) and (0 <= self.y <= 9):
            return grid[self.x - 1][self.y]

    def pick_up(self, grid):
        if (0 <= self.x <= 9) and (0 <= self.y <= 9) and grid[self.x][self.y] == 1:
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

    def next_action(self, q_matrix, current_state):
        action_lists = list()
        pick_up = q_matrix[current_state][0]
        action_lists.append(pick_up)
        north = q_matrix[current_state][1]
        action_lists.append(north)
        south = q_matrix[current_state][2]
        action_lists.append(south)
        east = q_matrix[current_state][3]
        action_lists.append(east)
        west = q_matrix[current_state][4]
        action_lists.append(west)
        max_action = max(action_lists)
        if max_action == pick_up:
            action = 0
        if max_action == north:
            action = 1
        elif max_action == south:
            action = 2
        elif max_action == east:
            action = 3
        elif max_action == west:
            action = 4
        return action

    def action_selection(self, q_matrix, current_state, epsilon):
        if random.randint(1, 100) <= (100 * epsilon):
            action = random.randint(0, 4)
        else:
            action = self.next_action(q_matrix, current_state)
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
            action = self.action_selection(q_matrix, current_state, epsilon)
            reward = self.action_performed(action, grid)
            self.rewards += reward

            next_state = self.convert_state(grid)
            if next_state not in q_matrix:
                q_matrix[next_state] = np.zeros(5)

            q_matrix[current_state][action] = q_matrix[current_state][action] + learning_rate * (
                    reward + discount_factor * max(q_matrix[next_state]) - q_matrix[current_state][action])
            step_count += 1

    def train_robby(self, q_matrix):
        n_episodes = 5000
        epsilon = 0.1
        episode_count = 0
        reward_list = list()

        while episode_count < n_episodes:
            grid = create_grid()
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 9)
            self.collection = 0
            self.rewards = 0
            self.train_episode(grid, q_matrix, epsilon)
            # print("Iteration: ", episode_count)
            # print("Total can collected: ", self.collection)
            # print("Total reward received: ", self.rewards)
            # point_lost = (self.collection * 10) - self.rewards
            # print("Point lost: ", point_lost)
            episode_count += 1
            if ((n_episodes - episode_count) % 50) == 0:
                epsilon -= 0.001
                reward_list.append(self.rewards)
            average_train_reward = sum(reward_list) / (n_episodes / 50)
        print("Average reward for training: ", average_train_reward)
        plt.title("Training Reward to the episodes")
        plt.plot(reward_list)
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
        n_episodes = 5000
        epsilon = 0.1
        episode_count = 0
        reward_list = list()

        while episode_count < n_episodes:
            grid = create_grid()
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 9)
            self.collection = 0
            self.rewards = 0
            self.test_episode(grid, q_matrix, epsilon)
            reward_list.append(self.rewards)
            episode_count += 1
        average_test_reward = sum(reward_list) / n_episodes
        stddev_test = st.stdev(reward_list)
        print("Average reward for test: ", average_test_reward)
        print("Test Standard Deviation ", stddev_test)


Q_matrix = {}
Robot = Robby()
Robot.train_robby(Q_matrix)
Robot.test_robby(Q_matrix)




