import os
from pathlib import Path
# import sys

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


# args = sys.argv

def output(filename: str):
    filename_without_ext = os.path.splitext(filename)
    abspath = Path(filename).absolute()
    print('cwd', Path.cwd())
    print('abspath', abspath)
    print(os.path.exists(filename))
    print(filename)
    print(filename_without_ext)

    # drawing = svg2rlg(filename)
    # renderPDF.drawToFile(drawing, filename_without_ext + ".pdf")
    drawing = svg2rlg(filename)
    renderPM.drawToFile(drawing, filename_without_ext[0] + ".png", fmt="PNG")
