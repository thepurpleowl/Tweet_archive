from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pandas as pd
import string
import matplotlib.pyplot as plt
import sys
import os
from message_dialog import messageDialog
from predict_show import predictShow
import pickle
with open('stylesheet_compare.txt','r') as f:
    sheet=f.read()
companies={'nokia/microsoft':'nokia.pkl','lenovo':'lenovo.pkl','apple':'apple.pkl','sony':'sony.pkl'}
class predictWindow(QWidget):
    def __init__(self,products,years,parent=None):
        super(predictWindow,self).__init__(parent)
        self.setMinimumHeight(400)
        self.setMinimumWidth(200)
        self.list_products=products
        self.list_years=years
        self.list_quartile=['q1','q2','q3','q4']
        self.setStyleSheet(sheet)
        self.pred_wind_list=[]
        self.layout_pred=QVBoxLayout()
        self.setupUI()
        self.setLayout(self.layout_pred)

    def setupUI(self):
        self.cb_product=QComboBox()
        self.cb_product.addItems(self.list_products)
        self.cb_years=QComboBox()
        self.cb_years.addItems(self.list_years)
        self.cb_quartile=QComboBox()
        self.cb_quartile.addItems(self.list_quartile)
        self.button_predict=QPushButton("Predict")
        self.button_predict.clicked.connect(self.predict_clicked)
        self.layout_pred.addWidget(self.cb_product)
        self.layout_pred.addWidget(self.cb_years)
        self.layout_pred.addWidget(self.cb_quartile)
        self.layout_pred.addWidget(self.button_predict)

    def predict_clicked(self):
        name_product=str(self.cb_product.currentText())
        name_year=str(self.cb_years.currentText())
        name_quartile=str(self.cb_quartile.currentText())
        print name_product
        if name_product not in companies.keys():
            win=messageDialog()
            self.pred_wind_list.append(win)
            return
            #win.show()
        key=name_year[2:]+'/'+name_quartile
        dir_name='data/'+companies[name_product]
        ob=pickle.load(open(dir_name,'r'))
        if key not in ob.keys():
            win=messageDialog()
            self.pred_wind_list.append(win)
            return
        win=predictShow(name_product,ob,key)
        self.pred_wind_list.append(win)
        win.show()