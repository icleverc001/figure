import sys
import os
sys.path.append(os.path.dirname(__file__))
import math

import numpy as np

from baseElement import BaseElement
from parts.point import Point
from parts.size import Size
from parts.fillstroke import FillStroke
from parts.path import Path
from parts.transform import Transform

class ArrowCurve(BaseElement):
    def __init__(self, startPoint: Point, endPoint: Point, tmpPoint: Point, headSize: Size, stroke: FillStroke) -> None:
        super().__init__()
        # self.pointStart: Point = pointStart
        # self.length: Point = length
        # self.headSize: Size = headSize
        # self.transform: Transform = Transform()
        # self.transform.rotate(origin, angle)

        self.pathCurve: Path = Path(stroke.get_fillnone())
        self.pathCurve.M(startPoint.X, startPoint.Y)
        self.pathCurve.Q(tmpPoint.X, tmpPoint.Y, endPoint.X, endPoint.Y)
        
        # self.pathArrowStart: Path = self.get_arrow(startPoint, tmpPoint, headSize, stroke.get_dashnone())
        self.pathArrowEnd: Path = self.get_arrow(endPoint, tmpPoint, headSize, stroke.get_dashnone())

    def get_arrow(self, startPoint: Point, tmpPoint: Point, headSize: Size, stroke: FillStroke) -> Path:
        arrow: Path = Path(stroke.get_dashnone())
        theta: float = math.atan2(startPoint.Y - tmpPoint.Y, startPoint.X - tmpPoint.X)
        r = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        
        arrow.M(startPoint.X, startPoint.Y)
        # arrow.m(headSize.width * 0.7 * math.cos(theta), headSize.width * 0.7 * math.sin(theta))
        _a = np.array([headSize.width * 0.7, 0])
        a = np.dot(r, _a)
        arrow.m(a[0], a[1])
        _a = np.array([-headSize.width, -headSize.heigth / 2])
        a = np.dot(r, _a)
        arrow.l(a[0], a[1])
        _a = np.array([0, headSize.heigth])
        a = np.dot(r, _a)
        arrow.l(a[0], a[1])
        arrow.Z()
        
        return arrow

    def get_text(self) -> str:
        lst: list[str] = []
        lst.append(f'<g>')
        lst.append(self.pathCurve.get_text())
        # lst.append(self.pathArrowStart.get_text())
        lst.append(self.pathArrowEnd.get_text())
        lst.append(f'</g>')
        txt: str = '\n'.join(lst)
        return txt
        