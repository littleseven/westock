###############################################################################
#
# Copyright (C) 2021 - Skinok
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from PySide2 import QtWidgets

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2.QtWidgets import QDockWidget
from numpy import NaN

from pyqtgraph.dockarea import DockArea, Dock

import sys, os

from app.gui import controlPanelUI

sys.path.append('../finplot')
import finplot as fplt
import backtrader as bt

# Ui made with Qt Designer
import strategyTester
import strategyResults
import indicatorParameters
import loadDataFiles

# Import Chart lib
import finplotWindow

import datetime

import qdarkstyle

import pandas as pd
import functools

os.environ['QT_MAC_WANTS_LAYER'] = '1'


class UserInterface:

    def __init__(self, controller):

        self.controller = controller

        # It does not finish by a "/"
        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))

        # Qt 
        self.app = QtWidgets.QApplication([])
        self.win = QtWidgets.QMainWindow()
        desktop = self.app.desktop()
        if desktop.screenCount() > 1:
            primaryScreen = desktop.primaryScreen()
            self.widget = desktop.screen(primaryScreen)
        else:
            self.widget = desktop
        print("屏幕宽:" + str(self.widget.width()))
        print("屏幕高:" + str(self.widget.height()))

        self.winWidth = int(self.widget.width() * 0.9)
        self.winHeight = int(self.widget.height() * 0.9)

        self.chartWidth = self.winWidth * 0.8
        self.chartHeight = self.winHeight * 0.8

        self.leftPanelWidth = self.winWidth * 0.2
        self.leftPanelHeight = self.chartHeight

        self.bottomPanelWidth = self.winWidth
        self.bottomPanelHeight = self.winHeight * 0.2

        # All dock area of each time frame
        self.dockAreaTimeframes = {}
        self.dock_charts = {}
        self.dock_rsi = {}
        self.dock_stochastic = {}
        self.dock_stochasticRsi = {}
        self.fpltWindow = {}
        self.timeFramePB = {}

        # self.current_timeframe = "H1"
        # Resize windows properties
        self.win.resize(self.winWidth, self.winHeight)
        self.win.setWindowTitle("WeStock v0.3")

        # Set width/height of QSplitter
        self.app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

        pass

    def initialize(self):

        # Docks
        self.createMainDocks()

        # Create all buttons above the chart window
        self.createControlPanel()

        self.createUIs()

        # Enable run button
        # self.strategyTesterUI.runBacktestPB.setEnabled(False)
        #
        # self.strategyTesterUI.initialize()

        pass


    #########
    #  Create all main window docks
    #########
    def createMainDocks(self):
        self.dockArea = DockArea()
        self.win.setCentralWidget(self.dockArea)

        # Create Stacked widget
        self.dock_stackedCharts = Dock("dock_stackedCharts", size=(1000, 500), closable=False, hideTitle=True)
        self.dockArea.addDock(self.dock_stackedCharts, position='above')

        self.stackedCharts = QtWidgets.QStackedWidget(self.dock_stackedCharts)
        self.dock_stackedCharts.addWidget(self.stackedCharts, 1, 0)

        # Create Strategy Tester Tab
        self.dock_strategyTester = Dock("Strategy Tester", size=(200, 500), closable=False, hideTitle=True)
        self.dockArea.addDock(self.dock_strategyTester, position='left')

        # Create Strategy Tester Tab
        self.dock_strategyResults = Dock("Strategy Tester", size=(1000, 250), closable=False, hideTitle=True)
        self.dockArea.addDock(self.dock_strategyResults, position='bottom')

        pass
    #########
    #  Create all chart dock for ONE timeframe
    #########
    def createChartDock(self, timeframe):

        # this need to be changed later
        self.current_timeframe = timeframe

        # Each time frame has its own dock area
        self.dockAreaTimeframes[timeframe] = DockArea()
        self.stackedCharts.addWidget(self.dockAreaTimeframes[timeframe])

        # Create Chart widget
        self.dock_charts[timeframe] = Dock("dock_chart_" + timeframe, size=(self.chartWidth, self.chartHeight * 0.6), closable=False, hideTitle=True)
        self.dockAreaTimeframes[timeframe].addDock(self.dock_charts[timeframe])

        # Create Order widget
        self.dock_rsi[timeframe] = Dock("RSI", size=(self.chartWidth, self.chartHeight * 0.15), closable=False, hideTitle=True)
        self.dockAreaTimeframes[timeframe].addDock(self.dock_rsi[timeframe], position='bottom',
                                                   relativeTo=self.dock_charts[timeframe])
        self.dock_rsi[timeframe].hide()

        self.dock_stochastic[timeframe] = Dock("Stochastic", size=(self.chartWidth, self.chartHeight * 0.15), closable=False, hideTitle=True)
        self.dockAreaTimeframes[timeframe].addDock(self.dock_stochastic[timeframe], position='bottom',
                                                   relativeTo=self.dock_charts[timeframe])
        self.dock_stochastic[timeframe].hide()

        self.dock_stochasticRsi[timeframe] = Dock("Stochastic Rsi", size=(self.chartWidth, self.chartHeight * 0.15), closable=False, hideTitle=True)
        self.dockAreaTimeframes[timeframe].addDock(self.dock_stochasticRsi[timeframe], position='bottom',
                                                   relativeTo=self.dock_charts[timeframe])
        self.dock_stochasticRsi[timeframe].hide()

        # Create finplot Window
        self.fpltWindow[timeframe] = finplotWindow.FinplotWindow(self.dockAreaTimeframes[timeframe],
                                                                 self.dock_charts[timeframe], self)
        self.fpltWindow[timeframe].createPlotWidgets(timeframe)
        self.fpltWindow[timeframe].show()

        # Create timeframe button
        self.timeFramePB[timeframe] = QtWidgets.QRadioButton(self.controlPanel)
        self.timeFramePB[timeframe].setText(timeframe)
        self.timeFramePB[timeframe].setCheckable(True)
        self.timeFramePB[timeframe].setMaximumWidth(100)
        self.timeFramePB[timeframe].toggled.connect(lambda: self.toogleTimeframe(timeframe))
        self.timeFramePB[timeframe].toggle()

        self.controlPanelLayout.insertWidget(0, self.timeFramePB[timeframe])

        # init checked after connecting the slot
        if self.darkmodeCB.isChecked():
            self.dark_mode_toggle()

        pass

    #########
    #   Create all dock contents
    #########
    def createUIs(self):

        self.createStrategyTesterUI()
        self.createTradesUI()
        self.createLoadDataFilesUI()
        # self.createOrdersUI()
        self.createSummaryUI()

        self.createActions()
        self.createMenuBar()

        pass

    #########
    #  Quick menu actions
    #########
    def createActions(self):

        # Data sources
        self.backtestDataActionGroup = QtWidgets.QActionGroup(self.win)

        self.openCSVAction = QtWidgets.QAction(QtGui.QIcon(""), "Open CSV File", self.backtestDataActionGroup)
        self.openCSVAction.triggered.connect(self.loadDataFile.view.show)

        # AI
        self.aiActionGroup = QtWidgets.QActionGroup(self.win)

        self.loadTFModelAction = QtWidgets.QAction(QtGui.QIcon(""), "Load Tensorflow Model", self.aiActionGroup)
        self.loadTFModelAction.triggered.connect(self.strategyTesterUI.loadTFModel)

        # self.loadTorchModelAction = QtWidgets.QAction(QtGui.QIcon(""),"Load Torch Model", self.aiActionGroup)
        # self.loadTorchModelAction.triggered.connect( self.loadTorchModel )

        self.loadStableBaselines3Action = QtWidgets.QAction(QtGui.QIcon(""), "Load Stable Baselines 3 Model",
                                                            self.aiActionGroup)
        self.loadStableBaselines3Action.triggered.connect(self.strategyTesterUI.loadStableBaselinesModel)

        # Options
        self.optionsActionGroup = QtWidgets.QActionGroup(self.win)

        pass

    #########
    #  UI : main window menu bar
    #########
    def createMenuBar(self):

        self.menubar = self.win.menuBar()

        # self.indicatorsMenu = self.menubar.addMenu("Indicators")
        # self.indicatorsMenu.addActions(self.indicatorsActionGroup.actions())

        self.backtestDataMenu = self.menubar.addMenu("Backtest Data")
        self.backtestDataMenu.addActions(self.backtestDataActionGroup.actions())

        self.aiMenu = self.menubar.addMenu("Artificial Intelligence")
        self.aiMenu.addActions(self.aiActionGroup.actions())

        self.optionsMenu = self.menubar.addMenu("Options")
        self.optionsMenu.addActions(self.optionsActionGroup.actions())

        pass

    #########
    #  Strategy results : trades tab
    #########
    def createTradesUI(self):
        self.strategyResultsUI.createTradesUI()
        pass

    def fillTradesUI(self, trades):
        self.strategyResultsUI.fillTradesUI(trades)
        pass

    #########
    #  UI parameters for testing stategies
    #########
    def createLoadDataFilesUI(self):
        self.loadDataFile = loadDataFiles.LoadDataFiles(self.controller, self.win)
        pass

    #########
    #  UI parameters for testing stategies
    #########
    def createStrategyTesterUI(self):

        self.strategyTester = strategyTester.StrategyTesterController(self.controller)
        self.strategyTesterUI = self.strategyTester.getView()
        self.dock_strategyTester.addWidget(self.strategyTesterUI)

        self.strategyResults = strategyResults.StrategyResults(self.controller)
        self.strategyResultsUI = self.strategyResults.getView()
        self.dock_strategyResults.addWidget(self.strategyResultsUI)

        self.strategyTesterUI.startingCashLE.setText(str(self.controller.cerebro.broker.cash))
        self.strategyTesterUI.startingCashLE.textChanged.connect(self.controller.cashChanged)

        pass

    #########
    #  Strategy results : Summary UI
    #########
    def createSummaryUI(self):
        self.strategyResultsUI.createSummaryUI()
        pass

    def fillSummaryUI(self, brokerCash, brokerValue, tradeAnalysis):
        self.strategyResultsUI.fillSummaryUI(brokerCash, brokerValue, tradeAnalysis)
        pass

    #########
    #  Show all
    #########
    def show(self):
        # self.fpltWindow[timeframe].show() # prepares plots when they're all setup
        self.win.show()
        self.app.exec_()
        pass

    #########
    # Get strategy running progress bar
    #########
    def getProgressBar(self):
        return self.strategyTesterUI.runningStratPB

    #########
    # Draw chart
    #########
    def drawChart(self, data, timeframe):
        self.fpltWindow[timeframe].setChartData(data)
        self.fpltWindow[timeframe].updateChart()
        pass

    #########
    # Draw orders on chart
    #########
    def setOrders(self, orders):
        for timeframe, fpltWindow in self.fpltWindow.items():
            fpltWindow.drawOrders(orders)
        pass

    #########
    # Draw PnL chart
    # A python expert could do waaaaay better optimized on this function
    # But anyway... it works...
    #########
    def displayPnL(self, pnl_dataframe):
        # draw charts
        for timeframe, fpltwindow in self.fpltWindow.items():
            fpltwindow.drawPnL(pnl_dataframe)

        self.togglePnLWidget()

        pass

    #########
    # Control panel overlay on top/above of the finplot window
    #########
    def createControlPanel(self):
        self.controlPanel = controlPanelUI.ControlPanelUI(self.dock_stackedCharts, self)
        self.dock_stackedCharts.addWidget(self.controlPanel, 0, 0)
        return self.controlPanel

    #########
    # Toggle anther UI Theme
    #########
    def dark_mode_toggle(self):
        for key, window in self.fpltWindow.items():
            window.activateDarkMode(self.darkmodeCB.isChecked())
        pass

    ##########
    # INDICATORS
    ##########
    def toogleTimeframe(self, timeframe):
        if self.timeFramePB[timeframe].isChecked():
            print("Display " + timeframe)
            self.current_timeframe = timeframe
            index = self.stackedCharts.indexOf(self.dockAreaTimeframes[timeframe])
            self.stackedCharts.setCurrentIndex(index)
            self.togglePnLWidget()

        pass

    def togglePnLWidget(self):
        # hide all PnL windows & Show the good one
        for tf, fpltWindow in self.fpltWindow.items():
            if tf != self.current_timeframe:
                fpltWindow.hidePnL()
            else:
                fpltWindow.showPnL()

    def resetChart(self):
        self.fpltWindow[self.current_timeframe].resetChart()
        self.fpltWindow[self.current_timeframe].updateChart()
        pass

    # On chart indicators
    def addSma(self):

        # Show indicator parameter dialog
        paramDialog = indicatorParameters.IndicatorParametersController().view
        paramDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        paramDialog.setTitle("SMA Indicator parameters")
        paramDialog.addParameter("SMA Period", 14)
        paramDialog.addParameter("Plot width", 1)
        paramDialog.addParameterColor("Plot color", "#FFFF00")
        paramDialog.adjustSize()

        if paramDialog.exec() == QtWidgets.QDialog.Accepted:
            period = paramDialog.getValue("SMA Period")
            width = paramDialog.getValue("Plot width")
            qColor = paramDialog.getColorValue("Plot color")
            self.fpltWindow[self.current_timeframe].drawSma(period, qColor, width)

        pass

    # On chart indicators
    def addEma(self):

        # Show indicator parameter dialog

        paramDialog = indicatorParameters.IndicatorParametersController().view
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
            self.fpltWindow[self.current_timeframe].drawEma(period, qColor, width)

        pass

    # indicators in external windows
    def toogleRsi(self):

        if self.RsiPB.isChecked():
            # Show indicator parameter dialog
            paramDialog = indicatorParameters.IndicatorParametersController().view
            paramDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            paramDialog.setTitle("RSI Indicator parameters")
            paramDialog.addParameter("RSI Period", 14)
            paramDialog.addParameterColor("Plot color", "#FFFF00")
            paramDialog.adjustSize()

            if paramDialog.exec() == QtWidgets.QDialog.Accepted:
                period = paramDialog.getValue("RSI Period")
                qColor = paramDialog.getColorValue("Plot color")
                self.fpltWindow[self.current_timeframe].drawRsi(period, qColor)
                self.dock_rsi[self.current_timeframe].show()
            else:
                # Cancel
                self.RsiPB.setChecked(False)
                self.dock_rsi[self.current_timeframe].hide()

        else:
            self.dock_rsi[self.current_timeframe].hide()

        pass

    def toogleStochastic(self):

        if self.StochasticPB.isChecked():
            # Show indicator parameter dialog
            paramDialog = indicatorParameters.IndicatorParametersController().view
            paramDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            paramDialog.setTitle("Stochastic Indicator parameters")
            paramDialog.addParameter("Stochastic Period K", 14)
            paramDialog.addParameter("Stochastic Smooth K", 3)
            paramDialog.addParameter("Stochastic Smooth D", 3)
            paramDialog.adjustSize()

            if paramDialog.exec() == QtWidgets.QDialog.Accepted:
                period = paramDialog.getValue("Stochastic Period K")
                smooth_k = paramDialog.getValue("Stochastic Smooth K")
                smooth_d = paramDialog.getValue("Stochastic Smooth D")

                self.fpltWindow[self.current_timeframe].drawStochastic(period, smooth_k, smooth_d)
                self.dock_stochastic[self.current_timeframe].show()
            else:
                # Cancel
                self.RsiPB.setChecked(False)
                self.dock_stochastic[self.current_timeframe].hide()

        else:
            self.dock_stochastic[self.current_timeframe].hide()

        pass

    def toogleStochasticRsi(self):

        if self.StochasticRsiPB.isChecked():
            # Show indicator parameter dialog
            paramDialog = indicatorParameters.IndicatorParametersController().view
            paramDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            paramDialog.setTitle("Stochastic Indicator parameters")
            paramDialog.addParameter("Stochastic Rsi Period K", 14)
            paramDialog.addParameter("Stochastic Rsi Smooth K", 3)
            paramDialog.addParameter("Stochastic Rsi Smooth D", 3)
            paramDialog.adjustSize()

            if (paramDialog.exec() == QtWidgets.QDialog.Accepted):
                period = paramDialog.getValue("Stochastic Rsi Period K")
                smooth_k = paramDialog.getValue("Stochastic Rsi Smooth K")
                smooth_d = paramDialog.getValue("Stochastic Rsi Smooth D")

                self.fpltWindow[self.current_timeframe].drawStochasticRsi(period, smooth_k, smooth_d)
                self.dock_stochasticRsi[self.current_timeframe].show()
            else:
                # Cancel
                self.RsiPB.setChecked(False)
                self.dock_stochasticRsi[self.current_timeframe].hide()

        else:
            self.dock_stochasticRsi[self.current_timeframe].hide()

        pass

    # On chart indicators
    def toogleIchimoku(self):
        self.fpltWindow[self.current_timeframe].setIndicator("Ichimoku", self.IchimokuPB.isChecked())
        pass

    def volumes_toggle(self):
        self.fpltWindow[self.current_timeframe].setIndicator("Volumes", self.volumesCB.isChecked())
        pass

    def fillStrategyParameters(self, strategy):

        # Rest widget rows
        self.strategyTesterUI.parametersLayout = self.strategyTesterUI.findChild(QtWidgets.QFormLayout,
                                                                                 "parametersLayout")
        self.strategyTesterUI.parametersScrollArea = self.strategyTesterUI.findChild(QtWidgets.QScrollArea,
                                                                                     "parametersScrollArea")
        for indexRow in range(self.strategyTesterUI.parametersLayout.rowCount()):
            self.strategyTesterUI.parametersLayout.removeRow(0)

        # Insert parameters
        row = 0
        for parameterName, parameterValue in strategy.params._getitems():
            label = QtWidgets.QLabel(parameterName)
            lineEdit = QtWidgets.QLineEdit(str(parameterValue))
            lineEdit.setObjectName(parameterName)
            # Save the parameter to inject it in the addStrategy method
            self.controller.strategyParametersSave(parameterName, parameterValue)

            # Connect the parameter changed slot
            lineEdit.textChanged.connect(
                functools.partial(self.controller.strategyParametersChanged, lineEdit, parameterName, parameterValue))

            self.strategyTesterUI.parametersLayout.addRow(label, lineEdit)
            row = row + 1
            pass

        # Parameter box size
        self.strategyTesterUI.parametersLayout.update()
        # self.strategyTesterUI.parametersScrollArea.adjustSize()

        pass
