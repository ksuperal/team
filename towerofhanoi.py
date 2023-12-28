import turtle as t

class Disk:
    def __init__(self, name="", x=0, y=0, height=20, width=40):
        self.dname = name
        self.dxpos = x
        self.dypos = y
        self.dheight = height
        self.dwidth = width
    
    def showdisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.setheading(0)
        t.pendown()
        t.fillcolor("red")
        t.begin_fill()
        for i in range(2):
            t.forward(self.dwidth/2)
            t.left(90)
            t.forward(self.dheight)
            t.left(90)
        t.end_fill()
        t.penup()
        t.setheading(0)
        t.goto(self.dxpos, self.dypos)
    
    def newpos(self, x, y):
        self.dxpos = x
        self.dypos = y
    
    def cleardisk(self):
        t.setheading(0) 
        t.goto(self.dxpos, self.dypos) 
        t.clear()  
        t.setheading(0)  
        t.goto(self.dxpos, self.dypos)  
        
        