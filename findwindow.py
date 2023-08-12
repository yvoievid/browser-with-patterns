from tkinter import *
from structural.facade import *
from behaviour.command import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self._searchBar = SearchBar()
        self.html = ""
        self.title("Wallet")
        self.geometry("640x480")
        
        self.findInput = Entry(self)
        self.findInput.grid(row=3, column=2)
       # self.findInput.pack(expand=True)
        
        self.findButton = Button(self, text="find cats", command=self.find_something)
        self.findButton.grid(row=3, column=3)
       # self.findButton.pack(expand=True)
    
        self.copyButton = Button(self, text="copy", command=self.copy)
        self.copyButton.grid(row=3, column=4)
       # self.copyButton.pack(expand=True)
        
        self.saveButton = Button(self, text="save", command=self.save)
        self.saveButton.grid(row=3, column=5)
       # self.saveButton.pack(expand=True)
        
        self.searchText = Label(self, text="")
        #self.searchText.pack(expand=True)
    
    def find_something(self):
        textToSearch = self.findInput.get()
        searchCommand = SearchCommand(textToSearch)
        self.html = searchCommand.execute()
        print(self.html)
        self.searchText.config(text=self.html)
        
    def copy(self):
        copyCommand = CopyCommand(self.searchText)
        copyCommand.execute()
        
    def save(self):
        saveCommand = SaveCommand()
        saveCommand.execute()
        