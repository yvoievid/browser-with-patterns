from abc import ABC, abstractmethod
import requests
from tkinter import *
import pyperclip

class CommandFilterBuilder(ABC):
    def __init__(self) -> None:
        self.command = SearchCommand()
        super().__init__()
        
    def withQuery(self, query):
        self.query = query
        return self
    
    def build(self):
        return self.command

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    

class Search():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def find(query):
        page = requests.get("http://www.google.com/search?q=" + query)
        return page.text



class SearchCommand(Command):
    def __init__(self, query) -> None:
        self.query = query
        super().__init__()
        
    def execute(self):
        return Search().find(self.query)
    

class CopyCommand(Command):
    def __init__(self, searchedText: Label) -> None:
        self.searchedText = searchedText
        super().__init__()
        
    def execute(self):
        pyperclip.copy(self.searchedText.cget("text"))
        print("text copied!")
        
    

class SaveCommand(Command):
    def __init__(self) -> None:
        super().__init__()
        
    def execute(self):
        print("saved!")