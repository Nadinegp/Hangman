import pygame as py
from Start import Page
from GetWord import Page2
from Play import Page3
from pygame.locals import *

# Initialize the pages
p = Page()
p2 = Page2()
p3 = Page3()

# Start the application with the main intro
while p.running:
    p.mainIntro()

# Go to the word input page
while p2.running:
    p2.mainGetWord()

while p3.running:
    p3.getto()
