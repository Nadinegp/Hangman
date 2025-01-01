import pygame as py
import sys
from pygame.locals import *

# Screen resolution
res = (600, 600)
py.init()
running = True
screen = py.display.set_mode(res)

class Page:
    def __init__(self):
        # Variables to use later for other functions in the same class
        self.running = running
        self.screen = screen
        self.height, self.width = 600, 600
        self.bg = py.image.load('starttt.jpg')
        self.start_button = py.transform.scale(py.image.load('start.png'), (100, 100)).convert_alpha()

    def mainIntro(self):
        while self.running:
            for ev in py.event.get():
                # For quitting
                if ev.type == py.QUIT:
                    py.quit()
                    self.running = False
                    sys.exit()
                # When buttons are pressed or released
                if ev.type == py.MOUSEBUTTONDOWN:
                    mx, my = py.mouse.get_pos()
                    print(mx, my)
                    # Check if the mouse click is within the start button boundaries
                    if 300 <= mx <= 460 and 270 <= my <= 340:
                        self.running = False

            # Draw background and button
            self.screen.blit(self.bg, (0, 0))  # Blits background
            self.screen.blit(self.start_button, (self.width / 2 + 20, self.height / 2 - 50))  # Blits button
            py.display.update()

# # Create and run the page
# page = Page()
# page.mainIntro()