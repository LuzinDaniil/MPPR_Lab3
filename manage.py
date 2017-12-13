# -*- coding: cp1251 -*-
import time
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

__author__ = 'Work'
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QGraphicsScene
import sys  # We need sys so that we can pass argv to QApplication
from importlib import reload  # для python 3.0 - 3.3
reload(sys)
import design
from calc import *
import threading
import subprocess
val = '0.01'

global p
filename = 'D:\q.jpg'

t=time.time()







class ExampleApp(QMainWindow, design.Ui_MainWindow,QtCore.QThread):# this is class for administrator window

    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        self.thread1 = QWorker("thread1")
        self.thread2 = QWorker2("thread2")

        # It sets up layout and widgets that are defined

        self.toolButton.clicked.connect(self.browse_port)
        self.toolButton_2.clicked.connect(self.recognize)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.valueChanged.connect(self.getValueHorizontal)
        self.toolButton_3.clicked.connect(self.showDialog)

    



    def showDialog(self):
        global filename
        filename = QFileDialog.getOpenFileName(self, 'Open File', '*.jpg')[0]
        if filename=='':
                filename = 'D:\q.jpg'
        self.scence = QGraphicsScene()
        self.scence.addPixmap(QPixmap.scaled(QPixmap(filename),300, 180))
        self.graphicsView.setScene(self.scence)



    def getValueHorizontal(self):
        value = self.horizontalSlider.value()
        self.label.setText(str(value/1000))
        val=value/1000


    def recognize(self):
        r = recognize(filename)
        my_keys = r.keys()
        self.textEdit.setText(str('Результат:'))
        for i in my_keys:
            if i=='pansy':
                self.textEdit.append('Фиалка  = %.1f%%' % ( (r.get(i) * 100)))
            if i == 'lilyvalley':
                self.textEdit.append('Ландыш  = %.1f%%' % ( (r.get(i) * 100)))

    def browse_port(self):
        global p
        subprocess.Popen(["retrain.py", '--image_dir', 'images', '--learning_rate', val ], shell=True)






class QWorker(QtCore.QThread):
    def __init__(self, name):
        QtCore.QThread.__init__(self)
        self.counter = 0
        self.name = name
        self.ExampleApp = None

    def run(self):
        recognize(filename)



class QWorker2(ExampleApp):
    def __init__(self, name):
        QtCore.QThread.__init__(self)
        self.counter = 1
        self.name = name

    def run(self):
        global t
        global p
        while p.poll() is None:
            ExampleApp.label_2.setText('Ждите ...')
        QMainWindow.label_2.setText('Ура!!!!')


