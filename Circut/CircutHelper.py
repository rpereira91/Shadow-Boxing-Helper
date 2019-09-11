from gtts import gTTS
import os
import csv
import time, random
from Move import Move

class CircutHelper(object):
    def __init__(self,circut_name):
        self.current_circut = self.read_circut(circut_name)
        self.rest = Move("Rest",60)
        self.create_file(self.rest.get_file_name(),self.rest.get_moves())
        for combo  in self.current_circut:
            self.create_file(combo.get_file_name(), combo.get_moves())

    def read_circut(self,circut_name=""):
        with open(circut_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            all_moves = []
            for row in readCSV:
                all_moves.append(Move(row[0],row[1]))
        return all_moves

    def run_round(self):
        for move in self.current_circut:
            self.speak(move.get_file_name())
            time.sleep(int(move.get_time()))

    def run_circut(self, num_circuts=4):
        for i in range(num_circuts):
            self.run_round()
            self.speak(self.rest.get_file_name())
            time.sleep(self.rest.get_time())

    def speak(self,filename):
        os.system('mpg123 ' + filename)

    def create_file(self,filename, audio):
        if not os.path.exists(filename):
            tts = gTTS(text=audio, lang='en')
            tts.save(filename)

if __name__ == "__main__":
    CH = CircutHelper("circut_list/ippo.csv")
    CH.run_circut()