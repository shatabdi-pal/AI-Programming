import numpy as np
import math


class Node:
    def __init__(self, data, depth, f_score):
        self.data = data
        self.depth = depth
        self.f_score = f_score

    def generate_child_node(self):
        x, y = self.find_blank(self.data, 'b')
        """ blank_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
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
            temp_puz = self.create_matrix(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def create_matrix(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

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

    #To find best path 
    def evalution_function(self,initial, goal):
        return self.heuristic(initial.data, goal)


    #Misplaced tiles#
    def heuristic(self, initial, goal):
        x = np.asarray(initial)
        y = np.asarray(goal)
        hcost = np.sum(x != y) - 1

        if hcost > 0:
            return hcost
        else:
            return 0

    #Manhattan Distance calculation
    # def heuristic(self,initial,goal):
    #a1 = np.array(initial).flatten()
    #a2 = np.array(goal).flatten()
    #distance = sum(abs((int(val) - 1) % 3 - i % 3) + abs((int(val) - 1) // 3 - i // 3) for i, val in enumerate(a1) if val and val != 'b'))
    #distance = sum(abs(b % 3 - g % 3) + abs(b // 3 - g // 3) for b, g in ((a1.index(i), a2.index(i)) for i in range(1, 9)))
    #return distance


    # Euclidean Distance Calculation
    # def heuristic(self, initial, goal):
    #     a1 = np.array(initial).flatten()
    #     a2 = np.array(goal).flatten()
    #     x = list(a1)
    #     y = list(a2)
    #     x.remove("b")
    #     y.remove("b")
    #     # distance = math.dist(x, goal)
    #     p = [eval(i) for i in x]
    #     q = [eval(j) for j in y]
    #     distance = math.dist(p, q)
    #    return distance

    def a_search(self,initial,goal):
        initial = Node(initial, 0, 0)
        initial.f_score = self.evalution_function(initial, goal)
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
#Taking user input
print("Enter the initial state matrix \n")
ip = puz.user_input()
print("Enter the goal state matrix \n")
gs = puz.user_input()

#To check if the goal state is solvable from initial state
c1 = puz.is_solvable(ip)
c2 = puz.is_solvable(gs)
if c1 == c2:
    print("Initial state to goal state is solvable")
    print("Best First search algorithm using number of misplaced tiles\n")
    steps = puz.a_search(ip,gs)
    print("Average number of steps: ", steps)
else:
    print("Initial state to goal state is not solvable")





