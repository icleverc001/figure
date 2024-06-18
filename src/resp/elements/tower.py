import sys
import os
sys.path.append(os.path.dirname(__file__))

from baseElement import BaseElement
from parts.point import Point
from parts.size import Size
from parts.stroke import Stroke
import services.utilities as Utils

class Tower(BaseElement):
    def __init__(self, pointTop: Point, pointBottom: Point, offsetX: int, offsetY: int, stroke: Stroke) -> None:
        super().__init__()
        self.pointTop: Point = pointTop
        self.pointBottom: Point = pointBottom
        self.offsetX: int = offsetX
        self.offsetY: int = offsetY
        self.stroke: Stroke = stroke

    def get_text(self) -> str:
        startPoint: Point = self.pointTop.addedPoint(-self.offsetX, -self.offsetY)
        size: Size = Utils.get_size(self.pointBottom, self.pointTop)
        txt: str = f'<rect {startPoint.get_text_point()} {size.addedSize(self.offsetX * 2, self.offsetY * 2).get_text()} {self.stroke.get_text()} fill="transparent"></rect>'
        return txt
        

