from tkinter import *
from structural.facade import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self._searchBar = SearchBar()

        self.title("Wallet")
        self.geometry("640x480")
        
        self.findInput = Entry(self, background="white")
        self.findInput.pack(expand=True)
        
        self.button = Button(self, text="find cats", command=self.find_something)
        self.button.pack(expand=True)
    
        self.searchText = Label(self, text="")
        self.searchText.pack(expand=True)
    
    def find_something(self):
        textToSearch = self.findInput.get()
        html = self._searchBar.find(textToSearch)
        self.searchText.config(text=html)
        
        