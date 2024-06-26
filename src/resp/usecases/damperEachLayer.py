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
    model: Model = Model(Size(500, 540), ViewBox(Point(-100, -450), Size(500, 540)))

    # NodePoints
    nodeDisX = 100
    nodeDisY = 100
    masterPoints: list[Point] = [Point(i * nodeDisX, -(i + 1) * nodeDisY) for i in range(0, 4)]
    slavePoints: list[Point] = [Point((i + 1) * nodeDisX, -(i + 1) * nodeDisY) for i in range(0, 3)]
    baseNode: Point = Point(0, 0)
    
    tmpNodePoints: list[Point] = [p.addedPoint(0, -nodeDisY / 2) for p in masterPoints[:-1]]
    
    # Frame
    frameStroke: Stroke = Stroke('black', 3)
    model.line(masterPoints[0], baseNode, frameStroke)
    model.line(masterPoints[1], slavePoints[0], frameStroke)
    model.line(masterPoints[2], slavePoints[1], frameStroke)
    model.line(masterPoints[3], slavePoints[2], frameStroke)

    # model.groundHorizontal(Point(-40, 5), 60, 10, Stroke('black', 2))
    # model.groundVertical(Point(20, 25), 20, 10, Stroke('black', 2))

    # spring
    springLength: int = 100
    springStroke: Stroke = Stroke('black', 1)
    damperStroke: Stroke = Stroke('blue', 1)
    for m, s in zip(masterPoints, slavePoints):
        model.spring(m, s, Size(40, 20), springStroke)
    for tmp, m, s in zip(tmpNodePoints, masterPoints[:-1], slavePoints):
        r: float = 0.1
        disX = nodeDisX * (1 - r * 2)
        tmpRatio: float = 0.4
        sprLength: int = 32
        pleft: Point = tmp.addedPoint(nodeDisX * r, 0)
        pright: Point = tmp.addedPoint(nodeDisX * (1 - r), 0)
        
        
        p1 = pleft.addedPoint(disX * tmpRatio, 0)
        p2 = p1.addedPoint(sprLength, 0)
        model.dashpot(pleft, p1, Size(14, 28), damperStroke)
        model.spring(p1, pright, Size(sprLength, 22), damperStroke)
        # model.line(p2, pright, damperStroke)
        model.line(m, pleft, damperStroke)
        model.line(s, pright, damperStroke)
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
    # for p in tmpNodePoints:
    #     model.circle(p, masterNodeRadius, slaveNodeFillStroke)
    # model.circle(baseNode, masterNodeRadius, slaveNodeFillStroke)

    # model.circle(masterPoints[1], masterNodeRadius, masterNodeFillStroke)
    # model.circle(slavePoints[1], masterNodeRadius, slaveNodeFillStroke)
    # model.circle(masterPoints[2], masterNodeRadius, masterNodeFillStroke)
    # model.circle(slavePoints[2], masterNodeRadius, slaveNodeFillStroke)
    # model.circle(masterPoints[3], masterNodeRadius, masterNodeFillStroke)

    # Text
    textFont: Font = Font('black', 14)
    textPoints: list[Point] = [Utils.get_center_point(m, s) for m, s in zip(masterPoints[1:], slavePoints)]
    for p in textPoints:
        model.text(p.addedPoint(5, 5), "EI", textFont)
    textPointsSpring: list[Point] = [Utils.get_center_point(m, s) for m, s in zip(masterPoints, slavePoints)]
    for p in textPointsSpring:
        model.text(p.addedPoint(-30, 30), "せん断ばね", textFont)

    # frameTextPoints: list[Point] = [p.addedPoint(10, 50) for p in masterPoints[1:]]
    # for p in frameTextPoints:
    #     model.text(p, "剛体", Font('black', 14))
        
    # for i, p in enumerate(masterPoints):
    #     model.text(p.addedPoint(3, -16), f'Main{i}', Font('black', 11))
    # for i, p in enumerate(slavePoints):
    #     model.text(p.addedPoint(5, -16), f'Sub{i}', Font('black', 11))

    # 矢印
    arrowFillStroke: FillStroke = FillStroke('black', 'black', 1)
    arrowStartPoint: Point = Point(baseNode.X, tmpNodePoints[0].Y).addedPoint(0, - nodeDisY * 1.2)
    arrowHeadSize: Size = Size(10, 10)
    model.arrow(arrowStartPoint, 90, arrowHeadSize, arrowFillStroke, arrowStartPoint, 5)
    model.arrow(arrowStartPoint, 100, arrowHeadSize, arrowFillStroke, arrowStartPoint, 65)
    model.arrow(arrowStartPoint, 200, arrowHeadSize, arrowFillStroke, arrowStartPoint, -25)

    model.text(arrowStartPoint.addedPoint(-70, 0), "制振部材", Font('black', 16))


    # annotationPoint: Point = Point(10, 80)
    # model.circle(annotationPoint.addedPoint(-12, -5), masterNodeRadius, masterNodeFillStroke)
    # model.circle(annotationPoint.addedPoint(-12, -5).addedPoint(0, 28), masterNodeRadius, slaveNodeFillStroke)
    # model.text(annotationPoint, "Main：質量が入っている節点 ※最下層を除く", Font('black', 14))
    # model.text(annotationPoint.addedPoint(0, 28), "Sub：質量が入っていない節点", Font('black', 14))
    
    return model
