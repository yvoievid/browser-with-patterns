from tkinter import *

class Tab(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.title("tab")
        self.geometry("640x120")   
        