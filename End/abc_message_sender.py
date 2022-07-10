from abc import ABC
from abc import abstractmethod

class ABCMessageSender(ABC):
    @abstractmethod
    def SendMessage(self, message: str) -> None:
        pass
