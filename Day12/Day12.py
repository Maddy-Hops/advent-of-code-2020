import math
with open("/home/maddy/Documents/AoC-2020/Day12/input.txt","r") as f:
        data = [x.strip("\n") for x in f.readlines()]

class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0

    def resolveDirection(self,cmd,value):
            self.direction = math.degrees(self.direction)
            if cmd == 'L':
                self.direction += value
                if self.direction >= 360: self.direction -= 360
            elif cmd == 'R': 
                self.direction -= value
                if self.direction <    0: self.direction += 360
            self.direction = math.radians(self.direction)

    def move(self,value):
        self.x = self.x + (value * math.cos(self.direction))
        self.y = self.y + (value * math.sin(self.direction))
        if math.isclose(self.x, math.ceil(self.x), rel_tol=1e-9, abs_tol=0.0):
            self.x = math.ceil(self.x)
        elif math.isclose(self.x, math.floor(self.x), rel_tol=1e-9, abs_tol=0.0):
            self.x = math.floor(self.x)
        if math.isclose(self.y, math.ceil(self.y), rel_tol=1e-9, abs_tol=0.0):
            self.y = math.ceil(self.y)
        elif math.isclose(self.y, math.floor(self.y), rel_tol=1e-9, abs_tol=0.0):
            self.y = math.floor(self.y)

    def parseCommand(self, cmd):
        value = int(cmd[1:])
        cmd = cmd[0]
            
        if   cmd == 'E': self.x += value
        elif cmd == 'W': self.x -= value
        elif cmd == 'N': self.y += value
        elif cmd == 'S': self.y -= value
        elif cmd == 'L' or cmd == 'R': self.resolveDirection(cmd,value)
        elif cmd == 'F': self.move(value)
    
ship = Ship()

for i in data:
    ship.parseCommand(i)
print("X: ", ship.x,"\nY: ", ship.y)