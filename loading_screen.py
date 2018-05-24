import pygame
import colors
import random


class LoadingScreen:
    def __init__(self, max_steps, settings):
        self.all_steps = max_steps
        self.progress = 0
        self.settings = settings
        self.text = "loading ..."
        self.info = "Info: Das Spiel ist noch nicht fertig"

    def do_math(self, steps):
        progress = steps / self.all_steps
        return progress

    def update(self, step_now):
        self.progress = self.do_math(step_now)

    def draw(self, screen):
        screen.fill(colors.grey)

        """
        image = pygame.image.load("images/Grass.jpg").convert()
        image = pygame.transform.scale(image, (self.settings.resolution[0], self.settings.resolution[1]))
        screen.blit(image, [0, 0])"""

        center_x = int(self.settings.resolution[0] / 2)
        center_y = int(self.settings.resolution[1] / 1.6)
        width = int(self.settings.resolution[0] / 1.5)
        height = int(self.settings.resolution[1] / 105)
        line_strength = int(self.settings.resolution[0] / 500)
        pygame.draw.rect(screen, colors.light_grey, [center_x-width/2, center_y-height/2, width, height], 0)

        width_2 = int(self.progress*width)
        pygame.draw.rect(screen, colors.black, [center_x-width/2, center_y-height/2, width_2, height])

        font = pygame.font.SysFont("arial", int(self.settings.resolution[0]/25))

        title = font.render(self.text, True, colors.black)
        text_rect = title.get_rect(center=(center_x-int(width/2.7), center_y - int(0.1*center_y)))
        screen.blit(title, text_rect)

        prozent = str(str(int(self.progress*100)) + "%")
        title = font.render(prozent, True, colors.black)
        text_rect = title.get_rect(center=(center_x + int(width / 2.3), center_y - int(0.1 * center_y)))
        screen.blit(title, text_rect)

        title = font.render(self.info, True, colors.black)
        text_rect = title.get_rect(center=(center_x, center_y + int(0.12 * center_y)))
        screen.blit(title, text_rect)

        pygame.display.flip()
