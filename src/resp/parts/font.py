class Font:
    def __init__(self, color: str, fontsize: int) -> None:
        self.color: str = color
        self.fontsize: int = fontsize
    
    def get_text(self) -> str:
        txt = f'fill="{self.color}" font-size="{self.fontsize}"'
        return txt