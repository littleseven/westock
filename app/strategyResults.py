from PySide2 import QtCore

from app.gui.StrategyResultsUI import StrategyResultsUI


class StrategyResults(QtCore.QObject):

    def __init__(self, controller):
        self.controller = controller
        self.view = StrategyResultsUI()

    def getView(self):
        return self.view
