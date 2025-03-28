from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, surface):
        pass