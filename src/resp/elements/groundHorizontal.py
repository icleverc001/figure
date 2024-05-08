import sys
import os
sys.path.append(os.path.dirname(__file__))

from baseElement import BaseElement
from line import Line
from parts.point import Point
from parts.stroke import Stroke

class GroundHorizontal(BaseElement):
    def __init__(self, pointLeft: Point, length: float, thickness: float, stroke: Stroke) -> None:
        super().__init__()
        self.pointLeft: Point = pointLeft
        self.length: float = length
        self.thickness: float = thickness
        self.stroke: Stroke = stroke
    
    def getElements(self) -> list[BaseElement]:
        elements: list[BaseElement] = []
        elements.append(Line(self.pointLeft, Point(self.pointLeft.X + self.length, self.pointLeft.Y), self.stroke))
        
        num: int = self.length // self.thickness
        tmpXs: list[int] = [self.pointLeft.X + self.thickness * i for i in range(num + 1)]
        pointsTop: list[Point] = [Point(x, self.pointLeft.Y) for x in tmpXs[1:]] 
        pointsBtm: list[Point] = [Point(x, self.pointLeft.Y + self.thickness) for x in tmpXs[:-1]] 
        lines: list[Line] = [Line(t, b, self.stroke) for t, b in zip(pointsTop, pointsBtm)]
        elements.extend(lines)
        return elements
    
    def get_text(self) -> str:
        elements: list[BaseElement] = self.getElements()
        txt: str = '\n'.join([elem.get_text() for elem in elements])
        return txt