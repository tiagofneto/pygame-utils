import pygame

#Button class, the optional parameters correspond to the text displayed, its size and font
class button():
    def __init__(self, color, x, y, width, height, text="", size=60, font=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont(font, size)

    #Draws the button, outline may be provided
    def draw(self, win, outline=0):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), outline)

        if self.text != "":
            text = self.font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    #Returns true is the given pos (either tuple or list) is over the button
    def isOver(self, pos):
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
            return False
