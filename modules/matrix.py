class Matrix:

    # Check if the given n-dimensional array is a matrix
    def is_matrix(self, array):
        def is_consistent(array):
            # Check if all items are either arrays or elements
            items = list(map(lambda x: type(x), array))
            result = all(item == items[0] for item in items)
            return(result)
        
        def is_equal_length(array):
            # Check if sub-lists in the array are of the same length
            items = list(map(lambda x: len(x), array))
            result = all(item == items[0] for item in items)
            return(result)

        dimensions = []
        dimensions.append(len(array))
        current_array = array
        while(True):
            if(not is_consistent(array)):
                return(False)
            else:
                if(not isinstance(array[0], list)):
                    return(True)
                else:
                    if(not is_equal_length(array)):
                        return(False)
                    temp_array = []
                    if(isinstance(current_array[0], list)):
                        for item in current_array:
                            for x in item:
                                temp_array.append(x)
                    else:
                        return(True)
                    current_array = temp_array

        return

    def matrix_dimensions(self, array):
        

mat = Matrix()
import pprint
n = 3
distance = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
result = mat.is_matrix(distance)
print(result)
