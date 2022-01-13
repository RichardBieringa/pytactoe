import abc
import random

from typing import Tuple, List

Coordinate = Tuple[int, int]


class Player(abc.ABC):
    """Represents a player in the tic tac toe game."""

    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol

        if len(symbol) > 1:
            raise ValueError("Player symbol can only be a single character")

        if symbol == " ":
            raise ValueError("Player symbol can not be empty")

    @abc.abstractmethod
    def play_move(self, possible_moves: List[Coordinate]) -> Coordinate:
        """Gets the next move from the player"""
        pass


class RandomComputerPlayer(Player):
    """A computer player that plays random moves"""

    def __init__(self, name: str, symbol: str) -> None:
        super().__init__(name, symbol)

    def play_move(self, possible_moves: List[Coordinate]) -> Coordinate:
        return random.choice(possible_moves)


class HumanPlayer(Player):
    def __init__(self, name: str, symbol: str) -> None:
        super().__init__(name, symbol)

    def play_move(self, possible_moves: List[Coordinate]) -> Coordinate:
        while True:
            print(f"Enter move {self.symbol}")
            try:
                row = int(input("row: "))
                col = int(input("column: "))

                move = (row, col)
                if move in possible_moves:
                    return (row, col)
                else:
                    raise ValueError
            except ValueError:
                print("row/col should be valid numbers")
