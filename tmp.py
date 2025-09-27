from turtle import *

# ваш код
screen = Screen()
screen.bgcolor('lightblue')

class Sprite(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.color(color)

    def collide(self, sprite):
        x = self.xcor()
        y = self.ycor()

        sx = sprite.xcor()
        sy = sprite.ycor()
        if abs(x - sx) < 20 and abs(y - sy) < 20:
            return True
        return False
        
class Player(Sprite):
    def __init__(self, x, y, color, speed):
        super().__init__(x, y, color)
        self.shape('circle')
        self.speed = speed
        
    def moveL(self):
        self.sh(180)
        print(1)
        self.fd(self.speed)
    def moveR(self):
        self.sh(0)
        self.fd(self.speed)
    def moveU(self):
        self.sh(90)
        self.fd(self.speed)
    def moveD(self):
        self.sh(270)
        self.fd(self.speed)
        
p = Player(0, 0, "green", 5)

screen.onkey(p.moveL, "Left")
screen.onkey(p.moveR, "Right")
screen.onkey(p.moveU, "Up")
screen.onkey(p.moveD, "Down")
screen.listen()

done()