# -*- coding: cp1251 -*-
__author__ = 'Work'
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
import sys  # We need sys so that we can pass argv to QApplication
from importlib import reload  # для python 3.0 - 3.3
reload(sys) # для python 2.x
import manage



need_dialog=False

if __name__ == '__main__':  # if we're running file directly and not importing it
    app = QApplication(sys.argv)  # A new instance of QApplication
    #form1 = windowApp.ExampleApp()  # We set the form to be our ExampleApp (design)
    #form1.show()  # Show the form

    form1 = manage.ExampleApp()  # We set the form to be our ExampleApp (design)
    form1.show()  # Show the form
    app.exec_()  # and execute the app app