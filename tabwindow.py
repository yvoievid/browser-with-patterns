from tkinter import *

class Tab(Toplevel):
    def __init__(self, title = "tab", widget = None) -> None:
        super().__init__()
        self.title(title)
        self.geometry("640x120")   
        buttonText = "Call " + title
        self.callButton = Button(self, text=buttonText, command=self.call)     
        self.widget = widget   
        self.callButton.pack(expand=True)
    
    def call(self):
        print(self.widget.open())