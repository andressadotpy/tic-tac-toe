from game.board import Board


from game.board import Board


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