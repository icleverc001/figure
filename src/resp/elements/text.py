import sys
import os
sys.path.append(os.path.dirname(__file__))

from parts.font import Font
from parts.point import Point
from baseElement import BaseElement


class Text(BaseElement):
    def __init__(self, point: Point, text: str, font: Font) -> None:
        super().__init__()
        self.point: Point = point
        self.text: str = text 
        self.font: Font = font

    def get_text(self) -> str:
        txt: str = f'<text {self.point.get_text_point()} {self.font.get_text()}>{self.text}</text>'
        return txt
        

