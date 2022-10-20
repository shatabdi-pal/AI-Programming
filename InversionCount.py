def getInvCount(arr):
    inv_count = 0
    empty_value = 'b'
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle):
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)
    #return inv_count


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