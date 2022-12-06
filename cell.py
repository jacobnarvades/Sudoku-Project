class Cell:
  S = SudokuGenerator
    def __init__(self,value,row,col,screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cel_value(self,value):
        self.value = value
        
    def set_sketched_value(self,value):
        self.value = value
        
    def draw(self):
        #draws cell along wih value inside it
        # IF NOT ZERO displays value
        pass

