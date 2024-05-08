import sys
import os
sys.path.append(os.path.dirname(__file__))

from elements.line import Line
from elements.circle import Circle
from parts.fillstroke import FillStroke
from parts.point import Point
from parts.size import Size
from baseElement import BaseElement


class RotaryDamping(BaseElement):
    def __init__(self, pointLeft: Point, pointRight: Point, radius: float, stroke: FillStroke) -> None:
        super().__init__()
        self.pointLeft: Point = pointLeft
        self.pointRight: Point = pointRight
        self.radius: float = radius 
        self.stroke: FillStroke = stroke

    def getpoints(self) -> list[Point]:
        offsetLeft: float = (self.pointRight.X - self.pointLeft.X - self.radius * 2.5) / 2.0
        # offsetRight: float = self.pointRight.X - self.pointLeft.X - self.size.width - offsetLeft
        origin = self.pointLeft.addedPoint(offsetLeft, 0).addedPoint(self.radius, 0)
        cornerL = origin.addedPoint(self.radius * 1.5, 0)
        
        points: list[Point] = []
        points.append(self.pointLeft)
        points.append(origin)
        points.append(cornerL)
        points.append(self.pointRight)
        return points

    def getElements(self, points: list[Point]) -> list[BaseElement]:
        elements: list[BaseElement] = []
        
        elements.append(Line(points[0], points[1], self.stroke))
        elements.append(Line(points[2], points[3], self.stroke))
        point2L: Point = points[2].addedPoint(0, self.radius)
        pointLineEnd: Point = points[1].addedPoint(-self.radius, self.radius)
        elements.append(Line(points[2], point2L, self.stroke))
        elements.append(Line(pointLineEnd, point2L, self.stroke))
        
        elements.append(Circle(points[1], self.radius, self.stroke.get_fillnone()))
        elements.append(Circle(points[1], self.radius / 3, self.stroke))
        
        return elements

    def get_text(self) -> str:
        points: list[Point] = self.getpoints()
        elements: list[BaseElement] = self.getElements(points)
        txt: str = '\n'.join([element.get_text() for element in elements])
        return txt
