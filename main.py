import BlackJack


def main():
    game = BlackJack.BlackJack()
    game.add_player('Tyler')
    game.give_player_cards()
    print(game)
    for player in game.player_cards:



if __name__ == '__main__':
    main()