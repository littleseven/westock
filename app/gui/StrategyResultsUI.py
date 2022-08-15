from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QWidget

from app.gui.uic_strategyResults import Ui_StrategyResults
import backtrader as bt


class StrategyResultsUI(QWidget, Ui_StrategyResults):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.SummaryGB = self.findChild(QtWidgets.QGroupBox, "SummaryGB")
        self.TradesGB = self.findChild(QtWidgets.QGroupBox, "TradesGB")
        self.ResultsTabWidget = self.findChild(QtWidgets.QTabWidget, "ResultsTabWidget")

    #########
    #  Strategy results : Summary UI
    #########
    def createSummaryUI(self):

        self.summaryTableWidget = QtWidgets.QTableWidget(self.SummaryGB)

        self.summaryTableWidget.setColumnCount(2)

        self.summaryTableWidget.verticalHeader().hide()
        self.summaryTableWidget.horizontalHeader().hide()
        self.summaryTableWidget.setShowGrid(False)

        self.SummaryGB.layout().addWidget(self.summaryTableWidget)

        pass

    def fillSummaryUI(self, brokerCash, brokerValue, tradeAnalysis):

        # Delete all previous rows
        self.summaryTableWidget.setRowCount(0)

        self.summaryTableWidget.setRowCount(8)

        self.summaryTableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Cash"))
        self.summaryTableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(brokerCash)))

        self.summaryTableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Value"))
        self.summaryTableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(brokerValue)))

        # if there are some trades
        if len(tradeAnalysis) > 1:
            self.summaryTableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem("Profit total"))
            self.summaryTableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(str(tradeAnalysis["pnl"]["net"]["total"])))

            self.summaryTableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem("Number of trades"))
            self.summaryTableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(str(tradeAnalysis["total"]["total"])))

            self.summaryTableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem("Won"))
            self.summaryTableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(str(tradeAnalysis["won"]['total'])))

            self.summaryTableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem("Lost"))
            self.summaryTableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem(str(tradeAnalysis["lost"]['total'])))

            self.summaryTableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem("Long"))
            self.summaryTableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem(str(tradeAnalysis["long"]["total"])))

            self.summaryTableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem("Short"))
            self.summaryTableWidget.setItem(7, 1, QtWidgets.QTableWidgetItem(str(tradeAnalysis["short"]["total"])))

            self.summaryTableWidget.horizontalHeader().setStretchLastSection(True)
            self.summaryTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            self.summaryTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        pass

    def createTradesUI(self):

        self.tradeTableWidget = QtWidgets.QTableWidget(self.TradesGB)

        self.tradeTableWidget.setColumnCount(7)

        labels = ["Trade id", "Direction", "Date Open", "Date Close", "Price", "Commission", "Profit Net"]
        self.tradeTableWidget.setHorizontalHeaderLabels(labels)
        self.tradeTableWidget.verticalHeader().setVisible(False)

        self.tradeTableWidget.horizontalHeader().setStretchLastSection(True)
        self.tradeTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # self.tradeTableWidget.setStyleSheet("alternate-background-color: #AAAAAA;background-color: #CCCCCC;")
        self.tradeTableWidget.setAlternatingRowColors(True)
        self.tradeTableWidget.setSortingEnabled(True)
        self.tradeTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tradeTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ResultsTabWidget.widget(0).layout().addWidget(self.tradeTableWidget)
        pass

    def fillTradesUI(self, trades):

        # Delete all previous results by settings row count to 0
        self.tradeTableWidget.setRowCount(0)

        for key, values in trades:

            self.tradeTableWidget.setRowCount(len(values[0]))

            row = 0
            for trade in values[0]:

                if not trade.isopen:
                    # Trade id
                    item = QtWidgets.QTableWidgetItem(str(trade.ref))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tradeTableWidget.setItem(row, 0, item)

                    item = QtWidgets.QTableWidgetItem("Buy" if trade.long else "Sell")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tradeTableWidget.setItem(row, 1, item)

                    item = QtWidgets.QTableWidgetItem(str(bt.num2date(trade.dtopen)))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tradeTableWidget.setItem(row, 2, item)

                    item = QtWidgets.QTableWidgetItem(str(bt.num2date(trade.dtclose)))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tradeTableWidget.setItem(row, 3, item)

                    item = QtWidgets.QTableWidgetItem(str(trade.price))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tradeTableWidget.setItem(row, 4, item)

                    item = QtWidgets.QTableWidgetItem(str(trade.commission))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tradeTableWidget.setItem(row, 5, item)

                    item = QtWidgets.QTableWidgetItem(str(trade.pnlcomm))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tradeTableWidget.setItem(row, 6, item)

                row += 1

        pass


    #########
    #  Strategy results : Order tab
    #########
    def createOrdersUI(self):

        self.orderTableWidget = QtWidgets.QTableWidget(self.TradesGB)
        self.orderTableWidget.setColumnCount(8)

        labels = ["Order ref", "Direction", "Date Open", "Date Close", "Execution Type", "Size", "Price", "Profit"]

        self.orderTableWidget.setHorizontalHeaderLabels(labels)

        self.orderTableWidget.horizontalHeader().setStretchLastSection(True)
        self.orderTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.orderTableWidget.setStyleSheet("alternate-background-color: #AAAAAA;background-color: #CCCCCC;")
        self.orderTableWidget.setAlternatingRowColors(True)
        self.orderTableWidget.setSortingEnabled(True)
        self.orderTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.orderTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ResultsTabWidget.widget(0).layout().addWidget(self.orderTableWidget)
        # self.dock_orders.addWidget(self.orderTableWidget)

        pass

    def fillOrdersUI(self, orders):

        self.orderTableWidget.setRowCount(len(orders))

        for i in range(len(orders)):
            order = orders[i]

            self.orderTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(order.ref)))
            self.orderTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Buy" if order.isbuy() else "Sell"))

            self.orderTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(bt.num2date(order.created.dt))))
            self.orderTableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(bt.num2date(order.executed.dt))))

            self.orderTableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(order.exectype)))

            self.orderTableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(order.size)))
            self.orderTableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(order.price)))
            self.orderTableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(order.executed.pnl)))

        pass