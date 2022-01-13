from lib2to3.pgen2.token import OP
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
        self.player_list = []
        self.board = board.Board(3, 3)

        # Check for duplicate symbols
        seen_symbols = {}
        for player in player_list:

            # Prevent players with the same symbol
            if seen_symbols.get(player.symbol):
                raise ValueError(
                    f"Player with symbol: '{player.symbol}' already exists!"
                )

            seen_symbols[player.symbol] = True

            # Add the player to the player list
            self.player_list.append(player)
            self.player_count += 1

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
        """Checks the board to see if there are three pieces of the same symbol adjacent"""
        pass
        # for row in self.board.board:

    def check_if_finished(self) -> bool:
        """Checks to see if the game is finished.

        A game ends by someone winning or if there are no available moves."""

        # Someone won the game
        if self.check_if_winner():
            return True

        # No moves remaining
        if len(self.get_possible_moves()) == 0:
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
