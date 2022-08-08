from PySide2 import QtCore, QtWidgets

import os

from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class StrategyResultsUI(QtCore.QObject):

    def __init__(self, controller):
        # super(StrategyResultsUI, self).__init__()

        self.controller = controller

        # It does not finish by a "/"
        loader = QUiLoader()
        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.fspath(self.current_dir_path + "/ui/strategyResults.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.view = view = loader.load(ui_file)
        ui_file.close()

        # self.SummaryGB = view.findChild(QtWidgets.QGroupBox, "SummaryGB")
        # self.TradesGB = view.findChild(QtWidgets.QGroupBox, "TradesGB")
        # self.ResultsTabWidget = view.findChild(QtWidgets.QTabWidget, "ResultsTabWidget")

    def getView(self):
        return self.view
