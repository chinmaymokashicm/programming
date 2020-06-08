""" 
Decibinary system:
(2008)decibinary = 2*2^3 + 0*2^2 + 0*2^1 + 8*2^0 = 24(10)
x  Decibinary  Decimal
1  0            0
2  1            1
3  2            2
4  10           2
5  3            3
6  11           3
7  4            4

For given 'x', calculate decibinary value
"""

import math
import functools


def decibinary2decimal(decibinary):
    if(not isinstance(decibinary, int)):
        raise ValueError('Please provide an integer')
    str_num = str(decibinary)[::-1]
    decimal = 0
    for index in range(0, len(str_num)):
        decimal += pow(2, index) * int(str_num[index])
    return(decimal)
    
def max_power(decimal):
    if(not isinstance(decimal, int)):
        raise ValueError('Please provide an integer')
    max_power = 0
    if(decimal == 0):
        return(0)
    return(int(math.log2(decimal)))
    

def memoize(f):
    memo = {}
    def memoizer(x, power, list_digits, final_list, max_power):
        key = str(x) + str(power) + str(list_digits) + str(max_power)
        if(key not in memo):
            memo[key] = f(x, power, list_digits, final_list, max_power)
        return(memo[key])
    return(memoizer)


# @functools.lru_cache(maxsize=128)
@memoize
def all_decimal2decibinary(x, power, list_digits, final_list, max_power):
    if(power > max_power):
        return(final_list)
    for i in range(0, 10):
        next_x = x - pow(2, power) * i
        if(next_x == 0):
            list_digits.append(i)
            string = ''.join([str(x) for x in list_digits[::-1]])
            final_list.append(string)
            return(final_list)
        elif(next_x > 0):
            final_list = all_decimal2decibinary(next_x, power + 1, list_digits + [i], final_list, max_power)
        else:
            return(final_list)

    return(final_list)
    

def decibinaryNumbers(x):
    decimal = 0
    current_x = 0
    while(True):
        list_decibinary = [int(item) for item in all_decimal2decibinary(decimal, 0, [], [], max_power(decimal))]
        list_decibinary.sort(reverse=True)
        if(current_x + len(list_decibinary) >= x):
            return(list_decibinary[current_x + len(list_decibinary) - x])
        else:
            current_x += len(list_decibinary)
            decimal += 1
    return



print(decibinaryNumbers(4789))
