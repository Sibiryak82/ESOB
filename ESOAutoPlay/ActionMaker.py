from Spells.Idle import Idle
import time
from _main import ESOAutoPlay
from _Configuration import usingSkillSetUp
from InfoCollector import InfoCollector
from CurrentStates import CurrentStates
from SearchForEnemy.MoveToEnemy import MoveToEnemy
from SearchForEnemy.EnemySearcher import EnemySearcher
import _thread
from BasicControls import BasicControls
from FollowTarget import FollowTarget


class ActionMaker:
    isBlocking = False
    mainC: ESOAutoPlay = None
    states: CurrentStates = None
    enemySearcher: EnemySearcher = None
    followTarget: FollowTarget = None
    _lastTimeGetInfo = 0.0

    def __init__(self, mainC: ESOAutoPlay):
        self.mainC = mainC
        self.enemySearcher = EnemySearcher()
        self.followTarget = FollowTarget()

    def start(self):
        _thread.start_new_thread(self.startGetInfo, ())
        _thread.start_new_thread(self.startAction, ())

    def startGetInfo(self):
        while True:
            if self.mainC.isPlaying:
                self.states = InfoCollector.getInstance().getInfo()
                # print(self.states)
                self._lastTimeGetInfo = time.time()

                MoveToEnemy.getInstance().currentStates = self.states
                self.enemySearcher.currentStates = self.states
                self.followTarget.state = self.states

                if self.states.currentSkillBar == True:
                    BasicControls.getInstance().currentBar = 1
                else:
                    BasicControls.getInstance().currentBar = 2
                time.sleep(0.01)

            else:
                time.sleep(0.3)

    def startAction(self):
        while True:
            if self.mainC.isPlaying and time.time() - self._lastTimeGetInfo < 0.5 and self.states.gameIsReady:

                if self.mainC.useEnemyFinder and not self.states.isTargetingEnemy:
                    self.enemySearcher.startSearch()
                if self.mainC.useFollowTarget:
                    self.followTarget.start()

                time.sleep(0.16)
                self.makeActionAndRun()


            else:
                self.enemySearcher.endSearch()
                self.followTarget.end()
                time.sleep(0.3)


    def makeAction(self):
        if self.isBlocking:
            return Idle(0)


        for spell in usingSkillSetUp:
            if spell.shouldUseThisSpell(self.states):

                # print(f"spell name: {spell.spellName}, {spell.spellSlot}")

                return spell

    def makeActionAndRun(self):

        self.makeAction().use()


        return
