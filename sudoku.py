from sudoku_generator import SudokuGenerator, generate_sudoku
from sudoku_generator import 
from board import Board
from cell import Cell

S = SudokuGenerator

#start screen here


choice = input("pick a difficulty: ")
if choice =="1":
  #difficulty = 'easy'
  S(row_length, 30, board, box_length = 3)
elif choice =="2":
  #difficulty = "medium"
  S(row_length, 40, board, box_length = 3)
elif choice =="3":
  #difficulty  = "hard"
  S(row_length,50,board,box_length=3)

  