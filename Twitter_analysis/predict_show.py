from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pandas as pd
import string
import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge,Lasso
import numpy as np
import sys

sheet='''
    QLabel#Display{
font-size:20px;
padding:5px;
max-width:800px;
background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ede5a5, stop: 1 #dbd283);
}

QScrollArea{
margin-left:20px;
}
'''

class predictShow(QWidget):
    def __init__(self,name_product,ob,key,parent=None):
        super(predictShow,self).__init__(parent)
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)
        self.setStyleSheet(sheet)
        self.product_name=name_product
        self.twitter_data=ob
        self.key_predict=key
        print type(key)
        self.layout_predict=QHBoxLayout()
        self.analyze()
        self.setupUI()
        self.setLayout(self.layout_predict)

    def find_avg(self,lis_tweets):
        pol=0
        sub=0
        for tweet in lis_tweets:
            t=TextBlob(tweet)
            pol+=t.sentiment[0]
            sub+=t.sentiment[1]
        n=len(lis_tweets)
        return (pol/n,sub/n)

    def analyze(self):
        pol=[]
        sub=[]
        keys=sorted(self.twitter_data.keys())
        for key in keys:
            a,b=self.find_avg(self.twitter_data[key])
            pol.append(a)
            sub.append(b)

        ##saving figures for sentiment and polarity
        plt.figure(1)
        plt.plot(pol,'g')
        plt.xlabel('year/quartile')
        plt.ylabel('polarity')
        plt.title('Polarity of twitter data')
        plt.savefig('polarity.png')
        plt.close()
        plt.figure(2)
        plt.plot(sub,'r')
        plt.title('Subjectivity of twitter data')
        plt.xlabel('year/quartile')
        plt.ylabel('Subjectivity')
        plt.savefig('subjectivity.png')
        plt.close()

        df=pd.read_excel('data_sales.xlsx')
        df1=pd.pivot_table(df,index=['year'],values=[self.product_name])

        X=[]
        y=[]
        for i in range(len(df1)):
            val=float(df1.iloc[i])
            if str(val) !='nan':
                X.append([i,pol[i],sub[i]])
                y.append(float(df1.iloc[i]))

        reg=LinearRegression()
        reg.fit(X,y)
        predict_index=sorted(self.twitter_data.keys()).index(self.key_predict)
        x_predict=[predict_index,pol[predict_index],sub[predict_index]]
        self.predict_data=reg.predict([x_predict])[0]
        print self.predict_data

        ##saving figures
        plt.figure(1)
        df1.plot()
        plt.title('Actual data for '+self.product_name)
        plt.savefig('actual.png')
        plt.close()
        plt.figure(2)
        plt.title('Predicted data for '+self.product_name)
        plt.plot(range(len(X)),reg.predict(X))
        plt.savefig('predicted.png')
        plt.close()

    def setupUI(self):
        self.container_wid=QWidget()
        self.label1=QLabel()
        self.label2=QLabel()
        self.label3=QLabel()
        self.label4=QLabel()
        self.label5=QLabel()
        layout=QVBoxLayout()
        self.label1.setObjectName('Display')
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.label5)
        self.label1.setText("predicted sales value for "+self.product_name+' for '+self.key_predict+' is '+str(self.predict_data))
        self.label2.setPixmap(QPixmap('subjectivity.png'))
        self.label3.setPixmap(QPixmap('polarity.png'))
        self.label4.setPixmap(QPixmap('actual.png'))
        self.label5.setPixmap(QPixmap('predicted.png'))
        self.container_wid.setLayout(layout)
        scroll_area_comp=QScrollArea()
        scroll_area_comp.setMinimumWidth(900)
        scroll_area_comp.setWidgetResizable(True)
        scroll_area_comp.setWidget(self.container_wid)
        self.layout_predict.addWidget(scroll_area_comp)


