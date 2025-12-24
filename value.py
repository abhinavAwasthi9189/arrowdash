import pygame
import random
import pickle

Ar1 = pygame.image.load("images/arrow/1.png")
Ar2 = pygame.image.load("images/arrow/2.png")
Ar3 = pygame.image.load("images/arrow/3.png")
Ar4 = pygame.image.load("images/arrow/4.png")
Bor = pygame.image.load("images/arrow/Bor.png")
Ar=[Ar1,Ar2,Ar3,Ar4]

Gs1 = pygame.image.load("images/new/Gs1.png")
Gs2 = pygame.image.load("images/new/Gs2.png")
Gs3 = pygame.image.load("images/new/Gs3.png")
def game_new():
    H=random.choice([Gs1,Gs2,Gs3])
    return H

Bg1 = pygame.image.load("images/background/Bg1.png")
Bg2 = pygame.image.load("images/background/Bg2.png")
def back_new():
    H=random.choice([Bg1,Bg2])
    return H

points={}

file=open("game_values.bin",'rb+')
points=pickle.load(file)
file.close()

def finder(d,v):
    for i in d:
        if d[i]==v:
            return i
    


def check(core,name):
        x=list(points.values())
        x.sort(reverse=False)
        if core > min(x):
            if name in points:
                points[name] = core
            else:
                p=finder(points,min(x))
                points.pop(p)
                points[name]=core
        file=open("game_values.bin","wb")
        pickle.dump(points,file)

def ended():
    file=open("game_values.bin","wb")
    pickle.dump(points,file)

def leader():
    x=list(points.values())
    x.sort(reverse=True)
    point2=dict(points)
    hen=""
    for i in x:
        up=finder(point2,i)
        henp=up+"("+str(i)+")"
        hen=(hen+henp+"---")
        point2.pop(up)
    return hen

    
        
    


    

