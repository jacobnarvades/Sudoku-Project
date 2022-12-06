import math, random
"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
  '''
create a sudoku board - initialize class variables and set up the 2D board
This should initialize:
self.row_length		- the length of each row
self.removed_cells	- the total number of cells to be removed
self.board			- a 2D list of ints to represent the board
self.box_length		- the square root of row_length

Parameters:
  row_length is the number of rows/columns of the board (always 9 for this project)
  removed_cells is an integer value - the number of cells to be removed

Return:y
None
  '''

  def __init__(self, row_length, removed_cells): # initializes the SudokuGenerator class
    self.row_length = int(row_length)
    self.removed_cells = int(removed_cells)
    self.box_length = int(math.sqrt(row_length))
    self.board = [[0 for i in range(9)] for i in range(9)]
    # made sure to convert each value to int just in case due to ZyBooks error 

  '''
Returns a 2D python list of numbers which represents the board

Parameters: None
Return: list[list]
  '''

  def get_board(self):  # returns the board 
    return self.board

  '''
Displays the board to the console
  This is not strictly required, but it may be useful for debugging purposes

Parameters: None
Return: None
  '''

  def print_board(self):  # prints the board to the console for testing purposes
    for i in range(9):
      for j in range(9):
        print(self.board[i][j], end = " ")
      print()

  '''
Determines if num is contained in the specified row (horizontal) of the board
  If num is already in the specified row, return False. Otherwise, return True

Parameters:
row is the index of the row we are checking
num is the value we are looking for in the row

Return: boolean
  '''

  def valid_in_row(self, row, num):  # checks the validity of a number in the row
    if num in self.board[row]:
      return False
    else:
      return True

  '''
Determines if num is contained in the specified column (vertical) of the board
  If num is already in the specified col, return False. Otherwise, return True

Parameters:
col is the index of the column we are checking
num is the value we are looking for in the column

Return: boolean
  '''

  def valid_in_col(self, col, num): # checks the validity of a number in the column
    for i in range(self.row_length):
      if self.board[i][col] == num:
        return False
    return True

  '''
Determines if num is contained in the 3x3 box specified on the board
  If num is in the specified box starting at (row_start, col_start), return False.
  Otherwise, return True

Parameters:
row_start and col_start are the starting indices of the box to check
i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
num is the value we are looking for in the box

Return: boolean
  '''

  def valid_in_box(self, row_start, col_start, num): # checks the vailidity of the value in the box
    row = int(row_start)
    col = int(col_start)
    for i in range(row, row + 3):
      for j in range(col,col + 3):
        if self.board[i][j] == num:
          return False
    return True
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

  def is_valid(self, row, col, num): # uses the three different checks to see if a number can be put into the board
    row = int(row)
    col = int(col)
    num = int(num)
    if not self.valid_in_col(col,num):
      return False
    if not self.valid_in_row(row,num):
      return False
    # whether or not the num exists within the 3x3 box

    row_start = int((row // 3) * 3)   # converts to integer to avoid error
    col_start = int((col//3) * 3)
    
    if not self.valid_in_box(row_start, col_start, num):
      return False
    return True

  '''
      Fills the specified 3x3 box with values
      For each position, generates a random digit which has not yet been used in the box
  
  	Parameters:
  	row_start and col_start are the starting indices of the box to check
  	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
  
  	Return: None
  '''

  def fill_box(self, row_start, col_start): # fills the box with random integers
    row_start = int(row_start)
    col_start = int(col_start) 
    for i in range(row_start, row_start + 3):
      for j in range(col_start, col_start + 3):
        while self.board[i][j] == 0:
          num = int(random.randint(1, 9))
          
          if self.valid_in_box(row_start, col_start, num): # checks if it is ok to fill
            self.board[i][j] = num

  def fill_diagonal(self): # fills the top left middle and bottom right boxes to make the board
    i = 0
    while i <= 6:
      self.fill_box(i, i)
      i += 3

  '''
  DO NOT CHANGE
  Provided for students
  Fills the remaining cells of the board
  Should be called after the diagonal boxes have been filled
  
  Parameters:
  row, col specify the coordinates of the first empty (0) cell
  
  Return:
  boolean (whether or not we could solve the board)
  '''

  def fill_remaining(self, row, col):
    if (col >= self.row_length and row < self.row_length - 1):
      row += 1
      col = 0
    if row >= self.row_length and col >= self.row_length:
      return True
    if row < self.box_length:
      if col < self.box_length:
        col = self.box_length
    elif row < self.row_length - self.box_length:
      if col == int(row // self.box_length * self.box_length):
        col += self.box_length
    else:
      if col == self.row_length - self.box_length:
        row += 1
        col = 0
        if row >= self.row_length:
          return True

    for num in range(1, self.row_length + 1):
      row = int(row)
      col = int(col)
      if self.is_valid(row, col, num):
        self.board[row][col] = num
        if self.fill_remaining(row, col + 1):
          return True
        self.board[row][col] = 0
    return False

  '''
  DO NOT CHANGE
  Provided for students
  Constructs a solution by calling fill_diagonal and fill_remaining
  
  Parameters: None
  Return: None
  '''

  def fill_values(self):
    self.fill_diagonal()
    self.box_length = int(self.box_length)
    self.fill_remaining(0, self.box_length)

  '''
  Removes the appropriate number of cells from the board
  This is done by setting some values to 0
  Should be called after the entire solution has been constructed
  i.e. after fill_values has been called
  
  NOTE: Be careful not to 'remove' the same cell multiple times
  i.e. if a cell is already 0, it cannot be removed again
  
  Parameters: None
  Return: None
  '''
  #removes the appropriate number of cells from board
  #randomly generates(row)((col) coordinate and sets to 0)
  def remove_cells(self):
    #board is finished so no cells are removed
    cells_removed = 0
    #picks a random row and column
    while cells_removed != self.removed_cells:
      row = int(random.randint(0, 8))
      col = int(random.randint(0, 8))
      #if the (row,col) does not equal to 0
      if self.board[row][col] != 0:
        self.board[row][col] = 0
        cells_removed += 1
        #so it changed to add one to cells removed
        #in generated the game
      
  '''
  DO NOT CHANGE
  Provided for students
  Given a number of rows and number of cells to remove, this function:
  1. creates a SudokuGenerator
  2. fills its values and saves this as the solved state
  3. removes the appropriate number of cells
  4. returns the representative 2D Python Lists of the board and solution
  
  Parameters:
  size is the number of rows/columns of the board (9 for this project)
  removed is the number of cells to clear (set to 0)
  
  Return: list[list] (a 2D Python list to represent the board)
  '''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


generate_sudoku(9,0)

