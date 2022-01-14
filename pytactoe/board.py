import dataclasses
import enum

class Direction(enum.Enum):
    """Represents the four patters in which a sequence on the board may exist.
    
    Horizontal and Vertical patterns apply both ways but are searched left to right
    and top to bottom. The Diagonal patterns are checked from the top/bottom to right.
    """
    HORIZONTAL = enum.auto()
    VERTICAL = enum.auto()
    DIAGONAL_NE = enum.auto() # Goes North East
    DIAGONAL_SE =  enum.auto() # Checks South East


@dataclasses.dataclass
class Square:
    """Represents a square on the board."""

    symbol: str = " "

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
            self.board[row][col] = Square(symbol=symbol)
        else:
            raise ValueError("Invalid move, slot was not empty!")

    def get_longest_sequence_for_symbol(self, player_symbol: str) -> int:
        """Gets the longest sequence for a symbol in all the directions"""


        max_val = 0
        for direction in Direction:
            sequence_length = self.get_longest_sequence_in_direction(player_symbol, direction)
            if sequence_length > max_val:
                max_val = sequence_length

        return max_val

    
    def get_longest_sequence_in_direction(self, player_symbol: str, direction: Direction) -> int:
        """Checks a single direction and returns the longest direction.
        
        The direction is one of the valid ways to get a sequence (horizontal, vertical, diagonal)."""

        # Sets an empty matrix [width * height] to zero
        matrix = [[0 for col in range(self.width)] for row in range(self.height)]

        longest_sequence = 0

        for i in range(self.height):
            for j in range(self.width):
                square = self.board[i][j]

                # We should increase the score
                if square.symbol == player_symbol:

                    # Check if previous item set per direction
                    match direction:
                        case Direction.HORIZONTAL:
                            if j > 0:
                                matrix[i][j] = matrix[i][j - 1] + 1
                            else:
                                matrix[i][j] = 1

                        case Direction.VERTICAL:
                            if i > 0:
                                matrix[i][j] = matrix[i - 1][j] + 1
                            else:
                                matrix[i][j] = 1

                        case Direction.DIAGONAL_NE:
                            if i > 0 and j < self.width - 1:
                                matrix[i][j] = matrix[i - 1][j + 1]
                            else:
                                matrix[i][j] = 1

                        case Direction.DIAGONAL_SE:
                            if i > 0 and j > 0:
                                matrix[i][j] = matrix[i - 1][j - 1]
                            else:
                                matrix[i][j] = 1
                
                # Check if we have a new longest sequence
                if matrix[i][j] > longest_sequence:
                    longest_sequence = matrix[i][j]
        
        return longest_sequence



    def __repr__(self) -> str:
        """Custom representation for the TicTacToe board"""
        return "\n".join([" ".join([str(col) for col in row]) for row in self.board])
