import pytest

from game.board import Board
from game.player import Player


def test_board_valid_move():
    board = Board()
    board.change_board("TL", "X")

    expected_board = {
                "TL": "X", "TM": " ", "TR": " ",
                "ML": " ", "MM": " ", "MR": " ",
                "BL": " ", "BM": " ", "BR": " "
    }

    assert board.board == expected_board

def test_board_invalid_move():
    board = Board()
    board.change_board("TL", "X")
    board.change_board("TL", "O")

    expected_board = {
                "TL": "X", "TM": " ", "TR": " ",
                "ML": " ", "MM": " ", "MR": " ",
                "BL": " ", "BM": " ", "BR": " "
    }

    assert board.board == expected_board


@pytest.fixture(scope="session")
def player():
    player = Player("X")
    return player
    
def test_horizontal_win_for_player_X(player):
    board = Board()
    board.change_board("TL", "X")
    board.change_board("TM", "X")
    board.change_board("TR", "X")

    assert board.is_winner(player) == True

def test_horizontal_not_win_for_player_X(player):
    board = Board()
    board.change_board("TL", "X")
    board.change_board("TM", "O")
    board.change_board("TR", "X")

    assert board.is_winner(player) == False