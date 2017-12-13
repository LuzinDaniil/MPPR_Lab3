# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QToolButton, QMenuBar, QSlider, QStatusBar, QApplication, \
    QGraphicsView, QGraphicsScene, QListView, QTextEdit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(160, 170, 171, 19))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(450, 170, 191, 19))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(160, 240, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 270, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(400, 270, 300, 180))
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.scence = QGraphicsScene()
        self.scence.addPixmap(QPixmap.scaled(QPixmap('D:\q.jpg'),300, 180))
        self.graphicsView.setScene(self.scence)
        self.toolButton_3 = QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(450, 210, 191, 19))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 333, 191, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 463, 241, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(410, 480, 281, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная №3"))
        self.toolButton.setText(_translate("MainWindow", "Тренировка"))
        self.toolButton_2.setText(_translate("MainWindow", "Распознавание"))
        self.label.setText(_translate("MainWindow", "0.01"))
        self.toolButton_3.setText(_translate("MainWindow", "Изменить картинку"))


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("redrock.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()