# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leftSideBar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_leftMenu(object):
    def setupUi(self, leftMenu):
        if not leftMenu.objectName():
            leftMenu.setObjectName(u"leftMenu")
        leftMenu.resize(86, 699)
        self.gridLayout = QGridLayout(leftMenu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(leftMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(leftMenu)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(leftMenu)
    # setupUi

    def retranslateUi(self, leftMenu):
        leftMenu.setWindowTitle(QCoreApplication.translate("leftMenu", u"Form", None))
    # retranslateUi

