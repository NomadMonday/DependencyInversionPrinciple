from person import Person

class Emailer:
    def SendEmail(self, person: Person, message: str) -> None:
        print(f"Simulating sending an email to {person.email_address}")
