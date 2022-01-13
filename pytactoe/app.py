from pytactoe import board, player, game


def main() -> None:

    player_one = player.HumanPlayer("richard", board.BoardItem.X)
    player_two = player.ComputerPlayer("BOT (easy)", board.BoardItem.O)

    tictactoe = game.TicTacToe(player_one, player_two)

    pass


if __name__ == "__main__":
    main()
