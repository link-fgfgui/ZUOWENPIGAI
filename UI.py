# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWhQrEe.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 600)
        Form.setMinimumSize(QSize(900, 600))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.zongpingjiaLabel = QLabel(Form)
        self.zongpingjiaLabel.setObjectName(u"zongpingjiaLabel")
        font = QFont()
        font.setPointSize(16)
        self.zongpingjiaLabel.setFont(font)
        self.zongpingjiaLabel.setFrameShape(QFrame.Shape.Box)
        self.zongpingjiaLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.zongpingjiaLabel.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.zongpingjiaLabel)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lcdNumber = QLCDNumber(self.widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setProperty("intValue", 0)

        self.horizontalLayout.addWidget(self.lcdNumber)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalLayout.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.widget)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 1, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 20)
        self.gridLayout_2.setRowStretch(2, 200)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 200)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.zongpingjiaLabel.setText(QCoreApplication.translate("Form", u"\u603b\u8bc4\u4ef7:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5206", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u539f\u6587", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8bc4\u4ef7", None))
    # retranslateUi

