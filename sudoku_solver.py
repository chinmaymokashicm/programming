"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

https://leetcode.com/problems/sudoku-solver/
"""
import numpy as np

class SudokuBoard:
    def __init__(self, array_board):
        self.board = np.full((9,9), None)
        if(isinstance(array_board, list) and all(isinstance(list_row, list) for list_row in array_board) and len(array_board) == 9):
            for list_index, list_row in enumerate(array_board):
                if(len(list_row) == 9):
                    for cell_index, cell in enumerate(list_row):
                        if(cell in ["1","2","3","4","5","6","7","8","9", "."]):
                            if(cell == "."):
                                self.board[list_index][cell_index] = np.nan
                            else:
                                self.board[list_index][cell_index] = int(cell)
                        else:
                            self.board = None
                            raise ValueError("Incorrect input array.")            
        else:
            self.board = None
            raise ValueError("Incorrect input array.")
        self.board_new = np.copy(self.board)
        return

    def is_cell_fit_row(self, array_board, cell_row, cell_column):
        if(any(array_board[cell_row].tolist().count(number) > 1 for number in array_board[cell_row] if ~np.isnan(number))):
            return(False)
        else:
            return(True)

    def is_cell_fit_column(self, array_board, cell_row, cell_column):
        if(any(array_board[:, cell_column].tolist().count(number) > 1 for number in array_board[:, cell_column] if ~np.isnan(number))):
            return(False)
        else:
            return(True)

    def is_cell_fit_box(self, array_board, cell_row, cell_column):
        # Find the cell values in the corresponding box
        box_top_left = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        box_top_middle = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
        box_top_right = [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)]

        box_middle_left = [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)]
        box_middle_middle = [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]
        box_middle_right = [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)]

        box_bottom_left = [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)]
        box_bottom_middle = [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)]
        box_bottom_right = [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]

        list_boxes = [box_top_left, box_top_middle, box_top_right, box_middle_left, box_middle_middle, box_middle_right, box_bottom_left, box_bottom_middle, box_bottom_right]

        for box in list_boxes:
            if((cell_row, cell_column) in box):
                list_cell_values = [array_board[cell_row_value][cell_column_value] for cell_row_value, cell_column_value in box]

        
        # Remove nan
        # print("Hello")
        list_cell_values = [cell_value for cell_value in list_cell_values if ~np.isnan(cell_value)]
        if(any(list_cell_values.count(number) > 1 for number in list_cell_values)):
            return(False)
        else:
            return(True)

    def is_cell_fit_valid(self, array_board, cell_row, cell_column):
        if(
            self.is_cell_fit_row(array_board, cell_row, cell_column) and
            self.is_cell_fit_column(array_board, cell_row, cell_column) and
            self.is_cell_fit_box(array_board, cell_row, cell_column)
        ):
            return(True)
        else:
            return(False)

    def is_board_complete(self, array_board):
        for row_index, list_row in enumerate(array_board):
            for cell_index, cell in enumerate(list_row):
                if(np.isnan(cell)):
                    return(False)
        
        return(True)
    
    def get_first_na_cell(self, array_board):
        for row_index, list_row in enumerate(array_board):
            for cell_index, cell in enumerate(list_row):
                if(np.isnan(cell)):
                    return((row_index, cell_index))
        return(None)

    def solve(self, array_board):
        """Solve the sudoku puzzle

        Args:
            board (2D array): sudoku board
        """
        def generate_new_array(array_board, tuple_cell, cell_value):
            array_board[tuple_cell[0]][tuple_cell[1]] = cell_value
            return(array_board)
        
        def remove_from_array(array_board, tuple_cell):
            array_board[tuple_cell[0]][tuple_cell[1]] = np.nan
            return(array_board)

        tuple_next_cell = self.get_first_na_cell(array_board)
        if(tuple_next_cell is None):
            print(array_board)
            return(True)
        for number in range(1,10):
            if(self.is_cell_fit_valid(generate_new_array(array_board, tuple_next_cell, number), tuple_next_cell[0], tuple_next_cell[1])):
                array_board = generate_new_array(array_board, tuple_next_cell, number)
                if(self.solve(array_board)):
                    return(True)
            array_board = remove_from_array(array_board, tuple_next_cell)
                
        return(False)


if __name__ == "__main__":
    array_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."], 
        ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
        [".", "9", "8", ".", ".", ".", ".", "6", "."], 
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
        ["4", ".", ".", "8",".", "3", ".", ".", "1"], 
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
        [".", "6", ".", ".", ".", ".", "2", "8", "."], 
        [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    array_board = [
        [".", ".", "5", "8", ".", "9", "4", "7", "."], 
        [".", "2", ".", ".", "6", ".", ".", ".", "1"], 
        [".", "7", ".", ".", ".", ".", ".", "6", "9"], 
        ["4", ".", ".", ".", ".", ".", "1", ".", "."], 
        [".", ".", ".", "1", ".", "8", "9", ".", "6"], 
        ["3", ".", ".", "9", "4", ".", ".", ".", "8"], 
        ["2", "3", ".", "7", "5", ".", "6", "9", "4"], 
        ["5", ".", ".", ".", ".", "3", "8", ".", "."], 
        ["6", "9", ".", ".", ".", "2", "3", "5", "."]]
    array_board =[
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
    array_board =[
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "8", ".", ".", ".", ".", "4", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "6", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["2", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    board_obj = SudokuBoard(array_board)
    array_board = np.copy(board_obj.board_new)
    # print(board_obj.board_new)
    # print("\n\n\n")
    array_board_solved = board_obj.solve(array_board)
    # print(array_board_solved)