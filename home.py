from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QFont
import sys,random
app=QApplication(sys.argv)
ls=[1,2,3,1,2,3]
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1-UYGA VAZIFA")
        self.setGeometry(250,250,500,600)
        self.start()
        self.show()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",24))
        obj.setGeometry(x,y,80,80)
    def start(self):
        self.a1=QPushButton("",self)
        self.font(self.a1,50,50)
        self.a1.clicked.connect(self.A1)
        self.a2=QPushButton("",self)
        self.font(self.a2,150,50)
        self.a2.clicked.connect(self.A2)
        self.a3=QPushButton("",self)
        self.font(self.a3,250,50)
        self.a3.clicked.connect(self.A3)
        self.a4=QPushButton("",self)
        self.font(self.a4,50,150)
        self.a4.clicked.connect(self.A4)
        self.a5=QPushButton("",self)
        self.font(self.a5,150,150)
        self.a5.clicked.connect(self.A5)
        self.a6=QPushButton("",self)
        self.font(self.a6,250,150)
        self.a6.clicked.connect(self.A6)
    def check(self):
        if self.a1.text()!="" and self.a2.text()!="" and self.a1.text()==self.a2.text():
            self.a1.hide()
            self.a2.hide()
            self.a3.setText("")
            self.a4.setText("")
            self.a5.setText("")
            self.a6.setText("")
            ls.remove(int(self.a1.text()))
            ls.remove(int(self.a2.text()))
        elif self.a1.text()!="" and self.a2.text()!="":
            self.a1.setText("")
            self.a2.setText("")
            self.a3.setText("")
            self.a4.setText("")
            self.a5.setText("")
            self.a6.setText("")
    def A1(self):
        if self.a1.text()=="":
            a=random.choice(ls)
            self.a1.setText(str(a))
        self.check()
    def A2(self):
        if self.a2.text()=="":
            a=random.choice(ls)
            self.a2.setText(str(a))
        self.check()
    def A3(self):
        if self.a3.text()=="":
            a=random.choice(ls)
            self.a3.setText(str(a))
        self.check()
    def A4(self):
        if self.a4.text()=="":
            a=random.choice(ls)
            self.a4.setText(str(a))
        self.check()
    def A5(self):
        if self.a5.text()=="":
            a=random.choice(ls)
            self.a5.setText(str(a))
        self.check()
    def A6(self):
        if self.a6.text()=="":
            a=random.choice(ls)
            self.a6.setText(str(a))
        self.check()
win=Window()
app.exec_()