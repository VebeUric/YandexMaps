from PIL import Image
import pygame
import os
import sys


def load_alpha_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    image = image.convert()
    rect = image.get_rect()
    image.set_colorkey((255, 255, 255))
    alpha_channel = pygame.Surface(rect.size, pygame.SRCALPHA)
    alpha_channel.fill((0, 0, 0, 0))
    alpha_channel.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    image_with_transparent_background = pygame.Surface(rect.size, pygame.SRCALPHA)
    image_with_transparent_background.blit(alpha_channel, (0, 0))
    return image


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def prepear_frames(sprite_width, sprite_height, player_sprite_sheet, space, frame_count):
    frames = []
    for i in range(0, frame_count):
        frame_rect = pygame.Rect(i * space + sprite_width * i, 0, sprite_width, sprite_height)
        frames.append(player_sprite_sheet.subsurface(frame_rect))
    return frames


def prepear_trans_frames(sprite_width, sprite_height, player_sprite_sheet, space, frame_count):
    frames = []
    for i in range(0, frame_count):
        frame_rect = pygame.Rect(i * space + sprite_width * i, 0, sprite_width, sprite_height)
        frames.append(pygame.transform.flip(player_sprite_sheet.subsurface(frame_rect), True, False))
    return frames

class Animation:
    def __init__(self):
        pass

    def load_alpha_image(self, name):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            sys.exit()
        image = pygame.image.load(fullname)
        image = image.convert()
        rect = image.get_rect()
        image.set_colorkey((255, 255, 255))
        alpha_channel = pygame.Surface(rect.size, pygame.SRCALPHA)
        alpha_channel.fill((0, 0, 0, 0))
        alpha_channel.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        image_with_transparent_background = pygame.Surface(rect.size, pygame.SRCALPHA)
        image_with_transparent_background.blit(alpha_channel, (0, 0))
        return image


    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):

            sys.exit()
        image = pygame.image.load(fullname)
        return image
