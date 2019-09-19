import os
from gtts import gTTS

class Move(object):
    def __init__(self, move="Rest", time=60,rest=0,sets=1):
        self.move_name = move
        self.folder_path = "circut_clips/"+self.move_name.lower().replace(" ","-")
        self.workout_path = self.folder_path +"/workout.mp3"
        self.rest_path = self.folder_path +"/rest.mp3"
        self.time = int(time)
        self.rest = int(rest)
        self.sets = int(sets)
        self.create_all_files()

    def get_time(self):
        return self.time
    def get_rest(self):
        return self.rest
    def get_sets(self):
        return self.sets
    def create_all_files(self):
        self.create_folder()
        self.create_file(self.workout_path,self.create_audio_text(self.move_name,self.time))
        self.create_file(self.rest_path,self.create_audio_text("Rest",self.rest))

    def create_file(self,filename, audio):
        if not os.path.exists(filename):
            tts = gTTS(text=audio, lang='en')
            tts.save(filename)
    def create_folder(self):
        filename = "circut_clips/"+self.move_name.lower().replace(" ","-")
        if not os.path.exists(filename):
            os.mkdir(filename)
    def create_audio_text(self,activity,time):
        return activity + " for " +str(time)+ " seconds"
    
    def speak_workout(self):
        os.system('mpg123 ' + self.workout_path)
    def speak_rest(self):
        os.system('mpg123 ' + self.rest_path)
    def __str__(self):
        return "Moves: " + self.move_name + "\tTime: " + self.time +"\tRest: "+self.rest