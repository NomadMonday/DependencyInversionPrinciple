from emailer import Emailer
from logger import Logger
from person import Person

class Chore:
    def __init__(self):
        self.chore_name: str = None
        self.owner: Person = None
        self.hours_worked: float = 0.0
        self.is_complete: bool = None

    def PerformedWork(self, hours: float) -> None:
        self.hours_worked += hours
        log = Logger()
        log.Log(f"Performed work on {self.chore_name}")

    def CompleteChore(self) -> None:
        self.is_complete = True

        log = Logger()
        log.Log(f"Completed {self.chore_name}")

        emailer = Emailer()
        emailer.SendEmail(self.owner, f"The chore {self.chore_name} is complete.")
