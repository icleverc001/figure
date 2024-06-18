class Stroke:
    def __init__(self, color: str, width: int, dasharray: list[int] = []) -> None:
        self.color: str = color
        self.width: int = width
        self.dasharray: list[int] = dasharray
    
    def get_text(self) -> str:
        txt = f'stroke="{self.color}" stroke-width="{self.width}"'
        if self.dasharray:
            tmp = ' '.join([f'{x}' for x in self.dasharray])
            txt += f' stroke-dasharray="{tmp}"'
        return txt