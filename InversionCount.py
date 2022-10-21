import numpy as np
import math
def getInversionCount(puzzle):
    count = 0
    blank = 'b'
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if puzzle[i] != blank and puzzle[j] != blank and puzzle[i] > puzzle[j]:
                count += 1
    return count

def isSolvable(puzzle):
    #for sub in puzzle:
        #for j in sub:
    count = getInversionCount([j for sub in puzzle for j in sub])
           # count = getInversionCount(j)
    return (count % 2 == 0)



#initial = [[4, 5, 'b'], [6, 1, 8], [7, 3, 2]]
#goal = [[1, 2, 3], [4, 5, 6], [7, 8, 'b']]

initial = [['b', 2, 3], [1, 4, 5], [8, 7, 6]]
goal = [[1, 2, 3], [8, 'b', 4], [7, 6, 5]]

c1 = isSolvable(initial)
c2 = isSolvable(goal)
print (c1 , c2)

if c1 == c2:
    print("Solvable")
else:
    print("Not Solvable")

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
a1 = np.array(initial).flatten()
a2 = np.array(goal).flatten()
#Huristic#1
def manhattan_distance(initial, goal):
#     distance = 0
#     for x_i, y_i in zip(initial,goal):
#         if x_i != 'b' and y_i !='b':
#             #distance += abs(x_i - y_i)
#             distance += abs(int(x_i) - int(y_i))
#     return distance
    return sum(abs(int(val1.item())-int(val2.item())) for val1, val2 in zip(initial,goal))
#
hcost_manhattan = manhattan_distance(a1, a2)
print("huristic cost for manhattan distance: ", hcost_manhattan)
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
#Huristic#3
# def euclidean_distance(initial, goal):
#     x = list(initial)
#     y = list(goal)
#     # x.remove("b")
#     # y.remove("b")
#     #distance = math.dist(x, goal)
#
#     p = [eval(i) for i in x]
#     q = [eval(j) for j in y]
#     distance = math.dist(p,q)
#
#     return distance
# ecost = euclidean_distance(a1, a2)
# print("huristic cost for euclidean: ", ecost)
