"""
All sorting algorithms in a list
"""
class Sort:
    def selection_rec(self, ar):
        if(len(ar) == 1):
            return(ar)
        if(ar[0] != min(ar)):
            temp_var = ar[0]
            min_index = ar.index(min(ar))
            ar[0] = min(ar)
            ar[min_index] = temp_var
        return([ar[0]] + self.selection_rec(ar[1:]))

    # def selection(self, ar):
    #     if(len(ar) == 1):
    #         return(ar)
    #     output = []
    #     counter = 0
    #     while(True):

    
print(Sort().selection_rec([3,-8,1,4,1,10,-9]))
        