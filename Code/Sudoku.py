import random

class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def valid_move(self, row, col, num):
        # Zeile prüfen
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Spalte prüfen
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # 3x3 Block prüfen
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):  # alle Zahlen durchgehen
                        if self.valid_move(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0  # zurücksetzen
                    return False  # wenn keine Zahl passt
        return True  # wenn kein leeres Feld mehr vorhanden

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else "." for num in row))



  
        

        
        
