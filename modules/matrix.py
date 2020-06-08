import pprint
import numpy

class Matrix:
    def clean_adj_cells_dict(self, input_dict, output_dict):
        """
        Remove adjacent cells with zero values
        """
        """ 
        Start with
        output_dict = {key: {} for key,value in adjacent_cells.items()}
        """
        for key,value in input_dict.items():
            if(not isinstance(value, dict)):
                if(value != 0):
                    output_dict[key] = value
            else:
                output_dict[key] = self.clean_adj_cells_dict(
                    input_dict[key],
                    {key: {} for key,value in input_dict.items()}[key]
                )
            

        return(output_dict)

    def matrix_dimensions(self, array):
        a = []
        def recurse(element, count):
            if(not isinstance(element, list)):
                a.append(count)
                return(count)
            else:
                return([recurse(i, count + 1) for i in element])

        recurse(array, 0)
        output = {
            'is_matrix': False,
            'number_of_dimensions': None,
            'dimensions': []
        }
        if(not all(item == a[0] for item in a)):
            return(output)

        output['is_matrix'] = True
        output['number_of_dimensions'] = a[0]

        temp_array = []
        dimensions = []
        i = 0

        while i < output['number_of_dimensions']:
            dimensions.append(len(array))
            array = array[0]
            i += 1

        output['dimensions'] = dimensions

        return(output)

    def flatten_matrix(self, array, level):
        # Level: Number of times the matrix is to be flattened.
        ans = self.matrix_dimensions(array)
        if(not ans['is_matrix']):
            return(False)
        i = 0
        temp_array = []
        if(level > ans['number_of_dimensions']):
            level = ans['number_of_dimensions']
        while i < level:
            if(not isinstance(array[0], list)):
                return(array)
            for item in array:
                for element in item:
                    temp_array.append(element)
            array = temp_array
            temp_array = []
            i += 1

        return(array)
        return

    def get_adjacent_cells(self, array, cell_dimensions):
        """
        Returns the values of the adjacents cells to a given
        matrix

        """
        if(len(self.matrix_dimensions(array)['dimensions']) != len(cell_dimensions)):
            return(False)

        def recurse(result, array, list_current_dimensions):
            if(len(list_current_dimensions) == 0):
                return(array)
            else:
                current_dimension = list_current_dimensions[0]
                list_next_dimensions = list_current_dimensions[1:]
                result = dict(
                    [
                        (current_dimension - 1, None),
                        (current_dimension, None),
                        (current_dimension + 1, None),
                    ]
                        )
                for i in [-1, 0, 1]:
                    try:
                        new_array = array[current_dimension + i]
                        result[current_dimension + i] = recurse(result[current_dimension + i],
                        new_array, list_next_dimensions)
                    except IndexError:
                        # Remove the keys with None values
                        result.pop(current_dimension + i)
                        pass

                return(result)

        # Get all adjacent cells
        adjacent_cells = recurse({}, array, cell_dimensions)
        # Remove the original cell (TBC)
        # Remove the zero values
        adjacent_cells = self.clean_adj_cells_dict(
            adjacent_cells,
            {key: {} for key,value in adjacent_cells.items()}
        )
        


        return(adjacent_cells)


    def is_binary(self, array):
        ans = self.matrix_dimensions(array)
        if(not ans['is_matrix']):
            return(False)
        array = self.flatten_matrix(array, ans['number_of_dimensions'])
        if(all(item in (0,1) for item in array)):
            return(True)
        return(False)