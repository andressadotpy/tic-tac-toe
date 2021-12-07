from game.game import Game


def test_first_player_always_X():
    game = Game()

    assert game.get_player1().type ==  "X"

def test_change_player_turn():
    game = Game()
    player1 = game.get_player1()

    player2 = game.change_turn(player1)
    assert player2.type == "O"