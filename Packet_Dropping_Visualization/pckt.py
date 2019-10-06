##imports
import pygame


##Globals
packetWidth=30
packetHeight=15
gameWidth=1000
gameHeight=700


class Packet:
    
    def __init__(self,canvas,startx,starty,color,goto):
        
        self.startx=startx
        self.starty=starty
        self.color=self.getColor(color)
        self.canvas=canvas
        self.direction=None
        self.speed=1
        self.goto=None
    
    def setReceiver(self,s):
        self.goto=s
        
    def setDirection(self,direction):
        self.direction=direction
        
    
    def move(self):
        
        if self.direction=="topdownright":
            self.moveTopDownRight()
            
        elif self.direction=="bottomupright":
            self.moveBottomUpRight()
            
        elif self.direction=="bottomupleft":
            self.moveBottomUpLeft()
            
        elif self.direction=="bottomupleft":
            self.moveBottomUpLeft()
            
        elif self.direction=="right":
            self.moveRight()
            
        elif self.direction=="bottom":
            self.moveBottom()
            
        elif self.direction=="up":
            self.moveUp()
        
        
    def moveTopDownRight(self):
        
        self.startx+=self.speed
        self.starty+=self.speed
    
    def moveBottomUpRight(self):
        
        self.startx+=self.speed
        self.starty-=self.speed
        
    def moveTopDownLeft(self):
        
        self.startx-=self.speed
        self.starty+=self.speed
    
    def moveBottomUpLeft(self):
        
        self.startx-=self.speed
        self.starty-=self.speed
    
    def moveRight(self):
        
        self.startx+=self.speed
        
    def moveBottom(self):
        
        self.starty+=self.speed
        
    def moveUp(self):
        
        self.starty-=self.speed
    
    def changeColor(self,color):
        
        self.color=self.getColor(color)
    
    def draw(self):
        
        pygame.draw.rect(self.canvas,self.color,[self.startx,self.starty,packetWidth,packetHeight])
    
    def getColor(self,color):
        
        if color=="red":
            return (255,0,0)
        if color=="green":
            return (0,255,0)
        if color=="blue":
            return (0,0,255)
        if color=="white":
            return (255,255,255)
        if color=="black":
            return (0,0,0)
        if color=="pink":
            return (255,20,147)
        if color=="orange":
            return (255,165,0)
        return (0,0,0)
        
