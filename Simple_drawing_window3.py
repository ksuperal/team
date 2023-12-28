import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/flan.png")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([QPoint(70, 100), QPoint(100, 110), QPoint(130, 100), QPoint(100, 150)])
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        
        p.drawPolygon([QPoint(50, 200), QPoint(150, 200), QPoint(100, 400)])
        
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/player.png")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

       

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)

        p.setPen(QColor(0, 0, 0))  
        p.setBrush(QColor(255, 255, 255))  
        p.drawEllipse(QRect(150, 250, 100, 50))  
        p.drawLine(175, 250, 175, 300)
        p.drawLine(150, 275, 250, 275)
        p.end()

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/flan.png")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 100, 0))
        p.drawPolygon([QPoint(70, 100), QPoint(100, 110), QPoint(130, 100), QPoint(100, 150)])
        p.setBrush(QColor(127, 0, 0))
        p.drawPolygon([QPoint(110, 140), QPoint(140, 150), QPoint(170, 140), QPoint(140, 190)])
        p.setBrush(QColor(0, 0, 127))
        p.drawPolygon([QPoint(150, 180), QPoint(180, 190), QPoint(210, 180), QPoint(180, 230)])
        
       
        
       
        
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()
        
def main():
    app = QApplication(sys.argv)
    w1 = Simple_drawing_window1()
    w1.show()
    w2 = Simple_drawing_window2()
    w2.show()
    w3 = Simple_drawing_window3()
    w3.show()
    
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
