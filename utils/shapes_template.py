from abc import ABC, abstractmethod
import math

class GeometryShape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass


    def __str__(self) -> str:
        return f"{self.__class__.__name__} Perimeter {self.calculate_perimeter()} Area {self.calculate_area()}"

class Rectangle(GeometryShape):
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    def calculate_perimeter(self)-> float:
        return 2 * (self.width + self.length)
    
    def calculate_area(self)-> float:
        return self.width * self.length

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
        self.side = side
    
    
class Circle(GeometryShape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_perimeter(self)-> float:
        return self.radius*2*round(math.pi, 2)
    
    def calculate_area(self)-> float:
        return self.radius*self.radius*round(math.pi, 2)