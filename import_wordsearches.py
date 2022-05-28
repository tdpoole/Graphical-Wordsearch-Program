from support.user_select_file_tk import select_files
from support.button import Button
from support.settings import *
from support import csv_import_wordsearch
import pickle
from support.text_input import TextInputFeild


class ImportWordsearches:
    def __init__(self, surface):
        self.display_surface = surface
        self.state = "selectmessage"
        self.filelocation = ""

        self.count = 0

    def run(self, events):
        if self.state == "selectmessage":
            self.count += 1
            if self.count > 5:
                self.state = "choosingfile"
            Button(
                (SCREEN_WIDTH / 2, 500),
                (SCREEN_WIDTH, 500),
                BUTTON_DEFAULT_COLOUR,
                BUTTON_DEFAULT_COLOUR,
                "PLEASE SELECT A WORDSEARCH CSV FILE",
                FONT,
                fontsize=100,
            ).draw(self.display_surface)

        elif self.state == "choosingfile":
            file = select_files(
                [("CSV Files", "*.csv")],
                window_title="Import a Wordsearch",
                onefile=True,
            )
            if file == "":
                return "mainmenu"
            else:
                self.filelocation = file
                self.state = "loadingfiletext"

        elif self.state == "loadingfiletext":
            self.count += 1
            if self.count > 10:
                self.wordsearch_obj = csv_import_wordsearch.import_wordsearch_from_file(self.filelocation)
                self.state = "askname"
                self.text_feild = TextInputFeild(
                    (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                    (900, 200),
                    (200, 200, 200),
                    (175, 175, 175),
                    (100, 100, 100),
                    (255, 255, 255),
                    100,
                    FONT,
                    50,
                )
                self.accept_button = Button(
                    (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200),
                    (500, 100),
                    (0, 250, 0),
                    (0, 200, 0),
                    "ACCEPT",
                    FONT,
                    fontsize=100,
                )
            Button(
                (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                (SCREEN_WIDTH, 500),
                BUTTON_DEFAULT_COLOUR,
                BUTTON_DEFAULT_COLOUR,
                "LOADING FILE",
                FONT,
                fontsize=100,
            )

        elif self.state == "askname":
            Button(
                (SCREEN_WIDTH / 2, 100),
                (SCREEN_WIDTH, 150),
                BUTTON_DEFAULT_COLOUR,
                BUTTON_DEFAULT_COLOUR,
                "PLEASE ENTER THE NAME OF THIS WORDSEARCH",
                FONT,
                fontsize=100,
            ).draw(self.display_surface)
            self.text_feild.draw(self.display_surface, events)
            accept = self.accept_button.draw(self.display_surface)
            if accept:
                with open("imported_wordsearches/" + self.text_feild.string + ".ws", "wb") as f:
                    pickle.dump(self.wordsearch_obj, f)
                    self.state = "sucess"
                self.accept_button = Button(
                    (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                    (500, 100),
                    (0, 250, 0),
                    (0, 200, 0),
                    "SUCESS!",
                    FONT,
                    fontsize=100,
                )

        elif self.state == "sucess":
            exit_to_menu = self.accept_button.draw(self.display_surface)
            if exit_to_menu:
                return "mainmenu"


if __name__ == "__main__":
    import main
