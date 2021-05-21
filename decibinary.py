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

https://www.hackerrank.com/challenges/decibinary-numbers/
"""
def decibinary2decimal(int_decibinary):
    """Converts decibinary to decimal

    Args:
        int_decibinary (int): decibinary integer
    """
    if(not isinstance(int_decibinary, int)):
        raise ValueError("Requires integer, found {}".format(type(int_decibinary)))

    int_decimal = 0
    str_decibinary = str(int_decibinary)
    len_int_decibinary = len(str_decibinary)
    for digit, digit_value in enumerate(str_decibinary):
        int_decimal += int(digit_value) * pow(2, len_int_decibinary - digit - 1)
    
    return(int_decimal)
    
def generate_decibinary2decimal(int_start=1, int_end=100):
    """Generates decimal from decibinary for numbers in a range

    Args:
        int_start (int, optional): starting integer. Defaults to 1.
        int_end (int, optional): ending integer. Defaults to 10.
    """
    for i in range(int_start, int_end + 1):
        print(i, self.decibinary2decimal(i))
    
def number_of_possible_decibinary(int_decimal):
    """Returns the number of possible decibinary numbers for a given integer

    Args:
        int_decimal (int): integer
    """
    int_max_power = 1
    while(True):
        if(int_decimal < pow(2, int_max_power)):
            return(int_max_power)
        int_max_power += 1
    
    return(int_max_power)

def memoize(f):
    dict_decibinary = {}
    def memo(decimal):
        if(decimal not in dict_decibinary):
            dict_decibinary[decimal] = f(decimal)
        return(dict_decibinary[decimal])
    return(memo)

@memoize
def decimal2decibinary(int_decimal):
    """Returns a list of all decibinary numbers from the given decimal

    Args:
        int_decimal (int): decimal
    """
    list_decibinary = []
    def recurse(str_decibinary, int_decimal, power=0):
        if(int_decimal < 0):
            return(False)
        if(int_decimal == 0):
            if(str_decibinary == ""):
                str_decibinary = "0"
            list_decibinary.append(int(str_decibinary))
            return(True)
        if(pow(2, power) > int_decimal):
            return
        for i in range(0,10):
            int_decimal_new = int_decimal - i * pow(2, power)
            recurse(str(i) + str_decibinary, int_decimal_new, power=power+1)
    recurse(int_decimal=int_decimal, str_decibinary="")
    return(sorted(list_decibinary))


def index2decibinary(int_index):
    """Returns the decibinary number corresponding to the given index

    Args:
        int_index (int): index
    """
    int_decimal = 0
    int_index_dynamic = 0
    list_index_dynamic = [0]
    dict_decibinary = {}
    while(True):
        if(int_decimal not in dict_decibinary):
            int_index_dynamic += len(decimal2decibinary(int_decimal))
        else:
            int_index_dynamic = dict_decibinary[int_decimal]
        list_index_dynamic.append(int_index_dynamic)
        int_decimal += 1
        if(int_index_dynamic >= int_index):
            int_index_new = int_index - list_index_dynamic[-2] - 1
            return(decimal2decibinary(int_decimal - 1)[int_index_new])
    
    print(list_index_dynamic)
    

if __name__=='__main__':
    for i in range(1, 101):
        # print(decimal2decibinary(i))
        decibinary = index2decibinary(i)
        decimal = decibinary2decimal(decibinary)
        print(i, decibinary, decimal)
    # print(3, index2decibinary(3))
    # print("\n\n------------------------------\n\n")
    # print(4, index2decibinary(4))
    # print(2685452001065306, index2decibinary(2685452001065306))
    