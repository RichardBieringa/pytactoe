import enum
import abc


class PlayerType(enum.Enum):
    """Represents the the piece the player will play"""

    X = enum.auto()
    O = enum.auto()


class Player(abc.ABC):
    """Represents a player in the tic tac toe game."""

    @abc.abstractmethod
    def __init__(self, name: str, type: PlayerType) -> None:
        self.name = name
        self.type = type
        pass

    @abc.abstractmethod
    def get_move(self):
        pass


class ComputerPlayer(Player):
    def __init__(self, name: str, type: PlayerType) -> None:
        self.type = type
        self.name = name
        pass

    def get_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self, name: str, type: PlayerType) -> None:
        self.type = type
        self.name = name
        pass

    def get_move(self):
        pass
