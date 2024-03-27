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
        self.v = 0.1
        self.start_V = 0.1
        self.v_spn = 0.0005
        self.V_start_spn = 0.0005
        self.spn = self.St.spn
        self.low_spn_v  = 0.05
        self.lon = self.St.lon
        self.lat = self.St.lat
        self.previous_button = None
    def get_map(self, screen, x, y, w, h):
        map_image = load_image(self.St.get_static_image())
        map_image = pygame.transform.scale(map_image, (w, h))
        screen.blit(map_image, (x, y))



    def update_map(self, keys):
        if keys[pygame.K_PAGEUP]:
            if self.spn > 0.05:
                if self.previous_button == pygame.K_PAGEUP:
                    self.v_spn += 0.025
                else:
                    self.v_spn = self.V_start_spn
            else:
                 self.v_spn = self.V_start_spn
            if not self.spn - self.v_spn <= 0:
                 self.spn -= self.v_spn
            self.St.set_spn(self.spn)
            self.previous_button = pygame.K_PAGEUP
        elif keys[pygame.K_PAGEDOWN]:
            if keys[pygame.K_PAGEDOWN]:
                if self.previous_button == pygame.K_PAGEDOWN:
                    self.v_spn += 0.025
                else:
                    self.v_spn = self.V_start_spn
            self.spn += self.v_spn
            self.St.set_spn(self.spn)
            self.previous_button = pygame.K_PAGEDOWN


        if keys[pygame.K_UP]:
            if self.spn >= 0.05:
                if self.previous_button == pygame.K_UP:
                    self.v += 0.025
                else:
                    self.v = self.start_V
            else:
                self.v = self.low_spn_v * self.spn
            self.lat += self.v
            self.St.set_coords(self.lon, self.lat)
            self.previous_button = pygame.K_UP

        elif keys[pygame.K_DOWN]:
            if self.spn >= 0.05:
                if self.previous_button == pygame.K_DOWN:
                    self.v += 0.025
                else:
                    self.v = self.start_V
            else:
                self.v = self.low_spn_v * self.spn
            self.lat -= self.v
            self.St.set_coords(self.lon, self.lat)
            self.previous_button = pygame.K_DOWN

        if keys[pygame.K_LEFT]:
            if self.spn >= 0.05:
                if self.previous_button == pygame.K_LEFT:
                    self.v += 0.025
                else:
                    self.v = self.start_V
            else:
                self.v = self.low_spn_v * self.spn
            self.lon -= self.v
            self.St.set_coords(self.lon, self.lat)
            self.previous_button = pygame.K_LEFT


        elif keys[pygame.K_RIGHT]:
            if self.spn >= 0.05:
                if self.previous_button == pygame.K_RIGHT:
                    self.v += 0.025
                else:
                    self.v = self.start_V
            else:
                self.v = self.low_spn_v * self.spn
            self.lon += self.v
            self.St.set_coords(self.lon, self.lat)
            self.previous_button = pygame.K_RIGHT

