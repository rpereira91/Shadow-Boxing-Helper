class Move(object):
    def __init__(self, moves, time,rest=60):
        self.moves = moves
        self.file_name = self.create_file_name()
        self.time = time
        self.rest = rest
    def get_file_name(self):
        return self.file_name
    def get_moves(self):
        return self.moves + " for " +str(self.time) + " seconds"
    def get_time(self):
        return self.time
    def get_rest(self):
        return self.rest
    def create_file_name(self):
        fn = "circut_clips/"+self.moves.lower().replace(" ","-")+".mp3"
        return fn
    def __str__(self):
        return "Moves: " + self.moves + "\tTime: " + self.time +"\tRest: "+self.rest