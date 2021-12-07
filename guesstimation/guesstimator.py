from game.board import Board


class Guesstimator:

    def __init__(self, board_to_evaluate):
        self.board = Board()
        self.board = board_to_evaluate

    def estimate(self):
        ...

    def number_of_turns_by_player(self):
        x_counter = 0
        o_counter = 0
        for _, value in self.board.items():
            if value == "X":
                x_counter += 1
            elif value == "O":
                o_counter += 1
        return (x_counter, o_counter)