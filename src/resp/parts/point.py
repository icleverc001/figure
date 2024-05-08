from __future__ import annotations

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.__x: float = x
        self.__y: float = y
    
    @property
    def X(self) -> float:
        return self.__x

    @property
    def Y(self) -> float:
        return self.__y

    def get_text_point(self) -> str:
        txt:str = f'x="{self.__x}" y="{self.__y}"'
        return txt
    
    def get_text_point1(self) -> str:
        txt:str = f'x1="{self.__x}" y1="{self.__y}"'
        return txt
    
    def get_text_point2(self) -> str:
        txt:str = f'x2="{self.__x}" y2="{self.__y}"'
        return txt

    def addedPoint(self, x: float, y: float) -> Point:
        return Point(self.__x + x, self.__y + y)

# assert Point.add.__annotations__ == {
#     'addPoint': 'Point'
# }