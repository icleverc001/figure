import sys
import os
sys.path.append(os.path.dirname(__file__))

from resp.model import Model
# from resp.parts.point import Point
# from resp.parts.size import Size
# from resp.parts.stroke import Stroke
# from resp.parts.fillstroke import FillSStroke
# from resp.parts.viewbox import ViewBox
import resp.usecases.sample as sample
import resp.usecases.equivalentShear as eqshear
import resp.usecases.equivalentBendingShearEI as eqbendEI
import resp.usecases.equivalentBendingShear as eqbend
import resp.usecases.swayRocking as SwayRocking
import resp.usecases.damperEachLayer as DamperEachLayer
import resp.usecases.damperAnyLayer as DamperAnyLayer
import resp.usecases.damper.oilDamper as oilDamper
import resp.usecases.damper.asymmetricOilDamper as asymmetricOilDamper
import resp.usecases.damper.zener as zener
import resp.usecases.damper.iRDT as iRDT
import resp.usecases.damper.trc as trc
import resp.usecases.damper.adcVDW as adcVDW
import resp.usecases.damper.jFELowStrengthSteel as JFELowStrengthSteel
import resp.usecases.damper.oilesVWD as oilesVWD
import resp.usecases.damper.powerLaw as powerLaw
import resp.usecases.damper.rDT as RDT
import resp.usecases.damper.steelMaterial as steelMaterial
import resp.usecases.damper.unitRubber as unitRubbe

def wirtefile(path: str, model: Model) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(model.get_text())

def run() -> None:
    model: Model = sample.getmodel()
    path: str = "./output/tmp/sample.svg"
    wirtefile(path, model)

    model: Model = eqshear.getmodel()
    path: str = "./output/modeldiagram/eqshear.svg"
    wirtefile(path, model)

    model: Model = eqbendEI.getmodel()
    path: str = "./output/modeldiagram/eqbendEI.svg"
    wirtefile(path, model)

    model: Model = eqbend.getmodel()
    path: str = "./output/modeldiagram/eqbend.svg"
    wirtefile(path, model)

    # SwayRocking
    model: Model = SwayRocking.getmodel()
    path: str = "./output/modeldiagram/swayRocking.svg"
    wirtefile(path, model)

    # 制振部材：各回配置
    model: Model = DamperEachLayer.getmodel()
    path: str = "./output/modeldiagram/damperEachLayer.svg"
    wirtefile(path, model)

    # 制振部材：任意層間配置
    model: Model = DamperAnyLayer.getmodel()
    path: str = "./output/modeldiagram/damperAnyLayer.svg"
    wirtefile(path, model)

    model: Model = oilDamper.getmodel()
    path: str = "./output/damper/oilDamper.svg"
    wirtefile(path, model)

    model: Model = asymmetricOilDamper.getmodel()
    path: str = "./output/damper/asymmetricOilDamper.svg"
    wirtefile(path, model)

    model: Model = zener.getmodel()
    path: str = "./output/damper/zener.svg"
    wirtefile(path, model)

    model: Model = iRDT.getmodel()
    path: str = "./output/damper/iRDT.svg"
    wirtefile(path, model)

    model: Model = trc.getmodel()
    path: str = "./output/damper/trc.svg"
    wirtefile(path, model)

    model: Model = adcVDW.getmodel()
    path: str = "./output/damper/adcVDW.svg"
    wirtefile(path, model)

    model: Model = JFELowStrengthSteel.getmodel()
    path: str = "./output/damper/JFELowStrengthSteel.svg"
    wirtefile(path, model)

    model: Model = oilesVWD.getmodel()
    path: str = "./output/damper/oilesVWD.svg"
    wirtefile(path, model)

    model: Model = powerLaw.getmodel()
    path: str = "./output/damper/powerLaw.svg"
    wirtefile(path, model)

    model: Model = RDT.getmodel()
    path: str = "./output/damper/RDT.svg"
    wirtefile(path, model)

    model: Model = steelMaterial.getmodel()
    path: str = "./output/damper/steelMaterial.svg"
    wirtefile(path, model)

    model: Model = unitRubbe.getmodel()
    path: str = "./output/damper/unitRubbe.svg"
    wirtefile(path, model)

if __name__ == "__main__":
    run()