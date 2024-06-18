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

def getmodel() -> Model:
    model: Model = Model(Size(400, 540), ViewBox(Point(-50, -360), Size(400, 540)))

    # NodePoints
    masterPoints: list[Point] = [Point(i * 100, -i * 100) for i in range(0, 4)]
    slavePoints: list[Point] = [Point((i + 1) * 100, -i * 100) for i in range(0, 3)]
    
    # Frame
    frameStroke: Stroke = Stroke('black', 3)
    model.line(masterPoints[1], slavePoints[0], frameStroke)
    model.line(masterPoints[2], slavePoints[1], frameStroke)
    model.line(masterPoints[3], slavePoints[2], frameStroke)

    model.groundHorizontal(Point(-40, 5), 60, 10, Stroke('black', 2))
    model.groundVertical(Point(20, 25), 20, 10, Stroke('black', 2))

    # spring
    springLength: int = 100
    springStroke: Stroke = Stroke('blue', 1)
    model.spring(masterPoints[0], slavePoints[0], Size(50, 25), springStroke)
    model.spring(masterPoints[1], slavePoints[1], Size(50, 25), springStroke)
    model.spring(masterPoints[2], slavePoints[2], Size(50, 25), springStroke)
    # model.spring(Point(20, -120), 50, Stroke('blue', 1))
    # model.spring(Point(90, -200), 50, Stroke('blue', 1))
    # model.dashpot(Point(20, -80), 50, Stroke('blue', 1))
    # model.dashpot(Point(150, -260), 50, Stroke('blue', 1))
    # model.line(Point(10, -100), Point(20, -100), Stroke('blue', 1))
    # model.line(Point(70, -100), Point(80, -100), Stroke('blue', 1))
    # model.line(Point(20, -80), Point(20, -120), Stroke('blue', 1))
    # model.line(Point(70, -80), Point(70, -120), Stroke('blue', 1))

    rotationalPoints: list[Point] = [p.addedPoint(50, 40) for p in masterPoints[:-1]]
    
    for i, p in enumerate(rotationalPoints):
        r:RotationalSpring = model.rotationalSpring(p, 15, FillStroke('none', 'blue', 1))
        model.line(masterPoints[i], r.EndPoint, springStroke)
        model.line(slavePoints[i], r.StartPoint, springStroke)
    
    # Node
    masterNodeRadius: int = 5
    masterNodeFillStroke: FillStroke = FillStroke('white', 'black', 2)
    slaveNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    model.circle(masterPoints[0], masterNodeRadius, masterNodeFillStroke)
    model.circle(slavePoints[0], masterNodeRadius, slaveNodeFillStroke)
    model.circle(masterPoints[1], masterNodeRadius, masterNodeFillStroke)
    model.circle(slavePoints[1], masterNodeRadius, slaveNodeFillStroke)
    model.circle(masterPoints[2], masterNodeRadius, masterNodeFillStroke)
    model.circle(slavePoints[2], masterNodeRadius, slaveNodeFillStroke)
    model.circle(masterPoints[3], masterNodeRadius, masterNodeFillStroke)

    # Text
    textPoints: list[Point] = [p.addedPoint(-20, -120) for p in masterPoints[:-1]]
    # for p in textPoints:
    #     model.text(p, "回転方向", Font('black', 14))
    #     model.text(p.addedPoint(0, 20), "constraint", Font('black', 14))

    frameTextPoints: list[Point] = [p.addedPoint(10, 50) for p in masterPoints[1:]]
    for p in frameTextPoints:
        model.text(p, "剛体", Font('black', 16))
        
    for i, p in enumerate(masterPoints):
        model.text(p.addedPoint(3, -16), f'Main{i}', Font('black', 14))
    for i, p in enumerate(slavePoints):
        model.text(p.addedPoint(5, -16), f'Sub{i}', Font('black', 14))

    # 矢印
    arrowFillStroke: FillStroke = FillStroke('black', 'black', 1)
    arrowStartPoints: list[Point] = [p.addedPoint(0, -90) for p in masterPoints[:-1]]
    arrowHeadSize: Size = Size(10, 10)
    # for p in arrowStartPoints:
    #     model.arrow(p, 100, arrowHeadSize, arrowFillStroke, p, 40)
    #     model.arrow(p, 70, arrowHeadSize, arrowFillStroke, p, 90)


    annotationPoint: Point = Point(10, 80)
    annotationFont: Font = Font('black', 16)
    model.circle(annotationPoint.addedPoint(-12, -5), masterNodeRadius, masterNodeFillStroke)
    model.circle(annotationPoint.addedPoint(-12, -5).addedPoint(0, 28), masterNodeRadius, slaveNodeFillStroke)
    model.text(annotationPoint, "Main：質量が入っている節点 ※最下層を除く", annotationFont)
    model.text(annotationPoint.addedPoint(0, 28), "Sub：質量が入っていない節点", annotationFont)
    
    return model
