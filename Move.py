import pyttsx3

class Move(object):
    def __init__(self, move_name,move_time,rest_time=30):
        self.move_name = move_name
        self.move_time = int(move_time)
        self.rest_time = int(rest_time)
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 120) 

    def speak_move(self):
        self.speak(self.move_name + " for " + str(self.move_time) + " seconds")
    def speak_rest(self):
        self.speak("Rest for " + str(self.rest_time) + " seconds")
    def speak_upcoming(self):
        self.speak(self.move_name + " in 3...2...1")
    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()
    def get_move_time(self):
        return self.move_time

    def get_rest_time(self):
        return self.rest_time

class Circut_Move(Move):
    def __init__(self, move_name, move_time,rest_time=30,sets = 1):
        self.sets = int(sets)
        return super().__init__(move_name, move_time,rest_time)
    
    def get_sets(self):
        return self.sets
     
class Boxing_Move(Move):
    def __init__(self, move_name, move_time,rest_time=60):
        return super().__init__(move_name, move_time,rest_time)
    
    def speak_move(self):
        self.speak(self.move_name)
    def speak_rest(self):
        self.speak("Rest")

