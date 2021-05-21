"""
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
Print all the possible solutions.
For example, for 4X4 board:
[
    ["X", "Q", "X", "X"],
    ["X", "X", "X", "Q"],
    ["Q", "X", "X", "X"],
    ["X", "X", "Q", "X"]
]

P.S. The Queen can attack diagnolly or in straight lines.
"""
k = 1
def print_2D_list(list_2D):
    global k
    print(k)
    k += 1
    s = [[str(e) for e in row] for row in list_2D]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print("\n".join(table))
    print("\n")

def get_diagonal_cell_values(array_board, tuple_cell):
    """Gets all diagonal cell values of the given cell

    Args:
        array_board (2D array): Chessboard
        tuple_cell (tuple): Given cell
    """
    int_size_board = len(array_board)
    list_cell_values = []
    append = list_cell_values.append
    for i in range(1, int_size_board):
        for j in [-1,1]:
            x_coord = tuple_cell[0] + i*j
            y_coord = tuple_cell[1] + i*j
            if(x_coord >= 0 and y_coord >= 0):
                try:
                    append(array_board[x_coord][y_coord])
                except Exception:
                    pass

            x_coord = tuple_cell[0] + i*j
            y_coord = tuple_cell[1] - i*j
            if(x_coord >= 0 and y_coord >= 0):
                try:
                    append(array_board[x_coord][y_coord])
                except Exception:
                    pass
    
    return(list_cell_values)
    

def get_straight_cell_values(array_board, tuple_cell):
    """Gets all straight cell values of the given cell

    Args:
        array_board (2D array): Chessboard
        tuple_cell (tuple): Given cell
    """
    int_size_board = len(array_board)
    list_cell_values = []
    append = list_cell_values.append
    for i in [x for x in range(-int_size_board, int_size_board) if x != 0]:
        x_coord = tuple_cell[0] + i
        y_coord = tuple_cell[1] + i
        if(x_coord >= 0):
            try:
                append(array_board[x_coord][tuple_cell[1]])
            except Exception:
                pass
        if(y_coord >= 0):
            try:
                append(array_board[tuple_cell[0]][y_coord])
            except Exception:
                pass
    
    return(list_cell_values)

def is_board_layout_valid(array_board):
    """Checks if board layout is valid

    Args:
        array_board (2D array): Chessboard
    """
    for index_row in range(len(array_board)):
        for index_column in range(len(array_board[index_row])):
            if(array_board[index_row][index_column] == "Q"):
                if("Q" in get_diagonal_cell_values(array_board, (index_row, index_column)) or "Q" in get_straight_cell_values(array_board, (index_row, index_column))):
                    return(False)
    return(True)


def arrange_board_backtracking(size=4):
    """Prints all possible layouts for n queens in nxn chessboard

    Args:
        size (int, optional): chessboard size = number of queens. Defaults to 4.
    """
    array_board = []
    for i in range(0, size):
        array_board.append([])
        for j in range(0, size):
            array_board[i].append("X")
    list_tuple_cell = []
    append = list_tuple_cell.append
    for index_row in range(len(array_board)):
        for index_column in range(len(array_board[index_row])):
            append((index_row, index_column))
    
    def recurse(array_board, list_tuple_cell, counter=None):
        if(counter is None):
            counter = len(array_board[0])
        if(counter == 0):
            if(is_board_layout_valid(array_board)):
                # print(array_board)
                print_2D_list(array_board)
                return(True)
            return(False)
        if(len(list_tuple_cell) < 2):
            return(False)
        for index_coord, coord in enumerate(list_tuple_cell):
            array_board[coord[0]][coord[1]] = "Q"
            # if(recurse(array_board, list_tuple_cell[index_coord + 1:], counter - 1) is not None):
            #     print()
            recurse(array_board, list_tuple_cell[index_coord + 1:], counter - 1)
            array_board[coord[0]][coord[1]] = "X"
        return
    
    return(recurse(array_board, list_tuple_cell))



if __name__ == "__main__":
    array_board = [
    ["X", "Q", "X", "X"],
    ["X", "X", "X", "Q"],
    ["Q", "X", "X", "X"],
    ["X", "X", "Q", "X"]
    ]
    # print(is_board_layout_valid(array_board))
    arrange_board_backtracking(5)
    
    