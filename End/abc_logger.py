from abc import ABC
from abc import abstractmethod

class ABCLogger(ABC):
    @abstractmethod
    def Log(self, message: str):
        pass
