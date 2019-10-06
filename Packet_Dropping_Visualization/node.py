
##imports
import pygame


##Globals
packetWidth=30
packetHeight=15
gameWidth=1000
gameHeight=700




class Node:
    def __init__(self,canvas,image,capacity,x,y,fps,receiver):
        
        self.canvas=canvas
        self.capacity=capacity
        self.x=x
        self.y=y
        self.img=pygame.image.load("./images/"+image)
        self.filled=0
        self.fps=fps
        self.receiver=receiver
        self.packets=[]
        
    def receivePacket(self,packet):
        
        if self.capacity>len(self.packets): 
            self.packets.append(packet)
            self.filled+=1
            return True
        return False
        
        
    def sendPacket(self,time,direction):
        if time%(55-self.fps)==0 and len(self.packets)!=0:
            p=self.packets.pop()
            p.setDirection(direction)
            p.setReceiver(self.receiver)
            self.filled-=1
            return p
        else:
            return None
    
        
        
    def drawNodeWithCapacity(self):
        
        #draw node image
         self.canvas.blit(self.img,(self.x,self.y))
         
         filled=self.filled
         
         #drawing Bucket
         if self.receiver!=None:    #drawing Bucket for Nodes
             row=self.y+100
             column=(self.x+50,self.x+15)
             
             while filled>0:
                 
                 pygame.draw.rect(self.canvas,self.packets[filled-1].color,[column[filled%2],row,packetWidth,packetHeight])
                 if filled%2:row+=20    #changing row
                 filled-=1
         else:                      #drawing Bucket for Receiver
             row=self.y+210
             column=(self.x+150,self.x+110,self.x+70,self.x+30)
         
             while filled>0:
                 
                 pygame.draw.rect(self.canvas,self.packets[filled-1].color,[column[filled%4],row,packetWidth,packetHeight])
                 if filled%4==0:row+=20    #changing row
                 filled-=1
            