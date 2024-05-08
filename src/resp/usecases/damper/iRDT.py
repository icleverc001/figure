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
    model: Model = Model(Size(500, 400), ViewBox(Point(-100, -100), Size(500, 400)))

    # NodePoints
    points: list[Point] = [Point(i * 100, 0) for i in range(0, 4)]
    points.insert(0, points[0].addedPoint(-50, 0))
    dis: float = 30
    point1H: Point = points[1].addedPoint(0, -dis)
    point1L: Point = points[1].addedPoint(0, dis)
    point2H: Point = points[2].addedPoint(0, -dis)
    point2L: Point = points[2].addedPoint(0, dis)

    springStroke: Stroke = Stroke('black', 1)
    model.spring(points[3], points[4], Size(50, 25), springStroke)
    # model.spring(point1L, point2L, Size(50, 25), springStroke)

    model.dashpot(point1H.addedPoint(25, 0), 50, springStroke)
    model.line(point1H, point1H.addedPoint(25, 0), springStroke)
    model.line(point2H.addedPoint(-25, 0), point2H, springStroke)
    
    rotaryDampingFillStroke: FillStroke = FillStroke('black', 'black', 1)
    model.rotaryDamping(point1L, point2L, 15, rotaryDampingFillStroke)
    
    frictionSpringFillStroke: FillStroke = FillStroke('black', 'black', 1)
    model.frictionSpring(points[2], points[3], 15, frictionSpringFillStroke)
    
    model.line(points[0], points[1], springStroke)
    model.line(point1H, point1L, springStroke)
    model.line(point2H, point2L, springStroke)
    # model.line(point1L, point2L, springStroke)
    # model.line(points[2], points[3], springStroke)


    # Node
    masterNodeRadius: int = 2
    masterNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    model.circle(points[0], masterNodeRadius, masterNodeFillStroke)
    model.circle(points[1], masterNodeRadius, masterNodeFillStroke)
    model.circle(points[2], masterNodeRadius, masterNodeFillStroke)
    model.circle(points[3], masterNodeRadius, masterNodeFillStroke)
    model.circle(points[4], masterNodeRadius, masterNodeFillStroke)

    # Text
    textFont: Font = Font('black', 14)
    model.text(point1H.addedPoint(40, -25), "Cd", textFont)
    model.text(point1L.addedPoint(40, 35), "Md", textFont)
    model.text(points[2].addedPoint(40, 35), "Fr", textFont)
    model.text(points[3].addedPoint(40, 35), "Kd", textFont)
    
    commentLineStroke: Stroke =  Stroke('black', 1)
    point0LL: Point = points[0].addedPoint(0, 100)
    point2LL: Point = points[2].addedPoint(0, 140)
    point3LL: Point = points[3].addedPoint(0, 100)
    point4LL: Point = points[4].addedPoint(0, 140)
    model.line(point0LL, point3LL, commentLineStroke)
    model.line(point2LL, point4LL, commentLineStroke)
    model.line(point0LL, point0LL.addedPoint(0, -10), commentLineStroke)
    model.line(point3LL, point3LL.addedPoint(0, -10), commentLineStroke)
    model.line(point2LL, point2LL.addedPoint(0, -10), commentLineStroke)
    model.line(point4LL, point4LL.addedPoint(0, -10), commentLineStroke)

    commentTextFont: Font = Font('black', 14)
    model.text(point0LL.addedPoint(60, 25), "回転滑り", commentTextFont)
    model.text(point2LL.addedPoint(60, 25), "支持部材降伏", commentTextFont)

    return model
