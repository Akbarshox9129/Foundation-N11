from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application")
        self.setGeometry(200,200,500,500)
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",24))
        obj.move(x,y)
    def start(self):
        ok=QPushButton("OK",self)
        self.font(ok,50,50)

        cancel=QPushButton("CANCEL",self)
        self.font(cancel,200,50)
        
        hbox=QHBoxLayout(self)
        hbox.addStretch()
        hbox.addWidget(ok)
        hbox.addStretch()
        hbox.addWidget(cancel)
        hbox.addStretch()
        
        vbox=QVBoxLayout(self)
        vbox.addStretch()
        vbox.addWidget(cancel)
        vbox.addWidget(ok)
        vbox.addStretch()

        ok.clicked.connect(self.run)
    def run(self):
        miniwindow=QMessageBox(self)
        miniwindow.setWindowTitle("Xatoliklar bilan ishlash oynachasi")
        miniwindow.setText("Bu yerda dasturdagi xatoliklar chiqadi")
        miniwindow.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Reset)
        miniwindow.setDetailedText("Bu yerda xatolik bo'yicha to'liqroq ma'lumotga ega bo'lsa bo'ladi")
        miniwindow.setIcon(QMessageBox.Critical)
        miniwindow.setIcon(QMessageBox.Question)
        miniwindow.setIcon(QMessageBox.Information)
        miniwindow.show()
oyna=Window()
oyna.show()
app.exec_()