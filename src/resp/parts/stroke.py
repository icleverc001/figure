class Stroke:
    def __init__(self, color: str, width: int) -> None:
        self.color: str = color
        self.width: int = width
    
    def get_text(self) -> str:
        txt = f'stroke="{self.color}" stroke-width="{self.width}"'
        return txt