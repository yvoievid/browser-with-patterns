# from urllib.request import urlopen
import requests

class SearchBar():
    def __init__(self) -> None:
        pass
    
    
    def find(self, query: str):
        # url = 
        page = requests.get("http://www.google.com/search?q=" + query)
        # html_bytes = page.read()
        # html = html_bytes.decode("utf-8")
        return page.text