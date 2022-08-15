from PySide2 import QtCore

import os

from app.gui.StrategyTesterUI import StrategyTesterUI


class StrategyTesterController(QtCore.QObject):

    def __init__(self, controller):
        super(StrategyTesterController, self).__init__()

        self.controller = controller
        self.view = StrategyTesterUI()
        self.view.setController(self.controller)
        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))

    def run(self):
        self.controller.run()

    def getView(self):
        return self.view
