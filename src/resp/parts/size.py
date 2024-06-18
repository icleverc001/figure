from __future__ import annotations

class Size:
    def __init__(self, width: float, height: float) -> None:
        self.__width: float = width
        self.__height: float = height

    @property
    def width(self) -> float:
        return self.__width

    @property
    def heigth(self) -> float:
        return self.__height

    def get_text(self) -> str:
        txt: str = f'width="{self.__width}" height="{self.__height}"'
        return txt

    def addedSize(self, width: float, height: float) -> Size:
        return Size(self.__width + width, self.__height + height)
