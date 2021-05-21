"""
Given a non-negative integer array [a1,....,an] where each represents a point of coordinate (i, ai). 
Vertical lines are drawn from (i, ai) and (i, 0). 
Find two lines wich together along with the x axis can contain the most water.

https://leetcode.com/problems/container-with-most-water/

"""
import time
import random
def volume(height_left, height_right, distance):
    """Calculate the 'volume' between the given lines

    Args:
        height_left (int): Line at the left
        height_right (int): Line at the right
        distance (int): Distance between the two lines
    """
    volume = min(height_left, height_right) * distance
    return(volume)

def main_brute(array):
    """Get the two lines

    Args:
        array (list): non-negative integer array
    """
    int_max_volume = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if(i < j):
                int_volume = volume(array[i], array[j], j-i)
                int_max_volume = max(int_max_volume, int_volume)
                # print(array[i], array[j], int_volume)
    return(int_max_volume)

def main_from_extreme(array):
    """Get the two lines

    Args:
        array (list): non-negative integer array
    """
    int_left = 0
    int_right = len(array) - 1
    while(int_left < int_right):
        int_volume_current = volume(array[int_left], array[int_right], int_right-int_left)
        int_volume_shift_left = volume(array[int_left] + 1, array[int_right], int_right-int_left-1)
        int_volume_shift_right = volume(array[int_left], array[int_right] - 1, int_right-int_left-1)
        int_volume_max = max(int_volume_current, int_volume_shift_left, int_volume_shift_right)
        if(int_volume_current == int_volume_max):
            return(int_volume_current)
        elif(int_volume_shift_left == int_volume_max):
            int_left += 1
        else:
            int_right += 1
    return(int_volume_current)

def main_from_highest(array):
    """Get the two lines

    Args:
        array (list): non-negative integer array
    """
    if(len(array) < 2):
        raise ValueError("Array needs to have at least 2 items.")
    dict_position_and_height = {index: height for index, height in enumerate(array)}
    list_position_and_height = [(index, height) for index, height in sorted(dict_position_and_height.items(), key=lambda x: x[1], reverse=True)]
    int_left = 0
    int_right = 1
    while(int_right < len(array)):
        int_volume_current = volume(
            list_position_and_height[int_left][1], 
            list_position_and_height[int_right][1], 
            abs(list_position_and_height[int_left][0] - list_position_and_height[int_right][0])
        )
        if(int_right + 1 < len(array)):
            int_volume_shift_left = volume(
                list_position_and_height[int_left + 1][1], 
                list_position_and_height[int_right + 1][1], 
                abs(list_position_and_height[int_left + 1][0] - list_position_and_height[int_right + 1][0])
            )
            int_volume_shift_right = volume(
                list_position_and_height[int_left][1], 
                list_position_and_height[int_right + 1][1], 
                abs(list_position_and_height[int_left][0] - list_position_and_height[int_right + 1][0])
            )
        else:
            int_volume_shift_left = 0
            int_volume_shift_right = 0
        # print("\nCurrent: {}\nShift Left: {}\nShift right: {}\n".format(int_volume_current, int_volume_shift_left, int_volume_shift_right))
        int_volume_max = max(int_volume_current, int_volume_shift_left, int_volume_shift_right)
        if(int_volume_current == int_volume_max):
            return(int_volume_current)
        elif(int_volume_shift_left == int_volume_max):
            int_left += 1
        else:
            int_right +=1
    return(list_position_and_height)

def main(array):
    """Get the two lines

    Args:
        array (list): non-negative integer array
    """
    int_left = 0
    int_right = len(array) - 1
    int_volume_max = 0
    while(int_left < int_right):
        int_volume_max = max(int_volume_max, volume(array[int_left], array[int_right], int_right - int_left))
        if(array[int_left] <= array[int_right]):
            int_left += 1
        else:
            int_right -= 1
    return(int_volume_max)


if __name__=='__main__':
    array = [1,8,6,2,5,4,8,3,7]
    array = [1,2,10]
    array = [110,2,12,445,332,556,54,400]
    array = [1100,2,120,441,332,56,54,4000]
    array = [1,2,3,401,400,7,8,401]
    array = random.sample(range(5,500000), 10000)
    time_start = time.time()
    print("Size of the array: {}".format(len(array)))
    print("Brute: {}".format(main_brute(array)))
    print("Time taken: {} seconds".format(time.time() - time_start))
    time_start = time.time()
    print("Non-brute: {}".format(main(array)))
    print("Time taken: {} seconds".format(time.time() - time_start))

