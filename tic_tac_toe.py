class Board:
    """Represents one board to a Tic-Tac-Toe game."""

    def __init__(self):
        """Initializes a new board.
        A board is a dictionary which the key is the position in the board
        and the value can be 'X', 'O' or ' ' (representing an empty position
        in the board.)
        """
        self.board = {
                "TL": " ", "TM": " ", "TR": " ",
                "ML": " ", "MM": " ", "MR": " ",
                "BL": " ", "BM": " ", "BR": " "}

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
        if self.board[position] is " ":
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
        """Returns True if the player won and False otherwise."""
        if (self.board["TL"] == player.type and self.board["TM"] == player.type and self.board["TR"] == player.type or
            self.board["ML"] == player.type and self.board["MM"] == player.type and self.board["MR"] == player.type or
            self.board["BL"] == player.type and self.board["BM"] == player.type and self.board["BR"] == player.type or
            self.board["TL"] == player.type and self.board["ML"] == player.type and self.board["BL"] == player.type or
            self.board["TM"] == player.type and self.board["MM"] == player.type and self.board["BM"] == player.type or
            self.board["TR"] == player.type and self.board["MR"] == player.type and self.board["BR"] == player.type or
            self.board["TL"] == player.type and self.board["MM"] == player.type and self.board["BR"] == player.type or
            self.board["BL"] == player.type and self.board["MM"] == player.type and self.board["TR"] == player.type):
            return True
        return False


class Player:
    """Represents one player."""
    def __init__(self, type):
        """Initializes a player with type 'X' or 'O'."""
        self.type = type

    def __str__(self):
        return f"Player {self.type}"


class Game:
    """Represents a Tic-Tac-Toe game.
    The game defines player 1 always playing with 'X'.
    """
    def __init__(self):
        """Initilize 2 Players and one Board."""
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

    def print_valid_entries(self):
        """Prints the valid inputs to play the game."""
        print("""
            TL - top left    | TM - top middle    | TR - top right
            ML - middle left | MM - center        | MR - middle right
            BL - bottom left | BM - bottom middle | BR - bottom right
            """)

    def printing_board(self):
        self.board.print_board()

    def get_player1(self):
        return self.player1

    def change_turn(self, player):
        """Changes the player turn.
        Receives a player and returns the other.
        """
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def won_game(self, player):
        """Returns True if the player won the game, False otherwise."""
        return self.board.is_winner(player)

    def modify_board(self, position, player):
        """Receives position and player type ('X' or 'O').
        Returns modified board if position was valid.
        Asks to player try a different position otherwise.
        """
        if self.board.change_board(position, player.type) is not None:
            return self.board.change_board(position, type)
        else:
            position = input("Not available position. Please, try again: ")
            return self.board.change_board(position, player.type)


def play():
    game = Game()
    game.print_valid_entries()
    player = game.get_player1()
    num = 9
    while num > 0:
        num -= 1
        game.printing_board()
        position = input(f"{player} turn, what's your move? ")
        game.modify_board(position, player)
        if game.won_game(player):
            print(f"{player} is the Winner!")
            break
        else:
            player = game.change_turn(player)
    if num == 0:
        print("Game over! It's a tie!")


if __name__ == "__main__":
    play()
