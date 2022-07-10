## Summary
- I created this project as a demonstration of the Dependency Inversion Principle (the D in SOLID).
- It is a recreation of this demonstration by Tim Corey, except rewritten in Python: https://youtu.be/NnZZMkwI6KI
- I wanted to create a semi-guided exercise where the objective is known, but the exact solution is not due to language differences. In this way, I could create a more challenging and engaging problem to solve, while also learning how to apply SOLID principles in Python.
- The Begin folder contains the starting point of the code before the principle is applied, and the End folder contains the refactored code after.

## Notes
#### The Python standard library does not use interfaces.
- As we learned in the [Open Closed Principle](https://github.com/NomadMonday/OpenClosedPrinciple) project, abstract base classes must be used instead of interfaces.
#### An interesting mistake.
- During refactoring, I initially forgot to have the Emailer and Logger classes inherit from ABCMessageSender and ABCLogger, respectively.
- I also forgot to update the SendEmail() method name to SendMessage(), and the Chore class's CompleteChore() method still referenced the old SendEmail() method name.
- However, because Python uses duck typing and type hints aren't strictly enforced, my code still worked.
- An interesting mistake that flags something to look out for. A scenario like this could potentially introduce hard-to-find bugs. A possible workaround would be to implement strict type checking within the code to ensure the object that is being passed in is actually the type of object expected.
