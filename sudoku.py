from datetime import datetime
from typing import List
from math import sqrt

# Generic Sudoku Solver
# ******************************
# A sudoku puzzle is one such that given a set of unique characters, each row, column, and 
# square grid can only have 1 each character. See https://masteringsudoku.com/sudoku-rules-beginners/
# for more information on how to play.


class SudokuSolver:

    # Constructor
    # ************************
    # cell_options param might look like ["W", "L", "F", "S", "T", "R", "N", "G", "P"]
    # The size of the grid will always be the length of cell_options  
    def __init__(self, cell_options:List[str]) -> None:
       self.length:int = len(cell_options)
       self.options = set(cell_options)
       self.square_length:int = int(sqrt(self.length))

    # finds empty cells within the board to test  
    def find_empty(self, grid)-> List: #yay
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == None:
                    return (i,j) #row, col
        return None
    # optimized valid
    def square_set(self, grid)-> set:

        #init list for the sets of squares on the grid
        squares = []
        #itteration through the grid based on its length and the square root of this length
        for i in range (0, self.length, self.square_length):
            #list with all of the sets of squares in each row
            row_of_squares = []
            for a in range (0, self.length, self.square_length):
                #init for a individual square set
                square = set()
                for b in range (self.square_length):
                    for c in range(self.square_length):
                        #adding each value to the set
                        square.add(grid[i+b][a+c])
                #removal of "None" spaces as they are already gathered in the "none_spaces" method
                square.discard(None)
                #adds this square to a list with other squares in the same row
                row_of_squares.append(square)
            #adds the row of squares to another list
            squares.append(row_of_squares)
        #returns a list that cotains lists of sets of squares from each row
        return squares
        
    def get_square(self, x,y):
        #returns ths sqare that specific coordinate is in
        x_val = int(x / self.square_length)
        y_val = int(y / self.square_length)
        return (x_val,y_val)
    

    
       

    
    # *************************
    # Takes a sudoku grid with some values filled in (2D array) and returns a solution grid 
    # with all cells filled in (also a 2D array).  Empty cell values are None.
    #
    # Reminder: Don't change this function signature. This is a "wrapper" that is called by the test. 
    # Modify solve_recursive to include needed parameters, and call that inside this function.   
    def solve(self, grid:List[List[str]]) -> List[List[str]]:
        #init for lists of sets containing all rows and cols
        rows = []
        cols = []
        #creating the sets of rows
        for i in range (self.length):
            temp_set_row = set()
            for j in range(self.length):
                temp_set_row.add(grid[i][j])
            rows.append(temp_set_row)
        #creating the sets of cols
        for i in range (len(grid)):
            temp_set_col = set()
            for j in range (len(grid[0])):
                temp_set_col.add(grid[j][i])
            cols.append(temp_set_col)

        squares = self.square_set(grid)
        self.solve_recursive(grid, rows, cols, squares, self.options, cols, rows, squares)
        return grid

   
                





    # A recursive function used to solve the puzzle. This is NOT used by any test cases, so 
    # modify parameters to include whatever you need!
    def solve_recursive(self, grid:List[List[str]], rows, cols, squares, options_set:set, cols_set:set, rows_set:set, squares_set:set) -> bool:
        find = self.find_empty(grid)
        #base case checkking if board is full
        if find == None: 
            return True
        else : #start backtracking recursive algorithm
            row, col = find
            
        #check each item in options to see if they work, and 
        x, y = self.get_square(row, col)
        #get the options that aren't found in the respective sets of row col square, (basically valid options)
        possible_options = options_set.difference(cols_set[col].union(rows_set[row], squares_set[x][y]))
        for i in possible_options:
            #choose
            grid[row][col] = i
            #update sets
            cols[col].add(i)
            rows[row].add(i)
            squares[x][y].add(i)
            updated_solve = self.solve_recursive(grid, rows, cols, squares, options_set, cols_set, rows_set, squares_set)
            if updated_solve:
                return True 
            rows[row].discard(i)
            cols[col].discard(i)
            squares[x][y].discard(i)

        grid[row][col] = None
        return False