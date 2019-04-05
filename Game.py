import pygame
import random
pygame.init()
black = (0,0,0)
red = (255,0,0)
size = (700,600)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30,30])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 550
        self.movex = 0
        self.movey = 0
    def goL(self):
        self.movex = -3
    def goR(self):
        self.movex = 3
    def goU(self):
        self.movey = -3
    def goD(self):
        self.movey = 3
    def stop(self):
        self.movex = 0
        self.movey = 0
    def update(self):
        if self.rect.x <= 1:
            self.rect.x = 1
        elif self.rect.x >= size[0] - (self.image.get_width() + 1):
            self.rect.x = size[0] - (self.image.get_width() + 1)
        if self.rect.y <= 1:
            self.rect.y = 1
        elif self.rect.y >= size[1] - (self.image.get_height() + 1):
            self.rect.y = size [1] - (self.image.get_height() +1)


        self.rect.x += self.movex
        self.rect.y += self.movey

p = Player()



class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5,10])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        
        #defines the exact position of the bullet (so it appears in the middle over the player):
        self.rect.x = p.rect.x + p.image.get_width()/2-self.image.get_width()/2

        self.rect.y = p.rect.y 
        self.movey = -5
    def update(self):
        self.rect.y += self.movey
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([60,60])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 100
        self.movey = 3

    def update(self):
        self.rect.y += self.movey
        if self.rect.y > size[1]:

            #Random appearance on x Axis:
            self.rect.x = random.randrange(0,size[0]-e.image.get_width())

            self.rect.y = -self.image.get_height()


e = Enemy()



lista = pygame.sprite.Group()
lista.add(p)
lista.add(e)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("THE Game")
yellow = (255,255,0)
clock = pygame.time.Clock()


done = False

def fire():
    b = Bullet()
    lista.add(b)



while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            p.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                fire()


        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            p.goL()
        elif keys[pygame.K_RIGHT]:
            p.goR()
        if keys[pygame.K_UP]:
            p.goU()
        elif keys[pygame.K_DOWN]:
            p.goD()
        
      
    
    screen.fill(yellow)
    lista.update()
    lista.draw(screen)
    pygame.display.flip()       
    clock.tick(60)
pygame.quit()



