import pytest

from pytactoe import player


@pytest.mark.parametrize("symbol", ["a", "B", "!"])
def test_valid_player_symbols(symbol):

    player_instance = player.HumanPlayer("test", symbol)
    assert player_instance.symbol == symbol


@pytest.mark.parametrize("symbol", [1, "XXXXXXXXXXXXXXXXX"])
def test_invalid_player_symbols(symbol):

    with pytest.raises(ValueError):
        player_instance = player.HumanPlayer("test", symbol)
