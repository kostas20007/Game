import pygame
pygame.init()
black = (0,0,0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30,30])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
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
lista = pygame.sprite.Group()
lista.add(p)

size = (700,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("THE Game")
yellow = (255,255,0)
clock = pygame.time.Clock()


done = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            p.stop()


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



