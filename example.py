import sys
import pygame
import button
import checkbox
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
win = pygame.display.set_mode((width, height))
WHITE = (255, 255, 255)

but1 = button.button((142, 87, 230), 100, 100, 100, 100, "Button", 30)
checkb1 = checkbox.checkbox((100, 100, 100), 300, 300, 100, 100, text="Checkbox", outline=3)

def update():
    pass

def draw():
    but1.draw(win)
    checkb1.draw(win)
    pass
 
# Main loop.
while True:
    win.fill(WHITE)
  
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if but1.isOver(pos):
                print("But1")
            elif checkb1.isOver(pos):
                checkb1.convert()
                print("Checkb1")
        
        if event.type == pygame.MOUSEMOTION:
            if but1.isOver(pos):
                but1.color = (100, 200, 200)
            else:
                but1.color = (142, 87, 230)
  
    update()
  
    draw()
  
    pygame.display.flip()
    fpsClock.tick(fps)
