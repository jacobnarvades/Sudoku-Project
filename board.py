import pygame
pygame.init()

class Board:

    global BLACK, CELL_SIZE
    BLACK = (0, 0, 0)
    CELL_SIZE = 50
    
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # Create a 2D list to store the board values
        self.board = []

        # Create a 2D list to store the original board values (for resetting)
        self.original_board = []

        # Create a 2D list to store the cells in the board
        self.cells = []

    def draw(self):
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes."""

        # Draw horizontal lines of the grid
        for i in range(0, 10):  # 0 - 9 horizontal lines (10 total)

            if i % 3 == 0:  # Every third line is thicker than others (to delineate 3x3 boxes)
                pygame.draw.line(self.screen, BLACK, [0, i * CELL_SIZE], [9 * CELL_SIZE, i * CELL_SIZE], 4)  # Horizontal
            else:
                pygame.draw.line(self.screen, BLACK, [0, i * CELL_SIZE], [9 * CELL_SIZE, i * CELL_SIZE])  # Horizontal

        # Draw vertical lines of the grid
        for j in range(0, 10):  # 0 - 9 vertical lines (10 total)

            if j % 3 == 0:  # Every third line is thicker than others (to delineate 3x3 boxes)
                pygame.draw.line(self.screen, BLACK, [j * CELL_SIZE, 0], [j * CELL_SIZE, 9 * CELL_SIZE], 4)  # Vertical
            else:
                pygame.draw.line(self.screen, BLACK, [j * CELL_SIZE, 0], [j * CELL_SIZE, 9 * CELL_SIZE])  # Vertical

        # Draw every cell on this board
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value."""

        # Mark the cell at (row, col) as selected
        self.cells[row][col].selected = True

    def click(self, x, y):
        """If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        of the cell which was clicked. Otherwise, this function returns None."""

        # Check if x and y are within bounds of board
        if 0 <= x <= 9 * CELL_SIZE and 0 <= y <= 9 * CELL_SIZE:

            # Return row and column of clicked cell
            return int(y // CELL_SIZE), int(x // CELL_SIZE)

    def clear(self):
        """Clears  the  value  cell.  Note  that  the  user  can  only  remove  the  cell  values  and sketched value that are filled by themselves."""

        # Clear all cells that were filled by user
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value != 0 and self.cells[row][col].filled_by_user:
                    self.cells[row][col].value = 0

    def sketch(self, value):
        """Sets the sketched value of the current selected cell equal to user entered value.
        It will be displayed at the top left corner of the cell using the draw() function."""

        # Set sketched value of current selected cell to user entered value
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].selected:  # If cell is selected, set its sketched value to user entered value
                    self.cells[row][col].sketch = int(value)

    def place_number(self, value):
        """Sets the value of the current selected cell equal to user entered value. Called when the user presses the Enter key."""

        # Set value of current selected cell to user entered value and mark it as filled by user (for clearing)
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].selected:  # If cell is selected, set its value to user entered value
                    self.cells[row][col].value = int(value)
                    self.cells[row][col].filled_by_user = True

    def reset_to_original(self):
        """Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)."""

        # Reset all cells to their original values (0 if cleared, otherwise the corresponding digit)
        for row in range(9):
            for col in range(9):
                self.cells[row][col].value = self.original_board[row][col]

    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""

        # Check if any cell has a value of 0 (empty) and return False if so, otherwise return True (board is full)
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False

        return True

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""

        # Update underlying 2D board with values in all cells
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x, y)."""

        # Find an empty cell and return its row and col as a tuple (x, y)
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:  # If cell is empty, return its row and col as a tuple (x, y)
                    return row, col

    def check_board(self):
        """Check whether the Sudoku board is solved correctly."""

        # Check if any cell has a value of 0 (empty) and return False if so, otherwise check if board is solved correctly and return True
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:  # If cell is empty, return False
                    return False

        # Check if board is solved correctly and return True if so, otherwise return False
        return self.solve()
