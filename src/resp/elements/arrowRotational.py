import sys
import os
sys.path.append(os.path.dirname(__file__))

from baseElement import BaseElement
from parts.point import Point
from parts.size import Size
from parts.fillstroke import FillStroke
from parts.path import Path
from parts.transform import Transform

class ArrowRotational(BaseElement):
    def __init__(self, origin: Point, radius: float, headSize: Size, stroke: FillStroke, angle: float) -> None:
        super().__init__()
        # self.pointStart: Point = pointStart
        # self.length: Point = length
        # self.headSize: Size = headSize
        self.transform: Transform = Transform()
        self.transform.rotate(origin, angle)

        self.pathCircle: Path = Path(stroke.get_fillnone())
        self.pathCircle.M(origin.X, origin.Y)
        self.pathCircle.m(0, -radius)
        self.pathCircle.a(radius, radius, False, False, False, 0, radius * 2)
        
        self.pathArrow: Path = Path(stroke)
        self.pathArrow.M(origin.X, origin.Y)
        self.pathArrow.m(0, radius)
        self.pathArrow.m(headSize.width * 0.7, 0)
        self.pathArrow.l(-headSize.width, -headSize.heigth / 2)
        self.pathArrow.v(headSize.heigth)
        self.pathArrow.Z()

    def get_text(self) -> str:
        lst: list[str] = []
        lst.append(f'<g {self.transform.get_text()}>')
        lst.append(self.pathCircle.get_text())
        lst.append(self.pathArrow.get_text())
        lst.append(f'</g>')
        txt: str = '\n'.join(lst)
        return txt
        