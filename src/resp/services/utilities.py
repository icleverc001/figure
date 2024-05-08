import sys
import os
sys.path.append(os.path.dirname(__file__))

from resp.model import Model
from resp.parts.point import Point
from resp.parts.size import Size
from resp.parts.stroke import Stroke
from resp.parts.fillstroke import FillStroke
from resp.parts.viewbox import ViewBox

def get_size(point1: Point, point2: Point) -> Size:
    return Size(point2.X - point1.X, point2.X - point1.X)

def get_center_point(point1: Point, point2: Point) -> Point:
    return Point((point1.X + point2.X) / 2, (point1.Y + point2.Y) / 2)