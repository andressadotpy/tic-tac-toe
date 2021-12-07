class Board:

    def __init__(self):
        """Initializes a new board.
        A board is a dictionary which the key is the position in the board
        and the value can be 'X', 'O' or ' ' (representing an empty position
        in the board.)
        """
        self._board = {
                "TL": " ", "TM": " ", "TR": " ",
                "ML": " ", "MM": " ", "MR": " ",
                "BL": " ", "BM": " ", "BR": " "
        }

    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, board):
        self._board = board

    def print_board(self):
        print(self._board["TL"] + "|" + self._board["TM"] \
            + "|" + self._board["TR"] + "|")
        print("-+" * 3)
        print(self._board["ML"] + "|" + self._board["MM"] \
            + "|" + self._board["MR"] + "|")
        print("-+" * 3)
        print(self._board["BL"] + "|" + self._board["BM"] \
            + "|" + self._board["BR"] + "|")

    def _is_valid_move(self, position):
        if self._board[position] == " ":
            return True
        return False

    def change_board(self, position, type):
        """Receive a position and if the player is 'X' or 'O'.
        Checks if the position is valid, modifies the board and returns the modified board.
        Returns None if the move is not valid.
        """
        if self._is_valid_move(position):
            self._board[position] = type
            return self._board
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
            if self._board[a] == self._board[b] == self._board[c] == player_type:
                return True
        return False