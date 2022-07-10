from abc_logger import ABCLogger

class Logger(ABCLogger):
    def Log(self, message: str) -> None:
        print(f"Write to Console: {message}")
