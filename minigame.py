import pygame
import os

Now = os.path.dirname(__file__)

WHITE = (255,255,255)
WIDTH = 800
HEIGHT = 600


def back(x,y):
    global gamepad, background
    gamepad.blit(background,(x,y))

def title(x,y):
    global gamepad, titlepicture
    gamepad.blit(titlepicture, (x,y))

def title1(x1,y1):
    global gamepad, gametitle1
    gamepad.blit(gametitle1, (x1,y1))

def title2(x2,y2):
    global gamepad, gametitle2
    gamepad.blit(gametitle2, (x2,y2))

def title3(x3,y3):
    global gamepad, gametitle3
    gamepad.blit(gametitle3, (x3,y3))

def title4(x4,y4):
    global gamepad, gametitle4
    gamepad.blit(gametitle4, (x4,y4))

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
    global gamepad, clock, block1, block2, block3, block4, background, titlepicture, gametitle1, gametitle2, gametitle3, gametitle4

    x1 = WIDTH * 0.2
    y1 = HEIGHT * 0.3
    x2 = WIDTH * 0.6
    y2= HEIGHT * 0.3
    x3 = WIDTH * 0.2
    y3 = HEIGHT * 0.7
    x4 = WIDTH * 0.6
    y4 = HEIGHT * 0.7

    background_x = 0
    title_x = 275
    title_y = 25
    gametitle_x1 = 120
    gametitle_y1 = 140
    gametitle_x2 = 440
    gametitle_y2 = 140
    gametitle_x3 = 120
    gametitle_y3 = 380
    gametitle_x4 = 440
    gametitle_y4 = 380

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if mx > 180 and mx < 340 and my > 200 and my < 330:
                    print("1")
                if mx > 500 and mx < 660 and my > 200 and my < 330:
                    print("2")
                if mx > 180 and mx < 340 and my > 440 and my < 580:
                    print("3")
                if mx > 550 and mx < 660 and my > 440 and my < 580:
                    print("4")

        gamepad.fill(WHITE)
        back(background_x, 0)
        title(title_x, title_y)
        startbutton1(x1, y1)
        startbutton2(x2, y2)
        startbutton3(x3, y3)
        startbutton4(x4, y4)
        title1(gametitle_x1, gametitle_y1)
        title2(gametitle_x2, gametitle_y2)
        title3(gametitle_x3, gametitle_y3)
        title4(gametitle_x4, gametitle_y4)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def initGame():
    global gamepad, clock, block1, block2, block3, block4, background, titlepicture,  gametitle1, gametitle2, gametitle3, gametitle4
    pygame.init()
    clock = pygame.time.Clock()
    Img = os.path.join(Now, "img")
    gamepad = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("sub's minigame")
    Start_B = os.path.join(Img, "startbutton.png")
    gametitle_1 = os.path.join(Img, "gametitle1.png")
    gametitle_2 = os.path.join(Img, "gametitle2.png")
    gametitle_3 = os.path.join(Img, "gametitle3.png")
    gametitle_4 = os.path.join(Img, "gametitle4.png")
    background_1 = os.path.join(Img, "background.png")
    title_1 = os.path.join(Img, "title.png")
    block1 = pygame.image.load(Start_B).convert_alpha()
    block2 = pygame.image.load(Start_B).convert_alpha()
    block3 = pygame.image.load(Start_B).convert_alpha()
    block4 = pygame.image.load(Start_B).convert_alpha()
    gametitle1 = pygame.image.load(gametitle_1).convert_alpha()
    gametitle2 = pygame.image.load(gametitle_2).convert_alpha()
    gametitle3 = pygame.image.load(gametitle_3).convert_alpha()
    background = pygame.image.load(background_1).convert_alpha()
    gametitle4 = pygame.image.load(gametitle_4).convert_alpha().convert_alpha()
    titlepicture = pygame.image.load(title_1).convert_alpha()

    clock = pygame.time.Clock()
    runGame()

initGame()
