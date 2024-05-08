import sys
import os
sys.path.append(os.path.dirname(__file__))

from baseElement import BaseElement
from parts.point import Point
from parts.fillstroke import FillStroke

class Circle(BaseElement):
    def __init__(self, origin: Point, radius: float, fill_stroke: FillStroke) -> None:
        super().__init__()
        self.origin:Point = origin
        self.radius: float = radius
        self.fill_stroke: FillStroke = fill_stroke
    
    def get_text(self) -> str:
        txt: str = f'<circle cx="{self.origin.X}" cy="{self.origin.Y}" r="{self.radius}" {self.fill_stroke.get_text()}></circle>'
        return txt


# <circle cx="0" cy="-100" r="10" fill="white" stroke="black" stroke-width="2"></circle>