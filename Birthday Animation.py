import pygame as py
import time
py.init()
screen = py.display.set_mode((700, 700))
py.display.set_caption("Birthday Animation")

bg1 = py.image.load("birthday party 1.jpg")
bg2 = py.image.load("birthday party 2.jpg")
bg3 = py.image.load("Birthday party 3.jpg")
bg4 = py.image.load("birthday party 4.jpg")
bg5 = py.image.load("birthday party 5.jpg")
birthdaycake = py.image.load("birthday cake.jpg")

bg1 = py.transform.scale(bg1,(700, 700))
bg2 = py.transform.scale(bg2,(700, 700))
bg3 = py.transform.scale(bg3,(700, 700))
bg4 = py.transform.scale(bg4,(700, 700))
bg5 = py.transform.scale(bg5,(700, 700))
birthdaycake = py.transform.scale(birthdaycake,(200,200))
birthdaycakesprite = birthdaycake.get_rect()
birthdaycakesprite.center = (350, 350)

font1 = py.font.SysFont("Arial", 40)
text1 = font1.render("Happy Birthday", True, "black")

Running = True
while Running:
    for event in py.event.get():
        if event.type == py.QUIT:
            Running = False
    screen.fill("orange")
    screen.blit(bg1, (0,0))
    screen.blit(birthdaycake, birthdaycakesprite)
    screen.blit(text1, (350, 100))
    py.display.update()
    
    time.sleep(2)
    screen.fill("orange")
    
    screen.blit(bg2, (0,0))
    screen.blit(birthdaycake, birthdaycakesprite)
    text2 = font1.render("Have a good year", True, "black")
    screen.blit(text2, (350,100))
    py.display.update()
    
    time.sleep(2)
    screen.fill("orange")
    
    screen.blit(bg3, (0,0))
    screen.blit(birthdaycake, birthdaycakesprite)
    text3 = font1.render("Hope you get a lot of presents", True, "black")
    screen.blit(text3, (350,100))
    py.display.update()
    
    time.sleep(2)
    screen.fill("orange")
    
    screen.blit(bg4, (0,0))
    screen.blit(birthdaycake, birthdaycakesprite)
    text4 = font1.render("Hope you have a fun birthday party", True, "black")
    screen.blit(text4, (350,100))
    py.display.update()
    
    time.sleep(2)
    screen.fill("orange")
    
    screen.blit(bg5, (0,0))
    screen.blit(birthdaycake, birthdaycakesprite)
    py.display.update()
    
    time.sleep(2)
py.quit()