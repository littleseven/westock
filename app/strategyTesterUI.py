from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

import os


class StrategyTesterUI(QtWidgets.QWidget):

    def __init__(self, controller):
        super(StrategyTesterUI, self).__init__()

        self.controller = controller

        # It does not finish by a "/"
        loader = QUiLoader()
        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.fspath(self.current_dir_path + "/ui/strategyTester.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


        self.runBacktestPB = self.findChild(QtWidgets.QPushButton, "runBacktestPB")
        self.runBacktestPB.clicked.connect(self.run)

        self.runningStratPB = self.findChild(QtWidgets.QProgressBar, "runningStratPB")
        self.startingCashLE = self.findChild(QtWidgets.QLineEdit, "startingCashLE")

        self.strategyNameCB = self.findChild(QtWidgets.QComboBox, "strategyNameCB")
        self.strategyNameCB.currentIndexChanged.connect(self.strategyNameActivated)

        self.runLabel = self.findChild(QtWidgets.QLabel, "runLabel")

        self.runBacktestPB.setEnabled(False)

    def initialize(self):
        # adding list of items to combo box
        self.strategyNames = list(QtCore.QDir(self.current_dir_path + "/strategies").entryList(QtCore.QDir.Files))

        # Remove straty .py file name
        self.strategyBaseName = []
        for stratName in self.strategyNames:
            self.strategyBaseName.append(QtCore.QFileInfo(stratName).baseName())

        self.strategyNameCB.addItems(self.strategyBaseName)

        pass

    def run(self):
        self.controller.run()

    def strategyNameActivated(self):
        stratBaseName = self.strategyNameCB.currentText()
        self.controller.addStrategy(stratBaseName)
