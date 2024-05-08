from parts.point import Point
from parts.stroke import Stroke
from elements.line import Line
from baseElement import BaseElement
import sys
import os
sys.path.append(os.path.dirname(__file__))


class Dashpot(BaseElement):
    def __init__(self, pointLeft: Point, length: float, stroke: Stroke) -> None:
        super().__init__()
        self.pointLeft: Point = pointLeft
        self.length: float = length
        self.stroke: Stroke = stroke

    def getlines(self) -> list[Line]:
        lenX: float = self.length / 6
        lenY: float = lenX

        p0: Point = self.pointLeft
        p2: Point = self.getAddedPoint(p0, x=lenX * 2)
        p2t: Point = self.getAddedPoint(p2, y=-lenY * 2)
        p2b: Point = self.getAddedPoint(p2, y=lenY * 2)
        p3: Point = self.getAddedPoint(p2, x=lenX)
        p3t: Point = self.getAddedPoint(p3, y=-lenY)
        p3b: Point = self.getAddedPoint(p3, y=lenY)
        p4: Point = self.getAddedPoint(p3, x=lenX)
        p4t: Point = self.getAddedPoint(p4, y=-lenY * 2)
        p4b: Point = self.getAddedPoint(p4, y=lenY * 2)
        p6: Point = self.getAddedPoint(p4, x=lenX * 2)

        elements: list[Line] = []
        elements.append(Line(p0, p2, self.stroke))
        elements.append(Line(p2t, p2b, self.stroke))
        elements.append(Line(p2t, p4t, self.stroke))
        elements.append(Line(p2b, p4b, self.stroke))
        elements.append(Line(p3t, p3b, self.stroke))
        elements.append(Line(p3, p6, self.stroke))
        
        return elements

    def get_text(self) -> str:
        lines: list[Line] = self.getlines()
        txt: str = '\n'.join([line.get_text() for line in lines])
        return txt
