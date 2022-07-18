import pygame as py
from GoTo1 import Page
# from GoTo3 import Page3
from pygame.locals import *
import sys
p = Page()
# p3 = Page3()

height = Page().height
color = Page().color
width = Page().width
screen = Page().screen
py.init()
class Page2:
        def __init__(self):
            self.running = True
            self.font = py.font.Font(None, 100)
            self.font1 = py.font.Font(None, 30)
            self.bg = py.image.load('backgroud.jpg')
            submit = py.image.load('submit.jpg')
            self.submit = py.transform.scale(submit,(100,60)).convert_alpha(Page().screen)
            self.HeaderText = self.font.render(("Enter Text here"),1,'BLACK')
            # input_active = True
            self.input_text=""
            
        def getWord(self):
            input_active = True
            while self.running:
                for event in py.event.get():
                    if event.type == py.QUIT:
                        self.running = False
                        py.quit()
                        sys.exit()
                    if event.type == py.MOUSEBUTTONDOWN:
                        mouse = py.mouse.get_pos() ########################
                        print(width)
                        print(mouse)
                        input_active = True
                        self.input_text = ""
                    elif event.type == py.KEYDOWN and input_active:
                        if event.key == py.K_RETURN:
                            input_active = False
                            self.running = False
                        elif event.key == py.K_BACKSPACE:
                            self.input_text =  self.input_text[:-1]
                        else:
                            self.input_text += event.unicode
                            print(self.input_text)
                    if event.type == py.MOUSEBUTTONDOWN:
                        mx,my = py.mouse.get_pos() 
                        if mx>=210 and mx<=370 and my>=325 and my <=400:
                            self.running = False
                # screen.fill(color)
                    screen.blit(self.bg, (0,0))
                    text_surf = self.font1.render(self.input_text, True, (255, 0, 0))
                    screen.blit(text_surf, (width/2-120,height/2-60))
                    screen.blit(self.HeaderText , (width/2-250,height/2-120))
                    screen.blit(self.submit , (width/2-60,height/2+60))
                    py.display.update()
                    
        # def sendText(self):
        #     print("heyehye")
        #     return Page2().getWord().self.input_text