# from urllib.request import urlopen
from behaviour.command import Search
class SearchBar():
    def __init__(self) -> None:
        pass
    
    
    def find(self, query: str):
       return Search.find(query=query)