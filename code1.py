import tkinter
from network import Network


width = 500
height = 500
win = tkinter.display.set_mode(width, height)
tkinter.display.set_caption("client")

clientNumber = 0

class Player():
    def  init  (self, x, y, width, height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        
    def draw (self, win):
        tkinter.draw.rect(win, self.color, self.rect)
        
    def move (self):
        keys = tkinter.key.get.pressed()
        
        if keys[tkinter.K_LEFT]:
            self.x -= self.vel
            
        if keys[tkinter.K_RIGHT]:
            self.x += self.vel
            
        if keys[tkinter.K_UP]:
            self.y -= self.vel
            
        if keys[tkinter.K_DOWN]:
            self.y += self.vel
            
            self.update()
            
     def update(self):           
            self.rect = (self.x, self.y, self.width, self.height)
 
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup][1])     

def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player.draw(win)
    tkinter.display.update()
    
def main():
    run = True
    n = Network()
    startPos = read_Pos(n.getPos())
    p = Player(50,50,100,100,(0,255,0))
    p2 = Player(50,50,100,100,(255,0,0))
    clock = tkinter.time.clock()
    
    while run:
        
        clock.tick(60)
 
        p2Pos = read_pos(n.send(make_pos((p.x. p.y)))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        
        for event in tkinter.event.get():
            if event.type == tkinter.QUIT:
                run = False
                tkinter.quit()
                
                
        p.move()        
        redrawWindow(win, p, p2)
        
main()
