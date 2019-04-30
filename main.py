def clear():
    win.delete("all")


def displaybase():
    pt1=Point(20,20)
    pt4=Point(980,580)
    pt5=Point(20,300)
    pt6=Point(980,300)
    Rectangle(pt1,pt4).draw(win)

    Line(pt5,pt6).draw(win)
def displaychar(x,y):
    Image(Point(x+25,y-50),"char.png").draw(win)
def displayobs(x,y):
    if x>980 or x<20:
        return
    if y==1:
        Image(Point(x,290),"grass.png").draw(win)
    if y==2:
        Image(Point(x,280),"grass3.png").draw(win)
    if y==3:
        Image(Point(x,270),"obs1.png").draw(win)
def random(x):
    return(math.ceil(3*(math.sin(x)+1)/2))
def score(x):
    msg=Text(Point(900,45),x).draw(win)
    msg.setSize(20)
import math
from graphics import *
win= GraphWin("RAMAILO",1000,600)
displaybase()
displaychar(25,300)
i=True
flag=0
x_ord=0
y_ord=0
obsloc=[100,250,780]
obstyp=[1,2,3]
while(i):
    for m in range(100000):
        m
    clear()
    displaybase()
    score(x_ord)
    displaychar(25,300-y_ord)
    for j in range(3):
        displayobs(obsloc[j],obstyp[j])
        obsloc[j]=obsloc[j]-1

    x_ord=x_ord+1
    if y_ord<=0 and obsloc[0]==50:
        Text(Point(500,200),"GAME OVER").draw(win)
        Rectangle(Point(450,180),Point(550,220)).draw(win)
        win.getKey()
        break
    if obsloc[0]<21:
        obsloc[0]=obsloc[1]
        obsloc[1]=obsloc[2]
        obsloc[2]=obsloc[1]+math.floor(240+15*random(x_ord))
        obstyp[0]=obstyp[1]
        obstyp[1]=obstyp[2]
        obstyp[2]=math.floor(random(x_ord))
    cont=win.checkKey()
    if flag==0 and cont=="space":
        flag=1
        temp=x_ord
    if flag==1:
        y_ord=4*(x_ord-temp+1)-.20/4*(x_ord-temp+1)**2
    if y_ord<=0:
        flag=0
        y_ord=0
    if cont=="Escape":
        break

win.close
