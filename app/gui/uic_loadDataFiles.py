# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadDataFiles.ui'
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
        Form.resize(488, 458)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dataFilesListWidget = QListWidget(Form)
        self.dataFilesListWidget.setObjectName(u"dataFilesListWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataFilesListWidget.sizePolicy().hasHeightForWidth())
        self.dataFilesListWidget.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.dataFilesListWidget, 3, 0, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.importPB = QPushButton(Form)
        self.importPB.setObjectName(u"importPB")
        self.importPB.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.importPB, 5, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_2.addLayout(self.verticalLayout, 3, 1, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.semicolonRB = QRadioButton(self.groupBox)
        self.semicolonRB.setObjectName(u"semicolonRB")

        self.gridLayout.addWidget(self.semicolonRB, 3, 3, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.tabRB = QRadioButton(self.groupBox)
        self.tabRB.setObjectName(u"tabRB")
        self.tabRB.setChecked(True)

        self.gridLayout.addWidget(self.tabRB, 3, 1, 1, 1)

        self.commaRB = QRadioButton(self.groupBox)
        self.commaRB.setObjectName(u"commaRB")

        self.gridLayout.addWidget(self.commaRB, 3, 2, 1, 1)

        self.filePathLE = QLineEdit(self.groupBox)
        self.filePathLE.setObjectName(u"filePathLE")

        self.gridLayout.addWidget(self.filePathLE, 0, 1, 1, 3)

        self.openFilePB = QToolButton(self.groupBox)
        self.openFilePB.setObjectName(u"openFilePB")

        self.gridLayout.addWidget(self.openFilePB, 0, 4, 1, 1)

        self.datetimeFormatLE = QLineEdit(self.groupBox)
        self.datetimeFormatLE.setObjectName(u"datetimeFormatLE")

        self.gridLayout.addWidget(self.datetimeFormatLE, 1, 1, 1, 4)

        self.loadFilePB = QPushButton(self.groupBox)
        self.loadFilePB.setObjectName(u"loadFilePB")
        self.loadFilePB.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.loadFilePB, 4, 1, 1, 4)

        self.errorLabel = QLabel(self.groupBox)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setStyleSheet(u"color: red")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.errorLabel, 5, 0, 1, 5)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-style: italic")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Import one or multiple data files", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"List of all files to import in cerebro", None))
        self.importPB.setText(QCoreApplication.translate("Form", u"Import all data files", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Loading a new data file", None))
        self.semicolonRB.setText(QCoreApplication.translate("Form", u"semicolon", None))
        self.label.setText(QCoreApplication.translate("Form", u"Import a new data file", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Date time format", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Separator", None))
        self.tabRB.setText(QCoreApplication.translate("Form", u"tab", None))
        self.commaRB.setText(QCoreApplication.translate("Form", u"comma", None))
        self.openFilePB.setText(QCoreApplication.translate("Form", u"...", None))
        self.loadFilePB.setText(QCoreApplication.translate("Form", u"Load .CSV file", None))
        self.errorLabel.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Files should be ordered from lower (on top) to higher timeframe (at bottom).", None))
    # retranslateUi

