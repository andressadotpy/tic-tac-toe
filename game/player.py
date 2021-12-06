class Player:

    def __init__(self, type):
        """Initializes a player with type 'X' or 'O'."""
        self.type = type

    def __str__(self):
        return f"Player {self.type}"