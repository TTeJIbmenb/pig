from pygame import *
from random import *

window=display.set_mode((700,500))
display.set_caption("Pig_Pog")
background = transform.scale(image.load("трава.jpg"),(700,500))
game = True
clock = time.Clock()
FPS = 120
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image. load(player_image), (size_x, size_y))
        self. speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y> 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y< 500-80:
            self.rect.y+=self.speed
class Player1(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y> 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y< 500-80:
            self.rect.y+=self.speed
ball = GameSprite("диз-removebg-preview.png", 0, 0, 30, 30, 10)
sosiska = Player("мышка_сосиска-removebg-preview1.png", 0, 100, 150, 300, 10)
sosiska1 = Player1("мышка_сосиска-removebg-preview.png", 600, 150, 150, 300, 10)
speed_x = 3
speed_y = 3
finish = False
while game:

    for e in event.get():
        if e.type==QUIT:
            game=False
    if  finish != True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(sosiska, ball) or sprite.collide_rect(sosiska1, ball):
            speed_x *= -1
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
    ball.update()
    ball.reset()
    sosiska.update()
    sosiska.reset()
    sosiska1.update()
    sosiska1.reset()
    clock.tick(FPS)
    display.update() 