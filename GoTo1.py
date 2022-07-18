import pygame as py
import sys
from pygame.locals import *

class Page:
    def __init__(self):
        running = True
        self.running = running
        res =  (600,600)
        py.init()
        screen = py.display.set_mode(res)
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.color = (200, 0, 150)
        self.screen = screen
        start = py.image.load('start.png')
        self.start = py.transform.scale(start,(100,100)).convert_alpha(self.screen)

    def Intro(self):
        while self.running:
            for ev in py.event.get():
                
                if ev.type == py.QUIT:
                    py.quit()
                    self.running = False
                    sys.exit()
                if ev.type == py.MOUSEBUTTONDOWN:
                    mx, my = py.mouse.get_pos()
                    print(mx,my)
                    if mx>=300 and mx<=460 and my>=320 and my<=422:
                        self.running = False
            self.screen.fill(self.color)
            self.screen.blit(self.start , (self.width/2,self.height/2))
            py.display.update()
            
# height = Page().height
# color = Page().color
# width = Page().width
# screen = Page().screen
# py.init()
# font = py.font.Font(None, 100)
# font1 = py.font.Font(None, 30)
# bg = py.image.load('backgroud.jpg')
# submit = py.image.load('submit.jpg')
# submit = py.transform.scale(submit,(100,60)).convert_alpha(Page().screen)
# HeaderText = font.render(("Enter Text here"),1,'BLACK')
# input_active = True
# input_text=""
# while True:
#     for event in py.event.get():
#         if event.type == py.QUIT:
#             py.quit()
#         if event.type == py.MOUSEBUTTONDOWN:
#             mouse = py.mouse.get_pos() ########################
#             print(width)
#             print(mouse)
#             input_active = True
#             input_text = ""
#         elif event.type == py.KEYDOWN and input_active:
#             if event.key == py.K_RETURN:
#                 input_active = False
#             elif event.key == py.K_BACKSPACE:
#                 input_text =  input_text[:-1]
#             else:
#                 input_text += event.unicode
#         if event.type == py.MOUSEBUTTONDOWN:
#             mx,my = py.mouse.get_pos() 
#             if mx>=365 and mx<=460 and my>=440 and my <=460:
#                 py.exit()
#        # screen.fill(color)
#         screen.blit(bg, (0,0))
#         text_surf = font1.render(input_text, True, (255, 0, 0))
#         screen.blit(text_surf, (width/2-120,height/2-60))
#         screen.blit(HeaderText , (width/2-250,height/2-120))
#         screen.blit(submit , (width/2-60,height/2+60))
#         py.display.update()