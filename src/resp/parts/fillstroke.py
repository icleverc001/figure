from __future__ import annotations

import sys
import os
sys.path.append(os.path.dirname(__file__))

from stroke import Stroke

class FillStroke(Stroke):
    def __init__(self, fill_color: str, color: str, width: int) -> None:
        super().__init__(color, width)
        self.fill_color: str = fill_color
    
    def get_text(self) -> str:
        txt: str = f'fill="{self.fill_color}" {super().get_text()}'
        return txt
    
    def get_fillnone(self) -> FillStroke:
        tmp: FillStroke = FillStroke("none", self.color, self.width)
        return tmp