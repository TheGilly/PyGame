import pygame as py
import time 
py.init()
screen = py.display.set_mode((800, 800))
py.display.set_caption("Car Game")
font1 = py.font.SysFont("Calibri", 50)

Running = True

bg1 = py.image.load("Road Topview.jpg")
bg2 = py.image.load("Road Topview.jpg")
car = py.image.load("top_view_of_car-removebg-preview (1).png")
obstacle1 = py.image.load("barricade_1-removebg-preview.png")
obstacle2 = py.image.load("barricade_2-removebg-preview.png")
obstacle3 = py.image.load("barricade_3-removebg-preview.png")


car = py.transform.scale(car, (70, 90))
car = py.transform.rotate(car, -90)
bg1 = py.transform.scale(bg1,(800, 800))
bg1 = py.transform.rotate(bg1, 90)
bg2 = py.transform.scale(bg2,(800, 800))
bg2 = py.transform.rotate(bg2, 90)
obstacle1 = py.transform.scale(obstacle1,(50, 50))
obstacle2 = py.transform.scale(obstacle2,(50, 50))
obstacle3 = py.transform.scale(obstacle3,(50, 50))

bg1sprite = bg1.get_rect()
bg2sprite = bg2.get_rect()
carsprite = car.get_rect()
obstacle1sprite = obstacle1.get_rect()
obstacle2sprite = obstacle2.get_rect()
obstacle3sprite = obstacle3.get_rect()



bg1sprite.center = (400, 400)
bg2sprite.center = (400, -400)
carsprite.center = (400,600)
obstacle1sprite.center = (100, 300)
obstacle2sprite.center = (500, 200)
obstacle3sprite.center = (600, 100)
bg1sprite.topleft = (0, 0)
bg2sprite.topleft = (0, -800)

velocity = 1
Score = 0



while Running:
    bg1sprite.y = bg1sprite.y + velocity
    bg2sprite.y = bg2sprite.y + velocity
    obstacle1sprite.y = obstacle1sprite.y + velocity
    obstacle2sprite.y = obstacle2sprite.y + velocity
    obstacle3sprite.y = obstacle3sprite.y + velocity
    if obstacle1sprite.y > 800:
        obstacle1sprite.y = 0
        Score = Score + 1
    if obstacle2sprite.y > 800:
        obstacle2sprite.y = 0
        Score = Score + 1
    if obstacle3sprite.y > 800:
        obstacle3sprite.y = 0
        Score = Score + 1
    
        
    
    


    
    if bg1sprite.y > 800:
        bg1sprite.y = -800
    if bg2sprite.y > 800:
        bg2sprite.y = -800
    for event in py.event.get():
        if event.type == py.QUIT:
            Running = False

    keys = py.key.get_pressed()
    if keys [py.K_LEFT]:
        carsprite.x = carsprite.x - 2
    if keys [py.K_RIGHT]:
        carsprite.x = carsprite.x + 2

    if carsprite.colliderect(obstacle1sprite) or carsprite.colliderect(obstacle2sprite) or carsprite.colliderect(obstacle3sprite):
        text1 = font1.render("You lose", True, "black")
        velocity = 0
        screen.blit(text1, (200, 400))
        text2 = font1.render("Your score was " + str(Score), True, "black")
        
    
                

    screen.fill("black")
    screen.blit(bg1, bg1sprite)
    screen.blit(bg2, bg2sprite)
    screen.blit(car, carsprite)
    screen.blit(obstacle1, obstacle1sprite)
    screen.blit(obstacle2, obstacle2sprite)
    screen.blit(obstacle3, obstacle3sprite)
    if velocity == 0:
         screen.blit(text1, (200, 400))
         screen.blit(text2, (400,600))
    
        

    py.display.update()

py.quit()