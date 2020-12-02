"""
Given a matrix of mxn length filled with non-negative numbers, find the path from top-left to bottom-right
with the smallest sum.
You can either move right or down, diagonal movement is not allowed.
"""
import sys

def memoize(f):
    memo = {}
    def memoizer(array, current_x, current_y, sum_path):
        key = str(current_x) + str(current_y) + str(sum_path)
        if(key not in memo):
            memo[key] = f(array, current_x, current_y, sum_path)
        return(memo[key])
    return(memoizer)

@memoize
def shortest_path(array, current_x, current_y, sum_path):
    if(current_x + 1 == len(array) and current_y + 1 == len(array[0])):
        sum_path += array[current_x][current_y]
        return(sum_path)
    elif(current_x >= len(array) or current_y >= len(array[0])):
        return(sys.maxsize)
    sum_path += array[current_x][current_y]
    return(min(
        shortest_path(array, current_x + 1, current_y, sum_path),
        shortest_path(array, current_x, current_y + 1, sum_path)
        # shortest_path(array, current_x + 1, current_y + 1, sum_path)
    ))

matrix = [
    [1,3,1],
    [1,8,1],
    [4,1,1]
    ]

def shortest_path_matrix(array):
    def shortest_path(current_x, current_y, sum_path):
        if(current_x + 1 == len(array) and current_y + 1 == len(array[0])):
            sum_path += array[current_x][current_y]
            return(sum_path)
        elif(current_x >= len(array) or current_y >= len(array[0])):
            return(sys.maxsize)
        sum_path += array[current_x][current_y]
        return(min(
            shortest_path(current_x + 1, current_y, sum_path),
            shortest_path(current_x, current_y + 1, sum_path)
            # shortest_path(array, current_x + 1, current_y + 1, sum_path)
        ))
    return(shortest_path(0, 0, 0))

print(shortest_path_matrix(matrix))
