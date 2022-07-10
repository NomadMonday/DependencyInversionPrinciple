from abc import ABC
from abc import abstractmethod
from abc_person import ABCPerson

class ABCMessageSender(ABC):
    @abstractmethod
    def SendMessage(self, person: ABCPerson, message: str) -> None:
        pass
