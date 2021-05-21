""" 
Princess Peach is trapped in one of the four corners of a square grid. 
You are in the center of the grid and can move one step at a time in any of the four directions. 
Can you rescue the princess?

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. 
This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). 
The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the character array grid. 
The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0]. 
The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. 
The goal is to reach the princess in as few moves as possible.

https://www.hackerrank.com/challenges/saveprincess
"""

def displayPathtoPrincess(n,grid):
    # (pos_x, pos_y) = lambda x,y: 
    for i in range(0, n):
        for j in range(0, n):
            if(grid[i][j] == 'm'):
                (pos_x, pos_y) = (i, j)
            if(grid[i][j] == 'p'):
                (pri_x, pri_y) = (i, j)
        
    # up_or_down = 'UP' if pos_x > pri_x else 'DOWN' if pos_x < pri_y else ''
    # left_or_right = 'LEFT' if pos_x > pri_x else 'RIGHT' if pos_x < pri_y else ''

    if(pos_x > pri_x):
        up_or_down = 'UP'
    elif(pos_x < pri_x):
        up_or_down = 'DOWN'
    
    if(pos_y > pri_y):
        left_or_right = 'LEFT'
    elif(pos_y < pri_y):
        left_or_right = 'RIGHT'

    if("up_or_down" in locals()):
        list_up_or_down = abs(pos_x - pri_x) * [up_or_down]
        print("\n".join(list_up_or_down))
    if("left_or_right" in locals()):
        list_left_or_right = abs(pos_y - pri_y) * [left_or_right]
        print("\n".join(list_left_or_right))
    

grid = [
    ['-', '-', '-'], 
    ['-', '-', '-'], 
    ['m', '-', 'p']
    ]
n = 3

displayPathtoPrincess(n, grid)