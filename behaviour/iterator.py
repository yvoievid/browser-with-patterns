from collections.abc import Iterable, Iterator

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
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection