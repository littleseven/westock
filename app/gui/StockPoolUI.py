import logging
import os

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QWidget, QSizePolicy

import app.utils.dateUtil as dateUtil
from app.gui.uic_stockPool import Ui_StockPool
from app.utils.fileUtil import FileUtil


class StockPoolUI(QWidget, Ui_StockPool):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = None
        self.setupUi(self)

    def createStockPoolUI(self):
        self.stockTableWidget = QtWidgets.QTableWidget(self.stockTab)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.stockTableWidget.setSizePolicy(sizePolicy)

        self.stockTableWidget.setColumnCount(2)

        labels = ["Name", "Code"]
        self.stockTableWidget.setHorizontalHeaderLabels(labels)
        self.stockTableWidget.verticalHeader().setVisible(False)

        self.stockTableWidget.horizontalHeader().setStretchLastSection(True)
        self.stockTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.stockTableWidget.setAlternatingRowColors(True)
        self.stockTableWidget.setSortingEnabled(True)
        self.stockTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.stockTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.stockTableWidget.itemClicked.connect(self.onItemClicked)

        self.stockLayout.addWidget(self.stockTableWidget)
        pass

    def onItemClicked(self, item):
        print(item.text())
        items = self.stockTableWidget.selectedItems()
        name = items[0].text()
        code = items[1].text()
        if self.controller is not None:
            kwargs = {}
            kwargs["code"] = code
            kwargs["start_date"] = dateUtil.get_year_ago()
            kwargs["end_date"] = dateUtil.now()
            self.controller.loadData(kwargs)
        pass

    def setController(self, controller):
        self.controller = controller

    def fillStockPoolUI(self):
        stocks = FileUtil.load_sys_settings("stock_self_pool.json")["股票"]
        self.stockTableWidget.setRowCount(0)
        row = 0
        for i in stocks.items():
            self.stockTableWidget.setRowCount(row + 1)
            item = QtWidgets.QTableWidgetItem(i[0])
            item.setTextAlignment(QtCore.Qt.AlignLeft)
            self.stockTableWidget.setItem(row, 0, item)

            item = QtWidgets.QTableWidgetItem(i[1])
            item.setTextAlignment(QtCore.Qt.AlignLeft)
            self.stockTableWidget.setItem(row, 1, item)
            row += 1
        self.adjustSize()

    pass
