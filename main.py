import menu
import Saved_Settings
import pygame

settings = Saved_Settings.Settings()
pygame.mixer.init()


# show intro ?

Saved_Settings.loadSettings(Saved_Settings.FILENAME)

menu.show_menu(settings)
