import pygame as py
from GoTo2 import Page2
from pygame.locals import *
import sys
# # py.init()


class Page3:
    def __init__(self):
        self.text = Page2().sendText()
        print(self.text)
        self.running = True
        
    def getto(self):
        while self.running:
            for event in py.event.get():
                    if event.type == py.QUIT:
                        self.running = False
                        py.quit()
                        sys.exit()
                    elif event.type == py.KEYDOWN and input_active:
                        if event.key == py.K_RETURN:
                            input_active = False
                        elif event.key == py.K_BACKSPACE:
                            self.input_text =  self.input_text[:-1]
                        else:
                            self.input_text += event.unicode
                            print(self.input_text)
                        
            
   
                
    
           