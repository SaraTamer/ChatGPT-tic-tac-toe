from abc import ABC, abstractmethod


class Board:
    def __init__(self):
        self.dimension = 0
        self.board = None
        self.count_moves = 0

    def set_dimension(self, dim):
        self.dimension = dim
        self.board = [[0 for _ in range(dim)] for _ in range(dim)]
        count = 1
        for i in range(dim):
            for j in range(dim):
                self.board[i][j] = str(count)
                count += 1
        self.count_moves = 0

    def display_board(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.board[i][j], end=" ")
            print()

    def update_board(self, x, symbol):
        row = (x - 1) // self.dimension
        col = (x - 1) % self.dimension
        if self.board[row][col] != 'X' and self.board[row][col] != 'O':
            self.board[row][col] = symbol
            self.count_moves += 1
            return True
        else:
            return False

    def is_winner(self, symbol):
        # Check rows and columns for winner
        for i in range(self.dimension):
            if all(self.board[i][j] == symbol for j in range(self.dimension)):
                return True
            if all(self.board[j][i] == symbol for j in range(self.dimension)):
                return True
        # Check diagonals for winner
        if all(self.board[i][i] == symbol for i in range(self.dimension)):
            return True
        if all(self.board[i][self.dimension - i - 1] == symbol for i in range(self.dimension)):
            return True
        # No winner
        return False

    def is_draw(self):
        return self.count_moves == self.dimension ** 2


class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def get_move(self):
        pass

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name


class Game(ABC):
    @abstractmethod
    def run(self):
        pass
