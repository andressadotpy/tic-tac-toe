class Board:

    def __init__(self):
        """Initializes a new board.
        A board is a dictionary which the key is the position in the board
        and the value can be 'X', 'O' or ' ' (representing an empty position
        in the board.)
        """
        self.board = {
                "TL": " ", "TM": " ", "TR": " ",
                "ML": " ", "MM": " ", "MR": " ",
                "BL": " ", "BM": " ", "BR": " "
        }

    def print_board(self):
        print(self.board["TL"] + "|" + self.board["TM"] \
            + "|" + self.board["TR"] + "|")
        print("-+" * 3)
        print(self.board["ML"] + "|" + self.board["MM"] \
            + "|" + self.board["MR"] + "|")
        print("-+" * 3)
        print(self.board["BL"] + "|" + self.board["BM"] \
            + "|" + self.board["BR"] + "|")

    def _is_valid_move(self, position):
        if self.board[position] == " ":
            return True
        return False

    def change_board(self, position, type):
        """Receive a position and if the player is 'X' or 'O'.
        Checks if the position is valid, modifies the board and returns the modified board.
        Returns None if the move is not valid.
        """
        if self._is_valid_move(position):
            self.board[position] = type
            return self.board
        return None

    def is_winner(self, player):
        player_type = player.type
        runs = [
            # horizontal
            ["TL", "TM", "TR"],
            ["ML", "MM", "MR"],
            ["BL", "BM", "BR"],
            # vertical
            ["TL", "ML", "BL"],
            ["TM", "MM", "BM"],
            ["TR", "MR", "BR"],
            # diagonal
            ["TL", "MM", "BR"],
            ["BL", "MM", "TR"]
            ]
        for a, b, c in runs:
            if self.board[a] == self.board[b] == self.board[c] == player_type:
                return True
        return False