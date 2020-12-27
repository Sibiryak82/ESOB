import time
import numpy as np
import Quartz.CoreGraphics as CG

from CurrentStates import CurrentStates


def ColorIsMatch(c1, c2):
    if (c1.size != 3) or (len(c2) != 3):
        return False
    if not [x for x in c1 + c2 if x > 35]:
        return True

    if abs(c1[0] - c2[0]) < 5 and abs(c1[1] - c2[1]) < 5 and abs(c1[2] - c2[2]) < 5:
        return True
    else:
        return False


class InfoCollector:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if InfoCollector.__instance == None:
            InfoCollector()
        return InfoCollector.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if InfoCollector.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            InfoCollector.__instance = self


    TrueColor = [208, 168, 77]
    FalseColor = [0, 0, 0]
    #
    # damageShieldColorPosition = [1948, 2015]
    # healthColorPosition = [1962, 2015]
    # magickaColorPosition = [1976, 2015]
    # staminaColorPosition = [1991, 2015]
    # currentSkillBarPosition = [2005, 2015]
    # isTargetingEnemyPosition = [2020, 2015]


    def getInfo(self):
        coloers = self.getColors()
        # print(damageShieldColor, healthColor, magickaColor, staminaColor)

        states = CurrentStates()

        states.gameIsReady = all(coloers[0] == self.TrueColor)

        states.haveDamageShield = all(coloers[1] == self.TrueColor)

        states.haveEnoughHealth = all(coloers[2] == self.TrueColor)

        states.haveEnoughMagicka = all(coloers[3] == self.TrueColor)

        states.haveEnoughStamina = all(coloers[4] == self.TrueColor)

        states.currentSkillBar = all(coloers[5] == self.TrueColor)

        states.isTargetingEnemy = all(coloers[6] == self.TrueColor)

        states.targetInShortRange = all(coloers[7] == self.TrueColor)

        states.targetInLongRange = all(coloers[8] == self.TrueColor)

        states.canUseUlt = all(coloers[9] == self.TrueColor)

        states.sp1 = all(coloers[10] == self.TrueColor)

        states.targetDirection.in_front = all(coloers[11] == self.TrueColor)

        states.targetDirection.behind = all(coloers[12] == self.TrueColor)

        states.targetDirection.right = all(coloers[13] == self.TrueColor)

        states.targetDirection.left = all(coloers[14] == self.TrueColor)

        return states

    def takeScreenshot(self):
        image = CG.CGWindowListCreateImage(CG.CGRectInfinite, CG.kCGWindowListOptionOnScreenOnly, CG.kCGNullWindowID,
                                           CG.kCGWindowImageDefault)

        prov = CG.CGImageGetDataProvider(image)
        _data = CG.CGDataProviderCopyData(prov)

        width = CG.CGImageGetWidth(image)
        height = CG.CGImageGetHeight(image)

        imgdata = np.frombuffer(_data, dtype=np.uint8).reshape(int(len(_data) / 4.0), 4)

        numpy_img = imgdata[:width * height, :-1].reshape(height, width, 3)
        return numpy_img

    def getColors(self):
        numpy_img = self.takeScreenshot()

        # print(numpy_img.shape)
        # return [numpy_img[1944 + n * 6 + 2][2013] for n in range(15)]
        return [numpy_img[1925 + n * 6 + 2][2013] for n in range(15)]
        # return [numpy_img[self.damageShieldColorPosition[0]][self.damageShieldColorPosition[1]],
        #         numpy_img[self.healthColorPosition[0]][self.healthColorPosition[1]],
        #         numpy_img[self.magickaColorPosition[0]][self.magickaColorPosition[1]],
        #         numpy_img[self.staminaColorPosition[0]][self.staminaColorPosition[1]],
        #         numpy_img[self.currentSkillBarPosition[0]][self.currentSkillBarPosition[1]],
        #         numpy_img[self.isTargetingEnemyPosition[0]][self.isTargetingEnemyPosition[1]]
        #         ]  # damageShieldColor, Health Color, Magicka Color,  Stamina Color


if __name__ == "__main__":
    i = InfoCollector()
    time.sleep(3)
    import matplotlib.pyplot as plt
    img = i.takeScreenshot()

    # for n in range(9):
    #     img[1944 + n * 6 + 2][2013] = (255, 255, 255)

    plt.imshow(img)
    plt.show()
    # print(i.getInfo())



# (2100, 5584, 3)
# (2100, 3360, 3)

# 2015, 1948
# 2015, 1962
# 2015, 1976
# 2015, 1991
# 2015, 2005
# 2015, 2020
