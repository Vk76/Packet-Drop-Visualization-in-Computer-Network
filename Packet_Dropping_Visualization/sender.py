##imports
import pygame
import pckt


##Globals
packetWidth=30
packetHeight=15
gameWidth=1000
gameHeight=700


class Sender:
    
    def __init__(self,canvas,x,y,img,numberOfPackets,fps,receiver,color):
        
        self.x=x
        self.y=y
        self.canvas=canvas
        self.numberOfPackets=numberOfPackets
        self.packets=[]
        for i in range(numberOfPackets):
            self.packets.append(pckt.Packet(canvas,x,y,color,None))
        self.fps=fps
        self.receiver=receiver
        self.image=pygame.image.load("./images/"+img)
        
        
    def sendPacket(self,time,direction):
        
        if time%(150-self.fps)==0 and len(self.packets)!=0:  #maintaining the FPS 
            p=self.packets.pop()
            p.setDirection(direction)
            p.setReceiver(self.receiver)
            return p
        else:
            return None
        
    def draw(self):
        
         self.canvas.blit(self.image,(self.x,self.y))