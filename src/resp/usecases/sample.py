import sys
import os
sys.path.append(os.path.dirname(__file__))

from resp.model import Model
from resp.parts.point import Point
from resp.parts.size import Size
from resp.parts.stroke import Stroke
from resp.parts.fillstroke import FillStroke
from resp.parts.viewbox import ViewBox

def getmodel() -> Model:
    model: Model = Model(Size(500, 500), ViewBox(Point(-100, -400), Size(500, 500)))

    model.line(Point(0, 0), Point(0, -100), Stroke('black', 3))
    model.line(Point(80, -100), Point(80, -200), Stroke('black', 3))
    model.line(Point(140, -200), Point(140, -260), Stroke('black', 3))
    model.line(Point(200, -260), Point(200, -320), Stroke('black', 3))

    model.groundHorizontal(Point(-50, 50), 100, 15, Stroke('black', 2))
    model.groundVertical(Point(-50, 50), 100, 15, Stroke('black', 2))

    model.circle(Point(0, -100), 10, FillStroke('white', 'black', 2))
    model.circle(Point(80, -200), 10, FillStroke('white', 'black', 2))
    model.circle(Point(140, -260), 10, FillStroke('white', 'black', 2))
    model.circle(Point(200, -320), 10, FillStroke('white', 'black', 2))

    model.spring(Point(-50, 0), Point(0, 0), Size(60, 30), Stroke('blue', 1))
    # model.spring(Point(20, -120), 50, Stroke('blue', 1))
    # model.spring(Point(90, -200), 50, Stroke('blue', 1))
    model.dashpot(Point(20, -80), 50, Stroke('blue', 1))
    model.dashpot(Point(150, -260), 50, Stroke('blue', 1))
    model.line(Point(10, -100), Point(20, -100), Stroke('blue', 1))
    model.line(Point(70, -100), Point(80, -100), Stroke('blue', 1))
    model.line(Point(20, -80), Point(20, -120), Stroke('blue', 1))
    model.line(Point(70, -80), Point(70, -120), Stroke('blue', 1))

    model.rotationalSpring(Point(0, 0), 50, Stroke('black', 1))

    return model
