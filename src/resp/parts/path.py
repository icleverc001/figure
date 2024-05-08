import sys
import os
sys.path.append(os.path.dirname(__file__))

from fillstroke import FillStroke
from transform import Transform
from point import Point

class Path:
    def __init__(self, stroke: FillStroke) -> None:
        self.stroke: FillStroke = stroke
        self.elems: list[PathElem] = []
        self.transform: Transform = Transform()
    
    def get_text(self) -> str:
        txt: str = f'<path d="{" ".join([elem.get_text() for elem in self.elems])}" {self.stroke.get_text()} {self.transform.get_text()}/>'
        return txt
    
    def setRotate(self, point: Point, angle: float) -> None:
        self.transform.rotate(point, angle)
    
    def M(self, x: float, y: float) -> None:
        self.elems.append(M(x, y))

    def m(self, x: float, y: float) -> None:
        self.elems.append(M(x, y, True))
    
    def L(self, x: float, y: float) -> None:
        self.elems.append(L(x, y))

    def l(self, x: float, y: float) -> None:
        self.elems.append(L(x, y, True))
    
    def H(self, x: float) -> None:
        self.elems.append(H(x))

    def h(self, x: float) -> None:
        self.elems.append(H(x, True))
    
    def V(self, y: float) -> None:
        self.elems.append(V(y))

    def v(self, y: float) -> None:
        self.elems.append(V(y, True))
    
    def A(self, rx: float, ry: float, xAxisRotation: bool, largeArcFlag: bool, sweepFlag: bool, x:float, y: float) -> None:
        self.elems.append(A(rx, ry, xAxisRotation, largeArcFlag, sweepFlag, x, y))
    
    def a(self, rx: float, ry: float, xAxisRotation: bool, largeArcFlag: bool, sweepFlag: bool, x:float, y: float) -> None:
        self.elems.append(A(rx, ry, xAxisRotation, largeArcFlag, sweepFlag, x, y, True))

    def Z(self) -> None:
        self.elems.append(Z())

    def z(self) -> None:
        self.elems.append(Z(True))

class PathElem:
    def __init__(self) -> None:
        pass
    
    def get_text(self) -> str:
        raise Exception("Sub classで実装")
        

class M(PathElem):
    def __init__(self, x: float, y: float, isRelative: bool = False) -> None:
        super().__init__()
        self.__x: float = x
        self.__y: float = y
        self.__isRelative: bool = isRelative

    def get_text(self) -> str:
        cmd: str = 'm' if self.__isRelative else 'M'
        txt: str = f'{cmd} {self.__x} {self.__y}'
        return txt

class L(PathElem):
    def __init__(self, x: float, y: float, isRelative: bool = False) -> None:
        super().__init__()
        self.__x: float = x
        self.__y: float = y
        self.__isRelative: bool = isRelative

    def get_text(self) -> str:
        cmd: str = 'l' if self.__isRelative else 'L'
        txt: str = f'{cmd} {self.__x} {self.__y}'
        return txt

class H(PathElem):
    def __init__(self, x: float, isRelative: bool = False) -> None:
        super().__init__()
        self.__x: float = x
        self.__isRelative: bool = isRelative

    def get_text(self) -> str:
        cmd: str = 'h' if self.__isRelative else 'H'
        txt: str = f'{cmd} {self.__x}'
        return txt

class V(PathElem):
    def __init__(self, y: float, isRelative: bool = False) -> None:
        super().__init__()
        self.__y: float = y
        self.__isRelative: bool = isRelative

    def get_text(self) -> str:
        cmd: str = 'v' if self.__isRelative else 'V'
        txt: str = f'{cmd} {self.__y}'
        return txt

class A(PathElem):
    def __init__(self, rx: float, ry: float, xAxisRotation: bool, largeArcFlag: bool, sweepFlag: bool, x:float, y: float, isRelative: bool = False) -> None:
        super().__init__()
        self.rx: float = rx
        self.ry: float = ry
        self.xAxisRotation: bool = xAxisRotation
        self.largeArcFlag: bool = largeArcFlag
        self.sweepFlag: bool = sweepFlag
        self.x: float = x
        self.y: float = y
        self.__isRelative: bool = isRelative

    def get_text(self) -> str:
        cmd: str = 'a' if self.__isRelative else 'A'
        txt: str = f'{cmd} {self.rx} {self.ry} {int(self.xAxisRotation)} {int(self.largeArcFlag)} {int(self.sweepFlag)} {self.x} {self.y}'
        return txt


class Z(PathElem):
    def __init__(self, isRelative: bool = False) -> None:
        super().__init__()
        self.__isRelative: bool = isRelative

    def get_text(self) -> str:
        cmd: str = 'z' if self.__isRelative else 'Z'
        txt: str = f'{cmd}'
        return txt
