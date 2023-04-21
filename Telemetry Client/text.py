import pygame
from OpenGL.GL import *

COLOR_WHITE = (255, 255, 255, 255)

class Text:
    def __init__(self, text, x, y, font_size=24):
        pygame.font.init()
        self.font = pygame.font.SysFont('arial', font_size)
        self.textSurface = self.font.render(text, True, COLOR_WHITE).convert_alpha()
        self.textData = pygame.image.tostring(self.textSurface, "RGBA", True)
        self.x = x
        self.y = y

    def draw(self):
        glWindowPos2d(self.x, self.y)
        glDrawPixels(self.textSurface.get_width(), self.textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, self.textData)
