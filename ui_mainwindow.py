# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sixcables = QWidget(self.centralwidget)
        self.sixcables.setObjectName(u"sixcables")
        self.sixcables.setGeometry(QRect(0, 0, 311, 211))
        self.gridLayoutWidget = QWidget(self.sixcables)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 221, 211))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.blue_2 = QPushButton(self.gridLayoutWidget)
        self.blue_2.setObjectName(u"blue_2")
        self.blue_2.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.blue_2.setCheckable(True)

        self.gridLayout.addWidget(self.blue_2, 1, 1, 1, 1)

        self.red_2 = QPushButton(self.gridLayoutWidget)
        self.red_2.setObjectName(u"red_2")
        self.red_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.red_2.setCheckable(True)

        self.gridLayout.addWidget(self.red_2, 1, 0, 1, 1)

        self.white_6 = QPushButton(self.gridLayoutWidget)
        self.white_6.setObjectName(u"white_6")
        self.white_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.white_6.setCheckable(True)

        self.gridLayout.addWidget(self.white_6, 5, 3, 1, 1)

        self.blue_5 = QPushButton(self.gridLayoutWidget)
        self.blue_5.setObjectName(u"blue_5")
        self.blue_5.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.blue_5.setCheckable(True)

        self.gridLayout.addWidget(self.blue_5, 4, 1, 1, 1)

        self.red_4 = QPushButton(self.gridLayoutWidget)
        self.red_4.setObjectName(u"red_4")
        self.red_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.red_4.setCheckable(True)

        self.gridLayout.addWidget(self.red_4, 3, 0, 1, 1)

        self.white_5 = QPushButton(self.gridLayoutWidget)
        self.white_5.setObjectName(u"white_5")
        self.white_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.white_5.setCheckable(True)

        self.gridLayout.addWidget(self.white_5, 4, 3, 1, 1)

        self.black_4 = QPushButton(self.gridLayoutWidget)
        self.black_4.setObjectName(u"black_4")
        self.black_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.black_4.setCheckable(True)

        self.gridLayout.addWidget(self.black_4, 3, 4, 1, 1)

        self.black_3 = QPushButton(self.gridLayoutWidget)
        self.black_3.setObjectName(u"black_3")
        self.black_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.black_3.setCheckable(True)

        self.gridLayout.addWidget(self.black_3, 2, 4, 1, 1)

        self.black_6 = QPushButton(self.gridLayoutWidget)
        self.black_6.setObjectName(u"black_6")
        self.black_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.black_6.setCheckable(True)

        self.gridLayout.addWidget(self.black_6, 5, 4, 1, 1)

        self.black_5 = QPushButton(self.gridLayoutWidget)
        self.black_5.setObjectName(u"black_5")
        self.black_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.black_5.setCheckable(True)

        self.gridLayout.addWidget(self.black_5, 4, 4, 1, 1)

        self.white_3 = QPushButton(self.gridLayoutWidget)
        self.white_3.setObjectName(u"white_3")
        self.white_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.white_3.setCheckable(True)

        self.gridLayout.addWidget(self.white_3, 2, 3, 1, 1)

        self.white_4 = QPushButton(self.gridLayoutWidget)
        self.white_4.setObjectName(u"white_4")
        self.white_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.white_4.setCheckable(True)

        self.gridLayout.addWidget(self.white_4, 3, 3, 1, 1)

        self.yellow_2 = QPushButton(self.gridLayoutWidget)
        self.yellow_2.setObjectName(u"yellow_2")
        self.yellow_2.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.yellow_2.setCheckable(True)

        self.gridLayout.addWidget(self.yellow_2, 1, 2, 1, 1)

        self.yellow_3 = QPushButton(self.gridLayoutWidget)
        self.yellow_3.setObjectName(u"yellow_3")
        self.yellow_3.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.yellow_3.setCheckable(True)

        self.gridLayout.addWidget(self.yellow_3, 2, 2, 1, 1)

        self.yellow_4 = QPushButton(self.gridLayoutWidget)
        self.yellow_4.setObjectName(u"yellow_4")
        self.yellow_4.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.yellow_4.setCheckable(True)

        self.gridLayout.addWidget(self.yellow_4, 3, 2, 1, 1)

        self.yellow_6 = QPushButton(self.gridLayoutWidget)
        self.yellow_6.setObjectName(u"yellow_6")
        self.yellow_6.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.yellow_6.setCheckable(True)

        self.gridLayout.addWidget(self.yellow_6, 5, 2, 1, 1)

        self.yellow_5 = QPushButton(self.gridLayoutWidget)
        self.yellow_5.setObjectName(u"yellow_5")
        self.yellow_5.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.yellow_5.setCheckable(True)

        self.gridLayout.addWidget(self.yellow_5, 4, 2, 1, 1)

        self.white_2 = QPushButton(self.gridLayoutWidget)
        self.white_2.setObjectName(u"white_2")
        self.white_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.white_2.setCheckable(True)

        self.gridLayout.addWidget(self.white_2, 1, 3, 1, 1)

        self.blue_6 = QPushButton(self.gridLayoutWidget)
        self.blue_6.setObjectName(u"blue_6")
        self.blue_6.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.blue_6.setCheckable(True)

        self.gridLayout.addWidget(self.blue_6, 5, 1, 1, 1)

        self.red_3 = QPushButton(self.gridLayoutWidget)
        self.red_3.setObjectName(u"red_3")
        self.red_3.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.red_3.setCheckable(True)

        self.gridLayout.addWidget(self.red_3, 2, 0, 1, 1)

        self.blue_4 = QPushButton(self.gridLayoutWidget)
        self.blue_4.setObjectName(u"blue_4")
        self.blue_4.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.blue_4.setCheckable(True)

        self.gridLayout.addWidget(self.blue_4, 3, 1, 1, 1)

        self.black_2 = QPushButton(self.gridLayoutWidget)
        self.black_2.setObjectName(u"black_2")
        self.black_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.black_2.setCheckable(True)

        self.gridLayout.addWidget(self.black_2, 1, 4, 1, 1)

        self.blue_3 = QPushButton(self.gridLayoutWidget)
        self.blue_3.setObjectName(u"blue_3")
        self.blue_3.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.blue_3.setCheckable(True)

        self.gridLayout.addWidget(self.blue_3, 2, 1, 1, 1)

        self.red_5 = QPushButton(self.gridLayoutWidget)
        self.red_5.setObjectName(u"red_5")
        self.red_5.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.red_5.setCheckable(True)

        self.gridLayout.addWidget(self.red_5, 4, 0, 1, 1)

        self.red_6 = QPushButton(self.gridLayoutWidget)
        self.red_6.setObjectName(u"red_6")
        self.red_6.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.red_6.setCheckable(True)

        self.gridLayout.addWidget(self.red_6, 5, 0, 1, 1)

        self.white_1 = QPushButton(self.gridLayoutWidget)
        self.white_1.setObjectName(u"white_1")
        self.white_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.white_1.setCheckable(True)

        self.gridLayout.addWidget(self.white_1, 0, 3, 1, 1)

        self.black_1 = QPushButton(self.gridLayoutWidget)
        self.black_1.setObjectName(u"black_1")
        self.black_1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.black_1.setCheckable(True)

        self.gridLayout.addWidget(self.black_1, 0, 4, 1, 1)

        self.blue_1 = QPushButton(self.gridLayoutWidget)
        self.blue_1.setObjectName(u"blue_1")
        self.blue_1.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.blue_1.setCheckable(True)

        self.gridLayout.addWidget(self.blue_1, 0, 1, 1, 1)

        self.red_1 = QPushButton(self.gridLayoutWidget)
        self.red_1.setObjectName(u"red_1")
        self.red_1.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.red_1.setCheckable(True)

        self.gridLayout.addWidget(self.red_1, 0, 0, 1, 1)

        self.yellow_1 = QPushButton(self.gridLayoutWidget)
        self.yellow_1.setObjectName(u"yellow_1")
        self.yellow_1.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.yellow_1.setCheckable(True)

        self.gridLayout.addWidget(self.yellow_1, 0, 2, 1, 1)

        self.clear_1 = QPushButton(self.gridLayoutWidget)
        self.clear_1.setObjectName(u"clear_1")
        self.clear_1.setCheckable(True)

        self.gridLayout.addWidget(self.clear_1, 0, 5, 1, 1)

        self.clear_2 = QPushButton(self.gridLayoutWidget)
        self.clear_2.setObjectName(u"clear_2")
        self.clear_2.setCheckable(True)

        self.gridLayout.addWidget(self.clear_2, 1, 5, 1, 1)

        self.clear_3 = QPushButton(self.gridLayoutWidget)
        self.clear_3.setObjectName(u"clear_3")
        self.clear_3.setCheckable(True)

        self.gridLayout.addWidget(self.clear_3, 2, 5, 1, 1)

        self.clear_4 = QPushButton(self.gridLayoutWidget)
        self.clear_4.setObjectName(u"clear_4")
        self.clear_4.setCheckable(True)

        self.gridLayout.addWidget(self.clear_4, 3, 5, 1, 1)

        self.clear_5 = QPushButton(self.gridLayoutWidget)
        self.clear_5.setObjectName(u"clear_5")
        self.clear_5.setCheckable(True)

        self.gridLayout.addWidget(self.clear_5, 4, 5, 1, 1)

        self.clear_6 = QPushButton(self.gridLayoutWidget)
        self.clear_6.setObjectName(u"clear_6")
        self.clear_6.setCheckable(True)

        self.gridLayout.addWidget(self.clear_6, 5, 5, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.blue_2.setText("")
        self.red_2.setText("")
        self.white_6.setText("")
        self.blue_5.setText("")
        self.red_4.setText("")
        self.white_5.setText("")
        self.black_4.setText("")
        self.black_3.setText("")
        self.black_6.setText("")
        self.black_5.setText("")
        self.white_3.setText("")
        self.white_4.setText("")
        self.yellow_2.setText("")
        self.yellow_3.setText("")
        self.yellow_4.setText("")
        self.yellow_6.setText("")
        self.yellow_5.setText("")
        self.white_2.setText("")
        self.blue_6.setText("")
        self.red_3.setText("")
        self.blue_4.setText("")
        self.black_2.setText("")
        self.blue_3.setText("")
        self.red_5.setText("")
        self.red_6.setText("")
        self.white_1.setText("")
        self.black_1.setText("")
        self.blue_1.setText("")
        self.red_1.setText("")
        self.yellow_1.setText("")
        self.clear_1.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.clear_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.clear_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.clear_4.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.clear_5.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.clear_6.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

