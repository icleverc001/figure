import sys
import os
sys.path.append(os.path.dirname(__file__))

from baseElement import BaseElement
from parts.point import Point
from parts.stroke import Stroke

class Line(BaseElement):
    def __init__(self, point1: Point, point2: Point, stroke: Stroke) -> None:
        super().__init__()
        self.point1: Point = point1
        self.point2: Point = point2
        self.stroke: Stroke = stroke

    def get_text(self) -> str:
        txt: str = f'<line {self.point1.get_text_point1()} {self.point2.get_text_point2()} {self.stroke.get_text()}></line>'
        return txt
        

