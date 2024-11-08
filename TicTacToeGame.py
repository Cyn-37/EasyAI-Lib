from easyAI import TwoPlayerGame, AI_Player, Negamax
from easyAI.Player import Human_Player

class TicTacToe(TwoPlayerGame):

    def __init__(self, players):
        self.players = players  # Initialize players (human and AI)
        self.board = [0] * 9  # Create a board with 9 empty spaces (0 indicates empty)
        self.current_player = 1  # Set the current player to player 1 (human)

    def possible_moves(self):
        # Return a list of possible moves
        return [x + 1 for x, y in enumerate(self.board) if y == 0]

    def make_move(self, move):
        # Place the current player's mark (X or O) on the board
        self.board[int(move) - 1] = self.current_player

    def unmake_move(self, move):  
        # Remove the current player's mark from the board (used for undoing moves)
        self.board[int(move) - 1] = 0

    def lose(self):
        # Check if the current player has lost
        return any(
            [
                # Check all possible winning combinations
                all([(self.board[z - 1] == self.opponent_index) for z in line])
                for line in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
            ]
        )

    def is_over(self):
        # Check if the game is over (either all moves are made or the current player has lost)
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        # Print the current state of the board
        print(
            "\n"
            + "\n".join(
                [
                    " ".join([[".", "O", "X"][self.board[3 * j + i]] for i in range(3)])  # Show board with '.' for empty, 'O' for AI, 'X' for human
                    for j in range(3)
                ]
            )
        )

    def scoring(self):
        # Return a score for the current board state
        return -100 if self.lose() else 0  


if __name__ == "__main__":
    ai_algo = Negamax(6)  # Create an AI player using Negamax algorithm
    TicTacToe([Human_Player(), AI_Player(ai_algo)]).play()  # Start the game