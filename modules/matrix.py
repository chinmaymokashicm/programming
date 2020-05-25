import pprint
class Matrix:

    def is_consistent(self,array):
        # Check if all items are either arrays or elements
        # print(array)
        # for item in array:
        #     print(item, type(item))
        items = list(map(lambda x: type(x), array))
        # result = all(item == items[0] for item in items)
        if(isinstance(items[0], list)):
            if(all(isinstance(item), list) for item in items):
                return(True)
        else:
            if(all(not isinstance(item), list) for item in items):
                return(True)
        return(False)
    
    def is_equal_length(self,array):
        # Check if sub-lists in the array are of the same length
        items = list(map(lambda x: len(x), array))
        result = all(item == items[0] for item in items)
        return(result)

    def is_matrix(self, array):
        # Check if the given n-dimensional array is a matrix

        dimensions = []
        dimensions.append(len(array))
        current_array = array
        while(True):
            # if(not self.is_consistent(array)):
            #     return(False)
            # else:
            #     if(not isinstance(array[0], list)):
            #         return(True)
            #     else:
            #         if(not self.is_equal_length(array)):
            #             return(False)
            #         temp_array = []
            #         if(isinstance(current_array[0], list)):
            #             for item in current_array:
            #                 for x in item:
            #                     temp_array.append(x)
            #             print(temp_array)
            #         else:
            #             return(True)
            #         current_array = temp_array

            if(self.is_consistent(array)):
                if(isinstance(array[0], list)):
                    if(self.is_equal_length(array)):
                        array = self.flatten_matrix(array, 1)
                        continue
                    else:
                        return(False)
                else:
                    return(True)
            else:
                return(False)

            
        return
    
    def flatten_matrix(self, array, level):
        temp_array = []
        i = 0
        while i < level:
            if(not self.is_consistent(array)):
                return(False)
            else:
                # Check if all elements are non-arrays
                if(not isinstance(array[0], list)):
                    return(array)
                else:
                    if(not self.is_equal_length(array)):
                        return(False)
                    for item in array:
                        for element in item:
                            temp_array.append(element)
                    array = temp_array
                    temp_array = []
                    i += 1
        return(array)
    
    def number_of_dimensions(self, array):
        number_of_dimensions = 1
        if(not self.is_matrix(array)):
            return(False)
        while(True):
            if(not isinstance(array[0], list)):
                return(number_of_dimensions)
            array = self.flatten_matrix(array, 1)
            number_of_dimensions += 1

    def dimensions(self, array):
        dimensions = []
        if(not self.is_matrix(array)):
            return(False)
        while(True):
            if(not isinstance(array[0], list)):
                break
            dimensions.append(len(array[0]))
            array = self.flatten_matrix(array, 1)
        if(len(dimensions) == 0):
            dimensions.append(1)
        return(dimensions)




            
        

        

mat = Matrix()

n = 3
distance = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
# pprint.pprint(distance)

dist = [
    [[[0]], [[0]], [[0]]],
    [[[0]], [[0]], [[0]]],
    [[[0]], [['i']], [[0]]]
]

# result_1 = mat.is_matrix(distance)
# result_2 = mat.is_matrix(dist)
# print(result_1)
# print(result_2)

# pprint.pprint(mat.flatten_matrix(distance,1))
# mat.flatten_matrix(distance,1)
# pprint.pprint(distance)

# print(mat.matrix_dimensions(distance))


ar = [0, [0], [0], [0], [0], [0], [0], [0], [0]]
# print(mat.is_consistent(ar))

# print(mat.number_of_dimensions(dist))
# print(mat.dimensions(distance))
# print(mat.dimensions(dist))
# print(mat.dimensions(ar))

arrays = [distance, dist, ar]

for item in arrays:
    # print(eval(item), end='\t')
    print(mat.number_of_dimensions(item), end='\t')
    print(mat.dimensions(item))
