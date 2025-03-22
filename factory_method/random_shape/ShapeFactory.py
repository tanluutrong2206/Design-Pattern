from factory_method.random_shape.Circle import Circle
from factory_method.random_shape.Rectangle import Rectangle
from factory_method.random_shape.ShapeContext import ShapeContext
from factory_method.random_shape.ShapeType import ShapeType


class ShapeFactory:
    @staticmethod
    def create_shape(context: ShapeContext):
        if context.shape_type == ShapeType.CIRCLE:
            return Circle(context.x, context.y)
        elif context.shape_type == ShapeType.RECTANGLE:
            return Rectangle(context.x, context.y)
        else:
            raise ValueError(f"Unknown shape type: {context.shape_type}")