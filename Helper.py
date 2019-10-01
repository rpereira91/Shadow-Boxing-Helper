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
                print(i+1)
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

    def read_circut(self,circut_name=""):
        with open(circut_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            self.current_circut = []
            for row in readCSV:
                self.current_circut.append(Boxing_Move(row[0],row[1]))
    def run_round(self,round_len=180):
        start = time.time()
        move_index = 0
        while(time.time() - start < round_len):
            if move_index >= len(self.current_circut):
                move_index = 0
            current_move = self.current_circut[move_index]
            current_move.speak_move()
            self.count_down(current_move.get_move_time()*2)
            move_index += 1
        self.current_circut[0].speak_rest()

    def run_match(self,num_rounds=3,rest_time=60,round_len=180):
        for i in range(num_rounds):
            self.run_round(round_len)
            self.count_down(rest_time)
    
    def conditioning(self,round_len=60):
        self.count_down(10)
        for i in range(len(self.current_circut)):
            move = self.current_circut[i]
            print(move.move_name)
            start = time.time()
            while(time.time() - start < round_len):
                move.speak_move()
                self.count_down(move.get_move_time()*2)
            if(i%3 == 0):
                move.speak_rest()
                self.count_down(30)
            start = time.time()
if __name__ == "__main__":
    helper = Circut_Helper("workouts/abs.csv")
    time.sleep(10)
    helper.run_workout()
    # helper = Combo_Helper("workouts/heavy-bag-con.csv")
    # helper.run_round(round_len=300)
    # helper.conditioning()
    # time.sleep(120)
    # helper.run_match(num_rounds=4, round_len=120,rest_time=30)
        