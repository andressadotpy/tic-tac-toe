from .board import Board
from .player import Player

class Game:
    def __init__(self):
        """Initilize 2 Players and one Board.
        Player one is always X."""
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

    def change_turn(self, player: Player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def won_game(self, player: Player):
        return self.board.is_winner(player)

    def modify_board(self, position: str, player: Player) -> dict[str, str]:
        """Receives position and player type ('X' or 'O').
        Returns modified board if position was valid.
        Asks to player try a different position otherwise.
        """
        if self.board.change_board(position, player.type) is not None:
            return self.board.change_board(position, type)
        else:
            position = input("Not available position. Please, try again: ")
            return self.board.change_board(position, player.type)