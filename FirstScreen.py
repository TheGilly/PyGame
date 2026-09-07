import pygame as py
py.init()
screen = py.display.set_mode((700, 700))
py.display.set_caption("FirstScreen")
Shrek_Image = py.image.load("shrek_PNG4.png")
Shrek_Image = py.transform.scale(Shrek_Image, (200,200))
Shrek_Sprite = Shrek_Image.get_rect()
Shrek_Sprite.center = (350,350)

Donkey_Image = py.image.load("Donkey Image.jpg")
Donkey_Image = py.transform.scale(Donkey_Image, (200,200))
Donkey_Sprite = Donkey_Image.get_rect()
Shrek_Sprite.center = (600,600)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    key = py.key.get_pressed()
    if key[py.K_a]:
        Donkey_Sprite.x = Donkey_Sprite.x-7
    if key[py.K_d]:
            Donkey_Sprite.x = Donkey_Sprite.x+7
    if key[py.K_w]:
                Donkey_Sprite.y = Donkey_Sprite.y-7
    if key[py.K_s]:
                Donkey_Sprite.y = Donkey_Sprite.y+7
    screen.fill("orange" )
    screen.blit(Shrek_Image, Shrek_Sprite)
    screen.blit(Donkey_Image, Donkey_Sprite)
    py.display.update()






















py.quit()