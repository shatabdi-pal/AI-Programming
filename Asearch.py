import numpy as np
import math


class Node:
    def __init__(self, data, depth, f_score):
        self.data = data
        self.depth = depth
        self.f_score = f_score

    def generate_child_node(self):
        x, y = self.find_blank(self.data, 'b')
        blank_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in blank_list:
            child = self.swap(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.depth + 1, 0)
                children.append(child_node)
        return children

    def swap(self, puz, x1, y1, x2, y2):

        if (x2 >= 0) and (x2 < len(self.data)) and (y2 >= 0) and (y2 < len(self.data)):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    #To find blank space
    def find_blank(self, puz, x):

        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def user_input(self):
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def get_inversion_count(self, matrix):
        count = 0
        blank = 'b'
        for i in range(0, self.n**2):
            for j in range(i + 1, self.n**2):
                if matrix[i] != blank and matrix[j] != blank and matrix[i] > matrix[j]:
                    count += 1
        return count

    def is_solvable(self, matrix):
        count = self.get_inversion_count([j for sub in matrix for j in sub])
        return count % 2 == 0

    def evalution_function(self,initial, goal):
        return self.heuristic(initial.data, goal) + initial.depth


    # Misplaced tiles#
    def heuristic(self, initial, goal):
        x = np.asarray(initial)
        y = np.asarray(goal)
        hcost = np.sum(x != y) - 1

        if hcost > 0:
            return hcost
        else:
            return 0

    # Manhattan Distance
    # def heuristic(self,initial,goal):
    #     a1 = np.array(initial).flatten()
    #     a2 = np.array(goal).flatten()
    #
    #     # a1 = ['b', 2, 3, 1, 4, 5, 8, 7, 6]
    #     # a2 = [1, 2, 3, 8, 'b', 4, 7, 6, 5]
    #     distance = sum(abs(b % 3 - g % 3) + abs(b // 3 - g // 3) for b, g in ((a1.index(i), a2.index(i)) for i in range(1, 9)))
    #     return distance

    #Eucedian Distance
    # def heuristic(self, initial, goal):
        #return distance

    def a_search(self,initial,goal):
        initial = Node(initial, 0, 0)
        initial.f_score = self.evalution_function(initial, goal)
        """ Put the initial node in the open list"""
        self.open.append(initial)
        print("\n\n")
        count = 0
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            if self.heuristic(cur.data, goal) == 0:
                break
            for i in cur.generate_child_node():
                count += 1
                i.f_score = self.evalution_function(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            self.open.sort(key=lambda x: x.f_score, reverse=False)
        return count


puz = Puzzle(3)
print("Enter the initial state matrix \n")
ip = puz.user_input()
print("Enter the goal state matrix \n")
gs = puz.user_input()

c1 = puz.is_solvable(ip)
c2 = puz.is_solvable(gs)
if c1 == c2:
    print("Initial state to goal state is solvable")
    print("A* search algorithm using number of misplaced tiles\n")
    steps = puz.a_search(ip,gs)
    print("Average number of steps: ", steps)
else:
    print("Initial state to goal state is not solvable")




