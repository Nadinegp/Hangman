import pygame as py
from Start import Page
from pygame.locals import *
import time

# Function to dynamically get the word from the file
def get_word_from_file():
    try:
        with open("text.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""  # Return empty string if the file doesn't exist yet

py.init()

# Initialize display
height = Page().height
width = Page().width
screen = Page().screen

# Initialize word and display
newText = get_word_from_file()  # Get the word from the file
size = len(newText)
display = "_" * size  # Create an underscore display for the word

class Page3:
    def __init__(self):
        self.text = newText  # Word to guess (initially from file)
        self.font = py.font.Font(None, 40)
        self.entered_font = py.font.SysFont('yugothicuilight', 30)
        self.running = True
        self.input_letter = ""
        self.count = 6  # Number of attempts
        self.word = ""  # Letters entered by the user
        self.guessed = ""  # Correctly guessed letters
        self.display = display
        self.spaceDisplay = ""
        self.timer_font = py.font.SysFont(None, 50, False, False)
        self.mins = 2
        self.secs = 60
        self.t = 120  # Timer in seconds
        self.exit = py.transform.scale(py.image.load('exit.png'), (50, 50))  
        self.len=len(self.text)
        
    def countdown(self):
        """Manages the countdown timer."""
        if self.t != 0:
            self.mins, self.secs = divmod(self.t, 60)
            timer = '{:02d}:{:02d}'.format(self.mins, self.secs)
            time.sleep(1)
            timer = str(timer)
            time_surf = self.font.render(timer, True, "red")
            screen.blit(time_surf, (40, 20))
            py.display.flip()
            self.t -= 1
        else:
            return False

    def result(self, word, flag):
        """Displays the result (win/lose)."""
        state = "Congrats! " if flag else "You Lost! "
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    mx, my = py.mouse.get_pos()
                    if 270 <= mx <= 310 and 400 <= my <= 430:
                        self.running = False
                        py.quit()
            screen.fill("black")
            screen.blit(self.exit, (270, 400))
            state_surf = self.font.render(state, True, "white")
            word_surf = self.font.render("The Word was " + word, True, "white")
            screen.blit(state_surf, state_surf.get_rect(center=(width / 2, height / 2 - 50)))
            screen.blit(word_surf, word_surf.get_rect(center=(width / 2, height / 2 + 20)))
            py.display.update()

    def draw(self, letter, flag):
        """Updates the displayed word."""
        if flag:
            for i, char in enumerate(self.text):
                if char == letter:
                    self.display = self.display[:i] + letter + self.display[i + 1:]
            self.spaceDisplay = " ".join(self.display)
        else:
            self.spaceDisplay = " ".join(self.display)
        display_surf = self.font.render(self.spaceDisplay, True, "white")
        screen.blit(display_surf, (width / 2 - len(self.spaceDisplay) * 10, height / 2 + 75))
        py.display.update()

    def getto(self):
        """Main game loop."""
        while self.running:
            # Re-read the word each time to get the updated word
            self.text = get_word_from_file()  # Refresh the word every loop
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        if self.input_letter in self.word:
                            entered_surf = self.entered_font.render(
                                "*letter already pressed*", True, "white"
                            )
                            screen.blit(entered_surf, entered_surf.get_rect(center=(width / 2, height / 2 + 170)))
                            py.display.update()
                            py.time.wait(100)
                        else:
                            self.word += self.input_letter
                            if self.input_letter in self.text:
                                self.draw(self.input_letter, True)
                                self.guessed += self.input_letter
                                if "_" not in self.display:  # All letters guessed
                                    self.result(self.text, True)
                            else:
                                self.count -= 1
                    else:
                        self.input_letter = event.unicode
                        if self.count == 0:
                            self.result(self.text, False)

            self.bg = py.image.load('hangman' + str(self.count) + '.jpg')
            screen.blit(self.bg, (0, 0))
            if self.countdown() == False:
                self.result(self.text, False)
            input_surf = self.font.render(self.input_letter, True, "white")
            screen.blit(input_surf, (width / 2, height / 2 + 120))
            self.draw(self.input_letter, False)
            py.display.update()
