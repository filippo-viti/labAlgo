from abc import ABC, abstractmethod


class DataStructure(ABC):
    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def os_select(self, i):
        pass

    @abstractmethod
    def os_rank(self, x):
        pass
