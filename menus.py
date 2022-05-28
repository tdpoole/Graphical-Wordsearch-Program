from support.button import Button
from support.settings import *


class Menus:
    def __init__(self, surface):
        self.display_surface = surface

        self.setup_main_menu()

    def run(self, events):

        command = None
        if self.screen == "main":
            for i, x in enumerate(self.buttons):

                if x.draw(self.display_surface):

                    if i == 0:
                        command = "quit"
                    if i == 1:
                        command = "import"
                    if i == 2:
                        command = "manage"
                    if i == 3:
                        command = "generate"

            if command != None:
                return command

        return False

    def setup_main_menu(self):
        self.screen = "main"
        self.buttons = []
        self.buttons.append(
            Button(
                (SCREEN_WIDTH / 2, 700),  # Pos
                (100, 50),  # Size
                BUTTON_DEFAULT_COLOUR,  # Default Colour
                BUTTON_HILIGHTED_COLOUR,  # Hover Colour
                "QUIT",  # Display Text
                FONT,  # Text Font
                fontsize=50,  # Font Size
                fontcol=(0, 0, 0),  # Font Colour
            )
        )
        self.buttons.append(
            Button(
                (SCREEN_WIDTH / 2, 600),
                (500, 50),
                BUTTON_DEFAULT_COLOUR,
                BUTTON_HILIGHTED_COLOUR,
                "IMPORT WORDSEARCHES",
                FONT,
                fontsize=50,
            )
        )
        self.buttons.append(
            Button(
                (SCREEN_WIDTH / 2, 500),
                (500, 50),
                BUTTON_DEFAULT_COLOUR,
                BUTTON_HILIGHTED_COLOUR,
                "MANAGE WORDSEARCHES",
                FONT,
                fontsize=50,
            )
        )
        self.buttons.append(
            Button(
                (SCREEN_WIDTH / 2, 400),
                (500, 50),
                BUTTON_DEFAULT_COLOUR,
                BUTTON_HILIGHTED_COLOUR,
                "GENERATE WORDSEARCHES",
                FONT,
                fontsize=50,
            )
        )
        # Add menu title to be a button, but make sure it does nothing!
        self.buttons.append(
            Button(
                (SCREEN_WIDTH / 2, 100),
                (800, 150),
                BUTTON_DEFAULT_COLOUR,
                BUTTON_DEFAULT_COLOUR,
                "MAIN MENU",
                FONT,
                fontsize=100,
            )
        )


if __name__ == "__main__":
    import main
