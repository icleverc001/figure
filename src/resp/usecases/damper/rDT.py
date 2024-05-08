import sys
import os
sys.path.append(os.path.dirname(__file__))

from resp.model import Model
# from resp.parts.point import Point
# from resp.parts.size import Size
# from resp.parts.stroke import Stroke
# from resp.parts.fillstroke import FillStroke
# from resp.parts.font import Font
# from resp.parts.viewbox import ViewBox
import iRDT

def getmodel() -> Model:
    model: Model = iRDT.getmodel()
    return model
