import os

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QWidget

from app.gui.uic_loadDataFiles import Ui_Form
from app.utils.fileUtil import FileUtil


class LoadDataFileUI(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.current_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

        self.dataFileName = self.filePathLE.text()

        self.openFilePB = self.findChild(QtWidgets.QToolButton, "openFilePB")
        self.loadFilePB = self.findChild(QtWidgets.QPushButton, "loadFilePB")
        self.importPB = self.findChild(QtWidgets.QPushButton, "importPB")

        self.errorLabel = self.findChild(QtWidgets.QLabel, "errorLabel")

        self.dataFilesListWidget = self.findChild(QtWidgets.QListWidget, "dataFilesListWidget")
        # Default values
        self.datetimeFormatLE.setText("%Y-%m-%d %H:%M:%S")

        self.openFilePB.clicked.connect(self.openFile)
        self.loadFilePB.clicked.connect(self.loadFile)
        self.importPB.clicked.connect(self.importFiles)

        self.hide()

    def setController(self, controller):
        self.controller = controller

    def openFile(self):
        self.dataFileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open data file',
                                                                  self.current_dir_path + "/data",
                                                                  "CSV files (*.csv)")[0]
        self.filePathLE.setText(self.dataFileName)
        pass

    def loadFile(self):

        # try loading file by controller
        separator = '\t' if self.tabRB.isChecked() else ',' if self.commaRB.isChecked() else ';'
        success, errorMessage = FileUtil.loadData(self.controller.dataframes, self.dataFileName, self.datetimeFormatLE.text(),
                                         separator)

        if success:

            self.errorLabel.setStyleSheet("color:green")
            self.errorLabel.setText("The file has been loaded correctly.")

            # Add file name
            fileName = os.path.basename(self.dataFileName)
            items = self.dataFilesListWidget.findItems(fileName, QtCore.Qt.MatchFixedString)

            if len(items) == 0:
                self.dataFilesListWidget.addItem(os.path.basename(self.dataFileName))

        else:

            self.errorLabel.setStyleSheet("color:red")
            self.errorLabel.setText(errorMessage)

        pass
    
    def importFiles(self):

        # Get all element in list widget
        items = []
        for x in range(self.dataFilesListWidget.count()):
            items.append(self.dataFilesListWidget.item(x).text())

        # Sort item by timeframe

        # Give all ordered data path to the controller
        if self.controller.importData(items):
            self.dataFilesListWidget.clear()
            self.hide()

        pass