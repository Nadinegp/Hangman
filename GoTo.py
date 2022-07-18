import pygame as py
class Page:
    def __init__(self, width , height,color,screen,res):
        self.width = width
        self.height = height
        self.color = color
        self.res = res
        self.screen = screen
        def screen():
            return screen
        def height():
            return height
        def width():
            return width
        def res():
            return  res
        def color():
            return color

# def bef(self, width , height,color,screen,res):
#     self.width = width
#     self.height = height
#     self.color = color
#     self.res = res
#     self.screen = screen
#res =  (720,720)
py.init()
font = py.font.Font(None, 100)
# screen = py.display.set_mode(res)
# width = screen.get_width()
# height = screen.get_height()
bg = py.image.load('backgroud.jpg')
screen = Page.screen()
color = Page.color()
width = Page.width()
height = Page.height()
res = Page.res()
# bg = py.transform.scale(bg,(720,720))
submit = py.image.load('submit.jpg')
submit = py.transform.scale(submit,(100,60)).convert_alpha(screen)
# color = (200, 0, 150)
textBox = font.render(("Enter Text here"),1,(255,255,255))
input_active = True
text=""
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        if event.type == py.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == py.KEYDOWN and input_active:
            if event.key == py.K_RETURN:
                input_active = False
            elif event.key == py.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode
        if event.type == py.MOUSEBUTTONDOWN:
            mx,my = py.mouse.get_pos() 
            if mx>=365 and mx<=460 and my>=440 and my <=460:
                py.exit()
        screen.fill(color)
        screen.blit(bg, (0,0))
        text_surf = font.render(text, True, (255, 0, 0))
        screen.blit(text_surf, (width/2,height/2-60))
        screen.blit(textBox , (width/2,height/2+20))
        screen.blit(submit , (width/2,height/2+60))
        py.display.update()