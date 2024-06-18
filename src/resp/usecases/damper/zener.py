import sys
import os
sys.path.append(os.path.dirname(__file__))
from collections import deque

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
    points: list[Point] = [Point(i * 100, 0) for i in range(0, 3)]
    points.append(points[-1].addedPoint(40, 0))
    dis: float = 30
    point1H: Point = points[1].addedPoint(0, -dis)
    point1L: Point = points[1].addedPoint(0, dis)
    point2H: Point = points[2].addedPoint(0, -dis)
    point2L: Point = points[2].addedPoint(0, dis)

    springStroke: Stroke = Stroke('black', 1)
    model.spring(points[0], points[1], Size(50, 25), springStroke)
    model.spring(point1H, point2H, Size(50, 25), springStroke)

    model.dashpot(point1L, point2L, Size(18, 36), springStroke)
    # model.line(point1L, point1L.addedPoint(25, 0), springStroke)
    # model.line(point2L.addedPoint(-25, 0), point2L, springStroke)
    
    model.line(point1H, point1L, springStroke)
    model.line(point2H, point2L, springStroke)
    model.line(points[2], points[3], springStroke)


    # Node
    masterNodeRadius: int = 2
    masterNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    model.circle(points[0], masterNodeRadius, masterNodeFillStroke)
    model.circle(points[1], masterNodeRadius, masterNodeFillStroke)
    model.circle(points[3], masterNodeRadius, masterNodeFillStroke)
    model.circle(point1H, masterNodeRadius, masterNodeFillStroke)
    model.circle(point1L, masterNodeRadius, masterNodeFillStroke)
    model.circle(point2H, masterNodeRadius, masterNodeFillStroke)
    model.circle(point2L, masterNodeRadius, masterNodeFillStroke)

    # Text
    textFont: Font = Font('black', 14)
    model.text(points[0].addedPoint(40, 35), "K0", textFont)
    model.text(point1H.addedPoint(40, -25), "K1", textFont)
    model.text(point1L.addedPoint(40, 35), "C0", textFont)

    commentTextFont: Font = Font('black', 11)
    commentTextPoints: deque[Point] = deque([points[0].addedPoint(-20, 100 + i * 20) for i in range(0, 10)])
    model.text(commentTextPoints.popleft(), "※フォークトモデルに支持ばね(K0)が直列に取り付いた", commentTextFont)
    model.text(commentTextPoints.popleft(), "　線形モデルを設定します", commentTextFont)
    model.text(commentTextPoints.popleft(), "　K1の入力を省略した場合には、線形のマックスウェルモデル", commentTextFont)
    model.text(commentTextPoints.popleft(), "　となります", commentTextFont)
    model.text(commentTextPoints.popleft(), "※固有値解析に考慮するを指定した場合には", commentTextFont)
    model.text(commentTextPoints.popleft(), "　固有値解析において、K0とK1の直列ばねが考慮されます", commentTextFont)

    return model
