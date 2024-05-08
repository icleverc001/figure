import sys
import os
sys.path.append(os.path.dirname(__file__))
import math

from elements.line import Line
from parts.stroke import Stroke
from parts.point import Point
from baseElement import BaseElement


class RotationalSpring(BaseElement):
    # def __init__(self, origin: Point, radius: float, stroke: Stroke) -> None:
    #     super().__init__()
    #     self.origin: Point = origin
    #     self.radius: float = radius
    #     self.stroke: Stroke = stroke
    def __init__(self, pointTop: Point, length: float, stroke: Stroke) -> None:
        super().__init__()
        self.pointTop: Point = pointTop
        self.length: float = length
        self.origin: Point = Point(pointTop.X, pointTop.Y - length / 2)
        self.radius: float = length / 4
        self.stroke: Stroke = stroke

    def getTmpPoints(self) -> list[Point]:
        radius: float = self.radius
        ori: Point = self.origin
        
        c_rate = 50
        last_line_rate = 0.2
        
        len_rate = (1 - last_line_rate) / (11 * c_rate) 
        ang_rate = -math.pi / (2 * c_rate)
        
        
        rng = range(0, 10 * c_rate)
        dxs =[math.sin(ang_rate * i) * radius * (1-len_rate*i) + ori.X for i in rng]
        dys =[-math.cos(ang_rate * i) * radius * (1-len_rate*i) - ori.Y for i in rng]
        
        
        points = [Point(x,y) for x, y in zip(dxs, dys)]
        return points
    
    def getlines(self, points: list[Point]) -> list[Line]:
        lines: list[Line] = [Line(p1, p2, self.stroke) for p1, p2 in zip(points[:-1], points[1:])]
        return lines

    def get_text(self) -> str:
        points: list[Point] = self.getTmpPoints()
        lines: list[Line] = self.getlines(points)
        lines.append(Line(points[0], self.pointTop, self.stroke))
        lines.append(Line(points[-1], Point(self.pointTop.X, self.pointTop.Y + self.length), self.stroke))
        txt: str = '\n'.join([line.get_text() for line in lines])
        return txt
