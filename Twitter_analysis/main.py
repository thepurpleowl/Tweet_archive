from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import pandas as pd
import string
import matplotlib.pyplot as plt
import sys
from compare import compareWindow
from predict import predictWindow
with open('stylesheet.txt','r') as f:
    sheet=f.read()
df1=pd.read_excel('data_sales.xlsx')
df=pd.pivot_table(df1,index=['year'])
years=['2010','2011','2012','2013','2014','2015','2016']
companies=['samsung','apple','nokia/microsoft','lg','lenovo','sony']

class qWindow(QWidget):
    def __init__(self, parent=None):
        super(qWindow, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.list_columns=list(df.columns)
        #print self.list_columns
        self.topUI()
        self.mainUI()
        self.wrap_layout.addWidget(self.top_window)
        self.wrap_layout.addWidget(self.main_window)
        self.setLayout(self.wrap_layout)
        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(sheet)
        self.compare_list=[]
        # self.wrap_layout.addLayout(self.main_layout)

    def topUI(self):
        self.top_window = QWidget()
        self.top_window.setObjectName("topwindow")
        self.top_window.setMinimumHeight(150)
        self.button_predict=QPushButton("Predict")
        self.button_predict.setMaximumWidth(200)
        self.button_predict.clicked.connect(self.predict_clicked)
        self.button_compare=QPushButton("Compare")
        self.button_compare.setMaximumWidth(200)
        self.button_compare.clicked.connect(self.compare_clicked)
        self.top_window_layout=QHBoxLayout()
        self.top_window_layout.addStretch()
        self.top_window_layout.addWidget(self.button_compare)
        self.top_window_layout.addWidget(self.button_predict)
        self.top_window_layout.addStretch()
        self.top_window.setLayout(self.top_window_layout)

    def compare_clicked(self):
        w=compareWindow(self.list_columns,df1)
        self.compare_list.append(w)
        w.show()

    def predict_clicked(self):
        w=predictWindow(companies,years)
        self.compare_list.append(w)
        w.show()

    def mainUI(self):
        self.main_window = QWidget()
        self.main_window.setMinimumHeight(300)
        self.main_window.setMinimumWidth(1000)
        self.main_window_layout=QHBoxLayout()
        self.main_leftUI()
        self.main_rightUI()

        self.main_window.setLayout(self.main_window_layout)
        # self.main_window.setStyleSheet("*{background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #8bf192, stop: 1 #41c34a);}")

    def main_leftUI(self):
        scroll_left_main=QScrollArea()
        scroll_left_main.setWidgetResizable(True)
        self.list_widget=QListWidget()
        self.list_widget.addItems(self.list_columns)
        self.list_widget.itemClicked.connect(self.Clicked)
        scroll_left_main.setMinimumHeight(250)
        scroll_left_main.setMaximumWidth(300)
        self.list_widget.setMinimumWidth(250)
        self.list_widget.setMaximumWidth(300)
        scroll_left_main.setWidget(self.list_widget)
        self.main_window_layout.addWidget(scroll_left_main)

    def Clicked(self,item):
        df1_curr=pd.pivot_table(df1,index=['year'],values=[str(item.text())])
        f1=plt.figure(2)
        plt.title("Data for "+item.text())
        df1_curr.plot(ax=f1.gca())
        lgd1=plt.legend(loc='center left', bbox_to_anchor=(-0.4, 0.5))
        f1.savefig('temp1.png', bbox_extra_artists=(lgd1,), bbox_inches='tight')
        #plt.close()
        f2=plt.figure(2)
        plt.title("bar graph for "+item.text())
        df1_curr.plot(kind='bar',ax=f2.gca())
        lgd2=plt.legend(loc='center left', bbox_to_anchor=(-0.4, 0.5))
        f2.savefig('temp2.png', bbox_extra_artists=(lgd2,), bbox_inches='tight')
        plt.close()
        self.label1.setPixmap(QPixmap('temp1.png'))
        self.label2.setPixmap(QPixmap('temp2.png'))



    def main_rightUI(self):
        scroll_area_right=QScrollArea()
        scroll_area_right.setWidgetResizable(True)
        self.main_right=QWidget()
        #self.main_right.setMinimumHeight(250)
        #self.main_right.setMinimumWidth(600)
        #scroll_area_right.setMinimumHeight(250)
        #scroll_area_right.setMinimumWidth(600)

        self.label1=QLabel()
        self.label2=QLabel()
        #label1.setMinimumHeight(600)
        #label2.setMinimumHeight(600)
        #label1.setMaximumWidth(400)
        #label2.setMaximumWidth(400)
        self.label1.setPixmap(QPixmap('temp1.png'))
        self.label2.setPixmap(QPixmap('temp2.png'))
        self.main_right_layout=QVBoxLayout()
        #self.main_right_layout.setSpacing(0)
        self.main_right_layout.addWidget(self.label1)
        self.main_right_layout.addWidget(self.label2)
        self.main_right.setLayout(self.main_right_layout)
        scroll_area_right.setWidget(self.main_right)
        #scroll_area_right.setLayout(self.main_right_layout)

        self.main_window_layout.addWidget(scroll_area_right)




app = QApplication(sys.argv)
wind = qWindow()
wind.show()
sys.exit(app.exec_())
