import pygame
import time

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

x = 400
y = 400

surface = pygame.display.set_mode((x, y))

pygame.display.set_caption("Caption text blablabla")

fonts = "C:/Users/Maxy/AppData/Local/Microsoft/Windows/Fonts/"
font = pygame.font.Font(fonts + "UbuntuMono-Bold.ttf", 32)
text = font.render("This is a test", True, blue, black)

textRect = text.get_rect()
textRect.center = (x/2, y/2)

framecount = 0

while True:
    surface.fill(black)
    surface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

    time.sleep(3)

    text = font.render("Do not panic", True, blue, black)
