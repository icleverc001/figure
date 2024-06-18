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
from resp.elements.rotationalSpring import RotationalSpring
import resp.services.utilities as Utils

def getmodel() -> Model:
    model: Model = Model(Size(730, 540), ViewBox(Point(-80, -400), Size(730, 540)))

    targetFloorIndex: int = 1

    # NodePoints
    floorNum: int = 4
    nodeDisX = 70
    nodeDisY = 100
    modelOffset: int = 100
    masterRDPoints: list[Point] = [Point(0, -i * nodeDisY) for i in range(0, floorNum)]
    masterXPoints: list[Point] = [Point(masterRDPoints[0].X + modelOffset + nodeDisX * i, -nodeDisY * i) for i in range(0, floorNum)]
    masterYPoints: list[Point] = [Point(masterXPoints[0].X + modelOffset * 2 + nodeDisX * i, -nodeDisY * i) for i in range(0, floorNum)]
    masterZPoints: list[Point] = [Point(masterYPoints[-1].X + modelOffset, -nodeDisY * i) for i in range(0, floorNum)]
    slaveXPoints: list[Point] = [p.addedPoint(nodeDisX, 0) for p in masterXPoints[:-1]]
    slaveYPoints: list[Point] = [p.addedPoint(nodeDisX, 0) for p in masterYPoints[:-1]]
    
    # baseNode: Point = Point(0, 0)
    # baseNode2: Point = baseNode.addedPoint(modelOffset, 0)
    
    cornerNodePoints: list[Point] = [masterXPoints[0].addedPoint(0, -nodeDisY), masterXPoints[1].addedPoint(0, -nodeDisY * 2)]
    
    # Frame
    frameStroke: Stroke = Stroke('black', 3)
    frameStrokeDash: Stroke = Stroke('black', 1, dasharray=[2, 2])
    # model.line(masterPoints[0], baseNode, frameStroke)
    # model.line(masterPoints2[0], baseNode2, frameStroke)
    for t, b in zip(masterRDPoints[1:], masterRDPoints[:-1]):
        model.line(t, b, frameStrokeDash)
    for m, s in zip(masterXPoints[1:], slaveXPoints):
        model.line(m, s, frameStroke)
    for m, s in zip(masterYPoints[1:], slaveYPoints):
        model.line(m, s, frameStroke)
    for t, b in zip(masterZPoints[1:], masterZPoints[:-1]):
        model.line(t, b, frameStrokeDash)

    model.groundHorizontal(Point(-55, 5), 60, 10, Stroke('black', 2))
    model.groundVertical(Point(5, 25), 20, 10, Stroke('black', 2))

    # spring
    springLength: int = 100
    springStroke: Stroke = Stroke('black', 1)
    damperStroke: Stroke = Stroke('blue', 1)
    for m, s in zip(masterXPoints, slaveXPoints):
        model.spring(m, s, Size(30, 20), springStroke)
    for m, s in zip(masterYPoints, slaveYPoints):
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

    rotationalPoints: list[Point] = [Utils.get_center_point(b, t).addedPoint(-40, 0) for b, t in zip(masterZPoints[:-1], masterZPoints[1:])]
    
    for i, p in enumerate(rotationalPoints):
        r:RotationalSpring = model.rotationalSpring(p, 15, FillStroke('none', 'black', 1), startRadian=math.pi / 2, aspectRatioY=0.5)
        model.line(masterZPoints[i], r.EndPoint, springStroke)
        model.line(masterZPoints[i + 1], r.StartPoint, springStroke)
    
    # floorLine
    floorLineStroke: Stroke = Stroke('blue', 1, dasharray=[6, 6])
    model.line(masterRDPoints[targetFloorIndex].addedPoint(-50, 0), masterZPoints[targetFloorIndex].addedPoint(50, 0), floorLineStroke)
    
    # Node
    masterNodeRadius: int = 5
    masterNodeFillStroke: FillStroke = FillStroke('white', 'black', 2)
    slaveNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    for p in masterRDPoints:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    for p in masterXPoints:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    for p in masterYPoints:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    for p in masterZPoints:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    for p in slaveXPoints:
        model.circle(p, masterNodeRadius, slaveNodeFillStroke)
    for p in slaveYPoints:
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
    textFont: Font = Font('black', 18)
    model.text(masterRDPoints[-1].addedPoint(-35, -20), '代表節点', textFont)
    model.text(masterXPoints[-1].addedPoint(-25, -20), 'X方向', textFont)
    model.text(masterYPoints[-1].addedPoint(-25, -20), 'Y方向', textFont)
    model.text(masterZPoints[-1].addedPoint(-25, -20), 'Z方向（ねじれ）', textFont)
    textPoints: list[Point] = [Utils.get_center_point(m, s) for m, s in zip(masterXPoints[1:], slaveXPoints)]
    # for p in textPoints:
    #     model.text(p.addedPoint(5, 5), "EI", textFont)
    # textPointsSpring: list[Point] = [Utils.get_center_point(m, s) for m, s in zip(masterPoints, slavePoints)]
    # for p in textPointsSpring:
    #     model.text(p.addedPoint(-30, 30), "せん断ばね", textFont)
    
    model.text(masterRDPoints[targetFloorIndex].addedPoint(60, 55), '剛床', textFont)
    model.text(masterRDPoints[targetFloorIndex].addedPoint(-40, -10), 'NodeRD', textFont)
    model.text(masterXPoints[targetFloorIndex].addedPoint(-40, -10), 'NodeX', textFont)
    model.text(masterYPoints[targetFloorIndex].addedPoint(-40, -10), 'NodeY', textFont)
    model.text(masterZPoints[targetFloorIndex].addedPoint(-40, -10), 'NodeCenter', textFont)
    
    # frameTextPoints: list[Point] = [p.addedPoint(10, 50) for p in masterPoints[1:]]
    # for p in frameTextPoints:
    #     model.text(p, "剛体", Font('black', 14))
        
    # for i, p in enumerate(masterPoints):
    #     model.text(p.addedPoint(3, -16), f'Main{i}', Font('black', 11))
    # for i, p in enumerate(slavePoints):
    #     model.text(p.addedPoint(5, -16), f'Sub{i}', Font('black', 11))

    # 矢印
    # arrowFillStroke: FillStroke = FillStroke('black', 'black', 1, dasharray=[5, 2])
    # arrowHeadSize: Size = Size(10, 10)
    arrowFillStroke: FillStroke = FillStroke('black', 'black', 1)
    arrowHeadSize: Size = Size(15, 15)
    arrowOffset: float = 15
    p1Points: list[Point] = [masterXPoints[targetFloorIndex], masterYPoints[targetFloorIndex], masterZPoints[targetFloorIndex]]
    for i, _p1 in enumerate(p1Points):
        p0: Point = masterRDPoints[targetFloorIndex].addedPoint(arrowOffset, arrowOffset)
        p1: Point = _p1.addedPoint(-arrowOffset, arrowOffset)
        tmpPoint: Point = Utils.get_center_point(p0, p1).addedPoint(0, nodeDisY * 0.3 * (i + 1))
        model.arrowCurve(p1, p0, tmpPoint, arrowHeadSize, arrowFillStroke)

    # model.text(tmpPoint.addedPoint(-55, -10), "任意ばね", Font('black', 16))

    annotationPoint: Point = masterRDPoints[0].addedPoint(25, 80)
    annotationFont: Font = Font('black', 20)
    # model.text(annotationPoint, "回転と並進を伝達", annotationFont)
    
    # for p in masterRDPoints[1:]:
    #     model.text(p.addedPoint(50, 80), "並進を伝達", annotationFont)
    
    return model
