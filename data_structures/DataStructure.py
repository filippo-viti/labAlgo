from abc import ABC, abstractmethod


class DataStructure(ABC):
    @abstractmethod
    def insert(self, value):
        pass
