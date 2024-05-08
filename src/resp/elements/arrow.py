import sys
import os
sys.path.append(os.path.dirname(__file__))

from baseElement import BaseElement
from parts.point import Point
from parts.size import Size
from parts.fillstroke import FillStroke
from parts.path import Path

class Arrow(BaseElement):
    def __init__(self, pointStart: Point, length: float, headSize: Size, stroke: FillStroke, rotatePoint: Point, angle: float) -> None:
        super().__init__()
        # self.pointStart: Point = pointStart
        # self.length: Point = length
        # self.headSize: Size = headSize
        
        self.path: Path = Path(stroke)
        self.path.M(pointStart.X, pointStart.Y)
        self.path.h(length)
        self.path.l(-headSize.width, headSize.heigth / 2)
        self.path.v(-headSize.heigth)
        self.path.l(headSize.width, headSize.heigth / 2)
        self.path.Z()
        
        self.path.setRotate(rotatePoint, angle)

    def get_text(self) -> str:
        txt: str = f'{self.path.get_text()}'
        return txt
        

