# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'strategyTester.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(254, 699)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.backTestingGroupBox = QGroupBox(Form)
        self.backTestingGroupBox.setObjectName(u"backTestingGroupBox")
        self.gridLayout = QGridLayout(self.backTestingGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.runningStratPB = QProgressBar(self.backTestingGroupBox)
        self.runningStratPB.setObjectName(u"runningStratPB")
        self.runningStratPB.setValue(0)

        self.gridLayout.addWidget(self.runningStratPB, 9, 0, 1, 1)

        self.strategyNameCB = QComboBox(self.backTestingGroupBox)
        self.strategyNameCB.setObjectName(u"strategyNameCB")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strategyNameCB.sizePolicy().hasHeightForWidth())
        self.strategyNameCB.setSizePolicy(sizePolicy)
        self.strategyNameCB.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.strategyNameCB, 2, 0, 1, 1)

        self.label_3 = QLabel(self.backTestingGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.label_4 = QLabel(self.backTestingGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.runLabel = QLabel(self.backTestingGroupBox)
        self.runLabel.setObjectName(u"runLabel")

        self.gridLayout.addWidget(self.runLabel, 10, 0, 1, 1)

        self.runBacktestPB = QPushButton(self.backTestingGroupBox)
        self.runBacktestPB.setObjectName(u"runBacktestPB")
        self.runBacktestPB.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.runBacktestPB.sizePolicy().hasHeightForWidth())
        self.runBacktestPB.setSizePolicy(sizePolicy1)
        self.runBacktestPB.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.runBacktestPB, 8, 0, 1, 1)

        self.parametersScrollArea = QScrollArea(self.backTestingGroupBox)
        self.parametersScrollArea.setObjectName(u"parametersScrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.parametersScrollArea.sizePolicy().hasHeightForWidth())
        self.parametersScrollArea.setSizePolicy(sizePolicy2)
        self.parametersScrollArea.setMinimumSize(QSize(200, 200))
        self.parametersScrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.parametersScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 198, 200))
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(198, 200))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parametersLayout = QFormLayout()
        self.parametersLayout.setObjectName(u"parametersLayout")
        self.parametersLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.parametersLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)

        self.verticalLayout.addLayout(self.parametersLayout)

        self.parametersScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.parametersScrollArea, 6, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.backTestingGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.startingCashLE = QLineEdit(self.backTestingGroupBox)
        self.startingCashLE.setObjectName(u"startingCashLE")

        self.gridLayout_3.addWidget(self.startingCashLE, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)


        self.gridLayout_2.addWidget(self.backTestingGroupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.backTestingGroupBox.setTitle(QCoreApplication.translate("Form", u"Back testing", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Parameters", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Strategy", None))
        self.runLabel.setText("")
        self.runBacktestPB.setText(QCoreApplication.translate("Form", u"Run", None))
        self.label.setText(QCoreApplication.translate("Form", u"Starting cash", None))
        self.startingCashLE.setInputMask("")
    # retranslateUi

