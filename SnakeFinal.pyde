x1=600
y1=390
foodx=180
foody=150
coinx=750
coiny=270
coins=0
d=0
l=3
t=0
body = []
i=0
g=0
r=0
de=0
cv1=False
cv2=False
cv3=False
w=False
bs=False
bx=0
by=780
bi=False
bhe = 0
ti = 0
wx = 0
wy = 780
d2 = 0
bsc = 15


def setup():
    global img1,img2,img3,img4,img5
    size(1200,780)
    img1 = loadImage("RSG.png")
    img2 = loadImage("MCSG.png")
    img3 = loadImage("GSG.png")
    img4 = loadImage("RSSG.png")
    img5 = loadImage("RBSG.png")
def bossloop():
    global x1,y1,d,l,t,foodx,foody,i,coinx,coiny,coins,g,img1,r,de,img2,cv1,cv2,cv3,img3,w,bx,by,bs,bhe,img5,ti,wx,wy
    if bs == True:
        if bx > x1:
            bx-=7.5
        elif bx < x1:
            bx+=7.5
        if by > y1:
            by-=7.5
        elif by < y1:
            by+=7.5
        fill(250,100,100)
        rect(50,760,bhe,15)
        fill(100,100,100)
        square(wx,wy,30)
        if w == True:
            bhe-=(len(body)/5)
        if bhe <= 0:
            bs = False
            g = 2
    
        if x1 >= bx and x1 <= bx+60 and y1 >= by and y1 <= by + 60:
            if r == 0 and de == 0:
                x1 = 600
                y1 = 390
                l = 3
                bs = False
                wx = 0
                wy = 780
                bx=0
                by=780
            elif de == 0:
                r -= 1
                de = l + 3
            if de > 0:
                de -= 0.75
            elif de < 0:
                de=0
        
        if ti < 30:
            ti += 1
            
        else:
            ti = 0
            if d == 1:
                wx = x1
                wy = y1-240
            elif d == 2:
                wx = x1+240
                wy = y1
            elif d == 3:
                wx = x1
                wy = y1+240
            elif d == 4:
                wx = x1-240
                wy = y1
        if wx == x1 and wy == y1:
            if r == 0 and de == 0:
                x1 = 600
                y1 = 390
                l = 3
                bs = False
                wx = 0
                wy = 780
                bx=0
                by=780
            elif de == 0:
                r -= 1
                de = l + 4
            if de > 0:
                de -= 0.75
            elif de < 0:
                de=0

def gameloop():
    global x1,y1,d,l,t,foodx,foody,i,coinx,coiny,coins,g,r,de,cv1,cv2,cv3,w,bx,by,bs,bhe,d2,bsc
    clear()
    fill(199,21,133)
    square(1080,0,120)
    if i > 0:
        fill(150,150,0)
    else:
        fill(255,255,125)
    fill(255,255,255)
    square(x1,y1,30)
    if bs == True:
        image(img5,bx,by,60,60)
    for segment in body:
        if i > 0:
            fill(125.5,125.5,125.5)
            square(segment[0],segment[1],30)
            if w == True:
                fill(255,100,100)
                square(segment[0] + 10,segment[1] + 10,10)
                if bs == True:
                    stroke(255,125,125)
                    line(segment[0] + 15,segment[1] + 15,bx + random(0,10) + 25,by + random(0,10) + 25)
                    stroke(0,0,0)
            i=0
        else:
            fill(255,255,255)
            square(segment[0],segment[1],30)
            i=1
        if [x1,y1]==segment and d != 0 and r == 0 and de == 0:
            x1 = 600
            y1 = 390
            l = 3
        elif [x1,y1] == segment and d != 0 and de == 0:
            r -= 1
            de = l + 3
        if de > 0:
            de -= 0.75
        elif de < 0:
            de=0
     
           
        if bs == True and segment[0] >= bx and segment[0] <= bx+60 and segment[1] >= by and segment[1] <= by + 60:
            bsc-=1
    if bsc <= 0:
        bsc = 15
        l-=1
                
            
    if x1==foodx and y1==foody:
        l+=1
        foodx = floor(random(0,40))*30
        foody = floor(random(0,26))*30
        
    if cv1 == True:
        if x1 > coinx:
            if cv3 == True:
                coinx+=30
            elif cv2 == True:
                coinx+=15
            elif cv1 == True:
                coinx+=7.5
            
        elif x1 < coinx:
            if cv3 == True:
                coinx-=30
            elif cv2 == True:
                coinx-=15
            elif cv1 == True:
                coinx-=7.5
                
        if y1 > coiny:
            if cv3 == True:
                coiny+=30
            elif cv2 == True:
                coiny+=15
            elif cv1 == True:
                coiny+=7.5
                
        elif y1 < coiny:
            if cv3 == True:
                coiny-=30
            elif cv2 == True:
                coiny-=15
            elif cv1 == True:
                coiny-=7.5
            
    if x1 >= coinx - 29 and x1 <= coinx + 29 and y1 >= coiny - 29 and y1 <= coiny + 29:
        coins+=1
        coinx = floor(random(0,40))*30
        coiny = floor(random(0,26))*30
    textSize(50)
    fill(200,200,125)
    text(coins,1000,730)
    fill(125,255,125)
    square(foodx,foody,30)
    fill(200,200,100)
    square(coinx,coiny,30)
    fill(255,50,50)
    text(r,1150,730)
    while len(body)>=l and d!=0:
        body.pop(0)
    delay(100)
    if d!=0:
        body.append([x1,y1])
    
    if d==1:
        y1-=30
    if d==2:
        x1+=30
    if d==3:
        y1+=30
    if d==4:
        x1-=30
    
    if x1 >= 1200:
        x1 = 0
    elif x1 < 0:
        x1 = 1170
    if y1 >= 780:
        y1 = 0
    elif y1 < 0:
        y1 = 750
    
    
    if d == 0:
        textSize(30)
        fill(255,255,255)
        text("w",x1+4,y1-5)
        text("s",x1+8,y1+55)
        text("d",x1+35,y1+27)
        text("a",x1-20,y1+27)
        fill(199,21,133)
        text("Shop ->",950,100)
        fill(200,200,100)
        textSize(20)
        text("Coin (Used in shop)",coinx-40,coiny-10)
        fill(125,255,125)
        text("Food (Grows your snake)",foodx-50,foody-10)
        fill(200,200,125)
        text("Coin counter",965,680)
        fill(255,50,50)
        text("Extra Life Counter",1050,660)
        fill(255,255,255)
        textSize(40)
        text("Space to pause during the game",50,75)
    
    if x1 >= 1080 and x1 <= 1200 and y1 >= 0 and y1 <= 90:
        textSize(40)
        fill(255,255,255)
        text("Press g to open shop",400,400)

def shoploop():
    global x1,y1,d,l,t,foodx,foody,i,coinx,coiny,coins,g,img1,r,de,img2,cv1,cv2,cv3,img3,w,bx,by,bs,bh,bi,img4
    background(50,50,50)
    fill(0,0,0)
    rect(0,100,1200,10)
    rect(0,270,1200,10)
    rect(0,440,1200,10)
    rect(0,610,1200,10)
    fill(100,100,100)
    square(1100,0,100)
    fill(0,0,0)
    line(1110,10,1190,90)
    line(1111,10,1190,89)
    line(1110,11,1189,90)
    line(1110,90,1190,10)
    line(1109,90,1190,9)
    line(1110,91,1191,10)
    textSize(80)
    text("Shop",100,80)
    image(img1,250,465,100,100)
    textSize(40)
    text("Extra Lives",175,605)
    fill(255,50,50)
    text(r,360,605)
    fill(200,200,125)
    text("10",525,150)
    text("Coins",580,150)
    text("15",525,320)
    text("Coins",580,320)
    text("20",525,490)
    text("Coins",580,490)
    text("25",525,660)
    text("Coins",580,660)
    text("You have",650,30)
    text(coins,810,30)
    text("coins",880,30)
    image(img2,850,125,100,100)
    image(img2,850,295,100,100)
    image(img2,850,465,100,100)
    fill(0,0,0)
    textSize(40)
    text("Coin Vacuum Level 1",750,265)
    text("Coin Vacuum Level 2",750,435)
    text("Coin Vacuum Level 3",750,605)
    textSize(30)
    if cv1 == True:
        fill(250,100,100)
        text("Bought",1100,265)
    else:
        fill(100,250,100)
        text("Buy",1100,265)
    if cv2 == True:
        fill(250,100,100)
        text("Bought",1100,435)
    else:
        fill(100,250,100)
        text("Buy",1100,435)
    if cv3 == True:
        fill(250,100,100)
        text("Bought",1100,605)
    else:
        fill(100,250,100)
        text("Buy",1100,605)
    image(img3,250,635,100,100)
    fill(0,0,0)
    textSize(40)
    text("Laser Weapons",150,775)
    textSize(30)
    if w == True:
        fill(250,100,100)
        text("Bought",410,775)
    else:
        fill(100,250,100)
        text("Buy",410,775)
    image(img4,850,635,100,100)
    fill(0,0,0)
    textSize(40)
    text("Boss Summon",780,775)
    
    
    if mouseX > 250 and mouseX < 350 and mouseY > 475 and mouseY < 575 and coins >= 20 and mousePressed:
        r+=1
        coins-=20
        delay(500)
    if mouseX > 850 and mouseX < 1150 and mouseY > 135 and mouseY < 235 and coins >= 10 and mousePressed and cv1 == False:
        cv1 = True
        coins-=10
    if mouseX > 850 and mouseX < 1150 and mouseY > 305 and mouseY < 405 and coins >= 15 and mousePressed and cv2 == False and cv1 == True:
        cv2 = True
        coins-=15
    if mouseX > 850 and mouseX < 1150 and mouseY > 475 and mouseY < 575 and coins >= 20 and mousePressed and cv3 == False and cv1 == True and cv2 == True:
        cv3 = True
        coins-=20
    if mouseX > 850 and mouseX < 1150 and mouseY > 475 and mouseY < 575 and coins >= 20 and mousePressed and cv3 == False and cv1 == True and cv2 == True:
        cv3 = True
        coins-=20
    if mouseX > 250 and mouseX < 350 and mouseY > 645 and mouseY < 745 and coins >= 25 and mousePressed and w == False:
        w = True
        coins-=25
    if mouseX > 850 and mouseX < 1150 and mouseY > 645 and mouseY < 745 and coins >= 25 and mousePressed and bs == False:
        bi = True
        bs = True
        coins-=25

def gameend():
    clear()
    fill(255,255,255)
    textSize(80)
    text("Thanks for Playing!",200,400)
    textSize(50)
    text("g to continue",300,500)
    

def draw():
    global x1,y1,d,l,t,foodx,foody,i,coinx,coiny,coins,g,r,de,bs,bi,bhe,d2
    if g == 0:
        gameloop()
        if bs == True:
            if bi == True:
                bhe = 1000
                bi = False
            bossloop()
    if g == 1:
        shoploop()
    if g == 2:
        gameend()

def keyPressed():
    global x1,y1,d,l,t,foodx,foody,i,coinx,coiny,coins,g,r,de,d2,r
    if key=="w" and d != 3:
        if d == 0 and d2 != 3:
            d=1
        elif d != 0:
            d=1
        redraw()
    if key=="d" and d != 4:
        if d == 0 and d2 != 4:
            d=2
        elif d != 0:
            d=2
        redraw()
    if key=="s" and d != 1:
        if d == 0 and d2 != 1:
            d=3
        elif d != 0:
            d=3
        redraw()
    if key=="a" and d != 2:
        if d == 0 and d2 != 2:
            d=4
        elif d != 0:
            d=4
        redraw()
    if key==" ":
        d2 = d
        d=0
        redraw()
    if key=="g" and (x1 >= 1080 and x1 <= 1200) and (y1 >= 0 and y1 <= 90):
        if d != 0:
            d2 = d
        g = 1
        d = 0
    if key=="g" and g==2:
        g = 0

        
def mousePressed():
    global x1,y1,d,l,t,foodx,foody,i,coinx,coiny,coins,g,r,de
    if mouseButton == LEFT and (mouseX >= 1100 and mouseX <= 1200) and (mouseY >= 0 and mouseY <= 100) and g == 1:
        g = 0
        
    
