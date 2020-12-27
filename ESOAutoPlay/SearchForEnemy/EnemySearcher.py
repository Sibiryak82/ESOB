from CurrentStates import CurrentStates
from pynput.mouse import Button, Controller
import time
import _thread


class EnemySearcher:
    currentStates = CurrentStates()

    mouseC = Controller()
    _needSearch = False
    _startT = 0

    def __init__(self):
        _thread.start_new_thread(self.search, ())

    def resetCamera(self):
        self.mouseC.move(0, 1500)
        time.sleep(0.1)
        self.mouseC.move(0, -700)
        time.sleep(0.1)

    def search(self):
        while True:
            if self._needSearch:
                if not self.currentStates.isTargetingEnemy:
                    if time.time() - self._startT < 2:
                        self.mouseC.move(10, 0)
                        time.sleep(0.02 * 0.8)
                    else:
                        self.mouseC.move(-10, 0)
                        time.sleep(0.02 * 0.8)
                else:
                    self._needSearch = False
            else:
                time.sleep(0.1)

    def startSearch(self):
        if not self._needSearch:
            self.resetCamera()
            self._needSearch = True
            self._startT = time.time()

    def endSearch(self):
        self._needSearch = False
