"""  
Given a rod of length n inches, and an array of prices
that contains prices of all pieces of size smaller than n.

Determine the maximum value obtainable by cutting up the rod and
selling them for pieces.
For example- here it is 22
length  | 1 2   3   4   5   6   7   8
prices  | 1 5   8   9   10  17  17  20 
"""

def max_rod_prices(list_prices, n):
    for i in range(0, n):
        x = (n -1) - i - 1

    def rec(x):
        pass


list_prices = [1, 5, 8, 9, 10, 17, 17, 20]

answer = max_rod_prices(list_prices, len(list_prices))