from factory_method.random_shape.ShapeType import ShapeType


class ShapeContext:
    def __init__(self, shape_type: ShapeType, x, y):
        self.shape_type = shape_type
        self.x = x
        self.y = y