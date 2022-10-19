import numpy as np
import math

# Taking user input for initial state
# b is considered as blank
# initial_state = []
# print("Please input values for the initial state")
# for i in range(0,9):
#     x = (input("enter values:"))
#     initial_state.append(x)
#
# initial = tuple(initial_state)
initial = ('b',2,3,1,4,5,8,7,6)
#initial = ("b", "2", "3", "1", "4", "5", "8", "7", "6")
print(initial)

#Taking user input for goal state
#b is considered as blank
# goal_state = []
# print("Please input values from 0-8 for the goal state")
# for j in range(0,9):
#     y = (input("enter values:"))
#     goal_state.append(y)
#
# goal = tuple(goal_state)

goal = (1,2,3,8,'b',4, 7,6,5)

#goal = ("1","2","3","8", "b", "4", "7", "6", "5")
print(goal)

print("Please enter your choice to run A* search algorithm: \n")
choice = int(input("1.Misplaced tiles  \n2.Manhattan distance \n3.Euclidean Distance"))
 

#Huristic#1
def manhattan_distance(initial, goal):
    distance = 0
    for x_i, y_i in zip(initial,goal):
        if x_i != 'b' and y_i !='b':
            distance += abs(x_i - y_i)
            #distance += abs(int(x_i) - int(y_i))
    return distance

hcost_manhattan = manhattan_distance(initial, goal)
print("huristic cost for manhattan distance: ", hcost_manhattan)

#Huristic#2
def misplaced_tiles(initial, goal):
    x = np.asarray(initial)
    y = np.asarray(goal)
    hcost = np.sum(x != y) - 1
    if hcost > 0:
       return hcost
    else:
        return 0
hcost = misplaced_tiles(initial, goal)
print("huristic cost for misplaced tiles: ", hcost)

#Huristic#3
def euclidean_distance(initial, goal):
    x = list(initial)
    y = list(goal)
    x.remove("b")
    y.remove("b")
    distance = math.dist(x,y)

    # p = [eval(i) for i in x]
    # q = [eval(j) for j in y]
    # distance = math.dist(p,q)

    return distance
ecost = euclidean_distance(initial, goal)
print("huristic cost for euclidean: ", ecost)
