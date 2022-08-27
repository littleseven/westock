# from app.gui.indicator import Indicator
from PySide2 import QtCore, QtWidgets

from app.gui.IndicatorParamtersUI import IndicatorParametersUI
from app.utils.fileUtil import FileUtil


class RsiSetting(object):
    def __init__(self):
        self.load_settings()

    def load_settings(self):
        self.settings = FileUtil.load_sys_settings("indicator.json")
        self.rsi = rsi = self.settings["rsi"]
        self.period = rsi["period"]
        self.color = rsi["color"]

    def save_settings(self):
        FileUtil.save_sys_settings("indicator.json", self.settings)

    def change_settings(self):
        # Show indicator parameter dialog
        paramDialog = IndicatorParametersUI()
        paramDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        paramDialog.setTitle("RSI Indicator parameters")
        paramDialog.addParameter("RSI Period", self.period)
        paramDialog.addParameterColor("Plot color", self.color)
        paramDialog.adjustSize()

        if paramDialog.exec() == QtWidgets.QDialog.Accepted:
            period = paramDialog.getValue("RSI Period")
            qColor = paramDialog.getColorValue("Plot color")
            self.rsi["period"] = period
            self.rsi["color"] = qColor
            self.save_settings()

        pass
