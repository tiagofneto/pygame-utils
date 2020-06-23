import pygame
from button import button

class checkbox():
    def __init__(self, color, x, y, width, height, outline=1, check=False, text="", size=60, font=None, textGap = 10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.outline = outline
        self.color = color
        self.check = check
        self.text = text
        self.font = pygame.font.SysFont(font, size)
        self.size = size
        self.textGap = textGap

    def draw(self, win):
        but = button(self.color, self.x, self.y, self.width, self.height)
        but.draw(win, self.outline)

        if self.text != "":
            text = self.font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + self.width+self.textGap, self.y + (self.height/2 - text.get_height()/2)))
        if self.check:
            pygame.draw.line(win, (0, 0, 0), (self.x, self.y), (self.x + self.width - self.outline, self.y + self.height - self.outline))
            pygame.draw.line(win, (0, 0, 0), (self.x - self.outline + self.width, self.y), (self.x, self.y + self.height - self.outline))

    def isOver(self, pos):
        return pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height

    def isChecked(self):
        return self.check

    def convert(self):
        self.check = not self.check