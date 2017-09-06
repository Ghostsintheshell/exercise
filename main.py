# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 22:49:13 2017

@author: Yew
"""

"""
This is the main program.
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
import dataspider
import tradingrecord
from datetime import date

"""
class Fund:
    def __init__(self,name,code):
        self.name = name
        self.code = code
"""        

def main():
    print('main program loaded!')
    
    #Trading day judgement. If tradingday = 1 then is a tradingday, else is not
    #a tradingday.
    datenow = date.today()
    #print(datenow)
    if datenow.isoweekday() == 6 or datenow.isoweekday() == 7 :
        tradingday = 0
    else:
        tradingday = 1
    #print(tradingday)
    
    #If it is a tradingday, then download the data from the Internet.
    if tradingday == 1:
        dataspider.dataspider()
    
    #Load tradingrecord
    TRflag = input("Do you want to add an trading recored?Y/N")
    if TRflag == "Y" or "y":
        tradingrecord.tradingrecord()
    else:
        pass
"""    
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('是的',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('ETFtrader')
        self.show()
"""
class QuitButton(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Quit Button')
        self.show()
        
app = QApplication(sys.argv)
#ex = Example()
qtn = QuitButton()


sys.exit(app.exec_())
if __name__ == '__main__':
    main()
    
    