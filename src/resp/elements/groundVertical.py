import sys
import os
sys.path.append(os.path.dirname(__file__))

from baseElement import BaseElement
from line import Line
from parts.point import Point
from parts.stroke import Stroke

class GroundVertical(BaseElement):
    def __init__(self, pointBottom: Point, length: float, thickness: float, stroke: Stroke) -> None:
        super().__init__()
        self.pointBottom: Point = pointBottom
        self.length: float = length
        self.thickness: float = thickness
        self.stroke: Stroke = stroke
    
    def getElements(self) -> list[BaseElement]:
        pointBtm = self.pointBottom
        
        elements: list[BaseElement] = []
        elements.append(Line(pointBtm, Point(pointBtm.X, pointBtm.Y - self.length), self.stroke))
        
        num: int = self.length // self.thickness
        tmpYs: list[int] = [pointBtm.Y - self.thickness * i for i in range(num + 1)]
        pointsRight: list[Point] = [Point(pointBtm.X, y) for y in tmpYs[1:]] 
        pointsLeft: list[Point] = [Point(pointBtm.X - self.thickness, y) for y in tmpYs[:-1]] 
        lines: list[Line] = [Line(r, l, self.stroke) for r, l in zip(pointsRight, pointsLeft)]
        elements.extend(lines)
        return elements
    
    def get_text(self) -> str:
        elements: list[BaseElement] = self.getElements()
        txt: str = '\n'.join([elem.get_text() for elem in elements])
        return txt