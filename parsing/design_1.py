# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parcer_prot_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QSpinBox, QLabel, QLineEdit
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        #MainWindow.resize(395, 250)
        MainWindow.resize(450, 290)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 290))
        MainWindow.setAcceptDrops(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        #self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 251))
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 251))
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.textBrowser = QtWidgets.QTextBrowser(self.tab_1)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 401, 231))
        self.textBrowser.setObjectName("textBrowser")

        self.tabWidget.addTab(self.tab_1, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")

        self.verticalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)

        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 391, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_2.addWidget(self.plainTextEdit_2)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_2.addWidget(self.spinBox_2)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)

        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 391, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)

        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.verticalLayout_3.addWidget(self.plainTextEdit_3)

        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)

        self.spinBox_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_3.addWidget(self.spinBox_3)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.tabWidget.addTab(self.tab_4, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Парсер"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Парсер группы БСУ1901 </span><span style=\" font-size:12pt;\"><br />Самойлов<br />Хуейлов <br />Назмик<br />Маленький<br />Чувашик (крутой)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ну тыкаете там бля сверху и короче вот парсим сайтики и не ебет <br />Докучаев крутой!!</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Информация"))
        self.label.setText(_translate("MainWindow", "Напиши название вакансии"))
        self.label_2.setText(_translate("MainWindow", "Выбери количество страниц для спизжевания"))
        self.pushButton.setText(_translate("MainWindow", "Ебашим!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "HH.ru"))
        self.label_3.setText(_translate("MainWindow", "Напиши название вакансии"))
        self.label_4.setText(_translate("MainWindow", "Выбери количество страниц для спизжевания"))
        self.pushButton_2.setText(_translate("MainWindow", "Ебашим!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Workius.ru"))
        self.label_5.setText(_translate("MainWindow", "Напиши название вакансии"))
        self.label_6.setText(_translate("MainWindow", "Выбери количество страниц для спизжевания"))
        self.pushButton_3.setText(_translate("MainWindow", "Ебашим!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Залупа №3"))