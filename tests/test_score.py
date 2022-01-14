import pytest

from pytactoe import board


def test_horizontal_score():
    board_instance = board.Board(3, 3)

    test_squares = [
        ["x", "x", "x"],
        [" ", " ", " "],
        ["o", "o", " "],
    ]

    for i in range(board_instance.height):
        for j in range(board_instance.width):
            board_instance.insert_piece(i, j, test_squares[i][j])

    score_x = board_instance.get_longest_sequence_in_direction(
        "x", board.Direction.HORIZONTAL
    )
    score_o = board_instance.get_longest_sequence_in_direction(
        "o", board.Direction.HORIZONTAL
    )

    assert score_x == 3
    assert score_o == 2


def test_vertical_score():
    board_instance = board.Board(3, 3)

    test_squares = [
        ["x", " ", " "],
        ["x", "o", " "],
        ["x", "o", " "],
    ]

    for i in range(board_instance.height):
        for j in range(board_instance.width):
            board_instance.insert_piece(i, j, test_squares[i][j])

    score_x = board_instance.get_longest_sequence_in_direction(
        "x", board.Direction.VERTICAL
    )
    score_o = board_instance.get_longest_sequence_in_direction(
        "o", board.Direction.VERTICAL
    )

    assert score_x == 3
    assert score_o == 2


def test_diagonal_ne_score():
    board_instance = board.Board(3, 3)

    test_squares = [
        ["y", " ", "x"],
        [" ", "x", "o"],
        ["x", "o", " "],
    ]

    for i in range(board_instance.height):
        for j in range(board_instance.width):
            board_instance.insert_piece(i, j, test_squares[i][j])

    score_x = board_instance.get_longest_sequence_in_direction(
        "x", board.Direction.DIAGONAL_NE
    )
    score_o = board_instance.get_longest_sequence_in_direction(
        "o", board.Direction.DIAGONAL_NE
    )
    score_y = board_instance.get_longest_sequence_in_direction(
        "y", board.Direction.DIAGONAL_NE
    )

    assert score_x == 3
    assert score_o == 2
    assert score_y == 1


def test_diagonal_se_score():
    board_instance = board.Board(3, 3)

    test_squares = [
        ["x", " ", " "],
        ["o", "x", " "],
        ["y", "o", "x"],
    ]

    for i in range(board_instance.height):
        for j in range(board_instance.width):
            board_instance.insert_piece(i, j, test_squares[i][j])

    score_x = board_instance.get_longest_sequence_in_direction(
        "x", board.Direction.DIAGONAL_SE
    )
    score_o = board_instance.get_longest_sequence_in_direction(
        "o", board.Direction.DIAGONAL_SE
    )
    score_y = board_instance.get_longest_sequence_in_direction(
        "y", board.Direction.DIAGONAL_SE
    )

    assert score_x == 3
    assert score_o == 2
    assert score_y == 1
