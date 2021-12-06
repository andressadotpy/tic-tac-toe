from game.game import Game

def play():
    game = Game()
    game.print_valid_entries()
    player = game.get_player1()
    num = 9
    while num > 0:
        num -= 1
        game.printing_board()
        position = input(f"{player} turn, what's your move? ")
        try:
            game.modify_board(position, player)
        except KeyError:
            position = input(f"Invalid position. {player}, try again: ")
            game.modify_board(position, player)
        finally:
            if game.won_game(player):
                print(f"{player} is the Winner!")
                break
            else:
                player = game.change_turn(player)
    if num == 0:
        print("DRAW")


if __name__ == "__main__":
    play()
