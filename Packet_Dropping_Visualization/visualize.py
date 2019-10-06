##imports
import pygame
import node
import sender

#Globals
packetWidth=30
packetHeight=15
gameWidth=1000
gameHeight=700


class Visualize:
    
    def __init__(self,NO_OF_PACKETS_SENDER1,NO_OF_PACKETS_SENDER2,NO_OF_PACKETS_SENDER3,FPS_OF_SENDER1,FPS_OF_SENDER2,FPS_OF_SENDER3,FPS_OF_NODE1,FPS_OF_NODE2,BUFFER_OF_NODE1,BUFFER_OF_NODE2):
        self.NO_OF_PACKETS_SENDER1=NO_OF_PACKETS_SENDER1
        self.NO_OF_PACKETS_SENDER2=NO_OF_PACKETS_SENDER2
        self.NO_OF_PACKETS_SENDER3=NO_OF_PACKETS_SENDER3
        self.FPS_OF_SENDER1=FPS_OF_SENDER1
        self.FPS_OF_SENDER2=FPS_OF_SENDER2
        self.FPS_OF_SENDER3=FPS_OF_SENDER3
        self.FPS_OF_NODE1=FPS_OF_NODE1
        self.FPS_OF_NODE2=FPS_OF_NODE2
        self.BUFFER_OF_NODE1=BUFFER_OF_NODE1
        self.BUFFER_OF_NODE2=BUFFER_OF_NODE2
        self.sender1=None
        self.sender2=None
        self.sender3=None
        self.node1=None
        self.node2=None
        self.receiver=None
        self.packets=[]
        self.font=None
        self.canvas=pygame.display.set_mode((gameWidth,gameHeight))
        self.FPS=60
        self.clock=None
        
        
    def initializeSenders(self):
        
        self.sender1=sender.Sender(self.canvas,10,90,"rsz_sender1.png",self.NO_OF_PACKETS_SENDER1,self.FPS_OF_SENDER1,"node1","pink")
        self.sender2=sender.Sender(self.canvas,10,530,"rsz_sender2.png",self.NO_OF_PACKETS_SENDER2,self.FPS_OF_SENDER2,"node1","green")
        self.sender3=sender.Sender(self.canvas,320,530,"rsz_sender3.png",self.NO_OF_PACKETS_SENDER3,self.FPS_OF_SENDER3,"node2","orange")
        
    def initializeNodes(self):
        
        self.node1=node.Node(self.canvas,"rsz_node.png",self.BUFFER_OF_NODE1,230,310,self.FPS_OF_NODE1,"node2")    
        self.node2=node.Node(self.canvas,"rsz_node.png",self.BUFFER_OF_NODE2,540,310,self.FPS_OF_NODE2,"receiver")
        
    def initializeReceivers(self):
        
        self.receiver=node.Node(self.canvas,"receiver.JPG",100,800,310,10,None)
        
    def start(self):
        pygame.init()
        
        pygame.display.set_caption('Packet Dropping Visualization')
        
        self.font=pygame.font.SysFont("Calibri",50,True,False)
        self.clock = pygame.time.Clock()

        self.initializeNodes()
        self.initializeSenders()
        self.initializeReceivers()
        
        self.loop()
        
        quit()
        
        
    def draw(self):
        
        self.canvas.fill((255,255,255))
        self.node1.drawNodeWithCapacity()
        self.node2.drawNodeWithCapacity()
        self.receiver.drawNodeWithCapacity()
        self.sender1.draw()
        self.sender2.draw()
        self.sender3.draw()
        for packet in self.packets:
            packet.draw()
        self.heading("Packet Dropping Visualization")
        
    def move(self):
        
        for packet in self.packets:
            packet.move()
            
    def send(self,time):
        
        p=self.sender1.sendPacket(time,"topdownright")
        if p!=None:
            self.packets.append(p)
        p=self.sender2.sendPacket(time,"bottomupright")
        if p!=None:
            self.packets.append(p)
        p=self.sender3.sendPacket(time,"bottomupright")
        if p!=None:
            self.packets.append(p)
            
        n=self.node1.sendPacket(time,"right")
        if n!=None:
            self.packets.append(n)
        n=self.node2.sendPacket(time,"right")
        if n!=None:
            self.packets.append(n)
            
    def heading(self,text):
        
        screen_text=self.font.render(text,True,(0,0,255))
        self.canvas.blit(screen_text,[200,20])
        
    def loop(self):
        
        time=0
        while True:
            
            #for quiting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            #send
            self.send(time)
                
            #crash condition
            self.crashes()
                            
            
            #motion
            self.move()
            
            #draw 
            self.draw()
            #updating canvas
            pygame.display.update()
    
            self.clock.tick(self.FPS)
            
            time+=1
        
    def crashes(self):
        #for 1 crash checking
        for packet in self.packets:
            
            if packet.goto=="node2":  #all nodes coming at node2
                
                if packet.startx==self.node2.x and packet.starty==self.node2.y:
                    
                    if not self.node2.receivePacket(packet):
                        
                        if not self.node2.receivePacket(packet):  #if unable to process
                            
                            packet.setDirection("up")       #drop them
                            packet.changeColor("red")
                            
                    else:
                        
                        self.packets.remove(packet)
                        
            if packet.goto=="node1":        #all nodes coming at node2
                
                if packet.startx==self.node1.x and packet.starty==self.node1.y: 
                    
                    if not self.node1.receivePacket(packet):   #if unable to process
                        
                        packet.setDirection("up")   #dropthem
                        packet.changeColor("red")
                        
                    else:
                        
                        self.packets.remove(packet)  
                        
            if packet.goto=="receiver":    #all nodes coming at node2
                
                if packet.startx==self.receiver.x+82 and packet.starty==self.receiver.y:
                    
                    if not self.receiver.receivePacket(packet):   #if unable to process worst case as receiver always takes it
                        
                        packet.setDirection("up")
                        packet.changeColor("red")
                    else:
                        self.packets.remove(packet)   
                        
        #check another time beacuse two nodes may come at same time same node
        for packet in self.packets:
            
            if packet.goto=="node2":
                
                if packet.startx==self.node2.x and packet.starty==self.node2.y:
                    
                    if not self.node2.receivePacket(packet):
                        
                        if not self.node2.receivePacket(packet):
                            
                            packet.setDirection("up")
                            packet.changeColor("red")
                    else:
                        
                        self.packets.remove(packet)
                        
            if packet.goto=="node1":
                
                if packet.startx==self.node1.x and packet.starty==self.node1.y:
                    
                    if not self.node1.receivePacket(packet):
                        
                        packet.setDirection("up")
                        packet.changeColor("red")
                        
                    else:
                        self.packets.remove(packet)
                        
            if packet.goto=="receiver":
                
                if packet.startx==self.receiver.x+82 and packet.starty==self.receiver.y:
                    
                    if not self.receiver.receivePacket(packet):
                        
                        packet.setDirection("up")
                        packet.changeColor("red")
                    else:
                        
                        self.packets.remove(packet)
                        
        for packet in self.packets:      #removal of the dropped packets from window
            if packet.starty==60:
                self.packets.remove(packet)
    
    










    

             

                



        
        
                      





         
         
         
         
         
         
        