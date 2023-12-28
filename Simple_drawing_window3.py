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
        
        p.setPen(QColor(221, 204, 162))
        p.setBrush(QColor(246, 227, 180))
        p.drawPolygon([QPoint(40, 300), QPoint(160, 300), QPoint(135, 200), QPoint(65, 200), QPoint(40, 300)])

        p.setPen(QColor(153, 114, 18))
        p.setBrush(QColor(153, 114, 18))
        p.drawPolygon([QPoint(57, 230), QPoint(143, 230), QPoint(135, 200), QPoint(65, 200), QPoint(57, 230)])

        p.drawPie(58, 218, 21, 21, 2880, 180 * 16)
        p.drawPie(79, 218, 21, 21, 2880, 180 * 16)
        p.drawPie(100, 218, 21, 21, 2880, 180 * 16)
        p.drawPie(121, 218, 21, 21, 2880, 180 * 16)
        
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window2(QWidget):
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

class Simple_drawing_window3(QWidget):
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
        
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    # w = Simple_drawing_window2()
    # w = Simple_drawing_window3()
    w.show()
    
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
        