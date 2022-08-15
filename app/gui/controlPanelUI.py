from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget


class ControlPanelUI(QWidget):
    def __init__(self, parent, interface):
        super(ControlPanelUI, self).__init__(parent)
        self.interface = interface
        self.setUpUi()

    def setUpUi(self):
        self.controlPanelLayout = QtWidgets.QHBoxLayout(self)
        # Rest
        self.ResetPB = QtWidgets.QPushButton(self)
        self.ResetPB.setText("Reset")
        self.ResetPB.setCheckable(True)
        self.ResetPB.setMaximumWidth(100)
        self.ResetPB.toggled.connect(self.interface.resetChart)
        self.controlPanelLayout.addWidget(self.ResetPB)

        # Spacer
        spacer = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum)
        self.controlPanelLayout.addSpacerItem(spacer)

        # SMA
        self.SmaPB = QtWidgets.QPushButton(self)
        self.SmaPB.setText("SMA")
        self.SmaPB.setCheckable(True)
        self.SmaPB.setMaximumWidth(100)
        self.SmaPB.toggled.connect(self.interface.addSma)
        self.controlPanelLayout.addWidget(self.SmaPB)

        # EMA
        self.EmaPB = QtWidgets.QPushButton(self)
        self.EmaPB.setText("EMA")
        self.EmaPB.setCheckable(True)
        self.EmaPB.setMaximumWidth(100)
        self.EmaPB.toggled.connect(self.interface.addEma)
        self.controlPanelLayout.addWidget(self.EmaPB)

        # Spacer
        spacer = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum)
        self.controlPanelLayout.addSpacerItem(spacer)

        # RSI
        self.RsiPB = QtWidgets.QPushButton(self)
        self.RsiPB.setText("RSI")
        self.RsiPB.setCheckable(True)
        self.RsiPB.setMaximumWidth(100)
        self.RsiPB.toggled.connect(self.interface.toogleRsi)
        self.controlPanelLayout.addWidget(self.RsiPB)

        # Stochastic
        self.StochasticPB = QtWidgets.QPushButton(self)
        self.StochasticPB.setText("Stochastic")
        self.StochasticPB.setCheckable(True)
        self.StochasticPB.setMaximumWidth(100)
        self.StochasticPB.toggled.connect(self.interface.toogleStochastic)
        self.controlPanelLayout.addWidget(self.StochasticPB)

        # Stochastic RSI
        self.StochasticRsiPB = QtWidgets.QPushButton(self)
        self.StochasticRsiPB.setText("Stochastic RSI")
        self.StochasticRsiPB.setCheckable(True)
        self.StochasticRsiPB.setMaximumWidth(100)
        self.StochasticRsiPB.toggled.connect(self.interface.toogleStochasticRsi)
        self.controlPanelLayout.addWidget(self.StochasticRsiPB)

        # Ichimoku
        self.IchimokuPB = QtWidgets.QPushButton(self)
        self.IchimokuPB.setText("Ichimoku")
        self.IchimokuPB.setCheckable(True)
        self.IchimokuPB.setMaximumWidth(100)
        self.IchimokuPB.toggled.connect(self.interface.toogleIchimoku)
        self.controlPanelLayout.addWidget(self.IchimokuPB)

        # Spacer 
        spacer = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum)
        self.controlPanelLayout.addSpacerItem(spacer)

        # Dark mode
        self.darkmodeCB = QtWidgets.QCheckBox(self)
        self.darkmodeCB.setText('Dark mode')
        self.darkmodeCB.toggled.connect(self.interface.dark_mode_toggle)
        self.darkmodeCB.setChecked(True)
        self.controlPanelLayout.addWidget(self.darkmodeCB)

        # Volumes
        self.volumesCB = QtWidgets.QCheckBox(self)
        self.volumesCB.setText('Volumes')
        self.volumesCB.toggled.connect(self.interface.volumes_toggle)
        # init checked after connecting the slot
        self.volumesCB.setChecked(False)
        self.controlPanelLayout.addWidget(self.volumesCB)

        # Spacer
        self.controlPanelLayout.insertSpacerItem(0,QtWidgets.QSpacerItem(0, 0, hPolicy=QtWidgets.QSizePolicy.Expanding,
                                                                       vPolicy=QtWidgets.QSizePolicy.Preferred))