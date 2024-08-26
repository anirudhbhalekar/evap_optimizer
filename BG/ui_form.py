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
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_EO_Window(object):
    def setupUi(self, EO_Window):
        if not EO_Window.objectName():
            EO_Window.setObjectName(u"EO_Window")
        EO_Window.resize(691, 289)
        EO_Window.setMinimumSize(QSize(691, 289))
        EO_Window.setMaximumSize(QSize(691, 289))
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
        self.terminal.setEnabled(True)
        self.terminal.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.terminal.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.verticalLayout.addWidget(self.terminal)

        self.ClearTerminalBttn = QPushButton(self.verticalLayoutWidget)
        self.ClearTerminalBttn.setObjectName(u"ClearTerminalBttn")

        self.verticalLayout.addWidget(self.ClearTerminalBttn)

        self.line = QFrame(EO_Window)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 18, 801, 16))
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

        self.line_3 = QFrame(EO_Window)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(360, 27, 20, 401))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget = QTabWidget(EO_Window)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(380, 30, 301, 251))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.forecastTable = QTableWidget(self.tab)
        if (self.forecastTable.columnCount() < 3):
            self.forecastTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.forecastTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.forecastTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.forecastTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.forecastTable.setObjectName(u"forecastTable")
        self.forecastTable.setGeometry(QRect(0, 0, 301, 221))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.controlTable = QTableWidget(self.tab_2)
        if (self.controlTable.columnCount() < 4):
            self.controlTable.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.controlTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.controlTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.controlTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.controlTable.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.controlTable.setObjectName(u"controlTable")
        self.controlTable.setGeometry(QRect(0, 0, 301, 221))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.outputsTable = QTableWidget(self.tab_3)
        if (self.outputsTable.columnCount() < 6):
            self.outputsTable.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.outputsTable.setObjectName(u"outputsTable")
        self.outputsTable.setEnabled(True)
        self.outputsTable.setGeometry(QRect(0, 0, 301, 221))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_4 = QLabel(self.tab_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 231, 16))
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 221, 16))
        self.OER_line = QLineEdit(self.tab_4)
        self.OER_line.setObjectName(u"OER_line")
        self.OER_line.setEnabled(True)
        self.OER_line.setGeometry(QRect(10, 30, 201, 24))
        self.OER_line.setReadOnly(True)
        self.HP_line = QLineEdit(self.tab_4)
        self.HP_line.setObjectName(u"HP_line")
        self.HP_line.setEnabled(True)
        self.HP_line.setGeometry(QRect(10, 90, 201, 24))
        self.HP_line.setReadOnly(True)
        self.label_6 = QLabel(self.tab_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 130, 221, 16))
        self.FP_line = QLineEdit(self.tab_4)
        self.FP_line.setObjectName(u"FP_line")
        self.FP_line.setEnabled(True)
        self.FP_line.setGeometry(QRect(10, 150, 201, 24))
        self.FP_line.setReadOnly(True)
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(EO_Window)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(EO_Window)
    # setupUi

    def retranslateUi(self, EO_Window):
        EO_Window.setWindowTitle(QCoreApplication.translate("EO_Window", u"EO_Window", None))
        self.LoadExcelFileBttn.setText(QCoreApplication.translate("EO_Window", u"Load Excel File", None))
        self.OptimizerBttn.setText(QCoreApplication.translate("EO_Window", u"Run Optimizer", None))
        self.terminal.setHtml(QCoreApplication.translate("EO_Window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.ClearTerminalBttn.setText(QCoreApplication.translate("EO_Window", u"Clear Terminal", None))
        self.label_2.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Evap Optimizer</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Set Target per Tube (Litres/Day)</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Location for Forecast</span></p></body></html>", None))
        self.LoadForecast.setText(QCoreApplication.translate("EO_Window", u"Load Tomorrows Forecast", None))
        self.InspectResultsBttn.setText(QCoreApplication.translate("EO_Window", u"Inspect Results Sheet (Excel)", None))
        ___qtablewidgetitem = self.forecastTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EO_Window", u"Time", None));
        ___qtablewidgetitem1 = self.forecastTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EO_Window", u"Temp (C)", None));
        ___qtablewidgetitem2 = self.forecastTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EO_Window", u"RH (%)", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("EO_Window", u"Forecast", None))
        ___qtablewidgetitem3 = self.controlTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EO_Window", u"Time", None));
        ___qtablewidgetitem4 = self.controlTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EO_Window", u"Brine Temp (C) ", None));
        ___qtablewidgetitem5 = self.controlTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EO_Window", u"Brine Flow Rate (L/Hr)", None));
        ___qtablewidgetitem6 = self.controlTable.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EO_Window", u"Air Speed (m/s)", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("EO_Window", u"Controls", None))
        ___qtablewidgetitem7 = self.outputsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EO_Window", u"Time", None));
        ___qtablewidgetitem8 = self.outputsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("EO_Window", u"Outlet Brine Temp (C)", None));
        ___qtablewidgetitem9 = self.outputsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("EO_Window", u"Outlet Humidity (%)", None));
        ___qtablewidgetitem10 = self.outputsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("EO_Window", u"Outlet Air Temp (C)", None));
        ___qtablewidgetitem11 = self.outputsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("EO_Window", u"Heating Power (W)", None));
        ___qtablewidgetitem12 = self.outputsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("EO_Window", u"Fan Power (W)", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("EO_Window", u"Outlets", None))
        self.label_4.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p><span style=\" font-weight:700;\">Optimized Evaporation Rate (Litres/Day)</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p><span style=\" font-weight:700;\">Heating Power (kWHr)</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("EO_Window", u"<html><head/><body><p><span style=\" font-weight:700;\">Fan Power (kWHr)</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("EO_Window", u"Result", None))
    # retranslateUi

