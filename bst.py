# Converting a sorted list to a Binary Search Tree

def list2bst(l, location, bst, left_or_right):
    if(len(l) < 1):
        return(bst)
    else:
        # print('bst= ' + str(bst))
        # print('l= ' + str(l))
        # print('i= ' + str(location))
        mid = int(len(l)/2)
        bst[location] = l[mid]
        bst = list2bst(l[0: mid], (2*location + 1), bst, 1)
        bst = list2bst(l[mid + 1:], (2*location + 2), bst, 2)
    return(bst)




def call_list2bst(l):
    l.sort()
    print(l)
    bst = [None] * len(l)
    return(list2bst(l, 0, bst, 0))
    # print(bst)

# print(call_list2bst([1,3,5,2,55,0,10]))
# print(call_list2bst([1,3,5,-10]))
print(call_list2bst([4,221,54,25534,225]))
