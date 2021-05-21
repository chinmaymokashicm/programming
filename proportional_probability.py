"""
Select a number randomly from a given list such that its probability is proportional to its magnitude.
Example-
a = [0, 5, 27, 6, 11]
f(x) = probability of picking x
f(27) > f(11) > f(6) > f(5) > f(0)
"""
"""
Approach:
1. Sort the list in ascending order
2. If smallest element is 0 or negative, add offset to make it 1 and similarly to every other element
3. Append 0 to the beginning
4. Scale the range (0-largest number) to 0-1 list
5. Pick numbers randomly from this new list
"""

import random

def scale(list_original, minimum=0, maximum=1):
    """Scales down/up a given list into a new list with range from minimum to maximum

    Args:
        list_original (list): original list
        minimum (integer): starting integer
        maximum (integer): ending integer
    """
    if(not all(isinstance(element, int) for element in list_original)):
        raise ValueError("Non-integers found!")
    if(len(list_original) == 0):
        raise ValueError("Empty list!")
    if(len(list_original) == 1):
        raise ValueError("Single element list!")
    # list_new = sorted(list_original)
    list_new = list_original
    if(minimum == 0 and list_new[0] != 0):
        raise ValueError("First element is not zero!")
    scaling_factor = maximum/list_new[-1]
    list_new = [element * scaling_factor for element in list_new]
    return(list_new)

def reconfigure_list(list_original):
    """Reconfigures the list according to the aforementioned logic

    Args:
        list_original (list): original list
    """
    if(not all(isinstance(element, int) for element in list_original)):
        raise ValueError("Non-integers found!")
    if(len(list_original) == 0):
        raise ValueError("Empty list!")
    if(len(list_original) == 1):
        raise ValueError("Single element list!")
    list_new = sorted(list_original)
    # Adding offset
    if(list_new[0] < 1):
        offset = 1 - list_new[0]
    else:
        offset = 0
    list_new = [0] + [element + offset for element in list_new]
    return([list_new, offset])

def get_corresponding_integer(list_numbers, list_scaled, number, offset):
    """Return the corresponding integer

    Args:
        list_numbers (list): original list
        list_scaled (list): scaled list
        number (decimal): randomly generated number
    """
    for i in range(len(list_scaled) - 1):
        if(number >= list_scaled[i] and number <= list_scaled[i+1]):
            return(list_numbers[i+1] - offset)

def proportional_probability(list_integers, number_of_events=100):
    """Main method

    Args:
        list_integers (list): original list
        number_of_events (int): number of times we pick a number randomly
    """
    list_new, offset = reconfigure_list(list_integers)
    list_scaled = scale(list_new)
    dict_outcomes = {}
    for i in range(0, number_of_events):
        decimal_random = random.uniform(0,1)
        dict_outcomes[str(i)] = [decimal_random, get_corresponding_integer(list_new, list_scaled, decimal_random, offset)]
    dict_probabilities = {key: 0 for key in list_integers}
    for key, list_values in dict_outcomes.items():
        dict_probabilities[list_values[1]] += 1
    return(dict_probabilities)

if __name__=='__main__':
    list_input = [1, 2, 5, -1, 10, 200]
    list_input = [1, 2, 3, 5, 100, 0]
    list_input = [1, 20, 30, 100]
    dict_probabilities = proportional_probability(list_input, 100000)
    print("Given list: {}".format(list_input))
    print("Probabilities: {}".format(dict_probabilities))