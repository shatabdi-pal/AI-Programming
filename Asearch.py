#Taking user input for initial state
#0 is considered as blank
initial_state = []
print("Please input values from 0-8 for the initial state")
for i in range(0,9):
    x = int(input("enter values:"))
    initial_state.append(x)

print(initial_state)

#Taking user input for goal state
#0 is considered as blank
goal_state = []
print("Please input values from 0-8 for the goal state")
for j in range(0,9):
    y = int(input("enter values:"))
    goal_state.append(y)
print(goal_state)

