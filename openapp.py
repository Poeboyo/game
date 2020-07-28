import sys, pygame
pygame.init()
pygame.display.init()
pygame.display.set_caption("Game")


criming = pygame.image.load('ifeelthat.jpeg')
pygame.display.set_icon(criming)

size = width, height = 865, 600
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
screen.fill(black)
ball = pygame.image.load("ifeelthat.jpeg")
ballrect = ball.get_rect()
pygame.draw.circle(screen, (0, 0, 0), (2, 2), 500, 250)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
