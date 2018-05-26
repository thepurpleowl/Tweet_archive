from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pandas as pd
import string
import matplotlib.pyplot as plt
import sys
from compare_show import compareShow

with open('stylesheet_compare.txt') as f:
    sheet=f.read()


class compareWindow(QWidget):
    def __init__(self,data_list,data_ob,parent=None):
        super(compareWindow,self).__init__(parent)
        self.setMinimumHeight(300)
        self.setMinimumWidth(600)
        self.setStyleSheet(sheet)
        self.items=data_list
        self.data_ob=data_ob
        self.comp_wind_list=[]
        self.layout_choose=QHBoxLayout()
        self.leftUI()
        self.rightUI()
        self.setLayout(self.layout_choose)
    def leftUI(self):
        self.left_wid=QWidget()
        self.left_wid.setMinimumWidth(300)
        self.left_layout=QVBoxLayout()
        self.left_layout_items=QVBoxLayout()
        self.left_items_list=[]
        self.left_layout.addLayout(self.left_layout_items)
        self.left_layout.addStretch()
        self.left_wid.setLayout(self.left_layout)
        scroll_area=QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.left_wid)
        self.layout_choose.addWidget(scroll_area)


    def rightUI(self):
        layout=QVBoxLayout()
        self.cb1=QComboBox()
        self.cb1_list=list(self.items)
        self.cb1.addItems(self.cb1_list)
        self.button_compare=QPushButton("Compare")
        self.button_compare.clicked.connect(self.compare_clicked)
        layout.addStretch()
        layout.addWidget(self.cb1)
        layout.addWidget(self.button_compare)
        layout.addStretch()
        self.cb1.activated.connect(self.select_cb1)
        self.layout_choose.addLayout(layout)
        self.lis_w=[]

    def select_cb1(self):
        ob=self.cb1.currentText()
        txt=self.cb1_list[self.cb1_list.index(ob)]
        self.cb1_list.remove(ob)
        self.left_items_list.append(txt)
        self.cb1.clear()
        self.cb1.addItems(self.cb1_list)
        label=QLabel()
        label.setText(ob)
        self.left_layout_items.addWidget(label)

    def compare_clicked(self):
        if len(self.left_items_list) ==0:
            return
        comp_wind=compareShow(self.left_items_list,self.data_ob)
        self.cb1_list=list(self.items)
        self.left_items_list=[]
        self.cb1.clear()
        self.cb1.addItems(self.cb1_list)
        for i in reversed(range(self.left_layout_items.count())):
            self.left_layout_items.itemAt(i).widget().setParent(None)
        self.comp_wind_list.append(comp_wind)
        comp_wind.show()