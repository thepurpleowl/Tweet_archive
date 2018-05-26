from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pandas as pd
import string
import matplotlib.pyplot as plt
import sys

with open('stylesheet_compare.txt','r') as f:
    sheet=f.read()

class messageDialog(QDialog):
    def __init__(self,parent=None):
        super(messageDialog,self).__init__(parent)
        self.setFixedSize(200,200)
        self.setStyleSheet(sheet)
        self.layout_ui=QVBoxLayout()
        self.setupUI()
        self.setLayout(self.layout_ui)
        self.setWindowModality(Qt.ApplicationModal)
        self.show()
        self.exec_()
    def setupUI(self):
        label=QLabel("Sorry,data not available")
        button=QPushButton("OK")
        self.layout_ui.addWidget(label)
        self.layout_ui.addWidget(button)
        button.clicked.connect(self.clicked)

    def clicked(self):
        self.setParent(None)
        self.close()
        #self.destroy(True)