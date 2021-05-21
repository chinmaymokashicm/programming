"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4


Example 2: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

Approach: 
# Calculate the area of triangles for every triplet of point
I think there should be two parameters which need to be calculated: m and c in y = mx + c | Greedy algorithm!

https://leetcode.com/problems/max-points-on-a-line/
"""
import math
from matplotlib import pyplot
class Solution:
    def distance(self, tuple_coordinate_0, tuple_coordinate_1):
        return(math.sqrt(pow(tuple_coordinate_0[0] - tuple_coordinate_1[0], 2) + pow(tuple_coordinate_0[1] - tuple_coordinate_1[1], 2)))

    def area_triangle_squared(self, tuple_coordinate_0, tuple_coordinate_1, tuple_coordinate_2):
        """Calculates the square of the area of the triangle

        Args:
            tuple_coordinate_0 (list_tuple): coordinates
            tuple_coordinate_1 (list_tuple): coordinates
            tuple_coordinate_2 (list_tuple): coordinates
        """
        distance_0 = self.distance(tuple_coordinate_0, tuple_coordinate_1)
        distance_1 = self.distance(tuple_coordinate_1, tuple_coordinate_2)
        distance_2 = self.distance(tuple_coordinate_2, tuple_coordinate_0)
        s = (distance_0 + distance_1 + distance_2)/2
        area_simple = (s - distance_0) * (s - distance_1) * (s - distance_2)
        area_simple = area_simple if area_simple >= 0.001 else 0
        print(tuple_coordinate_0, tuple_coordinate_1, tuple_coordinate_2, "Semi-perimeter:", s, "Area:", area_simple, "Distances: ", distance_0, distance_1, distance_2)
        return(area_simple)

    def get_linear_equation(self, tuple_coordinate_0, tuple_coordinate_1):
        """Returns constant and slope

        Args:
            tuple_coordinate_0 (tuple): coordinate
            tuple_coordinate_1 (tuple): coordinate
        """
        x0, y0 = tuple_coordinate_0
        x1, y1 = tuple_coordinate_1
        m = None
        c = x0
        if(x1 != x0):
            m = (y1 - y0)/(x1 - x0)
            c = y0 - m * x0
        return(m, c)
    
    def is_point_on_straight_line(self, m, c, tuple_coordinate):
        """Returns if given coordinate lies on the given straight line

        Args:
            m (int): slope
            c (int): constant
            tuple_coordinate (tuple): coordinate
        """
        x, y = tuple_coordinate
        if(m is None):
            if(x == c): # Check this
                return(True)
            else: return(False)
        if(math.ceil(y - m*x - c) == 0): # Check this
            return(True)
        else:
            return(False)
    
    def solve_brute(self, list_coordinates):
        """Brute force

        Args:
            list_coordinates (list): List of coordinates
        """
        if(len(list_coordinates) < 3):
            return(len(list_coordinates))
        list_pairs_coordinates = [((i0, x0, y0), (i1, x1, y1)) for i0, (x0, y0) in enumerate(list_coordinates) for i1, (x1, y1) in enumerate(list_coordinates) if i0 != i1]
        int_counter_max = 2
        for ((i0, x0, y0), (i1, x1, y1)) in list_pairs_coordinates:
            int_counter_current = 2
            for iP, (xP, yP) in enumerate(list_coordinates):
                if(not (i0 == iP or i1 == iP)):
                    m, c = self.get_linear_equation((x0, y0), (x1, y1))
                    if(self.is_point_on_straight_line(m, c, (xP, yP))):
                        int_counter_current += 1
                        print("YES: ", (x0, y0), (x1, y1), (xP, yP), yP - m*xP - c if m is not None else x0 - xP)
                    else:
                        print("NO: ", (x0, y0), (x1, y1), (xP, yP), m, c, yP - m*xP - c if m is not None else x0 - xP)
                        pass
            if(int_counter_current > int_counter_max):
                int_counter_max = int_counter_current
        
        return(int_counter_max)

if __name__ == "__main__":
    list_coordinates = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    list_coordinates = [[1,1],[2,2],[3,3]]
    list_coordinates = [[-54,-297],[-36,-222],[3,-2],[30,53],[-5,1],[-36,-222],[0,2],[1,3],[6,-47],[0,4],[2,3],[5,0],[48,128],[24,28],[0,-5],[48,128],[-12,-122],[-54,-297],[-42,-247],[-5,0],[2,4],[0,0],[54,153],[-30,-197],[4,5],[4,3],[-42,-247],[6,-47],[-60,-322],[-4,-2],[-18,-147],[6,-47],[60,178],[30,53],[-5,3],[-42,-247],[2,-2],[12,-22],[24,28],[0,-72],[3,-4],[-60,-322],[48,128],[0,-72],[-5,3],[5,5],[-24,-172],[-48,-272],[36,78],[-3,3]]
    # print(Solution().solve(list_coordinates))
    list_coordinates = [[1,1],[1,1],[0,0],[3,4],[4,5],[5,6],[7,8],[8,9]]
    # pyplot.plot(list_coordinates, "o")
    # pyplot.show()
    # print(Solution().solve(list_coordinates))
    list_coordinates = [[0,1], [3,4], [4,5], [5,6], [6,7], [7,8]]
    print(Solution().solve_brute(list_coordinates))
