from typing import Tuple

from attr import get_run_validators

from pytactoe import player
from pytactoe import board


class TicTacToe:
    def __init__(self, player_one: player.Player, player_two: player.Player):
        self.board = board.Board(3, 3)
        self.players = [player_one, player_two]
        self.turn_count = 0

        if player_one.type == player_two.type:
            raise ValueError(
                f"Players can not both have the same piece: '{player_one.type}'"
            )

    def get_available_moves(self) -> Tuple[int, int]:
        """Gets a list of available moves

        Available moves are presented in a list of x, y coordinates
        """

        moves = []

        for h, row in enumerate(self.board):
            for w, col in enumerate(row):
                if col == board.BoardItem.empty:
                    moves.append((h, w))

    def play(self):
        moves = self.get_available_moves()

        finished = False
        while not finished:
            # iterates over the player array in a circular fashion
            current_player = self.players[self.turn_count % len(self.players)]

            # get a move from the player
            move = current_player.get_move()

            # No winner
            if len(self.get_available_moves()) == 0:
                return None

            self.turn_count += 1
