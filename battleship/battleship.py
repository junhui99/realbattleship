class Game(object):
    def __init__(self,dimension_row:int,dimension_col:int): -> None:
        self.board = None
        self.players = [None] * 2
        self. cur_player_turn = 0

    def __play (self):
        while is_not_game_over(self):
            self.display_play_state()
            cur_player = self.get_cur_player()
            the_move  = self.get_cur_move()
            self.change_turn()
        self.display_the_winner()