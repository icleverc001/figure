import sys
import os
sys.path.append(os.path.dirname(__file__))

from point import Point

class Transform:
    def __init__(self) -> None:
        self.elems: list[TransformElem] = []
    
    def get_text(self) -> str:
        txt: str = f'transform="{" ".join([elem.get_text() for elem in self.elems])}"' if len(self.elems) > 0 else ''
        return txt
    
    def rotate(self, point: Point, angle: float) -> None:
        self.elems.append(Rotate(point, angle))


class TransformElem:
    def __init__(self) -> None:
        pass
    
    def get_text(self) -> str:
        raise Exception("Sub classで実装")
        

class Rotate(TransformElem):
    def __init__(self, point: Point, angle: float) -> None:
        super().__init__()
        self.point: Point = point
        self.angle: float = angle

    def get_text(self) -> str:
        txt: str = f'rotate({self.angle}, {self.point.X}, {self.point.Y})'
        return txt

