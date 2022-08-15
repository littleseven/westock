# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'strategyResults.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StrategyResults(object):
    def setupUi(self, StrategyResults):
        if not StrategyResults.objectName():
            StrategyResults.setObjectName(u"StrategyResults")
        StrategyResults.resize(963, 284)
        self.gridLayout = QGridLayout(StrategyResults)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SummaryGB = QGroupBox(StrategyResults)
        self.SummaryGB.setObjectName(u"SummaryGB")
        self.SummaryGB.setMinimumSize(QSize(200, 0))
        self.SummaryGB.setMaximumSize(QSize(250, 16777215))
        self.SummaryGB.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.SummaryGB)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.SummaryGB, 0, 0, 1, 1)

        self.ResultsTabWidget = QTabWidget(StrategyResults)
        self.ResultsTabWidget.setObjectName(u"ResultsTabWidget")
        self.tradeTab = QWidget()
        self.tradeTab.setObjectName(u"tradeTab")
        self.gridLayout_3 = QGridLayout(self.tradeTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.ResultsTabWidget.addTab(self.tradeTab, "")
        self.walletTab = QWidget()
        self.walletTab.setObjectName(u"walletTab")
        self.gridLayout_5 = QGridLayout(self.walletTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.ResultsTabWidget.addTab(self.walletTab, "")

        self.gridLayout.addWidget(self.ResultsTabWidget, 0, 1, 1, 1)


        self.retranslateUi(StrategyResults)

        self.ResultsTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StrategyResults)
    # setupUi

    def retranslateUi(self, StrategyResults):
        StrategyResults.setWindowTitle(QCoreApplication.translate("StrategyResults", u"Form", None))
        self.SummaryGB.setTitle(QCoreApplication.translate("StrategyResults", u"Strategy summary", None))
        self.ResultsTabWidget.setTabText(self.ResultsTabWidget.indexOf(self.tradeTab), QCoreApplication.translate("StrategyResults", u"Trades", None))
        self.ResultsTabWidget.setTabText(self.ResultsTabWidget.indexOf(self.walletTab), QCoreApplication.translate("StrategyResults", u"Wallet", None))
    # retranslateUi

