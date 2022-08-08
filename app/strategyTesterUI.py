from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

import os


class StrategyTesterUI(QtCore.QObject):

    def __init__(self, controller):
        super(StrategyTesterUI, self).__init__()

        self.controller = controller
        self.view = None
        # It does not finish by a "/"
        loader = QUiLoader(self)
        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.fspath(self.current_dir_path + "/ui/strategyTester.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.view = view = loader.load(ui_file)
        ui_file.close()

        self.runBacktestPB = view.findChild(QtWidgets.QPushButton, "runBacktestPB")
        self.runBacktestPB.clicked.connect(self.run)

        self.runningStratPB = view.findChild(QtWidgets.QProgressBar, "runningStratPB")
        self.startingCashLE = view.findChild(QtWidgets.QLineEdit, "startingCashLE")

        self.strategyNameCB = view.findChild(QtWidgets.QComboBox, "strategyNameCB")
        self.strategyNameCB.currentIndexChanged.connect(self.strategyNameActivated)

        self.runLabel = view.findChild(QtWidgets.QLabel, "runLabel")

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

    def getView(self):
        return self.view