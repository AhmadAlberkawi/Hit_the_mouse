import pygame
from pygame.locals import *
from pygame.sprite import *
import random
from playsound import playsound

pygame.init()

# Display configuration
pygame.display.set_caption('Hit the mouse')
size = (704, 523)
screen = pygame.display.set_mode(size)
pygame.mixer.init()
pygame.mixer.music.load('gamemusic.mp3')
pygame.mixer.music.play(-1)

# Entities
background = pygame.image.load('Hintergrund.jpg')
mouse1 = pygame.image.load('Maus.png')
hammer1 = pygame.image.load('Hammer1.png')
won = pygame.image.load('won.jpg')

mouses = [(176, 142), (350, 142), (530, 142), (145, 270), (350, 272), (562, 272), (120, 423), (350, 423), (584, 422)]

mouseclick = False
clock = pygame.time.Clock()
score = 0
pygame.time.set_timer(USEREVENT, 200)

class Maus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Maus.png')
        self.rect = self.image.get_rect()

    def cry(self):
        playsound('soundgame.mp3')

    def hit(self, pos):
        return self.rect.collidepoint(pos)

    def update(self):
        self.rect.center = mouses[random.randrange(0, 9)]


class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Hammer.png')
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


maus = Maus()
hammer = Hammer()

sprite_group = pygame.sprite.Group()
sprite_group.add(maus)
sprite_group.add(hammer)

font = pygame.font.Font(None, 25)
pygame.mouse.set_visible(False)

while True:

    screen.blit(won, (0, 0))
    if score != 3:
        screen.blit(background, (0, 0))
    else:
        screen.blit(won, (0, 0))
        pygame.display.update()

    clock.tick(60)
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                score = 0
        if score != 3:
            if event.type == MOUSEBUTTONDOWN:
                mouseclick = True
                if maus.hit(pygame.mouse.get_pos(x, y)):
                    maus.cry()
                    score += 1
                else:
                    score = 0
            elif event.type == USEREVENT:
                pygame.time.set_timer(USEREVENT, 1000)
                sprite_group.update()
                sprite_group.draw(screen)
                score_value = font.render(''+str(score), True, Color('white'))
                screen.blit(score_value, (380, 34))
            elif event.type == MOUSEBUTTONUP:
                mouseclick = False

            # hammer shape
            if mouseclick == False:
                screen.blit(hammer1, (x, y))
            pygame.display.flip()