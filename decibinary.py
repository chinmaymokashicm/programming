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

def decibinary2decimal(x):
    if(not isinstance(x, int)):
        raise ValueError('Please provide an integer')
    else:
        decimal = 0
        string = str(x)
        for i in range(len(string)):
            next = int(int(string[i]) * math.pow(2, len(string) - i - 1))
            # print(string[i] + ' * 2^' + str(len(string) - i - 1) + ' = ' + str(next))
            decimal = decimal + next
        return(decimal)



# def rec(digits, sum):
#     if(d == 0 and s == 0):
#         return(1)
#     elif(d == 0 and s !=0):
#         return(0)
#     elif(s < 0):
#         return(0)
#     else:
#         pass



# print(decibinary2decimal(10))

# output = []
# for i in range(10001):
#     output.append((i, decibinary2decimal(i)))

# output.sort(key = lambda x: x[1])

# print('X', end='\t\t\t\t')
# print('Decibinary', end='\t')
# print('Decimal')

# print('==================================')

# for i in range(len(output)):
#     print(i+1, end='\t\t\t\t')
#     print(output[i][0], end='\t\t\t\t')
#     print(output[i][1])