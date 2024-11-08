# AI-Based Games with easyAI

This repository contains Python code for implementing two AI-based games: **Tic-Tac-Toe** and **Last Coin Standing**. Both games use the `easyAI` library, which provides a framework for implementing AI algorithms like Negamax, an adversarial search algorithm often used for decision-making in two-player games. These games are inspired by the concepts taught in the book *"AI with Python"* by Prateek Joshi.

## Games Overview

### Tic-Tac-Toe Game

A classic two-player game where one player (human) competes against an AI. The board is represented by a list of 9 spaces, and players alternate placing their marks (X for human and O for AI). The AI uses the Negamax algorithm for decision-making. The game ends when one player wins or when there are no available moves left.

#### Key Functions:
- `possible_moves()`: Returns a list of available spots on the board.
- `make_move()`: Places the current player's mark (X or O) on the board.
- `unmake_move()`: Reverts a move (used for backtracking).
- `is_over()`: Checks if the game is over (either someone wins or the board is full).
- `show()`: Displays the current board state.
- `scoring()`: Returns a score based on the current game state, used by the AI to evaluate moves.

### Last Coin Standing Game

In this game, two players (one human and one AI) take turns removing between 1 to 4 coins from a pile of 15. The game ends when the last coin is taken. The AI uses the Negamax algorithm to decide how many coins to remove based on the current state of the game.

#### Key Functions:
- `possible_moves()`: Returns the valid number of coins a player can remove.
- `make_move()`: Decreases the number of coins remaining based on the move.
- `unmake_move()`: Increases the number of coins (used for undo functionality).
- `is_over()`: Checks if the game is over (i.e., when all coins are removed).
- `show()`: Displays the remaining number of coins.
- `scoring()`: Evaluates the current state and provides a score based on whether the game is over.

## Requirements

- Python 3.x
- easyAI (Install via `pip install easyAI`)

## How to Play

Run the Python script for each game, and it will automatically start the game with one human player and one AI.

## AI Algorithms

Both games utilize the **Negamax algorithm**, a variant of the Minimax algorithm optimized for two-player games. The Negamax algorithm assumes that both players are playing optimally, and it evaluates game states recursively to make the best possible move for the AI.

## How They Relate to "AI with Python"

These games are based on the teachings of *"AI with Python"* by Prateek Joshi, which walks through the process of building simple AI algorithms, including decision-making strategies like Negamax. The implementation of these games demonstrates how AI can be applied in classic games to simulate intelligent opponents.
