# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_EO_Window(object):
    def setupUi(self, EO_Window):
        if not EO_Window.objectName():
            EO_Window.setObjectName(u"EO_Window")
        EO_Window.resize(699, 289)
        EO_Window.setMinimumSize(QSize(161, 203))
        self.verticalLayoutWidget = QWidget(EO_Window)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 141, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LoadExcelFileBttn = QPushButton(self.verticalLayoutWidget)
        self.LoadExcelFileBttn.setObjectName(u"LoadExcelFileBttn")

        self.verticalLayout.addWidget(self.LoadExcelFileBttn)

        self.OptimizerBttn = QPushButton(self.verticalLayoutWidget)
        self.OptimizerBttn.setObjectName(u"OptimizerBttn")

        self.verticalLayout.addWidget(self.OptimizerBttn)

        self.terminal = QTextBrowser(self.verticalLayoutWidget)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setEnabled(False)

        self.verticalLayout.addWidget(self.terminal)

        self.line = QFrame(EO_Window)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 18, 711, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2 = QLabel(EO_Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, -3, 701, 31))
        self.line_2 = QFrame(EO_Window)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(150, 27, 20, 271))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayoutWidget_2 = QWidget(EO_Window)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(170, 30, 191, 251))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.TargetLine = QLineEdit(self.verticalLayoutWidget_2)
        self.TargetLine.setObjectName(u"TargetLine")

        self.verticalLayout_2.addWidget(self.TargetLine)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.LocationLine = QLineEdit(self.verticalLayoutWidget_2)
        self.LocationLine.setObjectName(u"LocationLine")

        self.verticalLayout_2.addWidget(self.LocationLine)

        self.LoadForecast = QPushButton(self.verticalLayoutWidget_2)
        self.LoadForecast.setObjectName(u"LoadForecast")

        self.verticalLayout_2.addWidget(self.LoadForecast)

        self.InspectResultsBttn = QPushButton(self.verticalLayoutWidget_2)
        self.InspectResultsBttn.setObjectName(u"InspectResultsBttn")

        self.verticalLayout_2.addWidget(self.InspectResultsBttn)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.line_3 = QFrame(EO_Window)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(360, 27, 20, 401))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.forecastTable = QTableWidget(EO_Window)
        if (self.forecastTable.columnCount() < 3):
            self.forecastTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.forecastTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.forecastTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.forecastTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.forecastTable.setObjectName(u"forecastTable")
        self.forecastTable.setGeometry(QRect(380, 31, 301, 251))

        self.retranslateUi(EO_Window)

        QMetaObject.connectSlotsByName(EO_Window)
    # setupUi

    def retranslateUi(self, EO_Window):
        EO_Window.setWindowTitle(QCoreApplication.translate("EO_Window", u"EO_Window", None))
        self.LoadExcelFileBttn.setText(QCoreApplication.translate("EO_Window", u"Load Excel File", None))
        self.OptimizerBttn.setText(QCoreApplication.translate("EO_Window", u"Run Optimizer", None))
        self.label_2.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Evap Optimizer</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Set Target per Tube (Litres)</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Location for Forecast</span></p></body></html>", None))
        self.LoadForecast.setText(QCoreApplication.translate("EO_Window", u"Load Forecast", None))
        self.InspectResultsBttn.setText(QCoreApplication.translate("EO_Window", u"Inspect Results Sheet (Excel)", None))
        self.pushButton_4.setText(QCoreApplication.translate("EO_Window", u"Open Tutorial", None))
        ___qtablewidgetitem = self.forecastTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EO_Window", u"Time", None));
        ___qtablewidgetitem1 = self.forecastTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EO_Window", u"Temp (C)", None));
        ___qtablewidgetitem2 = self.forecastTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EO_Window", u"RH (%)", None));
    # retranslateUi

