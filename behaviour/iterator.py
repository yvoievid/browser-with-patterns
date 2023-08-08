from collections.abc import Iterable, Iterator
from typing import Any, Iterator, List
from tkinter import *

class Tab():
    def __init__(self, title = "tab", widget = None) -> None:
        super().__init__()
        # self.title(title)
        # self.geometry("640x120")   
        # buttonText = "Call " + title
        # self.callButton = Button(self, text=buttonText, command=self.call)     
        # self.widget = widget   
        # self.callButton.pack(expand=True)
    

    def call(self):
        # print(self.widget.open())
        pass

class IterateTabs(Iterator):
    def __init__(self, collection, reverse = False) -> None:
        super().__init__()
        self._collection = collection
        self._reverse = reverse
    
    def __next__(self) -> Any:  
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
            
        except IndexError:
            raise StopIteration()
    
        return value

class TabsCollection(Iterable):
    def __init__(self, collection: List[Tab] = []) -> None:
        self._collection = collection
        
    def __iter__(self) -> IterateTabs:
        return IterateTabs(self._collection)

    def add_item(self, item: Any):
            self._collection.append(item)
