from abc import ABC

class ABCPerson(ABC):
    def __init__(self):
        self.first_name: str = None
        self.last_name: str = None
        self.phone_number: str = None
        self.email_address: str = None
