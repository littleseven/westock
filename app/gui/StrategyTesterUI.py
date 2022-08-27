import os

from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget

from app.gui.uic_strategyTester import Ui_Form


class StrategyTesterUI(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.current_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

        self.runBacktestPB = self.findChild(QtWidgets.QPushButton, "runBacktestPB")
        self.runBacktestPB.clicked.connect(self.run)

        self.runningStratPB = self.findChild(QtWidgets.QProgressBar, "runningStratPB")
        self.startingCashLE = self.findChild(QtWidgets.QLineEdit, "startingCashLE")

        self.strategyNameCB = self.findChild(QtWidgets.QComboBox, "strategyNameCB")


        self.runLabel = self.findChild(QtWidgets.QLabel, "runLabel")

        self.runBacktestPB.setEnabled(False)

        # initialize(self):
        self.strategyNameCB.currentIndexChanged.connect(self.strategyNameActivated)
        # adding list of items to combo box
        self.strategyNames = list(QtCore.QDir(self.current_dir_path + "/strategies").entryList(QtCore.QDir.Files))

        # Remove straty .py file name
        self.strategyBaseName = []
        for stratName in self.strategyNames:
            self.strategyBaseName.append(QtCore.QFileInfo(stratName).baseName())

        self.strategyNameCB.addItems(self.strategyBaseName)

        validator = QtGui.QDoubleValidator(-9999999, 9999999, 6, self.startingCashLE)
        validator.setLocale(QtCore.QLocale("zh"))
        self.startingCashLE.setValidator(validator)

        pass

    def setController(self, controller):
        self.controller = controller

    def run(self):
        self.controller.run()

    def strategyNameActivated(self):
        stratBaseName = self.strategyNameCB.currentText()
        if hasattr(self, 'controller'):
            self.controller.addStrategy(stratBaseName)

    # Load an AI Model from Tensor Flow framework
    def loadTFModel(self):

        ai_model_dir = QtWidgets.QFileDialog.getExistingDirectory(self.win, "Open Tensorflow Model",
                                                                  self.current_dir_path)

        # Add the AI Model Strategy
        self.controller.addStrategy("AiTensorFlowModel")

        self.strategyTesterUI.findChild(QtWidgets.QLineEdit, "model").setText(ai_model_dir)
        self.controller.strategyParametersSave("model", ai_model_dir)

        pass

    # Load an AI Model from Py Torch framework
    def loadTorchModel(self):

        ai_model_zip_file = \
        QtWidgets.QFileDialog.getOpenFileName(self.win, "Open Torch Model", self.current_dir_path, "*.zip")[0]

        # Add the AI Model Strategy
        self.controller.addStrategy("AiTorchModel")

        self.strategyTesterUI.findChild(QtWidgets.QLineEdit, "model").setText(ai_model_zip_file)
        self.controller.strategyParametersSave("model", ai_model_zip_file)

        pass

    # Load an AI Model from Stable Baselines framework
    def loadStableBaselinesModel(self):

        ai_model_zip_file = \
        QtWidgets.QFileDialog.getOpenFileName(self.win, "Open Torch Model", self.current_dir_path, "*.zip")[0]

        # Add the AI Model Strategy
        self.controller.addStrategy("AiStableBaselinesModel")

        self.strategyTesterUI.findChild(QtWidgets.QLineEdit, "model").setText(ai_model_zip_file)
        self.controller.strategyParametersSave("model", ai_model_zip_file)

        pass