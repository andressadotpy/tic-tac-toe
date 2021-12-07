from game.board import Board


class Guesstimator:

    best_agressive_plays = ["TL", "TR", "BL", "BR"]

    def __init__(self):
        ...

    def estimate(self, board_to_evaluate: dict[str, str]) -> list:
        _board_to_evaluate = Board()
        _board_to_evaluate.board = board_to_evaluate

        # If it's the first play of the game
        if self.number_of_turns_by_player(board_to_evaluate) == (0, 0):
            return Guesstimator.best_agressive_plays
        return []
        

    def number_of_turns_by_player(self, board_to_evaluate: dict[str, str]) -> tuple:
        x_counter = 0
        o_counter = 0
        for _, value in board_to_evaluate.items():
            if value == "X":
                x_counter += 1
            elif value == "O":
                o_counter += 1
        return (x_counter, o_counter)