from pytactoe import player, game


def main() -> None:
    players = [
        player.HumanPlayer("richard", "X"),
        player.RandomComputerPlayer("BOT (easy)", "O"),
    ]

    game_instance = game.TicTacToe(player_list=players)

    game_instance.play()


if __name__ == "__main__":
    main()
