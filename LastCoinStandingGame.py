from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class LastCoinGame(TwoPlayerGame):
    def __init__(self, players):
        self.players = players  # Players are initialized
        self.coins = 15  # Starting number of coins
        self.current_player = 1

    def possible_moves(self):
        # Possible moves are 1, 2, 3 or 4 coins taken
        return [1, 2, 3, 4] if self.coins > 4 else list(range(1, self.coins + 1))

    def make_move(self, move):
        # Take the specified number of coins
        self.coins -= move

    def unmake_move(self, move):
        # Undo the move
        self.coins += move

    def is_over(self):
        # The game is over if there are no coins left
        return self.coins <= 0

    def show(self):
        # Display the current number of coins
        print(f'Coins remaining: {self.coins}')

    def scoring(self):
        # Return a score based on the current state
        if self.is_over():
            return -100  # Losing condition
        return 0  # Game continues

if __name__ == "__main__":
    ai_algo = Negamax(6)  # AI algorithm
    game = LastCoinGame([Human_Player(), AI_Player(ai_algo)])  # Create game with human and AI
    game.play()  # Start the game
