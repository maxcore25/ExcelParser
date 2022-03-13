# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lettrs_gen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("letters_gen_228_epta")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 440, 261, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_run = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_run.setObjectName("pushButton_run")
        self.gridLayout.addWidget(self.pushButton_run, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 90, 681, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_getTemplate = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_getTemplate.setObjectName("pushButton_getTemplate")
        self.gridLayout_2.addWidget(self.pushButton_getTemplate, 2, 1, 1, 1)
        self.lineEdit_getTemplate = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_getTemplate.setObjectName("lineEdit_getTemplate")
        self.gridLayout_2.addWidget(self.lineEdit_getTemplate, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(80, 200, 681, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_getData = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_getData.setObjectName("pushButton_getData")
        self.gridLayout_3.addWidget(self.pushButton_getData, 2, 1, 1, 1)
        self.lineEdit_getData = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_getData.setObjectName("lineEdit_getData")
        self.gridLayout_3.addWidget(self.lineEdit_getData, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(80, 310, 681, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_chooseDir = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.pushButton_chooseDir.setObjectName("pushButton_chooseDir")
        self.gridLayout_4.addWidget(self.pushButton_chooseDir, 2, 1, 1, 1)
        self.lineEdit_chooseDir = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_chooseDir.setObjectName("lineEdit_chooseDir")
        self.gridLayout_4.addWidget(self.lineEdit_chooseDir, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ULTIMATE EPTA LETTERS GENERATOR"))
        self.pushButton_run.setText(_translate("MainWindow", "Сделать ЗАЕБИСЬ!!!!!"))
        self.pushButton_getTemplate.setText(_translate("MainWindow", "Выбрать"))
        self.label.setText(_translate("MainWindow", "Путь к файлу шаблона"))
        self.pushButton_getData.setText(_translate("MainWindow", "Выбрать"))
        self.label_2.setText(_translate("MainWindow", "Путь к файлу с данными"))
        self.pushButton_chooseDir.setText(_translate("MainWindow", "Выбрать"))
        self.label_3.setText(_translate("MainWindow", "Путь к папке, где будет сохранен архив"))
