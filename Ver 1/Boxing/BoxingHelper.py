from gtts import gTTS
import os
import csv
import time, random
from Move import Move

class BoxingCoach(object):
    def __init__(self):
        self.all_moves = self.read_combos()
        self.begin = Move("Begin Round")
        self.rest = Move("Rest")
        self.complete = Move("Complete")
        self.create_file(self.begin.get_file_name(),self.begin.get_moves())
        self.create_file(self.rest.get_file_name(),self.rest.get_moves())
        self.create_file(self.complete.get_file_name(),self.complete.get_moves())
        # Create all the files you need
        for combo  in self.all_moves:
            self.create_file(combo.get_file_name(), combo.get_moves())
        
    def read_combos(self):
        with open('move_list.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            all_moves = []
            for row in readCSV:
                all_moves.append(Move(row[0],row[1]))
        return all_moves
    #Speak
    def speak(self,filename):
        os.system('mpg123 ' + filename)

    def create_file(self,filename, audio):
        if not os.path.exists(filename):
            tts = gTTS(text=audio, lang='en')
            tts.save(filename)

    def run_round(self,round_len):
        start = time.time()
        
        while(time.time() - start < round_len):
            current_move = self.all_moves[random.randint(0,len(self.all_moves)-1)]
            self.speak(current_move.get_file_name())
            print("Time Passed: %.2f" % (time.time() - start))
            time.sleep(int(current_move.get_num_moves()) * 2)

    def one_combo(self,round_len,current_move):
        start = time.time()
        while(time.time() - start < round_len):
            self.speak(current_move.get_file_name())
            time.sleep(1)

    def run_match(self, rounds = 1, each_round = 600, rest = 60):
        for i in range(rounds):
            self.speak(self.begin.get_file_name())
            self.run_round(each_round)
            self.speak(self.rest.get_file_name())
            time.sleep(rest)
        self.speak(self.complete.get_file_name())

if __name__ == "__main__":
    BC = BoxingCoach()
    time.sleep(8)
    # BC.run_match(each_round=720)
    BC.run_match(4,(2*60),60)

