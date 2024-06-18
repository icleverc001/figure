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
from resp.elements.rotationalSpring import RotationalSpring
import resp.services.utilities as Utils

def getmodel() -> Model:
    model: Model = Model(Size(500, 540), ViewBox(Point(-80, -400), Size(500, 540)))

    # NodePoints
    nodeDisX = 70
    nodeDisY = 100
    modelOffset: int = 200
    masterPoints: list[Point] = [Point(i * nodeDisX, -i * nodeDisY) for i in range(0, 4)]
    slavePoints: list[Point] = [Point((i + 1) * nodeDisX, -i * nodeDisY) for i in range(0, 3)]
    masterPoints2: list[Point] = [p.addedPoint(modelOffset, 0) for p in masterPoints]
    slavePoints2: list[Point] = [p.addedPoint(modelOffset, 0) for p in slavePoints]
    # baseNode: Point = Point(0, 0)
    # baseNode2: Point = baseNode.addedPoint(modelOffset, 0)
    
    cornerNodePoints: list[Point] = [masterPoints[0].addedPoint(0, -nodeDisY), masterPoints[1].addedPoint(0, -nodeDisY * 2)]
    
    # Frame
    frameStroke: Stroke = Stroke('black', 3)
    # model.line(masterPoints[0], baseNode, frameStroke)
    # model.line(masterPoints2[0], baseNode2, frameStroke)
    for m, s in zip(masterPoints[1:], slavePoints):
        model.line(m, s, frameStroke)
    for m, s in zip(masterPoints2[1:], slavePoints2):
        model.line(m, s, frameStroke)

    model.groundHorizontal(Point(-55, 5), 60, 10, Stroke('black', 2))
    model.groundVertical(Point(5, 25), 20, 10, Stroke('black', 2))

    # spring
    springLength: int = 100
    springStroke: Stroke = Stroke('black', 1)
    damperStroke: Stroke = Stroke('blue', 1)
    for m, s in zip(masterPoints, slavePoints):
        model.spring(m, s, Size(30, 20), springStroke)
    for m, s in zip(masterPoints2, slavePoints2):
        model.spring(m, s, Size(30, 20), springStroke)
    # startPoints: list[Point] = [cornerNodePoints[0], cornerNodePoints[1].addedPoint(nodeDisX * 0.5, 0)]
    # endPoints: list[Point] = [masterPoints[1], masterPoints[-1].addedPoint(-nodeDisX * 0.5, 0)]
    # for m, tmp in zip(masterPoints, cornerNodePoints):
    #     model.line(m, tmp, damperStroke)
    # model.line(cornerNodePoints[1], startPoints[1], damperStroke)
    # model.line(endPoints[1], masterPoints[-1], damperStroke)
    # for st, ed in zip(startPoints, endPoints):
    #     model.spring(st, ed, Size(50, 25), damperStroke)
    # model.spring(masterPoints[1], slavePoints[1], Size(50, 25), springStroke)
    # model.spring(masterPoints[2], slavePoints[2], Size(50, 25), springStroke)
    # model.spring(Point(20, -120), 50, Stroke('blue', 1))
    # model.spring(Point(90, -200), 50, Stroke('blue', 1))
    # model.dashpot(Point(20, -80), 50, Stroke('blue', 1))
    # model.dashpot(Point(150, -260), 50, Stroke('blue', 1))
    # model.line(Point(10, -100), Point(20, -100), Stroke('blue', 1))
    # model.line(Point(70, -100), Point(80, -100), Stroke('blue', 1))
    # model.line(Point(20, -80), Point(20, -120), Stroke('blue', 1))
    # model.line(Point(70, -80), Point(70, -120), Stroke('blue', 1))

    # rotationalPoints: list[Point] = [p.addedPoint(50, 40) for p in masterPoints[:-1]]
    
    # for i, p in enumerate(rotationalPoints):
    #     r:RotationalSpring = model.rotationalSpring(p, 15, FillStroke('none', 'blue', 1))
    #     model.line(masterPoints[i], r.EndPoint, springStroke)
    #     model.line(slavePoints[i], r.StartPoint, springStroke)
    
    # Node
    masterNodeRadius: int = 5
    masterNodeFillStroke: FillStroke = FillStroke('white', 'black', 2)
    slaveNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    for p in masterPoints:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    for p in slavePoints:
        model.circle(p, masterNodeRadius, slaveNodeFillStroke)
    for p in masterPoints2:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    for p in slavePoints2:
        model.circle(p, masterNodeRadius, slaveNodeFillStroke)
    # for p in cornerNodePoints:
    #     model.circle(p, masterNodeRadius, slaveNodeFillStroke)
    # model.circle(baseNode, masterNodeRadius, slaveNodeFillStroke)

    # model.circle(masterPoints[1], masterNodeRadius, masterNodeFillStroke)
    # model.circle(slavePoints[1], masterNodeRadius, slaveNodeFillStroke)
    # model.circle(masterPoints[2], masterNodeRadius, masterNodeFillStroke)
    # model.circle(slavePoints[2], masterNodeRadius, slaveNodeFillStroke)
    # model.circle(masterPoints[3], masterNodeRadius, masterNodeFillStroke)

    # Text
    textFont: Font = Font('black', 14)
    model.text(masterPoints[-1].addedPoint(-80, -20), '復元力パネル１', textFont)
    model.text(masterPoints2[-1].addedPoint(-80, -20), '復元力パネル２', textFont)
    textPoints: list[Point] = [Utils.get_center_point(m, s) for m, s in zip(masterPoints[1:], slavePoints)]
    # for p in textPoints:
    #     model.text(p.addedPoint(5, 5), "EI", textFont)
    # textPointsSpring: list[Point] = [Utils.get_center_point(m, s) for m, s in zip(masterPoints, slavePoints)]
    # for p in textPointsSpring:
    #     model.text(p.addedPoint(-30, 30), "せん断ばね", textFont)
    
    
    # frameTextPoints: list[Point] = [p.addedPoint(10, 50) for p in masterPoints[1:]]
    # for p in frameTextPoints:
    #     model.text(p, "剛体", Font('black', 14))
        
    # for i, p in enumerate(masterPoints):
    #     model.text(p.addedPoint(3, -16), f'Main{i}', Font('black', 11))
    # for i, p in enumerate(slavePoints):
    #     model.text(p.addedPoint(5, -16), f'Sub{i}', Font('black', 11))

    # 矢印
    arrowFillStroke: FillStroke = FillStroke('black', 'black', 1, dasharray=[5, 2])
    arrowHeadSize: Size = Size(10, 10)
    arrowOffset: float = 15
    for _p1, _p2 in zip(masterPoints, masterPoints2):
        p1: Point = _p1.addedPoint(arrowOffset, arrowOffset)
        p2: Point = _p2.addedPoint(-arrowOffset, arrowOffset)
        tmpPoint: Point = Utils.get_center_point(p1, p2).addedPoint(0, nodeDisY * 0.8)
        model.arrowCurve(p2, p1, tmpPoint, arrowHeadSize, arrowFillStroke)

    # model.text(tmpPoint.addedPoint(-55, -10), "任意ばね", Font('black', 16))

    annotationPoint: Point = masterPoints[0].addedPoint(25, 80)
    annotationFont: Font = Font('black', 20)
    # model.circle(annotationPoint.addedPoint(-12, -5), masterNodeRadius, masterNodeFillStroke)
    # model.circle(annotationPoint.addedPoint(-12, -5).addedPoint(0, 28), masterNodeRadius, slaveNodeFillStroke)
    model.text(annotationPoint, "回転と並進を伝達", annotationFont)
    # model.text(annotationPoint.addedPoint(0, 28), "曲げによる水平方向変位が含まれる", annotationFont)
    
    for p in masterPoints[1:]:
        model.text(p.addedPoint(50, 80), "並進を伝達", annotationFont)
    
    return model
