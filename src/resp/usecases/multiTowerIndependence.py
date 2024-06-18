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
    model: Model = Model(Size(500, 540), ViewBox(Point(-100, -400), Size(500, 540)))

    # NodePoints
    nodeDisX = 150
    nodeDisY = 100
    masterPointsTower1: list[Point] = [Point(0, -i * nodeDisY) for i in range(0, 4)]
    masterPointsTower2: list[Point] = [Point(nodeDisX, -i * nodeDisY) for i in range(0, 4)]
    # slavePoints: list[Point] = [Point(, -i * nodeDisY) for i in range(0, 3)]
    # baseNode: Point = Point(0, 0)
    
    # tmpNodePoints: list[Point] = [p.addedPoint(0, -nodeDisY / 2) for p in masterPoints[:-1]]
    
    # Frame
    frameStroke: Stroke = Stroke('black', 3)
    # model.line(masterPoints[0], baseNode, frameStroke)
    model.line(masterPointsTower1[1], masterPointsTower1[0], frameStroke)
    model.line(masterPointsTower1[2], masterPointsTower1[1], frameStroke)
    model.line(masterPointsTower1[3], masterPointsTower1[2], frameStroke)
    model.line(masterPointsTower2[1], masterPointsTower2[0], frameStroke)
    model.line(masterPointsTower2[2], masterPointsTower2[1], frameStroke)
    model.line(masterPointsTower2[3], masterPointsTower2[2], frameStroke)
    frameStroke: Stroke = Stroke('black', 2)
    # model.line(masterPoints[1], slavePoints[1], frameStroke)
    # model.line(masterPoints[2], slavePoints[2], frameStroke)

    model.groundHorizontal(Point(-40, 5), 230, 20, Stroke('black', 2))
    # model.groundVertical(Point(20, 25), 20, 10, Stroke('black', 2))

    # spring
    springStroke: Stroke = Stroke('blue', 1)
    damperStroke: Stroke = Stroke('blue', 1)
    # for m, s in zip(masterPoints, slavePoints):
    #     model.spring(m, s, Size(50, 25), springStroke)
    # tmpPoint: Point = masterPoints[0].addedPoint(0, -nodeDisY * 2)
    # startPoints:list[Point] = [masterPoints[0], tmpPoint.addedPoint(nodeDisX * 0.5, 0)]
    # endPoints:list[Point] = [slavePoints[0], startPoints[-1].addedPoint(nodeDisX, 0)]
    # model.line(masterPoints[0], tmpPoint, springStroke)
    # model.line(tmpPoint, startPoints[-1], springStroke)
    # model.line(endPoints[-1], masterPoints[2], springStroke)
    # for st, ed in zip(startPoints, endPoints):
    #     r: float = 0.1
    #     disX = nodeDisX * (1 - r * 2)
    #     tmpRatio: float = 0.4
    #     sprLength: int = 32
    #     pUpLeft: Point = st.addedPoint(nodeDisX * r, -nodeDisY * 0.4)
    #     pUpRight: Point = st.addedPoint(nodeDisX * (1 - r), -nodeDisY * 0.4)
    #     pLowLeft: Point = st.addedPoint(nodeDisX * r, nodeDisY * 0.4)
    #     pLowRight: Point = st.addedPoint(nodeDisX * (1 - r), nodeDisY * 0.4)
        
    #     model.spring(st, ed, Size(sprLength, 22), springStroke)
        
    #     p1Up = pUpLeft.addedPoint(disX * tmpRatio, 0)
    #     p2Up = p1Up.addedPoint(sprLength, 0)
    #     model.dashpot(pUpLeft, pUpRight, Size(14, 28), damperStroke)
    #     # model.spring(p1Up, p2Up, Size(sprLength, 22), damperStroke)
    #     # model.line(p2Up, pUpRight, damperStroke)
    #     model.line(st, pUpLeft, damperStroke)
    #     model.line(ed, pUpRight, damperStroke)
        
    #     p1Low = pLowLeft.addedPoint(disX * tmpRatio, 0)
    #     p2Low = p1Low.addedPoint(sprLength, 0)
    #     model.dashpot(pLowLeft, p1Low, Size(14, 28), damperStroke)
    #     model.spring(p1Low, p2Low, Size(sprLength, 22), damperStroke)
    #     model.line(p2Low, pLowRight, damperStroke)
    #     model.line(st, pLowLeft, damperStroke)
    #     model.line(ed, pLowRight, damperStroke)
        
        # 枠線
    model.tower(masterPointsTower1[-1], masterPointsTower1[0], 15, 15, Stroke('black', 2, [10, 5]))
    model.tower(masterPointsTower2[-1], masterPointsTower2[0], 15, 15, Stroke('black', 2, [10, 5]))


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
    for p in masterPointsTower1:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    for p in masterPointsTower2:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
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
    textPoints: list[Point] = [masterPointsTower1[-1], masterPointsTower2[-1]]
    for i, p in enumerate(textPoints):
        model.text(p.addedPoint(-20, -30), f'タワー{i + 1}', textFont)
    # for p in startPoints:
    #     model.text(p.addedPoint(0, -70), "免震部材", textFont)
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
    # arrowFillStroke: FillStroke = FillStroke('black', 'black', 1)
    # arrowStartPoint: Point = Point(baseNode.X, tmpNodePoints[0].Y).addedPoint(0, - nodeDisY * 1.2)
    # arrowHeadSize: Size = Size(10, 10)
    # model.arrow(arrowStartPoint, 90, arrowHeadSize, arrowFillStroke, arrowStartPoint, 5)
    # model.arrow(arrowStartPoint, 100, arrowHeadSize, arrowFillStroke, arrowStartPoint, 65)
    # model.arrow(arrowStartPoint, 200, arrowHeadSize, arrowFillStroke, arrowStartPoint, -25)

    # model.text(arrowStartPoint.addedPoint(-70, 0), "制振部材", Font('black', 16))


    # annotationPoint: Point = Point(10, 80)
    # model.circle(annotationPoint.addedPoint(-12, -5), masterNodeRadius, masterNodeFillStroke)
    # model.circle(annotationPoint.addedPoint(-12, -5).addedPoint(0, 28), masterNodeRadius, slaveNodeFillStroke)
    # model.text(annotationPoint, "Main：質量が入っている節点 ※最下層を除く", Font('black', 14))
    # model.text(annotationPoint.addedPoint(0, 28), "Sub：質量が入っていない節点", Font('black', 14))
    
    return model
