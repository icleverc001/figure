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
from elements.rotationalSpring import RotationalSpring

def getmodel() -> Model:
    model: Model = Model(Size(500, 540), ViewBox(Point(-100, -400), Size(500, 540)))

    # NodePoints
    masterPoints: list[Point] = [Point(i * 100, -(i + 1) * 100) for i in range(0, 2)]
    slavePoints: list[Point] = [Point((i + 1) * 100, -(i + 1) * 100) for i in range(0, 1)]
    basePoint: Point = Point(0, 0)
    
    # Frame
    frameStroke: Stroke = Stroke('black', 3)
    # model.line(masterPoints[0], basePoint, frameStroke)
    model.line(masterPoints[1], slavePoints[0], frameStroke)

    model.groundHorizontal(Point(-40, 5), 80, 10, Stroke('black', 2))
    # model.groundVertical(Point(20, 25), 20, 10, Stroke('black', 2))

    # spring
    springLength: int = 100
    springStroke: Stroke = Stroke('blue', 1)
    model.spring(masterPoints[0], slavePoints[0], Size(50, 25), springStroke)
    
    tmpPointCenter: Point = Point(basePoint.X, (basePoint.Y + masterPoints[0].Y) / 2)
    tmpPointLeft: Point = Point(basePoint.X - (slavePoints[0].X - basePoint.X) / 2, tmpPointCenter.Y)
    tmpPointRight: Point = Point(basePoint.X + (slavePoints[0].X - basePoint.X) / 2, tmpPointCenter.Y)
    
    # model.dashpot(Point(150, -260), 50, Stroke('blue', 1))
    model.spring(tmpPointCenter, tmpPointRight, Size(25, 20), Stroke('blue', 1))
    model.line(basePoint, tmpPointCenter, springStroke)
    model.line(masterPoints[0], tmpPointRight, springStroke)

    rotSpr: RotationalSpring = model.rotationalSpring(tmpPointLeft, 15, FillStroke('none', springStroke.color, springStroke.width))
    model.line(basePoint, rotSpr.EndPoint, springStroke)
    model.line(masterPoints[0], rotSpr.StartPoint, springStroke)

    # Node
    masterNodeRadius: int = 5
    masterNodeFillStroke: FillStroke = FillStroke('white', 'black', 2)
    slaveNodeFillStroke: FillStroke = FillStroke('black', 'black', 2)
    for p in masterPoints:
        model.circle(p, masterNodeRadius, masterNodeFillStroke)
    for p in slavePoints:
        model.circle(p, masterNodeRadius, slaveNodeFillStroke)
    model.circle(basePoint, masterNodeRadius, slaveNodeFillStroke)
    
    # # Text
    textFont: Font = Font('black', 14)
    model.text(basePoint.addedPoint(10, -5), "NodeBase", textFont)
    model.text(masterPoints[0].addedPoint(-30, -15), "Master0", textFont)
    model.text(slavePoints[0].addedPoint(10, 5), "Slave0", textFont)
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
