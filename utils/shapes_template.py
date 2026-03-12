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

    @staticmethod
    def __get_side_length(point1: list[float], point2: list[float]):
        side_length = math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))

        return side_length

    def calculate_perimeter(self)-> float:
        return 2 * (self.width + self.length)
    
    def calculate_area(self)-> float:
        return self.width * self.length
    
    @classmethod
    def parse_data(cls, user_data: list):
        topright_index = user_data.index("topright")
        bottomleft_index = user_data.index("bottomleft")

        topright_points = [float(user_data[topright_index + 1]), float(user_data[topright_index + 2])]
        bottomleft_points = [float(user_data[bottomleft_index + 1]), float(user_data[bottomleft_index + 2])]
        bottomright_points = [topright_points[0], bottomleft_points[1]]

        rectangle_width = Rectangle.__get_side_length(topright_points, bottomright_points)
        rectangle_length = Rectangle.__get_side_length(bottomleft_points, bottomright_points)

        return cls(rectangle_width, rectangle_length)

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
        self.side = side

    @classmethod
    def parse_data(cls, user_data: list):
        side_index = user_data.index("side") + 1
        return cls(float(user_data[side_index]))
    
    
class Circle(GeometryShape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_perimeter(self)-> float:
        return self.radius*2*round(math.pi, 2)
    
    def calculate_area(self)-> float:
        return self.radius*self.radius*round(math.pi, 2)
    
    @classmethod
    def parse_data(cls, user_data: list):
        radius_index = user_data.index("radius") + 1
        return cls(float(user_data[radius_index]))