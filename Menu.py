import pygame
from Tools import Button, SearchBox

class MenuWidgets:
    def __init__(self, st):
        self.statick = st
        # self.change_format_button = Button()
        # self.change_format_button.add_buttton_picture('data/iconics/right.jpg')
        # self.change_format_button.connect_issue(self.open_tool_bar())
        # self.change_format_button.replace((0, 50))
        # self.change_format_button.resize((30, 80))
        #

        self.map_batton = Button()
        self.map_batton.add_buttton_picture('data/iconics/map.jpeg')
        self.map_batton.connect_issue(lambda: self.change_mode('map'))
        self.map_batton.resize((40, 40))
        self.map_batton.replace((10, 70))

        self.sputnik_button = Button()
        self.sputnik_button.add_buttton_picture('data/iconics/sputnik.jpg')
        self.sputnik_button.connect_issue(lambda: self.change_mode('sat'))
        self.sputnik_button.resize((40, 40))
        self.sputnik_button.replace((10, 130))


        self.gibrid = Button()
        self.gibrid.add_buttton_picture('data/iconics/gibrid.jpeg')
        self.gibrid.connect_issue(lambda: self.change_mode('sat,skl'))
        self.gibrid.resize((40, 40))
        self.gibrid.replace((10, 190))


        self.searchBox_label = SearchBox(70, 10, 500, 30, 18)


    def change_mode(self, mode_name):
        self.statick.set_mode(mode_name)

    def update_menu(self, event):
        self.searchBox_label.update(event)
        print(self.searchBox_label.text)
        self.map_batton.update(event)
        self.sputnik_button.update(event)
        self.gibrid.update(event)
        # self.change_format_button.update(event)

    def render(self, screen):
        self.searchBox_label.render(screen)
        self.map_batton.render(screen)
        self.sputnik_button.render(screen)
        self.gibrid.render(screen)
        # self.change_format_button.render(screen)


    def open_tool_bar(self):
           pass