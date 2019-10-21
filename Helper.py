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
                move.speak("Set: " + str(i+1) + " of " + str(move.get_sets()))
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
    def run_round(self,round_len=180,round=1,rnd_time = 30):
        start = 0
        move_index = 0
        self.current_circut[0].speak("Round: " + str(round))
        while(start < round_len):
            move_index = random.randint(0,len(self.current_circut)-1)
            current_move = self.current_circut[move_index]
            current_move.speak_move()
            time.sleep(rnd_time)
            start += rnd_time
        self.current_circut[0].speak_rest()

    def run_match(self,num_rounds=3,rest_time=60,round_len=180):
        for i in range(num_rounds):
            self.run_round(round_len,i+1)
            self.count_down(rest_time)
    
    def conditioning(self,round_len=60):
        self.count_down(10)
        for i in range(len(self.current_circut)):
            move = self.current_circut[i]
            print(move.move_name)
            move.speak_move()
            self.count_down(30)
def warm_up(total_time):
    helper = Combo_Helper("workouts/warm-up.csv")
    helper.conditioning()  
def shadow_box(total_time,round_len = 180, rest = 60):
    helper = Combo_Helper("workouts/combos.csv")
    rounds = int((total_time*60)/(round_len+rest))
    print(rounds)
    helper.run_match(num_rounds=rounds, round_len=round_len,rest_time=rest)  
def pull_workout():
    helper = Circut_Helper("workouts/pull.csv")
    helper.run_workout()

def push_workout():
    helper = Circut_Helper("workouts/push.csv")
    helper.run_workout()

def legs_workout():
    helper = Circut_Helper("workouts/legs.csv")
    helper.run_workout()

def abs_workout():
    helper = Circut_Helper("workouts/abs.csv")
    helper.run_workout()
def convert_to_time(minutes):
    left = minutes%60
    print(left)
    return("%d hours and %d minutes"  % (int(minutes/60) , int(left)))
    # return [int(minutes/60) , left*(6/10)]
def run_workout(heavy_bag = False):
    start = time.time()
    time.sleep(15)
    warm_up(5)
    print("Warm up complete, move to workout\tTime: " + convert_to_time(int((time.time()-start)/60)))
    time.sleep(30)
    pull_workout()
    time.sleep(30)
    print("Workout complete, move to heavy bag\tTime: " + convert_to_time(int((time.time()-start)/60)))
    # print((time.time()-start)/60)
    if heavy_bag:
        time.sleep(300)
    else:
        time.sleep(60)
    shadow_box(15,120,45)
    # print((time.time() - start)/60)
    print("Heavybag complete, move to abs\tTime: " + convert_to_time(int((time.time()-start)/60)))
    time.sleep(120)
    abs_workout()
    print((time.time()-start)/60)
def cardio(heavy_bag = True):
    start = time.time()
    time.sleep(15)
    # warm_up(5)
    print("Warm up complete,  heavy bag\tTime: " + convert_to_time(int((time.time()-start)/60)))
    # print((time.time()-start)/60)
    if heavy_bag:
        time.sleep(300)
    shadow_box(45,180,60)
    # print((time.time() - start)/60)
    time.sleep(120)
    print("Heavybag complete, move to Vest\tTime: " + convert_to_time(int((time.time()-start)/60)))
    shadow_box(15,30,30)
    print("Vest complete, move to abs\tTime: " + convert_to_time(int((time.time()-start)/60)))
    time.sleep(120)
    abs_workout()
    print("Workout Complete, Time: " + convert_to_time(int(time.time()-start)/60))
if __name__ == "__main__":
    print(convert_to_time(97))
    # run_workout(False)


        