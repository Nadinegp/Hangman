import pygame as py
import GoTo as page
import sys
from pygame.locals import *

res =  (600,600)
py.init()
screen = py.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()
color = (200, 0, 150)
start = py.image.load('start.png')
start = py.transform.scale(start,(100,100)).convert_alpha(screen)

while True:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.quit()
            sys.exit()
        if ev.type == py.MOUSEBUTTONDOWN:
            mx, my = py.mouse.get_pos()
            if mx>=366 and mx<=460 and my>=395 and my <=422:
                page.Page(width,height,color,screen,res)
        screen.fill(color)
        screen.blit(start , (width/2,height/2))
        py.display.update()