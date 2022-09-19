# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockPool.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StockPool(object):
    def setupUi(self, StockPool):
        if not StockPool.objectName():
            StockPool.setObjectName(u"StockPool")
        StockPool.resize(350, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StockPool.sizePolicy().hasHeightForWidth())
        StockPool.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(StockPool)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stockInfoTab = QTabWidget(StockPool)
        self.stockInfoTab.setObjectName(u"stockInfoTab")
        self.stockInfoTab.setElideMode(Qt.ElideLeft)
        self.stockInfoTab.setUsesScrollButtons(False)
        self.stockInfoTab.setDocumentMode(False)
        self.stockInfoTab.setTabsClosable(False)
        self.stockInfoTab.setMovable(False)
        self.stockTab = QWidget()
        self.stockTab.setObjectName(u"stockTab")
        self.gridLayout_3 = QGridLayout(self.stockTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stockLayout = QHBoxLayout()
        self.stockLayout.setObjectName(u"stockLayout")

        self.gridLayout_3.addLayout(self.stockLayout, 0, 0, 1, 1)

        self.stockInfoTab.addTab(self.stockTab, "")
        self.holdTab = QWidget()
        self.holdTab.setObjectName(u"holdTab")
        self.gridLayout_5 = QGridLayout(self.holdTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.holdLayout = QHBoxLayout()
        self.holdLayout.setObjectName(u"holdLayout")

        self.gridLayout_5.addLayout(self.holdLayout, 0, 0, 1, 1)

        self.stockInfoTab.addTab(self.holdTab, "")

        self.gridLayout.addWidget(self.stockInfoTab, 0, 0, 1, 1)


        self.retranslateUi(StockPool)

        self.stockInfoTab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(StockPool)
    # setupUi

    def retranslateUi(self, StockPool):
        StockPool.setWindowTitle("")
        self.stockInfoTab.setTabText(self.stockInfoTab.indexOf(self.stockTab), QCoreApplication.translate("StockPool", u"\u80a1\u7968\u6c60", None))
        self.stockInfoTab.setTabText(self.stockInfoTab.indexOf(self.holdTab), QCoreApplication.translate("StockPool", u"\u6301\u6709", None))
    # retranslateUi

