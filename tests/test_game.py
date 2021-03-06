import pytest
from pytactoe import game, player


def test_not_similar_teams():
    player_one = player.HumanPlayer("p1", "X")
    player_two = player.HumanPlayer("p2", "X")

    with pytest.raises(ValueError):
        game_instance = game.TicTacToe([player_one, player_two])
