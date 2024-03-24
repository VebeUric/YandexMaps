import pygame
from App_Manager import AppManager


window_width, windwo_hiegth = 900, 750
pygame.init()
screen = pygame.display.set_mode((window_width, windwo_hiegth))
AppManager = AppManager()

clock = pygame.time.Clock()
FPS = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
    AppManager.update_map(keys)
    AppManager.get_map(screen, window_width, windwo_hiegth)
    pygame.display.update()

clock.tick(FPS)