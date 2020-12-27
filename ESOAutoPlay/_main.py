import pynput
from pynput.keyboard import Key
import _thread
import time
from BasicControls import BasicControls
import _Configuration
from SearchForEnemy.MoveToEnemy import MoveToEnemy
from InfoCollector import InfoCollector
from CurrentStates import CurrentStates


class ESOAutoPlay:
    isPlaying = False
    useEnemyFinder = _Configuration.useEnemyFinder
    useFollowTarget = _Configuration.useFollowTarget
    isRuning = True

    def startListener(self):
        def on_press(key):

            return

        def on_release(key):

            if key == Key.delete or key == Key.caps_lock:
                self.isRuning = False
                self.isPlaying = False
                return False

            if f"{key}" == "'\\\\'":
                print("start")
                if not self.isPlaying:
                    self.isPlaying = True
                    BasicControls.getInstance().barChanged = True


            if key == Key.backspace:
                print("END")
                self.isPlaying = False
                self.useEnemyFinder = False

        with pynput.keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

        return

    def startController(self):
        from ActionMaker import ActionMaker

        actionM = ActionMaker(self)
        actionM.start()

    def start(self):
        _thread.start_new_thread(self.startListener, ())
        # _thread.start_new_thread(self.startController, ())
        self.startController()
        print("START\n")

        return


if __name__ == "__main__":
    gamePlayer = ESOAutoPlay()
    gamePlayer.start()

    while gamePlayer.isRuning:
        time.sleep(5)

