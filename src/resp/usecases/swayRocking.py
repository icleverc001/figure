import sys
import os
sys.path.append(os.path.dirname(__file__))
import math

from resp.model import Model
from resp.parts.point import Point
from resp.parts.size import Size
from resp.parts.stroke import Stroke
from resp.parts.fillstroke import FillStroke
from resp.parts.font import Font
from resp.parts.viewbox import ViewBox
from elements.rotationalSpring import RotationalSpring
import services.utilities as Utils

def getmodel() -> Model:
    model: Model = Model(Size(500, 540), ViewBox(Point(-200, -350), Size(500, 540)))

    # NodePoints
    masterPoints: list[Point] = [Point(100, -(i + 1) * 100) for i in range(0, 3)]
    # slavePoints: list[Point] = [Point((i + 1) * 100, -(i + 1) * 100) for i in range(0, 1)]
    basePoint: Point = Point(0, -100)
    srPoint: Point = Point(0, 0)
    
    # Frame
    frameStroke: Stroke = Stroke('black', 3)
    # model.line(masterPoints[0], basePoint, frameStroke)
    for t, b in zip(masterPoints[1:], masterPoints[:-1]):
        model.line(b, t, frameStroke)

    model.groundHorizontal(Point(-40, 5), 80, 10, Stroke('black', 2))
    # model.groundVertical(Point(20, 25), 20, 10, Stroke('black', 2))

    # spring
    springLength: int = 100
    springStroke: Stroke = Stroke('blue', 1)
    # model.spring(basePoint, masterPoints[0], Size(50, 25), springStroke)
    baseLineStroke: Stroke = Stroke('black', 2, dasharray=[3, 3])
    model.line(basePoint, masterPoints[0], baseLineStroke)

    tmpPointCenter: Point = Point(basePoint.X, (srPoint.Y + masterPoints[0].Y) / 2)
    tmpPointLeft: Point = Point(basePoint.X - (masterPoints[0].X - basePoint.X) / 2, tmpPointCenter.Y)
    tmpPointRight: Point = Point(basePoint.X + (masterPoints[0].X - basePoint.X) / 2, tmpPointCenter.Y)
    
    # model.dashpot(Point(150, -260), 50, Stroke('blue', 1))
    model.spring(tmpPointCenter, tmpPointRight, Size(25, 20), Stroke('blue', 1))
    model.line(srPoint, tmpPointCenter, springStroke)
    model.line(basePoint, tmpPointRight, springStroke)

    rotSpr: RotationalSpring = model.rotationalSpring(tmpPointLeft, 15, FillStroke('none', springStroke.color, springStroke.width), startRadian=math.pi / 2)
    model.line(srPoint, rotSpr.EndPoint, springStroke)
    model.line(basePoint, rotSpr.StartPoint, springStroke)

    # Node
    masterNodeRadius: int = 5
    masterNodeFillStroke: FillStroke = FillStroke('white', 'black', 2)
    slaveNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    for p in masterPoints:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    # for p in slavePoints:
    #     model.circle(p, masterNodeRadius, slaveNodeFillStroke)
    model.circle(basePoint, masterNodeRadius, slaveNodeFillStroke)
    model.circle(srPoint, masterNodeRadius, slaveNodeFillStroke)
    
    # Tower
    towerStroke: Stroke = Stroke('black', 2, dasharray=[10, 5])
    model.tower(pointTop=masterPoints[-1], pointBottom=masterPoints[0], offsetX=15, offsetY=15, stroke=towerStroke)
    
    # 矢印
    arrowOffset: int = 22
    arrowFillStroke: FillStroke = FillStroke('black', 'black', 1)
    arrowStartPoint: Point = tmpPointRight.addedPoint(arrowOffset, 0)
    arrowHeadSize: Size = Size(10, 10)
    lengthNodeSR: int = abs(srPoint.Y - arrowStartPoint.Y)
    lengthNodeBase: int = abs(basePoint.Y - arrowStartPoint.Y)
    model.arrow(arrowStartPoint, lengthNodeSR, arrowHeadSize, arrowFillStroke, arrowStartPoint, 90)
    model.arrow(arrowStartPoint, lengthNodeBase, arrowHeadSize, arrowFillStroke, arrowStartPoint, -90)
    # 括弧
    parenthesesStroke: Stroke = Stroke('black', 1)
    parenthesesOffset: int = 20
    parenthesesLength: int = abs(srPoint.Y - basePoint.Y)
    parenthesesPoint: Point = arrowStartPoint.addedPoint(parenthesesOffset, 0)
    parenthesesPointBottom: Point = parenthesesPoint.addedPoint(0, parenthesesLength)
    model.line(arrowStartPoint, parenthesesPoint, parenthesesStroke)
    model.line(parenthesesPoint, parenthesesPointBottom, parenthesesStroke)

    # Text
    textFont: Font = Font('black', 14)
    model.text(srPoint.addedPoint(10, -5), "NodeSR", textFont)
    model.text(basePoint.addedPoint(-30, -15), "NodeBase", textFont)
    
    model.text(parenthesesPointBottom.addedPoint(-180, 20), "NodeSRとNodeBase間の距離は解析に影響しない", textFont)
    model.text(parenthesesPointBottom.addedPoint(-180, 40), "（剛梁がついていないため）", textFont)
    # model.text(masterPoints[0].addedPoint(10, 5), "Slave0", textFont)
    # textPoints: list[Point] = [p.addedPoint(-20, -140) for p in masterPoints[:-1]]
    # for p in textPoints:
    #     model.text(p, "回転方向", Font('black', 14))
    #     model.text(p.addedPoint(0, 20), "constraint", Font('black', 14))

    # frameTextPoints: list[Point] = [p.addedPoint(10, 50) for p in masterPoints[1:]]
    # for p in frameTextPoints:
    #     model.text(p, "剛体", Font('black', 14))
    
    # for i, p in enumerate(masterPoints):
    #     model.text(p.addedPoint(3, -16), f'Main{i}', Font('black', 11))
    # for i, p in enumerate(slavePoints):
    #     model.text(p.addedPoint(5, -16), f'Sub{i}', Font('black', 11))
        
    # # 矢印
    # arrowFillStroke: FillStroke = FillStroke('black', 'black', 1)
    # arrowStartPoints: list[Point] = [p.addedPoint(0, -110) for p in masterPoints[:-1]]
    # arrowHeadSize: Size = Size(10, 10)
    # for p in arrowStartPoints:
    #     model.arrow(p, 80, arrowHeadSize, arrowFillStroke, p, 5)
    #     model.arrow(p, 80, arrowHeadSize, arrowFillStroke, p, 90)

    # for p in masterPoints:
    #     model.arrowRotational(p, masterNodeRadius * 2.5, Size(6, 4), arrowFillStroke, 45)
    
    # annotationPoint: Point = Point(10, 80)
    # model.circle(annotationPoint.addedPoint(-12, -5), masterNodeRadius, masterNodeFillStroke)
    # model.circle(annotationPoint.addedPoint(-12, -5).addedPoint(0, 28), masterNodeRadius, slaveNodeFillStroke)
    # model.text(annotationPoint, "Main：質量が入っている節点 ※最下層を除く", Font('black', 14))
    # model.text(annotationPoint.addedPoint(0, 28), "Sub：質量が入っていない節点", Font('black', 14))

    return model
