import sys
import os
sys.path.append(os.path.dirname(__file__))

from elements.line import Line
from parts.stroke import Stroke
from parts.point import Point
from parts.size import Size
from baseElement import BaseElement


class Spring(BaseElement):
    # def __init__(self, pointLeft: Point, length: float, stroke: Stroke) -> None:
    #     super().__init__()
    #     self.pointLeft: Point = pointLeft
    #     self.length: float = length
    #     self.stroke: Stroke = stroke
    def __init__(self, pointLeft: Point, pointRight: Point, size: Size, stroke: Stroke) -> None:
        super().__init__()
        self.pointLeft: Point = pointLeft
        self.pointRight: Point = pointRight
        self.size: Size = size 
        self.stroke: Stroke = stroke

    def getpoints(self) -> list[Point]:
        offsetLeft: float = (self.pointRight.X - self.pointLeft.X - self.size.width) / 2.0
        # offsetRight: float = self.pointRight.X - self.pointLeft.X - self.size.width - offsetLeft
        springLeft: Point = self.pointLeft.addedPoint(offsetLeft, 0)
        springRight: Point = springLeft.addedPoint(self.size.width, 0)
        
        lenX: float = self.size.width / 14
        lenY: float = self.size.heigth / 2
        x: float = springLeft.X
        y: float = springLeft.Y
        points: list[Point] = []
        points.append(self.pointLeft) # P0
        points.append(springLeft) # P3
        points.append(Point(x + lenX * 1, y - lenY)) # P4
        points.append(Point(x + lenX * 3, y + lenY)) # P6
        points.append(Point(x + lenX * 5, y - lenY)) # P8
        points.append(Point(x + lenX * 7, y + lenY)) # P10
        points.append(Point(x + lenX * 9, y - lenY)) # P12
        points.append(Point(x + lenX * 11, y + lenY)) # P14
        points.append(Point(x + lenX * 13, y - lenY)) # P16
        points.append(springRight) # P17
        points.append(self.pointRight) # P20
        return points

    def getlines(self, points: list[Point]) -> list[Line]:
        lines: list[Line] = [Line(p1, p2, self.stroke) for p1, p2 in zip(points[:-1], points[1:])]
        return lines

    def get_text(self) -> str:
        points: list[Point] = self.getpoints()
        lines: list[Line] = self.getlines(points)
        txt: str = '\n'.join([line.get_text() for line in lines])
        return txt
