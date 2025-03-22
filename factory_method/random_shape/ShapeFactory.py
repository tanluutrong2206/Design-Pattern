from factory_method.random_shape.Circle import Circle
from factory_method.random_shape.Rectangle import Rectangle


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, x: int, y: int):
        if shape_type == "circle":
            return Circle(x, y)
        elif shape_type == "square":
            return Rectangle(x, y)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")