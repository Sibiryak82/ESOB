from CurrentStates import CurrentStates
from BasicControls import BasicControls
import time
import _thread


class MoveToEnemy:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MoveToEnemy.__instance == None:
            MoveToEnemy()
        return MoveToEnemy.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MoveToEnemy.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MoveToEnemy.__instance = self

    currentStates = CurrentStates()

    def moveTo(self, dis):
        c: BasicControls = BasicControls.getInstance()
        if dis == "s":
            c.keyboard.press("w")
            while self.currentStates.isTargetingEnemy and not self.currentStates.targetInShortRange:
                time.sleep(0.1)
            c.keyboard.release("w")
            return
        else:
            c.keyboard.press("w")
            while self.currentStates.isTargetingEnemy and not self.currentStates.targetInLongRange:
                time.sleep(0.1)
            c.keyboard.release("w")
            return

    def moveToEnemyLong(self):
        _thread.start_new_thread(self.moveTo, ('l',))

    def moveToEnemyShort(self):
        _thread.start_new_thread(self.moveTo, ('s',))