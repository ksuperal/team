import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

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
    w = Simple_drawing_window3()
    w.show()
    
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())