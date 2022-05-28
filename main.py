import pygame
import sys
import menus
from manage_wordsearches import WordsearchManager
from import_wordsearches import ImportWordsearches
from generate_wordsearches import WordsearchGenerator
from support.settings import *
import os


class ProgramManager:
    def __init__(self):
        self.state = "menus"
        self.menus = menus.Menus(WIN)

    def run(self):
        if self.state == "menus":
            WIN.fill((0, 0, 0))
            return_value = self.menus.run(events)

            if return_value == "quit":
                pygame.quit()
                sys.exit()

            if return_value == "import":
                self.state = "importing"
                self.importer = ImportWordsearches(WIN)

            if return_value == "manage":
                self.state = "manage"
                self.manager = WordsearchManager(WIN)

            if return_value == "generate":
                self.state = "generate"
                self.generator = WordsearchGenerator(WIN)

        if self.state == "importing":
            WIN.fill((0, 0, 0))
            return_value = self.importer.run(events)

            if return_value == "mainmenu":
                self.state = "menus"
                self.menus = menus.Menus(WIN)

        if self.state == "manage":
            return_value = self.manager.run(events)
            if return_value == "mainmenu":
                self.state = "menus"
                self.menus = menus.Menus(WIN)

        if self.state == "generate":
            return_value = self.generator.run(events)
            if return_value == "mainmenu":
                self.state = "menus"
                self.menus = menus.Menus(WIN)


try:
    os.mkdir("imported_wordsearches")
except FileExistsError:
    pass

pygame.init()
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Thomas' Wordsearch Program!")
CLOCK = pygame.time.Clock()
manager = ProgramManager()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    manager.run()

    pygame.display.update()
    CLOCK.tick(60)
