from CurrentStates import CurrentStates
from pynput.keyboard import Controller
import _thread
import time


class FollowTarget:
    state: CurrentStates = CurrentStates()

    _using = False
    keyboardC: Controller = None

    _w = False
    _a = False
    _s = False
    _d = False

    def start(self):
        self._using = True

    def end(self):

        if self._using:
            self._using = False

            if self._w:
                self.keyboardC.release("w")
            if self._a:
                self.keyboardC.release("a")
            if self._s:
                self.keyboardC.release("s")
            if self._d:
                self.keyboardC.release("d")

            self._w = False
            self._a = False
            self._s = False
            self._d = False

    def _run(self):
        while 1:
            time.sleep(0.1)
            if not self._using:
                continue
            if self.state.targetDirection.in_front and not self._w:
                self.keyboardC.press("w")
                self._w = True
            elif (not self.state.targetDirection.in_front) and self._w:
                self.keyboardC.release("w")
                self._w = False

            if self.state.targetDirection.left and not self._a:
                self.keyboardC.press("a")
                self._a = True
            elif (not self.state.targetDirection.left) and self._a:
                self.keyboardC.release("a")
                self._a = False

            if self.state.targetDirection.behind and not self._s:
                self.keyboardC.press("s")
                self._s = True
            elif (not self.state.targetDirection.behind) and self._s:
                self.keyboardC.release("s")
                self._s = False

            if self.state.targetDirection.right and not self._d:
                self.keyboardC.press("d")
                self._d = True
            elif (not self.state.targetDirection.right) and self._d:
                self.keyboardC.release("d")
                self._d = False

    def __init__(self):
        _thread.start_new_thread(self._run, ())
        self.keyboardC = Controller()
