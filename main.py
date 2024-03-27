import pygame
from App_Manager import AppManager
from Menu import MenuWidgets


window_width, windwo_hiegth = 680, 480
WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((window_width, windwo_hiegth))
AppManager = AppManager()
menu_widgets = MenuWidgets(AppManager.St)

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()

    AppManager.get_map(screen, 0, 0, 680, 480)
    AppManager.update_map(keys)
    menu_widgets.update_menu(event)
    menu_widgets.render(screen)
    pygame.display.update()

clock.tick(FPS)