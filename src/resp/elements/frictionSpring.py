import sys
import os
sys.path.append(os.path.dirname(__file__))

from elements.line import Line
from elements.circle import Circle
from parts.fillstroke import FillStroke
from parts.point import Point
from parts.size import Size
from parts.path import Path
from baseElement import BaseElement


class FrictionSpring(BaseElement):
    def __init__(self, pointLeft: Point, pointRight: Point, radius: float, stroke: FillStroke) -> None:
        super().__init__()
        self.pointLeft: Point = pointLeft
        self.pointRight: Point = pointRight
        self.radius: float = radius 
        self.stroke: FillStroke = stroke

    def getpoints(self) -> list[Point]:
        offsetLeft: float = (self.pointRight.X - self.pointLeft.X - self.radius * 3) / 2.0
        pointL = self.pointLeft.addedPoint(offsetLeft, 0)
        # offsetRight: float = self.pointRight.X - self.pointLeft.X - self.size.width - offsetLeft
        origin = pointL.addedPoint(self.radius * 2, 0)
        pointR = origin.addedPoint(self.radius, 0)
        
        points: list[Point] = []
        points.append(self.pointLeft)
        points.append(pointL)
        points.append(origin)
        points.append(pointR)
        points.append(self.pointRight)
        return points

    def getElements(self, points: list[Point]) -> list[BaseElement]:
        elements: list[BaseElement] = []
        
        elements.append(Line(points[0], points[1], self.stroke))
        elements.append(Line(points[3], points[4], self.stroke))
        point1L: Point = points[1].addedPoint(0, self.radius)
        pointLineEnd: Point = points[2].addedPoint(0, self.radius)
        elements.append(Line(points[1], point1L, self.stroke))
        elements.append(Line(pointLineEnd, point1L, self.stroke))
        
        path: Path = Path(self.stroke.get_fillnone())
        path.M(points[2].X, points[2].Y)
        path.m(-self.radius, 0)
        path.a(self.radius, self.radius, False, False, False, self.radius * 2, 0)
        elements.append(path)
        
        return elements

    def get_text(self) -> str:
        points: list[Point] = self.getpoints()
        elements: list[BaseElement] = self.getElements(points)
        txt: str = '\n'.join([element.get_text() for element in elements])
        return txt
