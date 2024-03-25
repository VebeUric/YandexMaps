import pygame
from Tools import Button

class MenuWidgets:
    def __init__(self):
        self.change_format_button = Button()
        self.change_format_button.add_buttton_picture('data/iconics/right.jpg')
        self.change_format_button.connect_issue(self.open_tool_bar())
        self.change_format_button.replace((0, 50))
        self.change_format_button.resize((30, 80))

        self.map_batton = Button()
        self.map_batton.add_buttton_picture('data/iconics/map.jpeg')
        self.map_batton.resize((40, 40))
        self.map_batton.replace((0, 50))



    def open_tool_bar(self):
        pass

    def update_menu(self, event):
        self.map_batton.update(event)

        # self.change_format_button.update(event)

    def render(self, screen):
        self.map_batton.render(screen)
        # self.change_format_button.render(screen)


