from support.user_select_file_tk import select_files
from support.button import Button
from support.settings import *
from support import csv_import_wordsearch
import pickle
from support.text_input import TextInputFeild
from wordsearchclass import Wordsearch
import pygame

class WordsearchManager:
    def __init__(self, surface):
        self.display_surface = surface
        self.state = "selectmessage"
        self.filelocation = ""
        self.d=True

        self.count = 0

    def run(self, events):
        if self.state == "selectmessage":
            self.display_surface.fill((0,0,0))
            self.count += 1
            if self.count > 5:
                self.state = "choosingfile"
            Button(
                (SCREEN_WIDTH / 2, 500),
                (SCREEN_WIDTH, 500),
                BUTTON_DEFAULT_COLOUR,
                BUTTON_DEFAULT_COLOUR,
                "PLEASE SELECT A WORDSEARCH WS FILE",
                FONT,
                fontsize=100,
            ).draw(self.display_surface)

        elif self.state == "choosingfile":
            self.display_surface.fill((0,0,0))
            file = select_files(
                [("Wordsearch files", "*.ws")],
                window_title="Import a Wordsearch",
                onefile=True,
            )
            if file == "":
                return "mainmenu"
            else:
                self.filelocation = file
                self.state = "loadingfiletext"
        
        elif self.state=="loadingfiletext":
            self.display_surface.fill((0,0,0))
            self.count+=1
            if self.count>10:
                self.state="managewordsearch"
                
                with open(self.filelocation,"rb")as f:
                    self.loaded_wordsearch=pickle.load(f)
                    
                self.search_for_word_text_field=TextInputFeild(
                    (1500,100),
                    (450, 100),
                    (200, 200, 200),
                    (175, 175, 175),
                    (100, 100, 100),
                    (255, 255, 255),
                    100,
                    FONT,
                    50,
                )
                
                self.accept_button=Button(
                    (1500, 250),
                    (450, 100),
                    (0, 250, 0),
                    (0, 200, 0),
                    "SEARCH",
                    FONT,
                    fontsize=100,
                )
                self.exit_button=Button(
                    (1500, 350),
                    (200, 75),
                    (250, 0, 0),
                    (200, 0, 0),
                    "EXIT",
                    FONT,
                    fontsize=100,
                )
                self.result_header=Button((1500,475), (600,100), (0,0,0), (0,0,0), "RESULTS:", FONT, fontsize=150, fontcol=(255, 255, 255))
                self.status=Button((1500,575), (450,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
                self.pos_header=Button((1500,675), (450,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
                self.pos=Button((1500,775), (450,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
                self.dir_header=Button((1500,875), (500,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
                self._dir=Button((1500,975), (450,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
        
        elif self.state=="managewordsearch":
            search= self.accept_button.draw(self.display_surface)
            exit=self.exit_button.draw(self.display_surface)
            
            self.search_for_word_text_field.draw(self.display_surface,events)
            self.result_header.draw(self.display_surface)
            self.status.draw(self.display_surface)
            self.pos_header.draw(self.display_surface)
            self.pos.draw(self.display_surface)
            self.dir_header.draw(self.display_surface)
            self._dir.draw(self.display_surface)
            
            if self.d:
                self.display_surface.fill((0,0,0))
                self.loaded_wordsearch.draw_on_surface(self.display_surface)
                self.d=False
            
            if exit:
                return "mainmenu"
            
            if search:
                results=self.loaded_wordsearch.find_word(self.search_for_word_text_field.string.upper())
                if results[0]==None:
                    self.result_header=Button((1500,475), (600,100), (0,0,0), (0,0,0), "RESULTS:", FONT, fontsize=150, fontcol=(255, 255, 255))
                    self.status=Button((1500,575), (450,75), (0,0,0), (0,0,0), "FAILED", FONT, fontsize=100, fontcol=(255, 0, 0))
                    self.pos_header=Button((1500,675), (450,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
                    self.pos=Button((1500,775), (450,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
                    self.dir_header=Button((1500,875), (500,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
                    self._dir=Button((1500,975), (450,75), (0,0,0), (0,0,0), "", FONT, fontsize=100, fontcol=(255, 255, 255))
                
                else:
                    self.result_header=Button((1500,475), (600,100), (0,0,0), (0,0,0), "RESULTS:", FONT, fontsize=150, fontcol=(255, 255, 255))
                    self.status=Button((1500,575), (450,75), (0,0,0), (0,0,0), "SUCESS", FONT, fontsize=100, fontcol=(0, 255, 0))
                    self.pos_header=Button((1500,675), (450,75), (0,0,0), (0,0,0), "POSITION:", FONT, fontsize=125, fontcol=(255, 255, 255))
                    self.pos=Button((1500,775), (450,75), (0,0,0), (0,0,0), results[0], FONT, fontsize=100, fontcol=(255, 255, 255))
                    self.dir_header=Button((1500,875), (500,75), (0,0,0), (0,0,0), "DIRECTION:", FONT, fontsize=125, fontcol=(255, 255, 255))
                    self._dir=Button((1500,975), (450,75), (0,0,0), (0,0,0), results[1], FONT, fontsize=100, fontcol=(255, 255, 255))

if __name__=="__main__":
    import main