""" 
Given an amount of money, 
find out of the least number of coins ( with denominations) required.
"""

class Coins:

    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]

    def number_of_coins(self, money, denominations = None, rev = True):
        if(denominations is None):
            denominations = self.denominations
        denominations.sort(reverse=rev)
        result = []
        i = 0
        while(True):
            if(money <= 0):
                break
            else:
                if(i < len(denominations)):
                    if(money >= denominations[i]):
                        money -= denominations[i]
                        result.append(denominations[i])
                    else:
                        i += 1
        return(result)


coins = Coins()

print(coins.number_of_coins(5500))
print(coins.number_of_coins(55))