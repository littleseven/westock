from PySide2 import QtCore, QtWidgets

import os

from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class LoadDataFilesUI(QtCore.QObject):

    def __init__(self, controller, parent=None):

        super(LoadDataFilesUI, self).__init__()

        self.controller = controller

        self.parent = parent
        # self.setParent(parent)

        # It does not finish by a "/"
        loader = QUiLoader()
        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.fspath(self.current_dir_path + "/ui/loadDataFiles.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.view = view = loader.load(ui_file)
        ui_file.close()

        # self.filePathLE = view.findChild(QtWidgets.QLineEdit, "filePathLE")
        # self.datetimeFormatLE = view.findChild(QtWidgets.QLineEdit, "datetimeFormatLE")
        #
        # self.tabRB = view.findChild(QtWidgets.QRadioButton, "tabRB")
        # self.commaRB = view.findChild(QtWidgets.QRadioButton, "commaRB")
        # self.semicolonRB = view.findChild(QtWidgets.QRadioButton, "semicolonRB")

        self.openFilePB = view.findChild(QtWidgets.QToolButton, "openFilePB")
        self.loadFilePB = view.findChild(QtWidgets.QPushButton, "loadFilePB")
        # self.deletePB = view.findChild(QtWidgets.QLineEdit, "deletePB")
        self.importPB = view.findChild(QtWidgets.QPushButton, "importPB")

        self.errorLabel = view.findChild(QtWidgets.QLabel, "errorLabel")

        self.dataFilesListWidget = view.findChild(QtWidgets.QListWidget, "dataFilesListWidget")

        # Default values
        self.view.datetimeFormatLE.setText("%Y-%m-%d %H:%M:%S")

        # Connect slots : open file
        self.openFilePB.clicked.connect(self.openFile)
        self.loadFilePB.clicked.connect(self.loadFile)
        self.importPB.clicked.connect(self.importFiles)
        pass

    def openFile(self):
        self.dataFileName = \
        QtWidgets.QFileDialog.getOpenFileName(self.view, 'Open data file', self.current_dir_path + "/data",
                                              "CSV files (*.csv)")[0]
        self.view.filePathLE.setText(self.dataFileName)
        pass

    def loadFile(self):

        # try loading file by controller
        separator = '\t' if self.view.tabRB.isChecked() else ',' if self.view.commaRB.isChecked() else ';'
        success, errorMessage = self.controller.loadData(self.dataFileName, self.view.datetimeFormatLE.text(), separator)

        if success:

            self.view.errorLabel.setStyleSheet("color:green")
            self.view.errorLabel.setText("The file has been loaded correctly.")

            # Add file name
            fileName = os.path.basename(self.dataFileName)
            items = self.view.dataFilesListWidget.findItems(fileName, QtCore.Qt.MatchFixedString)

            if len(items) == 0:
                self.view.dataFilesListWidget.addItem(os.path.basename(self.dataFileName))

        else:

            self.view.errorLabel.setStyleSheet("color:red")
            self.view.errorLabel.setText(errorMessage)

        pass

    def importFiles(self):

        # Get all element in list widget
        items = []
        for x in range(self.view.dataFilesListWidget.count()):
            items.append(self.view.dataFilesListWidget.item(x).text())

        # Sort item by timeframe

        # Give all ordered data path to the controller
        if self.controller.importData(items):
            self.view.dataFilesListWidget.clear()
            self.view.hide()

        pass

    def hide(self):
        self.view.hide()

    def show(self):
        self.view.show()
    '''
    def showEvent(self, ev):
        # Move at the center of the window
        #if self.parent is not None:

        #    x = int(self.parent.sizeHint().width() / 2 - self.sizeHint().width())
        #    y = int(self.parent.sizeHint().height() / 2 - self.sizeHint().height()) 
        
        #    self.move( x, y )

        return QtWidgets.showEvent(self, ev)
    '''
