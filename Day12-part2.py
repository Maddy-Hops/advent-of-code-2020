import math
import numpy as np
from math import sin, cos, radians
with open("/home/maddy/Documents/AoC-2020/Day12/input.txt","r") as f:
        data = [x.strip("\n") for x in f.readlines()]

class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.wpx = 10
        self.wpy = 1
    def rotateAboutPoint(self,cmd,value):
        if cmd == 'R': 
            value -= 360
            value = abs(value)
        value = radians(value)
        #self.wpx = self.wpx - self.x
        #self.wpy = self.wpy - self.y
        self.wpx,self.wpy  = self.wpx * cos(value) - self.wpy * sin(value),self.wpy * cos(value) + self.wpx * sin(value)
        #self.wpx = self.wpx + self.x
        #self.wpy = self.wpy + self.y
    
    def move(self,value):
        self.x += self.wpx * value
        self.y += self.wpy * value
        
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
            
        if   cmd == 'E': self.wpx += value
        elif cmd == 'W': self.wpx -= value
        elif cmd == 'N': self.wpy += value
        elif cmd == 'S': self.wpy -= value
        elif cmd == 'L' or cmd == 'R': self.rotateAboutPoint(cmd,value)
        elif cmd == 'F': self.move(value)
    
ship = Ship()

for i in data:
    ship.parseCommand(i)
print("X: ", ship.x,"\nY: ", ship.y)
print(abs(ship.x)+abs(ship.y))