class Move(object):
    def __init__(self, moves, num_moves=1):
        self.moves = moves
        self.file_name = self.create_file_name()
        self.num_moves = num_moves
    def get_file_name(self):
        return self.file_name
    def get_moves(self):
        return self.moves
    def get_num_moves(self):
        return self.num_moves
    def create_file_name(self):
        fn = "move_clips/"+self.moves.lower().replace(" ","-")+".mp3"
        return fn
    def __str__(self):
        return "Moves: " + self.moves + "\tNumber of Moves: " + self.num_moves