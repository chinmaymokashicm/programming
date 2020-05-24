def increment(arr, start, end, x):
    # Increment everything from start to here by x
    return


def candies(n,arr):
    # peaks = []
    # crevices = []
    # for i in range(1, len(arr) - 1):
    #     if(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
    #         peaks.append(i)
    #         # print('\n')
    #     elif(arr[i] < arr[i-1] and arr[i] < arr[i+1]):
    #         crevices.append(i)

    # extremes = peaks + crevices + [0] + [len(arr) - 1]
    # extremes.sort()
    # print(extremes)
    
    left = ['x'] * len(arr)
    right = ['x'] * len(arr)

    left[0] = 1
    right[-1] = 1
    counter_right = 1
    counter_left = 1
    for i in range(1,len(arr) - 1):
        if(arr[i] > arr[i-1]):
            left[i] = counter_left + 1
            counter_left += 1
        if(arr[-(i + 1)] > arr[-(i+2)]):
            right[-(i+1)] = counter_right + 1
            counter_right += 1
        else:
            left[i] = 1
            right[-(i+1)] = 1
    
    print(left)
    print(right)

    return











# print(candies(19, [2,3,4,5,6,5,4,6,7,6,5,4,3,2,1,4,3,2,1]))
print(candies( 10, [2, 3, 4, 5, 6, 5, 4, 6, 7, 6, 2]))