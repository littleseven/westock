from PySide2 import QtCore, QtWidgets

import os

from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class StrategyResultsUI(QtWidgets.QWidget):

    def __init__(self, controller):
        super(StrategyResultsUI, self).__init__()

        self.controller = controller

        # It does not finish by a "/"
        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))

        loader = QUiLoader()
        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.fspath(self.current_dir_path + "/ui/strategyResults.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

        self.SummaryGB = self.findChild(QtWidgets.QGroupBox, "SummaryGB")
        self.TradesGB = self.findChild(QtWidgets.QGroupBox, "TradesGB")
        self.ResultsTabWidget = self.findChild(QtWidgets.QTabWidget, "ResultsTabWidget")

    