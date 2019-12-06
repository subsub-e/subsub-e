import pygame

WHITE = (255,255,255)
WIDTH = 800
HEIGHT = 600

def startbutton1(x1,y1):
    global gamepad, block1
    gamepad.blit(block1, (x1, y1))

def startbutton2(x2,y2):
    global gamepad, block2
    gamepad.blit(block2, (x2, y2))


def startbutton3(x3,y3):
    global gamepad, block3
    gamepad.blit(block3, (x3, y3))


def startbutton4(x4,y4):
    global gamepad, block4
    gamepad.blit(block4, (x4, y4))


def runGame():
    global gamepad, clock, block1, block2, block3, block4

    x1 = WIDTH * 0.2
    y1 = HEIGHT * 0.3
    x2 = WIDTH * 0.6
    y2= HEIGHT * 0.3
    x3 = WIDTH * 0.2
    y3 = HEIGHT * 0.7
    x4 = WIDTH * 0.6
    y4 = HEIGHT * 0.7



    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gamepad.fill(WHITE)
        startbutton1(x1, y1)
        startbutton2(x2, y2)
        startbutton3(x3, y3)
        startbutton4(x4, y4)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def initGame():
    global gamepad, clock, block1, block2, block3, block4

    pygame.init()
    gamepad = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("sub's minigame")
    block1 = pygame.image.load('startbutton.png')
    block2 = pygame.image.load('startbutton.png')
    block3 = pygame.image.load('startbutton.png')
    block4 = pygame.image.load('startbutton.png')

    clock = pygame.time.Clock()
    runGame()

initGame()
