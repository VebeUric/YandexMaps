import pygame
from pygame.sprite import Sprite
from pygame import Surface
from pygame import Rect
from GUI import Animation

anim = Animation()


class Button(Sprite):
    def __init__(self, text=None, issue=lambda: None, picture_path=None, alternative_picture_path=None):
        super().__init__()
        self.button_rect = None
        self.issue = issue
        self.text = text
        self.text_size = 50
        self.is_active = None
        self.color = (0, 0, 0)
        self.picture_path = picture_path
        self.alternative_picture_path = alternative_picture_path
        self.rect = Rect(0, 0, 100, 100)
        self.image = Surface(self.rect.size)
        self.add_buttton_picture(self.picture_path)
        self.render(self.image)

    def resize_text(self, new_size):
        self.text_size = new_size

    def resize(self, size):
        self.rect.width, self.rect.height = size

    def replace(self, pos):
        self.rect.x, self.rect.y = pos

    def make_new_text_color(self, new_color):
        self.color = new_color

    def on_click(self):
        print(self.issue)
        if self.issue:
            self.issue()

    def connect_issue(self, foo):
        self.issue = foo

    def add_buttton_picture(self, path):
        if path:
            self.picture_path = pygame.image.load(path)

    def add_alternative_picture(self, path):
        if path:
            self.alternative_picture_path = pygame.image.load(path)

    def update(self, *args):
        if not args:
            return
        if args[0].type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(args[0].pos):
                if not self.is_active:
                    self.is_active = True
                    self.render(self.image)

            else:
                if self.is_active:
                    self.is_active = False
                    self.render(self.image)
        elif args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.on_click()

    def render(self, screen):
        self.button_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        if self.picture_path:
            if self.alternative_picture_path:
                if self.is_active:
                    if not type(self.alternative_picture_path) is Surface:
                        self.alternative_picture_path = anim.load_image(self.alternative_picture_path)
                    self.alternative_picture_path = pygame.transform.scale(self.alternative_picture_path,
                                                                           (self.rect.width, self.rect.height))
                    screen.blit(self.alternative_picture_path, (self.rect.x, self.rect.y))
                else:
                    self.picture_path = pygame.transform.scale(self.picture_path, (self.rect.width, self.rect.height))
                    screen.blit(self.picture_path, (self.rect.x, self.rect.y))
            else:
                self.picture_path = pygame.transform.scale(self.picture_path, (self.rect.width, self.rect.height))
                screen.blit(self.picture_path, (self.rect.x, self.rect.y))
        else:
            if self.is_active:
                color = (200, 100, 100)
            else:
                color = (100, 200, 100)
            print(self.rect.width)
            # pygame.draw.rect(screen, color, (self.rect.width, self.rect.height // 2), self.rect.size // 2)
        font = pygame.font.Font(None, self.text_size)  # Сделать обособленную фуекцию чтобы можно было скрывать текст
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.rect.x + 10, self.rect.y + 10))
        screen.blit(text_surface, text_rect.center)


class Text:
    def __init__(self, text, font_size, color, x, y):
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(center=(self.x, self.y))

    def resize(self, font_size):
        self.font = pygame.font.Font(self.font.get_fontname(), font_size)
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(center=(self.x, self.y))

    def replace(self, text):
        self.text = text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.rendered_text, self.rect.topleft)


class RaangeSlider(Sprite):
    def __init__(self, text, min=0, max=100, issue=lambda: None):
        super().__init__()
        self.max = max
        self.issue = issue
        self.min = min
        self.text = text()

    def init_button(self):
        pass

    def resize(self, hiegth, width):
        pass

    def replace(self, x, y):
        pass

    def on_click(self):
        pass

class SearchBox:
    def __init__(self, x, y, width, height, font_size=32, font_color=(0, 0, 0), bg_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.font_color = font_color
        self.bg_color = bg_color
        self.text = '6'
        self.active = False
        self.cursor_visible = True
        self.cursor_timer = 0

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def render(self, screen):
        print(self.text)
        # Render the current text
        text_surface = self.font.render(self.text, True, self.font_color)

        # Render the background of the input box
        pygame.draw.rect(screen, self.bg_color, self.rect)

        # Render the text onto the input box
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        # Draw the cursor
        if self.active:
            self.cursor_timer += 1
            if self.cursor_timer >= 30:
                self.cursor_timer = 0
                self.cursor_visible = not self.cursor_visible
            if self.cursor_visible:
                cursor_x = self.rect.x + 5 + text_surface.get_width()
                cursor_y = self.rect.y + 5
                pygame.draw.line(screen, (0, 0, 0), (cursor_x, cursor_y), (cursor_x, cursor_y + text_surface.get_height()), 2)

    def resize(self, width, height):
        self.rect.width = width
        self.rect.height = height

    def replace(self, x, y):
        self.rect.x = x
        self.rect.y = y


# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()