from abc_person import ABCPerson
from abc_logger import ABCLogger
from abc_message_sender import ABCMessageSender

class Chore:
    def __init__(self, logger: ABCLogger, message_sender: ABCMessageSender):
        self.chore_name: str = None
        self.owner: ABCPerson = None
        self.hours_worked: float = 0.0
        self.is_complete: bool = None
        self.logger: ABCLogger = logger
        self.message_sender: ABCMessageSender = message_sender

    def PerformedWork(self, hours: float) -> None:
        self.hours_worked += hours
        self.logger.Log(f"Performed work on {self.chore_name}")

    def CompleteChore(self) -> None:
        self.is_complete = True
        self.logger.Log(f"Completed {self.chore_name}")
        self.message_sender.SendEmail(self.owner, f"The chore {self.chore_name} is complete.")
