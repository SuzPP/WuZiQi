class Player(object):
    def __init__(self, player, piece):
        self._player = player
        self._move = False
        self._piece = str(piece)

    def change_turn(self):
        self._move = True
        return self._move

    def get_player_piece(self):
        return self._piece
