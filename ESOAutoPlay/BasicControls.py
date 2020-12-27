import pynput
from pynput.keyboard import Key
import time
from InfoCollector import InfoCollector


class BasicControls:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if BasicControls.__instance == None:
            BasicControls()
        return BasicControls.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if BasicControls.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            BasicControls.__instance = self


    timeBetweenAttack = 1.15 - 0.20
    keyboard = pynput.keyboard.Controller()
    # keyboard = keyboard

    def click(self, key):
        self.keyboard.press(key)
        # time.sleep(0.15)
        self.keyboard.release(key)
        return

    currentBar = 1
    barChanged = True

    def swapToSpellBar1(self):
        print(BasicControls.swapToSpellBar1.__name__)

        if not self.barChanged and self.currentBar == 1:
            return
        self.barChanged = True

        self.click("`")
        time.sleep(0.15)
        timeStart = time.time()
        s = InfoCollector.getInstance().getInfo()
        # if time.time() - timeStart < 0.1:
        #     time.sleep(0.1 - (time.time() - timeStart))

        if s.currentSkillBar:
            self.currentBar = 1
            self.barChanged = False
            return
        else:
            print("swap to 1 f")
            return self.swapToSpellBar1()

    def swapToSpellBar2(self):
        print(BasicControls.swapToSpellBar2.__name__)

        if not self.barChanged and self.currentBar == 2:
            return
        self.barChanged = True

        self.click("]")
        time.sleep(0.15)
        timeStart = time.time()
        s = InfoCollector.getInstance().getInfo()

        # if time.time() - timeStart < 0.1:
        #     time.sleep(0.1 - (time.time() - timeStart))

        if not s.currentSkillBar:
            self.currentBar = 2
            self.barChanged = False
            return
        else:
            print("swap to 2 f")
            return self.swapToSpellBar2()

    def normalAttack(self):
        self.click(Key.f14)
        time.sleep(0.3)
        # time.sleep(self.timeBetweenAttack)
        return

    def heavyAttack(self, t=2.1):
        self.keyboard.press(Key.f14)
        time.sleep(t)
        self.keyboard.release(Key.f14)
        time.sleep(0.05)
        return

    def spell1(self):
        self.click(Key.f15)
        time.sleep(self.timeBetweenAttack)
        return

    def spell2(self):
        self.click(Key.f16)
        time.sleep(self.timeBetweenAttack)
        return

    def spell3(self):
        self.click(Key.f17)
        time.sleep(self.timeBetweenAttack)
        return

    def spell4(self):
        self.click(Key.f18)
        time.sleep(self.timeBetweenAttack)
        return

    def spell5(self):
        self.click(Key.f19)
        time.sleep(self.timeBetweenAttack)
        return

    def ultimate(self):
        self.click(Key.f13)
        time.sleep(self.timeBetweenAttack)
        return

