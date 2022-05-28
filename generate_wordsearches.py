import csv
from random import randint
from random import choice
from support.user_select_file_tk import select_files
from support.button import Button
from support.settings import *
from support import csv_import_wordsearch
import pickle
from support.text_input import TextInputFeild
from wordsearchclass import Wordsearch
import pygame
from tkinter import messagebox

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "NORTHEAST", "NORTHWEST", "SOUTHEAST", "SOUTHWEST"]
shift_values = {"NORTH": {"x": 0, "y": -1}, "SOUTH": {"x": 0, "y": 1}, "EAST": {"x": 1, "y": 0}, "WEST": {"x": -1, "y": 0}, "NORTHEAST": {"x": 1, "y": -1}, "NORTHWEST": {"x": -1, "y": -1}, "SOUTHEAST": {"x": 1, "y": 1}, "SOUTHWEST": {"x": -1, "y": 1}}


class WordsearchGenerator:
    def __init__(self, surface):
        self.display_surface = surface
        self.state = "addwords"
        self.words = []
        self.width = None
        self.height = None

        self.header = Button((SCREEN_WIDTH / 2, 100), (SCREEN_WIDTH, 200), BUTTON_DEFAULT_COLOUR, BUTTON_DEFAULT_COLOUR, "PLEASE ADD WORDS TO YOUR WORDSEARCH", FONT, fontsize=100)
        self.input_box = TextInputFeild(
            (SCREEN_WIDTH / 2, 300),
            (900 / 2, 200 / 2),
            (200, 200, 200),
            (175, 175, 175),
            (100, 100, 100),
            (255, 255, 255),
            100,
            FONT,
            50,
        )
        self.accept_button_respondant = True
        self.remove_button_respondant = True
        self.generate_button = Button((SCREEN_WIDTH / 2, 450), (300, 75), (0, 200, 0), (0, 175, 0), "GENERATE", FONT, fontsize=50)
        self.accept_button = Button((SCREEN_WIDTH / 2, 550), (300, 75), (0, 200, 0), (0, 175, 0), "ADD WORD", FONT, fontsize=50)
        self.remove_button = Button((SCREEN_WIDTH / 2, 650), (300, 75), (200, 0, 0), (175, 0, 0), "REMOVE WORD", FONT, fontsize=50)
        self.exit_button = Button((SCREEN_WIDTH / 2, 750), (100, 50), (200, 0, 0), (175, 0, 0), "EXIT", FONT, fontsize=50)

        self.length_title = Button(((SCREEN_WIDTH / 2) + SCREEN_WIDTH / 4, 450), (175, 75), (0, 0, 0), (0, 0, 0), "LENGTH:", FONT, fontsize=50, fontcol=(255, 255, 255))
        self.width_title = Button(((SCREEN_WIDTH / 2) + SCREEN_WIDTH / 4, 550), (175, 75), (0, 0, 0), (0, 0, 0), "WIDTH:", FONT, fontsize=50, fontcol=(255, 255, 255))

        self.length_input = TextInputFeild((((SCREEN_WIDTH / 2) + SCREEN_WIDTH / 4) + 200, 450), (175, 75), (200, 200, 200), (175, 175, 175), (100, 100, 100), (255, 255, 255), 50, FONT, 2)
        self.width_input = TextInputFeild((((SCREEN_WIDTH / 2) + SCREEN_WIDTH / 4) + 200, 550), (175, 75), (200, 200, 200), (175, 175, 175), (100, 100, 100), (255, 255, 255), 50, FONT, 2)

    def run(self, events):
        if self.state == "addwords":
            self.display_surface.fill((0, 0, 0))
            self.header.draw(self.display_surface)
            self.input_box.draw(self.display_surface, events)
            self.length_title.draw(self.display_surface)
            self.width_title.draw(self.display_surface)
            self.length_input.draw(self.display_surface, events)
            self.width_input.draw(self.display_surface, events)

            generate = self.generate_button.draw(self.display_surface)
            accept = self.accept_button.draw(self.display_surface)
            remove = self.remove_button.draw(self.display_surface)
            exit_to_menu = self.exit_button.draw(self.display_surface)

            for ind, word in enumerate(self.words):
                font = pygame.font.Font(FONT, 50)
                text = font.render(word, True, (255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (100, int(300 + (75 * ind)))
                self.display_surface.blit(text, text_rect)

            if not accept:
                self.accept_button_respondant = True
            if not remove:
                self.remove_button_respondant = True

            if exit_to_menu:
                return "mainmenu"

            if accept and self.accept_button_respondant:
                self.accept_button_respondant = False
                toadd = self.input_box.string.upper()
                error = False
                if toadd == "":
                    error = True
                for let in toadd:
                    if not (let in ALPHABET):
                        error = True

                if error:
                    messagebox.showerror("Error", "Please only use characters a-z")

                if not error:
                    self.words.append(toadd)

            if remove and self.remove_button_respondant:
                self.remove_button_respondant = False
                try:
                    self.words.pop()
                except IndexError:
                    messagebox.showerror("Error", "No words to remove")

            if generate:
                if len(self.words) == 0:
                    messagebox.showerror("Error", "You need to add words to generate a wordsearch")
                    return

                if len(self.width_input.string) == 0 or len(self.length_input.string) == 0:
                    messagebox.showerror("Error", "length or Width input invalid")

                try:
                    length = int(self.length_input.string)
                    width = int(self.width_input.string)
                except ValueError:
                    messagebox.showerror("Error", "length or Width input invalid")
                    return
                self.display_surface.fill((0, 0, 0))
                Button(
                    (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                    (SCREEN_WIDTH, 500),
                    BUTTON_DEFAULT_COLOUR,
                    BUTTON_DEFAULT_COLOUR,
                    "GENERATING",
                    FONT,
                    fontsize=100,
                ).draw(self.display_surface)
                self.state = "generating"

        if self.state == "generating":
            # GENERATE!
            grid = [["empty" for x in range(width)] for y in range(length)]

            for adding_word in self.words:
                gridbackup = grid
                sucess = False

                timeout = 0
                while not sucess:
                    timeout += 1

                    if timeout >= 100000:
                        messagebox.showerror("Error", "This wordsearch could not be generated")
                        return "mainmenu"

                    gridbackup = grid
                    chosen_direction = choice(directions)
                    chosen_x = randint(0, width - 1)
                    chosen_y = randint(0, length - 1)

                    for addingletter in list(adding_word):

                        try:
                            if gridbackup[chosen_y][chosen_x] == "empty" or gridbackup[chosen_y][chosen_x] == addingletter:
                                gridbackup[chosen_y][chosen_x] = addingletter
                                chosen_x += shift_values[chosen_direction]["x"]
                                chosen_y += shift_values[chosen_direction]["y"]
                            else:
                                break
                        except IndexError:
                            break

                        if addingletter == adding_word[-1]:
                            sucess = True
                            grid = gridbackup

            for y, row in enumerate(grid):
                for x, val in enumerate(row):
                    if val == "empty":
                        grid[y][x] = choice(alphabet)

            with open("output.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(grid)
            return "mainmenu"


if __name__ == "__main__":
    import main
