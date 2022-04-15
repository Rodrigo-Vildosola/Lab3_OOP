from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def checkout(self):
        pass


