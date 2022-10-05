x1 = 250
y1 = 100
speedy = 0.0981
speedx = 5
S = 1

def setup():
    size(1000,500)

def draw():
    global x1,y1,speedy,speedx,S
    clear()
    fill(255,255,255)
    circle(x1,y1,50)
    line(0,445,1000,445)
    stroke(255)
    delay(1)
    speedy = speedy+0.0981
    x1=x1+speedx
    speedx=speedx/1.0015
    if y1<420:
        y1=y1+speedy
    else:
        y1=419.9
        speedy=speedy*-1/1.25
    if x1>1025:
        x1=-25
    if x1<-25:
        x1=1025
        print(S)
    
    if mousePressed and (mouseButton == LEFT):
        if ((x1-60<mouseX<x1+60) and (y1-60<mouseY<y1+60)) or S==1:
            line(x1,y1,mouseX,mouseY)
            S=1
            speedx=speedx/1.2
            speedy=speedy/1.2
            if x1<mouseX:
                speedx=speedx+(mouseX-x1)/50
            if x1>mouseX:
                speedx=speedx-(x1-mouseX)/50
            if y1<mouseY:
                speedy=speedy+(mouseY-y1)/50
            if y1>mouseY:
                speedy=speedy-(y1-mouseY)/50
        else:
            S=0
