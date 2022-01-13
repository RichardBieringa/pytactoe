from pytactoe import piece


class Square:
    """Represents a square on the board."""

    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def __repr__(self) -> str:
        return f"[{self.symbol}]"


class Board:
    """Represents a TicTacToe board"""

    def __init__(self, width: int = 3, height: int = 3) -> None:
        self.width = width
        self.height = height

        # Creates a an empty board, matrix of height x width
        self.board = [[Square(" ") for w in range(width)] for h in range(height)]

    def insert_piece(self, row: int, col: int, symbol: str) -> None:
        """Sets a piece on the board if it is empty"""

        if self.board[row][col].symbol == " ":
            self.board[row][col] = symbol
        else:
            raise ValueError("Invalid move, slot was not empty!")

    def __repr__(self) -> str:
        """Custom representation for the TicTacToe board"""

        return "\n".join([" ".join([row for row in self.board])])
