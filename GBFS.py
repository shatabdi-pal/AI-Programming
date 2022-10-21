import numpy as np
import math


class Node:
    def __init__(self, data, depth, f_score):
        self.data = data
        self.depth = depth
        self.f_score = f_score

    def generate_child(self):
        x, y = self.find(self.data, 'b')
        """ value_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        value_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in value_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.depth + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):

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

    def find(self, puz, x):

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

    def f(self,initial, goal):
        return self.h(initial.data, goal)


    #Misplaced tiles#
    # def h(self, initial, goal):
    #     x = np.asarray(initial)
    #     y = np.asarray(goal)
    #     hcost = np.sum(x != y) - 1
    #
    #     if hcost > 0:
    #         return hcost
    #     else:
    #         return 0

    #Manhattan Distance
    def h(self,initial,goal):
        a1 = np.array(initial).flatten()
        a2 = np.array(goal).flatten()
        distance = 0
        for x_i, y_i in zip(a1, a2):
            if x_i != 'b' and y_i != 'b':
                distance += abs(int(x_i) - int(y_i))
        return distance

    def a_search(self,initial,goal):
        initial = Node(initial, 0, 0)
        initial.f_score = self.f(initial, goal)
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

            if self.h(cur.data, goal) == 0:
                break
            for i in cur.generate_child():
                count += 1
                i.f_score = self.f(i, goal)
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
    print("Please enter your choice to run A* search algorithm: \n")
    choice = int(input("1.Misplaced tiles  \n2.Manhattan distance \n3.Euclidean Distance"))
    steps = puz.a_search(ip,gs)
    print("Average number of steps: ", steps)
else:
    print("Initial state to goal state is not solvable")





