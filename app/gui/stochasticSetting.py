# from app.gui.indicator import Indicator
from PySide2 import QtCore, QtWidgets

from app.gui.IndicatorParamtersUI import IndicatorParametersUI
from app.utils.fileUtil import FileUtil


class StochasticSetting(object):
    def __init__(self):
        self.load_settings()

    def load_settings(self):
        self.settings = FileUtil.load_sys_settings("indicator.json")
        self.stochastic = stochastic = self.settings["stochastic"]
        self.period = stochastic["period_k"]
        self.smooth_k = stochastic["smooth_k"]
        self.smooth_d = stochastic["smooth_d"]

        self.color = stochastic["color"]

    def save_settings(self):
        FileUtil.save_sys_settings("indicator.json", self.settings)

    def change_settings(self):
        # Show indicator parameter dialog
        paramDialog = IndicatorParametersUI()
        paramDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        paramDialog.setTitle("Stochastic Indicator parameters")
        paramDialog.addParameter("Stochastic Period K", self.period)
        paramDialog.addParameter("Stochastic Smooth K", self.smooth_k)
        paramDialog.addParameter("Stochastic Smooth D", self.smooth_d)
        paramDialog.adjustSize()

        if paramDialog.exec() == QtWidgets.QDialog.Accepted:
            period = paramDialog.getValue("Stochastic Period K")
            smooth_k = paramDialog.getValue("Stochastic Smooth K")
            smooth_d = paramDialog.getValue("Stochastic Smooth D")

            self.stochastic["period_k"] = period
            self.stochastic["smooth_k"] = smooth_k
            self.stochastic["smooth_d"] = smooth_d

            self.save_settings()

        pass
