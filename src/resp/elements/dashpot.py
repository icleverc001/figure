from parts.point import Point
from parts.size import Size
from parts.stroke import Stroke
from elements.line import Line
from baseElement import BaseElement
import services.utilities as Utils
import sys
import os
sys.path.append(os.path.dirname(__file__))


class Dashpot(BaseElement):
    # def __init__(self, pointLeft: Point, length: float, stroke: Stroke) -> None:
    #     super().__init__()
    #     self.pointLeft: Point = pointLeft
    #     self.length: float = length
    #     self.stroke: Stroke = stroke
        
    #     self.lenX: float = length / 6
    #     self.lenY: float = self.lenX
        
        
    def __init__(self, pointLeft: Point, pointRight: Point, size: Size, stroke: Stroke) -> None:
        super().__init__()
        self.pointLeft: Point = pointLeft
        self.pointRight: Point = pointRight
        self.size: Size = size
        self.stroke: Stroke = stroke
        

    # def getlines(self) -> list[Line]:
    #     lenX: float = self.length / 6
    #     lenY: float = lenX

    #     p0: Point = self.pointLeft
    #     p2: Point = self.getAddedPoint(p0, x=lenX * 2)
    #     p2t: Point = self.getAddedPoint(p2, y=-lenY * 2)
    #     p2b: Point = self.getAddedPoint(p2, y=lenY * 2)
    #     p3: Point = self.getAddedPoint(p2, x=lenX)
    #     p3t: Point = self.getAddedPoint(p3, y=-lenY)
    #     p3b: Point = self.getAddedPoint(p3, y=lenY)
    #     p4: Point = self.getAddedPoint(p3, x=lenX)
    #     p4t: Point = self.getAddedPoint(p4, y=-lenY * 2)
    #     p4b: Point = self.getAddedPoint(p4, y=lenY * 2)
    #     p6: Point = self.getAddedPoint(p4, x=lenX * 2)

    #     elements: list[Line] = []
    #     elements.append(Line(p0, p2, self.stroke))
    #     elements.append(Line(p2t, p2b, self.stroke))
    #     elements.append(Line(p2t, p4t, self.stroke))
    #     elements.append(Line(p2b, p4b, self.stroke))
    #     elements.append(Line(p3t, p3b, self.stroke))
    #     elements.append(Line(p3, p6, self.stroke))
        
    #     return elements

    def getlines(self) -> list[Line]:
        pS = self.pointLeft
        pE = self.pointRight
        
        pC: Point = Utils.get_center_point(pS, pE)
        pCt: Point = pC.addedPoint(0, -self.size.heigth / 4)
        pCb: Point = pC.addedPoint(0, self.size.heigth / 4)
        
        pL: Point = pC.addedPoint(-self.size.width / 2, 0)
        pLt: Point = pL.addedPoint(0, -self.size.heigth / 2)
        pLb: Point = pL.addedPoint(0, self.size.heigth / 2)
        pRt: Point = pLt.addedPoint(self.size.width, 0)
        pRb: Point = pLb.addedPoint(self.size.width, 0)
        
        elements: list[Line] = []
        elements.append(Line(pS, pL, self.stroke))
        elements.append(Line(pLt, pLb, self.stroke))
        elements.append(Line(pLt, pRt, self.stroke))
        elements.append(Line(pLb, pRb, self.stroke))
        elements.append(Line(pCt, pCb, self.stroke))
        elements.append(Line(pC, pE, self.stroke))
        
        return elements

    def get_text(self) -> str:
        lines: list[Line] = self.getlines()
        txt: str = '\n'.join([line.get_text() for line in lines])
        return txt
