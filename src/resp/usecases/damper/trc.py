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
    points: list[Point] = [Point(i * 100 - 50, 0) for i in range(0, 4)]
    points.append(points[-1].addedPoint(50, 0))
    dis: float = 50
    point1H: Point = points[1].addedPoint(0, -dis)
    point1L: Point = points[1].addedPoint(0, dis)
    point3H: Point = points[3].addedPoint(0, -dis)
    point3L: Point = points[3].addedPoint(0, dis)
    
    springStroke: Stroke = Stroke('black', 1)
    model.spring(points[0], points[1], Size(50, 25), springStroke)
    model.spring(points[1], points[2], Size(50, 25), springStroke)
    model.spring(point1H, point3H, Size(50, 25), springStroke)

    model.dashpot(points[2].addedPoint(25, 0), 50, springStroke)
    model.line(points[2], points[2].addedPoint(25, 0), springStroke)
    model.line(points[3].addedPoint(-25, 0), points[3], springStroke)


    model.dashpot(point1L.addedPoint(75, 0), 50, springStroke)
    model.line(point1L, point1L.addedPoint(75, 0), springStroke)
    model.line(point3L.addedPoint(-75, 0), point3L, springStroke)
    
    model.line(point1H, point1L, springStroke)
    model.line(point3H, point3L, springStroke)
    model.line(points[2], points[4], springStroke)


    # Node
    masterNodeRadius: int = 2
    masterNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    model.circle(points[0], masterNodeRadius, masterNodeFillStroke)
    # model.circle(points[1], masterNodeRadius, masterNodeFillStroke)
    model.circle(points[4], masterNodeRadius, masterNodeFillStroke)
    # model.circle(point1H, masterNodeRadius, masterNodeFillStroke)
    # model.circle(point1L, masterNodeRadius, masterNodeFillStroke)
    # model.circle(point3H, masterNodeRadius, masterNodeFillStroke)
    # model.circle(point3L, masterNodeRadius, masterNodeFillStroke)

    # Text
    model.text(points[0].addedPoint(40, 35), "K0", Font('black', 14))
    model.text(points[1].addedPoint(40, 35), "K1", Font('black', 14))
    model.text(point1H.addedPoint(90, -25), "K2", Font('black', 14))
    model.text(points[2].addedPoint(40, 35), "C1", Font('black', 14))
    model.text(point1L.addedPoint(90, 35), "C2", Font('black', 14))


    return model
