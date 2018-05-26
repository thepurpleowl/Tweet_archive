from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pandas as pd
import string
import matplotlib.pyplot as plt
import sys

class compareShow(QWidget):
    def __init__(self,compare_list,data_ob,parent=None):
        super(compareShow,self).__init__(parent)
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)
        self.items=compare_list
        self.df1=data_ob
        self.layout=QHBoxLayout()
        self.setup()
        self.setupPlot()
        self.setLayout(self.layout)

    def setup(self):
        self.container_wid=QWidget()
        self.label1=QLabel()
        self.label2=QLabel()
        layout=QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.container_wid.setLayout(layout)
        scroll_area_comp=QScrollArea()
        scroll_area_comp.setMinimumWidth(800)
        scroll_area_comp.setWidgetResizable(True)
        scroll_area_comp.setWidget(self.container_wid)
        self.layout.addWidget(scroll_area_comp)

    def setupPlot(self):
        df1_curr=pd.pivot_table(self.df1,index=['year'],values=self.items)
        f1=plt.figure(2)
        plt.title("Comparing "+self.items[0]+"... ")
        df1_curr.plot(ax=f1.gca())
        lgd1=plt.legend(loc='center left', bbox_to_anchor=(-0.6, 0.5))
        f1.savefig('comp1.png', bbox_extra_artists=(lgd1,), bbox_inches='tight')
        #plt.close()
        f2=plt.figure(2)
        df1_curr.plot(kind='bar',ax=f2.gca())
        lgd2=plt.legend(loc='center left', bbox_to_anchor=(-0.6, 0.5))
        f2.savefig('comp2.png', bbox_extra_artists=(lgd2,), bbox_inches='tight')
        plt.close()
        self.label1.setPixmap(QPixmap('comp1.png'))
        self.label2.setPixmap(QPixmap('comp2.png'))