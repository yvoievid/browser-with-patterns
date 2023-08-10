from tkinter import *
from behaviour.strategy import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        
        self.title("Moodle")
        self.geometry("640x480")
        
        self.moodle = Button(self, text="Happy moodle", command=self.play_moodle)
        self.moodle.pack(expand=True)
    
    def play_moodle(self):
        newYearStrategy = NewYearMoodleStrategy()
        moodle = Moodle(newYearStrategy)
        moodle.play()