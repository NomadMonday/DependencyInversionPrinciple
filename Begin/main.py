from chore import Chore
from person import Person

def main():
    owner = Person()
    owner.first_name = "Tim"
    owner.last_name = "Corey"
    owner.email_address = "tim@iamtimcorey.com"
    owner.phone_number = "555-1212"

    chore = Chore()
    chore.chore_name = "Take out the trash"
    chore.owner = owner

    chore.PerformedWork(3)
    chore.PerformedWork(1.5)
    chore.CompleteChore()

if __name__ == "__main__":
    main()
