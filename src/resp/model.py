import sys
import os
sys.path.append(os.path.dirname(__file__))

from elements.baseElement import BaseElement
from elements.text import Text
from elements.line import Line
from elements.arrow import Arrow
from elements.arrowRotational import ArrowRotational
from elements.arrowCurve import ArrowCurve
from elements.circle import Circle
from elements.spring import Spring
from elements.dashpot import Dashpot
from elements.frictionSpring import FrictionSpring
from elements.rotaryDamping import RotaryDamping
from elements.rotationalSpring import RotationalSpring
from elements.groundHorizontal import GroundHorizontal
from elements.groundVertical import GroundVertical
from elements.tower import Tower
from parts.point import Point
from parts.size import Size
from parts.stroke import Stroke
from parts.fillstroke import FillStroke
from parts.viewbox import ViewBox
from parts.font import Font

class Model:
    def __init__(self, size: Size, viewbox: ViewBox) -> None:
        self.size: Size = size
        self.viewbox: ViewBox = viewbox
        self.elements: list[BaseElement] = []

    def get_text(self) -> str:
        txt: str = f'<svg xmlns="http://www.w3.org/2000/svg" {self.size.get_text()} {self.viewbox.get_text()} style="margin: 0px auto;">\n'
        txt += "\n".join([elem.get_text() for elem in self.elements])
        txt += '\n</svg>'
        return txt
        

    def text(self, point: Point, text: str, font: Font):
        t: Text = Text(point, text, font)
        self.elements.append(t)

    def line(self, point1: Point, point2: Point, stroke: Stroke):
        l: Line = Line(point1, point2, stroke)
        self.elements.append(l)

    def arrow(self, pointStart: Point, length: float, headSize: Size, stroke: FillStroke, rotatePoint: Point, angle: float) -> None:
        a: Arrow = Arrow(pointStart, length, headSize, stroke, rotatePoint, angle)
        self.elements.append(a)

    def arrowRotational(self, origin: Point, radius: float, headSize: Size, stroke: FillStroke, angle: float) -> None:
        a: ArrowRotational = ArrowRotational(origin, radius, headSize, stroke, angle)
        self.elements.append(a)

    def arrowCurve(self, startPoint: Point, endPoint: Point, tmpPoint: Point, headSize: Size, stroke: FillStroke) -> None:
        a: ArrowCurve = ArrowCurve(startPoint, endPoint, tmpPoint, headSize, stroke)
        self.elements.append(a)
    
    def circle(self, origin: Point, radius: float, fillstroke: FillStroke):
        c: Circle = Circle(origin, radius, fillstroke)
        self.elements.append(c)
    
    def spring(self, pointleft: Point, pointright: Point, size: Size, stroke: Stroke):
        s: Spring = Spring(pointleft, pointright, size, stroke)
        self.elements.append(s)
    
    def groundHorizontal(self, pointLeft: Point, length: float, thickness: float, stroke: Stroke):
        g: GroundHorizontal = GroundHorizontal(pointLeft, length, thickness, stroke)
        self.elements.append(g)

    def groundVertical(self, pointbottom: Point, length: float, thickness: float, stroke: Stroke):
        g: GroundVertical = GroundVertical(pointbottom, length, thickness, stroke)
        self.elements.append(g)

    def dashpot(self, pointLeft: Point, pointRight: Point, size: Size, stroke: Stroke):
        d: Dashpot = Dashpot(pointLeft, pointRight, size, stroke)
        self.elements.append(d)
        
    def rotationalSpring(self, origin: Point, radius: float, stroke: FillStroke, startRadian: float = 0, aspectRatioY: float = 1) -> RotationalSpring:
        r: RotationalSpring = RotationalSpring(origin, radius, stroke, startRadian=startRadian, aspectRatioY=aspectRatioY)
        self.elements.append(r)
        return r
    
    def rotaryDamping(self, pointleft: Point, pointright: Point, radius: float, fillstroke: FillStroke):
        r: RotaryDamping = RotaryDamping(pointleft, pointright, radius, fillstroke)
        self.elements.append(r)

    def frictionSpring(self, pointleft: Point, pointright: Point, radius: float, fillstroke: FillStroke):
        f: FrictionSpring = FrictionSpring(pointleft, pointright, radius, fillstroke)
        self.elements.append(f)

    def tower(self, pointTop: Point, pointBottom: Point, offsetX: int, offsetY: int, stroke: Stroke):
        t: Tower = Tower(pointTop=pointTop, pointBottom=pointBottom, offsetX=offsetX, offsetY=offsetY, stroke=stroke)
        self.elements.append(t)

