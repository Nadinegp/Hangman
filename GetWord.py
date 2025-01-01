from pickle import NONE
import pygame as py
from Start import Page  # Ensure Start.py exists and is properly structured
from pygame.locals import *
import sys

# Initialize pygame and retrieve shared attributes from Page
py.init()
page = Page()  # Create a single instance of Page
height = page.height
width = page.width
screen = page.screen

class Page2:
    def __init__(self):
        self.running = True
        self.font_header = py.font.Font(None, 100)
        self.font_input_word = py.font.Font(None, 40)
        self.bg = py.image.load('getText.jpg')
        self.submit_button = py.transform.scale(py.image.load('submit.jpg'), (120, 100))
        self.HeaderText_surf = self.font_header.render("Guessed Word", True, "WHITE")
        self.input_text = ""
        self.font_empty = py.font.Font(None, 20)

    def mainGetWord(self):
        while self.running:
            for event in py.event.get():
                # Quit the application
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
                    sys.exit()
                
                # Handle keyboard events
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN or (event.type == py.MOUSEBUTTONDOWN and 210 <= mx <= 370 and 325 <= my <= 450 and self.input_text):
                        if not self.input_text:  # Check for empty input
                            entered_surf = self.font_empty.render(
                                "*Guessed word can't be empty!*", True, "white"
                            )
                            screen.blit(entered_surf, entered_surf.get_rect(center=(width / 2, height / 2 + 260)))
                            py.display.update()
                            py.time.wait(2000)
                        else:
                            with open("text.txt", "w") as file:
                                file.write(self.input_text)  # Write input text to file
                                file.flush()  # Flush data immediately to disk
                            self.running = False

                    elif event.key == py.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]  # Remove last character
                    
                    else:  # Add character to input
                        self.input_text += event.unicode

                # Handle mouse click on the submit button
                elif event.type == py.MOUSEBUTTONDOWN:
                    mx, my = py.mouse.get_pos()
                    if 210 <= mx <= 370 and 325 <= my <= 450 and self.input_text:
                        with open("text.txt", "w") as file:
                            file.write(self.input_text)
                        self.running = False

            # Draw the screen
            screen.blit(self.bg, (0, 0))  # Background
            text_surf = self.font_input_word.render(self.input_text, True, "white")
            text_rect = text_surf.get_rect(center=(width / 2, height / 2))
            screen.blit(text_surf, text_rect)  # Input text
            
            HeaderText_rect = self.HeaderText_surf.get_rect(center=(width / 2, height / 2 - 120))
            screen.blit(self.HeaderText_surf, HeaderText_rect)  # Header text
            
            submit_rect = self.submit_button.get_rect(center=(width / 2, height / 2 + 170))
            screen.blit(self.submit_button, submit_rect)  # Submit button
            
            py.display.update()

# # Create and run Page2
# page2 = Page2()
# page2.mainGetWord()