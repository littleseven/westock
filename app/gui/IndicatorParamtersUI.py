import typing

import PySide2
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QDialog

from app.gui.uic_indicatorParameters import Ui_Dialog


class IndicatorParametersUI(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setTitle(self, title):
        self.title = self.findChild(QtWidgets.QLabel, "title")
        self.title.setText(title)
        pass

    def addParameter(self, parameterName, defaultValue):
        lineEdit = QtWidgets.QLineEdit(parameterName, self)
        lineEdit.setObjectName(parameterName)
        lineEdit.setText(str(defaultValue))
        self.parameterLayout.addRow(parameterName, lineEdit)
        pass

    def addParameterColor(self, parameterName, defaultValue):
        # Custom color picker
        colorButton = SelectColorButton(parameterName, self)
        self.parameterLayout.addRow(parameterName, colorButton)
        pass

    def getValue(self, parameterName):
        lineEdit = self.findChild(QtWidgets.QLineEdit, parameterName)
        if lineEdit is not None:
            try:
                return int(lineEdit.text())
            except:
                try:
                    return float(lineEdit.text())
                except:
                    try:
                        return lineEdit.text()
                    except:
                        return None
        else:
            return None

    def getColorValue(self, parameterName):
        colorButton = self.findChild(SelectColorButton, parameterName)
        if colorButton is not None:
            try:
                return colorButton.getColor().name()
            except:
                return None
        else:
            return None

    def getView(self):
        return self


class SelectColorButton(QtWidgets.QPushButton):

    def __init__(self, objectName, parent=None):
        super(SelectColorButton, self).__init__()

        self.setColor(QtGui.QColor("yellow"))

        self.setObjectName(objectName)
        self.setParent(parent)
        self.clicked.connect(self.changeColor)

    def setColor(self, color):
        self.color = color
        self.updateColor()

    def getColor(self):
        return self.color

    def updateColor(self):
        self.setStyleSheet("background-color: " + self.color.name())

    def changeColor(self):
        newColor = QtWidgets.QColorDialog.getColor(self.color, self.parentWidget())
        if newColor != self.color:
            self.setColor(newColor)