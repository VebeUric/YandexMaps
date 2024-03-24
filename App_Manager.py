import io

import pygame
from Map_Manager import StaticAPI, Geocoder
from GUI import load_image
from PIL import Image
from io import BytesIO

St = StaticAPI(41.0, 58.0)
geoc = Geocoder()
class AppManager:
    def __init__(self):
        self.St = St
        self.geoc = geoc
        self.scale_a = 0
        self.cnt = 0
        self.spn = 1
        self.lon = 0
        self.lat = 0

    def get_map(self, screen, W, H):
        map_image = load_image(self.St.get_static_image())
        # map_image = pygame.transform.scale(map_image, (700, 500))
        screen.blit(map_image, (100, 100))

    def update_map(self, keys):
        if keys[pygame.K_1]:
            print('okkkkk')
            self.spn -= 0.005
            self.St.set_spn(self.spn)
        elif keys[pygame.K_2]:
            self.spn += 0.005
            self.St.set_spn(self.spn)


        if keys[pygame.K_UP]:
            self.lon += 0.1
            self.lat += 0.1
            self.St.set_coords(self.lon, self.lon)
        elif keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass

