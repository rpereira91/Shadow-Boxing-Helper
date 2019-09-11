from gtts import gTTS
import os
import csv
import time, random
from Move import Move

class BoxingCoach(object):
    def __init__(self):
        self.all_moves = self.read_combos()
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
            time.sleep(int(current_move.get_num_moves()) - 0.5)

    def run_match(self):
        for i in range(3):
            self.run_round(180)
            time.sleep(50)
            self.speak("move_clips/ten_seconds.mp3")

if __name__ == "__main__":
    BC = BoxingCoach()
    BC.run_match()

