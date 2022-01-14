from lib2to3.pgen2.token import OP
from multiprocessing.sharedctypes import Value
from tabnanny import check
from typing import Tuple, List, Optional
from xmlrpc.client import Boolean

from pytactoe import player
from pytactoe import board

Coordinate = Tuple[int, int]


class TicTacToe:
    def __init__(self, player_list: List[player.Player]):
        self.is_playing = False
        self.player_count = 0
        self.turn_count = 0
        self.sequence_required = 3
        self.player_list = []
        self.symbols_used = {}
        self.board = board.Board(3, 3)

        for player in player_list:
            self.add_player(player)

    def add_player(self, player_instance: player.Player) -> None:
        """Adds a player to the game."""

        # Prevent user from adding a player to an active game
        if self.is_playing:
            raise ValueError("Can not add a player when a game is played.")

        # Prevent players with the same symbol
        if self.symbols_used.get(player_instance.symbol):
            raise ValueError(
                f"Player with symbol: '{player_instance.symbol}' already exists!"
            )

        self.symbols_used[player_instance.symbol] = True

        # Add the player to the player list
        self.player_list.append(player_instance)
        self.player_count += 1

    def remove_player(self, player_instance: player.Player) -> None:
        """Remove a player from the game."""

        # Prevent user from removing a player from an active game
        if self.is_playing:
            raise ValueError("Can not remove a player when a game is played.")

        # Check if the player is in the game
        if not self.symbols_used[player_instance.symbol]:
            raise ValueError("Player is not in the game")

        # Remove the player from the player list and make the symbol accessible again
        del self.symbols_used[player_instance.symbol]
        for player in self.player_list:
            if player == player_instance:
                self.player_list.remove(player)

        self.player_count -= 1

    def get_possible_moves(self) -> List[Coordinate]:
        """Gets a list of available moves

        Available moves are presented in a list of x, y coordinates
        """

        moves = []
        for h, row in enumerate(self.board.board):
            for w, col in enumerate(row):
                if col == board.Square(" "):
                    moves.append((h, w))

        return moves

    def get_current_player(self) -> player.Player:
        """Gets the current player based on the turncount"""
        # Circular array access used
        return self.player_list[self.turn_count % self.player_count]

    def check_if_winner(self) -> Optional[player.Player]:
        """Checks the board to see if any player won the game.
        
        A player has won the game if the maximum sequence length
        (default = 3) has been reached by a player on the board.
        Returns the player instance if someone won, otherwise None"""

        for player in self.player_list:
            # Checks in all wind directions for the largest sequence
            max_sequence = self.board.get_longest_sequence_for_symbol(player.symbol)

            # Checks if the player has reached the threshold
            if max_sequence >= self.sequence_required:
                return player
        
        return None


    def check_if_finished(self) -> bool:
        """Checks to see if the game is finished.

        A game ends by someone winning or if there are no available moves."""

        # Someone won the game
        winner = self.check_if_winner()
        if winner:
            print(f"Player {winner.symbol} has won the game!")
            return True

        # No moves remaining
        if len(self.get_possible_moves()) == 0:
            print(f"No available moves left, no one is a winner!")
            return True

        return False

    def play(self) -> None:
        """The main game loop"""
        self.is_playing = True

        while self.is_playing:
            print(self.board)
            print(f"Turn {self.turn_count}:")
            current_player = self.get_current_player()
            possible_moves = self.get_possible_moves()

            # Get a move from the player
            row, col = current_player.play_move(possible_moves)

            # Play the move from the player
            self.board.insert_piece(row, col, current_player.symbol)

            # Check if the game has ended
            if self.check_if_finished():
                self.is_playing = False
                return

            self.turn_count += 1
