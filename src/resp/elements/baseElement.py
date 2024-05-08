import sys
import os
sys.path.append(os.path.dirname(__file__))

from parts.point import Point

class BaseElement:
    def __init__(self) -> None:
        pass
    
    def get_text(self) -> str:
        raise Exception("Sub classで実装")
    
    def getAddedPoint(self, point: Point, x: float = 0, y: float = 0) -> Point:
        return Point(point.X + x, point.Y + y)