import menu
import Saved_Settings
import pygame

settings = Saved_Settings.Settings()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()


# show intro ?

settings = Saved_Settings.loadSettings(Saved_Settings.FILENAME)

menu.show_menu(settings)
