import Generic_Board_Game


class XOBoard(Generic_Board_Game.Board):
    def __init__(self):
        super().__init__()
        self.dimension = 3
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.count_moves = 0

    def display_board(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.board[i][j], end=" ")
            print()


class XOPlayer(Generic_Board_Game.Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
        self.name = name
        self.symbol = symbol

    def get_move(self):
        while True:
            try:
                x = int(input(f"{self.name}, enter your move (1-9): "))
                if x < 1 or x > 9:
                    print("Invalid move. Please enter a number between 1 and 9.")
                    continue
                return x
            except ValueError:
                print("Invalid move. Please enter a number between 1 and 9.")

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name


class XOGame(Generic_Board_Game.Game):
    def __init__(self):
        self.board = XOBoard()
        self.player1 = XOPlayer("Player 1", "X")
        self.player2 = XOPlayer("Player 2", "O")
        self.current_player = self.player1

    def run(self):
        """
        This function starts the game and alternates turns between the two players until
        there is a winner or it's a draw.
        """
        self.board.display_board()

        current_player = self.player1
        while True:
            # Get the current player's move
            print(current_player.name + "'s turn:")
            move = current_player.get_move()

            # Update the board with the player's move
            if self.board.update_board(move, current_player.symbol):
                # Print the updated board
                self.board.display_board()

                # Check if the current player is the winner
                if self.board.is_winner(current_player.symbol):
                    print(current_player.name + " wins!")
                    break

                # Check if it's a draw
                if self.board.is_draw():
                    print("It's a draw!")
                    break

                # Switch to the other player
                if current_player == self.player1:
                    current_player = self.player2
                else:
                    current_player = self.player1
            else:
                # Invalid move, try again
                print("Invalid move. Try again.")
                self.board.display_board()


game = XOGame()
game.run()


