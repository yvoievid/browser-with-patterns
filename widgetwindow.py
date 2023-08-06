from tkinter import *
from creational.abstractFactory import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Widgets")
        self.geometry("640x480")
        self.button = Button(self, text="show widgets", command=self.show_widgets)
        self.button.pack(expand=True)

    def show_widgets(self):
        wf = WidgetFactory()
        
        widgets = wf.widgets
        
        for w in widgets:
            self.button = Button(self, text=f"{w.name}")
            self.button.pack(expand=True)
            
        