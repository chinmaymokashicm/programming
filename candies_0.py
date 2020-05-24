def rank(a, start, end):
    if(start != end):
        if(start < end):
            step = 1
            counter = 1
        else:
            step = -1
            counter = end - start + 1
        for i in range(start, end, step):
            a[i] = counter
            counter = counter + step
            # print('i: ' + str(i) + '  a[i]: ' + str(a[i]) + '  counter:  ' + str(counter) )
        if(end < len(a)):
            a[end] = counter
        print(a)
        # return
    else:
        a[start] = 1
        # return
    return

def candies(n, arr):
    # Set start direction
    candies = ['x'] * len(arr)
    # counter = 1
    
    if(arr[0] <= arr[1]):
        direction = 1
        rank(candies, 0, 1)
    else:
        direction = -1
        rank(candies, 1, 0)
    
    old_direction = direction

    start = 0
    end = 1

    for i in range(1, len(arr)):
        if(i+1 < len(arr)):
            if(arr[i] == arr[i + 1]):
                direction = old_direction
                # end += 1
            elif(arr[i] < arr[i + 1]):
                direction = 1
            else:
                direction = -1
            
            if(direction == old_direction):
                end += 1
                rank(candies, start, end)
            else:
                start = i + 1
                if(i+2 < len(arr)):
                    end = i +2
                else:
                    end = start
                rank(candies, start, end)
        else:
            rank(candies, i, i)
        old_direction = direction
    
    # print(candies)
    print(arr)
    return(candies)

# print(candies(19, [2,3,4,5,6,5,4,6,7,6,5,4,3,2,1,4,3,2,1]))
print(candies( 10, [2, 3, 4, 5, 6, 5, 4, 6, 7, 6, 2]))