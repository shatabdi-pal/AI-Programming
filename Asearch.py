# import numpy as np
# import math
#
# # Taking user input for initial state
# # b is considered as blank
# # initial_state = []
# # print("Please input values for the initial state")
# # for i in range(0,9):
# #     x = (input("enter values:"))
# #     initial_state.append(x)
# #
# # initial = tuple(initial_state)
# initial = ('b',2,3,1,4,5,8,7,6)
# #initial = ("b", "2", "3", "1", "4", "5", "8", "7", "6")
# print(initial)
#
# #Taking user input for goal state
# #b is considered as blank
# # goal_state = []
# # print("Please input values from 0-8 for the goal state")
# # for j in range(0,9):
# #     y = (input("enter values:"))
# #     goal_state.append(y)
# #
# # goal = tuple(goal_state)
#
# goal = (1,2,3,8,'b',4, 7,6,5)
#
# #goal = ("1","2","3","8", "b", "4", "7", "6", "5")
# print(goal)
#
# print("Please enter your choice to run A* search algorithm: \n")
# choice = int(input("1.Misplaced tiles  \n2.Manhattan distance \n3.Euclidean Distance"))
#
#
# #Huristic#1
# def manhattan_distance(initial, goal):
#     distance = 0
#     for x_i, y_i in zip(initial,goal):
#         if x_i != 'b' and y_i !='b':
#             distance += abs(x_i - y_i)
#             #distance += abs(int(x_i) - int(y_i))
#     return distance
#
# hcost_manhattan = manhattan_distance(initial, goal)
# print("huristic cost for manhattan distance: ", hcost_manhattan)
#
# #Huristic#2
# def misplaced_tiles(initial, goal):
#     x = np.asarray(initial)
#     y = np.asarray(goal)
#     hcost = np.sum(x != y) - 1
#     if hcost > 0:
#        return hcost
#     else:
#         return 0
# hcost = misplaced_tiles(initial, goal)
# print("huristic cost for misplaced tiles: ", hcost)
#
# #Huristic#3
# def euclidean_distance(initial, goal):
#     x = list(initial)
#     y = list(goal)
#     x.remove("b")
#     y.remove("b")
#     distance = math.dist(x,y)
#
#     # p = [eval(i) for i in x]
#     # q = [eval(j) for j in y]
#     # distance = math.dist(p,q)
#
#     return distance
# ecost = euclidean_distance(initial, goal)
# print("huristic cost for euclidean: ", ecost)

import numpy as np
import math


class Node:
    def __init__(self, data, depth, f_score):
        """ Initialize the node with the data, depth of the node and the calculated f_score """
        self.data = data
        self.depth = depth
        self.f_score = f_score

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
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
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        """ Specifically used to find the position of the blank space """
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class puzzle:
    def __init__(self, size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []

    def user_input(self):
        """ user_inputs the puzzle from the user """
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,initial, goal):
        """ Heuristic Function to calculate heuristic value f(x) = h(x) + g(x) """
        return self.h(initial.data, goal) + initial.depth

    ##Misplaced tiles
    def h(self, initial, goal):
        x = np.asarray(initial)
        y = np.asarray(goal)
        hcost = np.sum(x != y) - 1

        if hcost > 0:
            return hcost
        else:
            return 0

    def Asearch(self):
        print("Enter the initial state matrix \n")
        initial = self.user_input()
        print(initial)
        print("Enter the goal state matrix \n")
        goal = self.user_input()
        print(goal)

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
            """ If the difference between current and goal node is 0 we have reached the goal node"""

            if self.h(cur.data, goal) == 0:
                break
            for i in cur.generate_child():
                count += 1
                i.f_score = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            """ sort the open list based on f value """
            self.open.sort(key=lambda x: x.f_score, reverse=False)
        return count


print("Please enter your choice to run A* search algorithm: \n")
choice = int(input("1.Misplaced tiles  \n2.Manhattan distance \n3.Euclidean Distance"))
puz = puzzle(3)
steps = puz.Asearch()
print("Average number of steps: ", steps)


