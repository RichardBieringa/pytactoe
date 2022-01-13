import pytest

from pytactoe import board


@pytest.mark.parametrize(
    "width",
    [3, 5, 1, 10, 3],
)
@pytest.mark.parametrize(
    "height",
    [3, 5, 1, 3, 10],
)
def test_board_dimensions(width: int, height: int) -> None:
    """Tests various TicTacToe Board dimensions"""
    board_instance = board.Board(width, height)

    # Check row count
    assert len(board_instance.board) == height

    # Check col count
    assert len(board_instance.board[0]) == width


def test_emtpy_board():
    """Creates a board and tests if the board starts empty"""
    width, height = 3, 3
    board_instance = board.Board(width, height)

    for row in range(height):
        for col in range(width):
            assert board_instance.board[row][col] == board.BoardItem.empty


def test_board_representation():
    """Tests the game board's __repr__ implementation"""

    width, height = 3, 3
    board_instance = board.Board(width, height)

    expected_representation = "[ ] [ ] [ ]\n[ ] [ ] [ ]\n[ ] [ ] [ ]"

    assert board_instance.__repr__() == expected_representation
