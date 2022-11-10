#def euclidean_distance():
import numpy as np
import math
# distance = 0
# x = [(0, 0),(0,1),(0, 2),(1,0),(1, 1),(1,2),(2, 0),(2,1),(2,2)]
# y = [(1,1),(0,1),(0,2),(0,0),(1,2),(2,2),(1,0),(2,0),(2,1)]
# P= np.array(x)
# Q= np.array(y)
# print(np.sum(np.abs(P[0, :] - Q[0, :])))
# #print(distance)


#board = [7, 2, 4, 5, 0, 6, 8, 3, 1]
# initial = ['b',2,3,1,4,5,8,7,6]
# goal = [1,2,3,8,'b',4, 7,6,5]
initial = []
for i in range(0, 3):
    temp = input().split(" ")
    initial.append(temp)
print(initial)

# #print(np.array(puz))
a1 = np.array(initial).flatten()
# print(a1[0])
goal = []
for i in range(0, 3):
    temp = input().split(" ")
    goal.append(temp)
print(goal)
a2 = (np.array(goal).flatten())
# print("Enter the goal state matrix \n")
# gs = user_input()
# print(gs)
# a1 = np.array(initial).flatten()
# a2 = np.array(goal).flatten()
print( sum(abs((int(val)-1)%3 - i%3) + abs((int(val)-1)//3 - i//3) for i, val in enumerate(a1) if val and val !='b'))
#print(sum(abs(b%3 - g%3) + abs(b//3 - g//3) for b, g in ((a1.index(i), a2.index(i)) for i in range(1, 9))))
# b = []
# g = []
# print(sum(abs(b%3 - g%3) + abs(b//3 - g//3) for b, val1 in enumerate(a1) if val1 #and val1!='b'
#           for g , val2 in (enumerate(a2)) if val2 ))#and val2!='b' ))
# # x = []
# y = []
# for i in enumerate(initial):
#     x.append(i)
# for j in enumerate(goal):
#     y.append(j)
# P= np.array(x)
# Q= np.array(y)
# # print(P)
# # print(Q)
# print(x)
# print(y)
# distance = np.sum(np.abs(P[0, :] - Q[0, :]))


#print(distance)


