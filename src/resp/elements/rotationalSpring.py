import sys
import os
sys.path.append(os.path.dirname(__file__))
import math

# import numpy as np

from elements.line import Line
from parts.path import Path
from parts.fillstroke import FillStroke
from parts.point import Point
from baseElement import BaseElement


class RotationalSpring(BaseElement):
    def __init__(self, origin: Point, radius: float, stroke: FillStroke, startRadian: float = 0, aspectRatioY: float = 1) -> None:
        super().__init__()
        self.origin: Point = origin
        self.radius: float = radius
        self.stroke: FillStroke = stroke
        self.startRadian: float = startRadian
        self.aspectRatioY: float = aspectRatioY
        self.path: Path = self.getPath()

    @property
    def StartPoint(self) -> Point:
        return self.startPoint

    @property
    def EndPoint(self) -> Point:
        return self.endPoint

        
    # def __init__(self, pointTop: Point, length: float, stroke: Stroke) -> None:
    #     super().__init__()
    #     self.pointTop: Point = pointTop
    #     self.length: float = length
    #     self.origin: Point = Point(pointTop.X, pointTop.Y - length / 2)
    #     self.radius: float = length / 4
    #     self.stroke: Stroke = stroke

    def getPath(self) -> Path:
        radius: float = self.radius
        ori: Point = self.origin
        
        piDiv: int = 40 # 半周の分割数
        piNum: int = 5 # 半周の繰返し数
        pointNum: int = piDiv * piNum
        rng = range(0, pointNum)
        
        lastLength: float = 0.2
        
        dxs = [radius * (1 - (1 - lastLength) * i / pointNum) * math.cos(self.startRadian + math.pi * (i / piDiv)) for i in rng]
        dys = [radius * self.aspectRatioY * (1 - (1 - lastLength) * i / pointNum) * math.sin(self.startRadian + math.pi * (i / piDiv)) for i in rng]
        # dxs = [radius * (1 - (1 - lastLength) * i / pointNum) * math.sin(math.pi * (0.5 + i / piDiv)) for i in rng]
        # dys = [radius * (1 - (1 - lastLength) * i / pointNum) * math.cos(math.pi * (0.5 + i / piDiv)) for i in rng]

        path: Path = Path(self.stroke)
        self.startPoint: Point = Point(ori.X + dxs[0], ori.Y - dys[0])
        path.M(self.startPoint.X, self.startPoint.Y)
        for x, y in zip(dxs, dys):
            self.endPoint: Point = Point(ori.X + x, ori.Y - y)
            path.L(self.endPoint.X, self.endPoint.Y)

        return path
    
    def get_text(self) -> str:
        # lines.append(Line(points[0], self.pointTop, self.stroke))
        # lines.append(Line(points[-1], Point(self.pointTop.X, self.pointTop.Y + self.length), self.stroke))
        txt: str = self.path.get_text()
        return txt
