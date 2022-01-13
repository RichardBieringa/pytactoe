import enum

class BoardItem(enum.Enum):
    """Represents a piece on the board"""

    empty = enum.auto()
    X = enum.auto()
    O = enum.auto()


class Board:
    """Represents a TicTacToe board"""

    def __init__(self, width: int = 3, height: int = 3) -> None:
        self.width = width
        self.height = height

        # Creates a an empty board, matrix of height x width
        self.board = [[BoardItem.empty for w in range(width)] for h in range(height)]

    def print_board(self) -> None:
        """Displays the current state of the board"""

        for row in self.board:
            print(row)

    def print_board_numbers(self) -> None:
        """Displays which numbers represent a square on the board."""

        rows = []
        for height in range(self.height):
            cols = []

            for width in range(self.width):
                column_index = height * self.width + width
                cols.append(f"[{column_index}")
            
            rows.append(" ".join(cols))
        
        output = "\n".join(rows)
        print(output)
    

    def __repr__(self) -> str:
        """Custom representation for the TicTacToe board"""

        rows = []
        for row in self.board:
            columns = []
            
            for col in row:
                icon = None
                match col:
                    case BoardItem.empty:
                        icon = "[ ]"
                    case BoardItem.X:
                        icon = "[X]"
                    case BoardItem.O:
                        icon = "[O]"
                    case invalid:
                        raise ValueError("Invalid BoardItem: ", invalid)

                columns.append(icon) 

            # Creates a single row e.g. "[ ] [X] [O]"
            rows.append(" ".join(columns))
        
        return "\n".join(rows)
        
