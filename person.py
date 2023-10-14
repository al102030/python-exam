from abc import ABC, abstractmethod


class Participant(ABC):
    def __init__(self, code=0, name="No-name", family="No-family"):
        self.code = code
        self.name = name
        self.family = family
        super().__init__()

    @abstractmethod
    def show_info(self):
        pass


class Lecturer(Participant):
    def show_info(self):
        print(
            f"Your Information: Code: {self.code}, Name: {self.name}, Family: {self.family}")

    def greet(self):
        print("Welcome Dear Professor.")


class Student(Participant):
    __city = "Rasht"

    def show_info(self):
        print(
            f"Your Information: Code: {self.code}, Name: {self.name}, Family: {self.family}, City: {self.__city}")
