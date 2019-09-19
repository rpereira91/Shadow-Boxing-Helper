from Move import *
import os, csv, time, random
class Helper(object):
    def __init__(self,circut_name):
        self.read_circut(circut_name)

    def read_circut(self,circut_name=""):
        with open(circut_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            self.current_circut = []
            for row in readCSV:
                self.current_circut.append(Move(row[0],row[1]))

    def get_total_workout_time(self):
        total_time = 0
        for move in self.current_circut:
            total_time += move.get_move_time()
        return total_time

    def get_total_rest_time(self):
        total_rest = 0
        for move in self.current_circut:
            total_rest += move.get_rest_time()
        return total_rest
    
    def get_total_time(self):
        return self.get_total_rest_time() + self.get_total_workout_time()
    
    def run_round(self):
        for move in self.current_circut:
            move.speak_upcoming()
            move.speak_move()
            self.count_down(move.get_move_time())

    def count_down(self,count_time):
        for i in range(1,count_time):
            time.sleep(1)
            if i % 10 == 0:
                print(i)

class Circut_Helper(Helper):
    def __init__(self, circut_name):
        return super().__init__(circut_name)
    
    def read_circut(self, circut_name=''):
        with open(circut_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            self.current_circut = []
            for row in readCSV:
                self.current_circut.append(Circut_Move(row[0],row[1],row[2],row[3]))

    def run_workout(self):
        start = time.time()
        for move in self.current_circut:
            move.speak_upcoming()
            for i in range(move.get_sets()):
                move.speak_move()
                self.count_down(move.get_move_time())
                move.speak_rest()
                self.count_down(move.get_rest_time())
        print((time.time()-start)/60)

    def run_circut(self,num_circuts=1,circut_rest=60):
        for i in range(num_circuts):
            self.run_round()
            time.sleep(circut_rest)
class Combo_Helper(Helper):
    # By default the round length is 3 minutes
    def __init__(self, circut_name,round_len=180,num_rounds=3):
        return super().__init__(circut_name)

if __name__ == "__main__":
    helper = Circut_Helper("workouts/ippo.csv")
    print(helper.run_circut(num_circuts=5))

        