import sys
import os
sys.path.append(os.path.dirname(__file__))

from point import Point
from size import Size

class ViewBox:
    def __init__(self, startpoint: Point, boxsize: Size) -> None:
        self.__startpoint: Point = startpoint
        self.__boxsize: Size = boxsize
        
    @property
    def startpoint(self) -> Point:
        return self.__startpoint
    
    @property
    def boxsize(self) -> Size:
        return self.__boxsize
    
    def get_text(self) -> str:
        txt = f'viewBox="{self.__startpoint.X} {self.__startpoint.Y} {self.__boxsize.width} {self.__boxsize.heigth}"'
        return txt