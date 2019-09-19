import os
import csv
import time, random
from Move import Move

class CircutHelper(object):
    def __init__(self,circut_name):
        self.read_circut(circut_name)

    def read_circut(self,circut_name=""):
        with open(circut_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            self.current_circut = []
            for row in readCSV:
                self.current_circut.append(Move(row[0],row[1],row[2],row[3]))

    def run_round(self):
        for move in self.current_circut:
            move.speak_workout()
            time.sleep(move.get_time())

    def run_workout(self):
        start = time.time()
        for move in self.current_circut:
            move.speak_rest()
            self.count_down(move.get_rest())
            for i in range(move.get_sets()):
                move.speak_workout()
                self.count_down(move.get_time())
                move.speak_rest()
                self.count_down(move.get_rest())
        print((time.time()-start)/60)


    def create_file(self,filename, audio):
        if not os.path.exists(filename):
            tts = gTTS(text=audio, lang='en')
            tts.save(filename)
    
    def count_down(self,rest_time):
        for i in range(rest_time):
            print(i)
            time.sleep(1)

if __name__ == "__main__":
    CH = CircutHelper("circut_list/abs.csv")
    CH.count_down(3)
    CH.run_workout()