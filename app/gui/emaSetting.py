# from app.gui.indicator import Indicator
from PySide2 import QtCore, QtWidgets

from app.gui.IndicatorParamtersUI import IndicatorParametersUI
from app.utils.fileUtil import FileUtil


class EmaSetting(object):
    def __init__(self):
        self.load_settings()

    def load_settings(self):
        self.settings = FileUtil.load_sys_settings("indicator.json")
        self.sma = sma = self.settings["sma"]
        self.period = sma["period"]
        self.width = sma["width"]
        self.color = sma["color"]

    def save_settings(self):
        FileUtil.save_sys_settings("indicator.json", self.settings)

    def change_settings(self):
        # Show indicator parameter dialog
        paramDialog = IndicatorParametersUI()
        paramDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        paramDialog.setTitle("EMA Indicator parameters")
        paramDialog.addParameter("EMA Period", 9)
        paramDialog.addParameter("Plot width", 1)
        paramDialog.addParameterColor("Plot color", "#FFFF00")
        paramDialog.adjustSize()

        if paramDialog.exec() == QtWidgets.QDialog.Accepted:
            period = paramDialog.getValue("EMA Period")
            width = paramDialog.getValue("Plot width")
            qColor = paramDialog.getColorValue("Plot color")
            self.sma["period"] = period
            self.sma["width"] = width
            self.sma["color"] = qColor
            self.save_settings()
            # self.fpltWindow[self.current_timeframe].drawEma(period, qColor, width)

        pass

        pass
