# LEETCODE
# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

# If there isn't any rectangle, return 0.

 

# Example 1:

# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:

# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
 

# Note:

# 1. 1 <= points.length <= 500
# 2. 0 <= points[i][0] <= 40000
# 3. 0 <= points[i][1] <= 40000
# 4. All points are distinct.



# --------------------------
# SOLUTION
# Area of the rectangle -> A = mod((x1 - x2) * (y1 - y2)) 
# where (x1,y1) and (x2,y2) are diagonals


def minAreaReact(points):

    x_set = set([])
    y_set = set([])
    for [x,y] in points:
        x_set.add(x)
        y_set.add(y)
    # Convert the sets into lists
    x_list = list(x_set)
    y_list = list(y_set)
    # print(x_list)
    # print(y_list)

    # Combine 
    distances = []
    for x in x_list:
        for y in y_list:
            if(x != y):
                distances.append([x,y])
    
    # print(distances)

    # distances.sort(key = lambda x: abs(x[1] - x[0]))
    # lengths = []
    # print(points)
    distances.sort(key = lambda x: abs(x[0] - x[1]))
    print(points)
    print(distances)

    area = 0
    for [x, y] in distances:
        for [a, b] in distances:
            coordinates_1 = [ [x,a], [x,b], [y,a], [y,b] ]
            coordinates_2 = [ [a,x], [a,y], [b,x], [b,y] ]

            if(all(i in points for i in coordinates_1)):
                print('1')
                print(coordinates_1)
                area = abs((x-y) * (a-b))
                return(area)
            elif(all(i in points for i in coordinates_2)):
                print('2')
                print(coordinates_2)
                area = abs((x-y) * (a-b))
                return(area)
    return(area)



    
    # for [x, y] in distances:
    #     lengths.append(abs(x - y))
    # print(lengths)
    # lengths = set(lengths)
    # print(lengths)
    # lengths = list(lengths)
    # print(lengths)
    # if(len(lengths) < 2):
    #     return(lengths[0] * lengths[0])
    # else:
    #     return(lengths[0] * lengths[1])
    # print(lengths)

    # print(distances)

    # for [x,y] in distances:
    #     coordinates = { [x,x], [y,y], [x,y], [y,x]}
    #     if(all(item in points for item in distances)):
    #         return()


    
    # points.sort(key = lambda x: x[0])
    
    # print(x_set)
    # print(y_set)

    # return(points)

# print(minAreaReact([[1,1],[1,3],[3,1],[3,3],[2,2]]))
# print(minAreaReact([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
print(minAreaReact([[3,2],[1,3],[3,3],[3,0],[3,1],[2,0],[4,2],[1,0],[4,1],[1,1]]))
