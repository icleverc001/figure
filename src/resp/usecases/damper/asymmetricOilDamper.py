import sys
import os
sys.path.append(os.path.dirname(__file__))

from resp.model import Model
from resp.parts.point import Point
from resp.parts.size import Size
from resp.parts.stroke import Stroke
from resp.parts.fillstroke import FillStroke
from resp.parts.font import Font
from resp.parts.viewbox import ViewBox

def getmodel() -> Model:
    model: Model = Model(Size(500, 400), ViewBox(Point(-100, -200), Size(500, 400)))

    # NodePoints
    points: list[Point] = [Point(i * 100, 0) for i in range(0, 3)]

    springLength: int = 100
    springStroke: Stroke = Stroke('black', 1)
    model.spring(points[0], points[1], Size(50, 25), springStroke)

    model.dashpot(points[1], points[2], Size(18, 36), springStroke)
    # model.line(points[1], points[1].addedPoint(25, 0), springStroke)
    # model.line(points[2].addedPoint(-25, 0), points[2], springStroke)
    
    # Node
    masterNodeRadius: int = 2
    masterNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    for p in points:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)

    # Text
    model.text(points[0].addedPoint(40, 35), "K0", Font('black', 14))
    model.text(points[1].addedPoint(40, 35), "C0", Font('black', 14))

    model.text(points[0].addedPoint(0, 80), "注）負側の定義を省略した場合は", Font('black', 14))
    model.text(points[0].addedPoint(0, 100), "　　正側と同じ(対称型)となります", Font('black', 14))
    model.text(points[0].addedPoint(0, 120), "注）折点が一つの対称型の場合は", Font('black', 14))
    model.text(points[0].addedPoint(0, 140), "　　オイルダンパーと同じ特性となります", Font('black', 14))

    return model
