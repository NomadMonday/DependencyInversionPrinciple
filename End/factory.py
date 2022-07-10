from abc_chore import ABCChore
from abc_person import ABCPerson
from abc_logger import ABCLogger
from abc_message_sender import ABCMessageSender
from chore import Chore
from person import Person
from logger import Logger
from emailer import Emailer

class Factory:
    def CreatePerson() -> ABCPerson:
        return Person()
    
    def CreateLogger() -> ABCLogger:
        return Logger()

    def CreateMessageSender() -> ABCMessageSender:
        return Emailer()
    
    def CreateChore() -> ABCChore:
        return Chore(Factory.CreateLogger(), Factory.CreateMessageSender())
