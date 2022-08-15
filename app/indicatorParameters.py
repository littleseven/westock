from PySide2 import QtCore, QtWidgets, QtGui

import os
from gui.IndicatorParamtersUI import IndicatorParametersUI
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class IndicatorParametersController(QtCore.QObject):

    def __init__(self, parent=None):
        super(IndicatorParametersController, self).__init__()

        # self.setParent(parent)
        self.view = IndicatorParametersUI(parent)
        # It does not finish by a "/"
        # loader = QUiLoader()
        # self.current_dir_path = os.path.dirname(os.path.realpath(__file__))
        # path = os.fspath(self.current_dir_path + "/ui/indicatorParameters.ui")
        # ui_file = QFile(path)
        # ui_file.open(QFile.ReadOnly)
        # self.view = loader.load(ui_file)
        # ui_file.close()
        pass

#     def setTitle(self, title):
#         self.title = self.view.findChild(QtWidgets.QLabel, "title")
#         self.title.setText(title)
#         pass
#
#     def addParameter(self, parameterName, defaultValue):
#         lineEdit = QtWidgets.QLineEdit(parameterName, self.view)
#         lineEdit.setObjectName(parameterName)
#         lineEdit.setText(str(defaultValue))
#         self.view.parameterLayout.addRow(parameterName, lineEdit)
#         pass
#
#     def addParameterColor(self, parameterName, defaultValue):
#         # Custom color picker
#         colorButton = SelectColorButton(parameterName, self.view)
#         self.view.parameterLayout.addRow(parameterName, colorButton)
#         pass
#
#     def getValue(self, parameterName):
#         lineEdit = self.view.findChild(QtWidgets.QLineEdit, parameterName)
#         if lineEdit is not None:
#             try:
#                 return int(lineEdit.text())
#             except:
#                 try:
#                     return float(lineEdit.text())
#                 except:
#                     try:
#                         return lineEdit.text()
#                     except:
#                         return None
#         else:
#             return None
#
#     def getColorValue(self, parameterName):
#         colorButton = self.view.findChild(SelectColorButton, parameterName)
#         if colorButton is not None:
#             try:
#                 return colorButton.getColor().name()
#             except:
#                 return None
#         else:
#             return None
#
#     def getView(self):
#         return self.view
#
#
# class SelectColorButton(QtWidgets.QPushButton):
#
#     def __init__(self, objectName, parent=None):
#         super(SelectColorButton, self).__init__()
#
#         self.setColor(QtGui.QColor("yellow"))
#
#         self.setObjectName(objectName)
#         self.setParent(parent)
#         self.clicked.connect(self.changeColor)
#
#     def setColor(self, color):
#         self.color = color
#         self.updateColor()
#
#     def getColor(self):
#         return self.color
#
#     def updateColor(self):
#         self.setStyleSheet("background-color: " + self.color.name())
#
#     def changeColor(self):
#         newColor = QtWidgets.QColorDialog.getColor(self.color, self.parentWidget())
#         if newColor != self.color:
#             self.setColor(newColor)
