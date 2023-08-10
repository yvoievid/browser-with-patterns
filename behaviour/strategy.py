from abc import ABC, abstractmethod

class MoodleStrategy(ABC):  
    @abstractmethod
    def execute(self):
        pass
    
    

class Moodle():
    def __init__(self, specificEventStrategy: MoodleStrategy) -> None:
        self._eventStrategy = specificEventStrategy
        pass
    
    def play(self):
        self._eventStrategy.execute()
        
        

class NewYearMoodleStrategy(MoodleStrategy):
    def __init__(self) -> None:
        super().__init__()
        
    def execute(self):
        print("Happy new Year")
        

class IndependenceDayMoodleStratery(MoodleStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self):
        print("Happy Independence Day")
        
    

class SaintNikolaiDayMoodleStratery(MoodleStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self):
        print("Happy St. Nikolai Day")
