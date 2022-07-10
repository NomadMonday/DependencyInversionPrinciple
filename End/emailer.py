from abc_message_sender import ABCMessageSender
from abc_person import ABCPerson

class Emailer(ABCMessageSender):
    def SendMessage(self, person: ABCPerson, message: str) -> None:
        print(f"Simulating sending an email to {person.email_address}")
