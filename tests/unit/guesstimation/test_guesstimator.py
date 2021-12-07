from guesstimation.guesstimator import Guesstimator


def test_guesstimator_structure():
    board = {
        "TL": " ", "TM": " ", "TR": " ",
        "ML": " ", "MM": " ", "MR": " ",
        "BL": " ", "BM": " ", "BR": " ",
    }
    guesstimator = Guesstimator()

    assert guesstimator.estimate(board) == ["TL", "TR", "BL", "BR"]

def test_counting_number_of_turns_each_player_already_played():
    board = {
        "TL": "X", "TM": "O", "TR": "X",
        "ML": " ", "MM": " ", "MR": " ",
        "BL": " ", "BM": " ", "BR": " ",
    }
    guesstimator = Guesstimator()

    assert guesstimator.number_of_turns_by_player(board) == (2, 1)