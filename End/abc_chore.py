from abc import ABC
from abc import abstractmethod
from abc_person import ABCPerson

class ABCChore(ABC):
    def __init__(self):
        self.chore_name: str = None
        self.owner: ABCPerson = None
        self.hours_worked: float = 0.0
        self.is_complete: bool = None

    @abstractmethod
    def PerformedWork(self, hours: float) -> None:
        pass

    @abstractmethod
    def CompleteChore(self) -> None:
        pass
