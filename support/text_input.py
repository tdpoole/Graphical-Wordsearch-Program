import pygame


class TextInputFeild:
    def __init__(
        self,
        position,
        size,
        colour,
        hilighted_colour,
        selected_colour,
        txt_col,
        txt_size,
        font,
        text_limit,
    ):
        self.pos = position
        self.size = size
        self.col = colour
        self.default_col = colour
        self.hilight_col = hilighted_colour
        self.select_col = selected_colour
        self.txt_col = txt_col
        self.txt_size = txt_size
        self.font = font
        self.text_limit = text_limit

        self.state = "nothing"
        self.string = ""

        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect(center=self.pos)

        self.font = pygame.font.SysFont(font, self.txt_size)
        self.displaytext = self.string

        self.font = pygame.font.SysFont(font, txt_size)
        self.animation_cycle = 0

    def draw(self, screen, events):
        pos = pygame.mouse.get_pos()

        if self.state == "nothing":
            self.displaytext=self.string
            if self.rect.collidepoint(pos) and not pygame.mouse.get_pressed()[0]:
                self.state = "hilight"
                self.col = self.hilight_col

        if self.state == "hilight":
            if not self.rect.collidepoint(pos):
                self.state = "nothing"
                self.col = self.default_col
            if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                self.state = "selected"
                self.col = self.select_col

        if self.state == "selected":
            if pygame.mouse.get_pressed()[0] and (not self.rect.collidepoint(pos)):
                self.state = "nothing"
                self.col = self.default_col

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.string = self.string[:-1]

                    elif len(self.string) < self.text_limit:
                        self.string += event.unicode

            self.animation_cycle += 1
            if self.animation_cycle > 50 and len(self.string) < self.text_limit:
                self.displaytext = self.string + "|"
            else:
                self.displaytext = self.string

            if self.animation_cycle > 100:
                self.animation_cycle = 0

        text_surf = self.font.render(self.displaytext, 1, self.txt_col)
        text_rect = text_surf.get_rect(center=self.pos)

        self.surface.fill(self.col)
        screen.blit(self.surface, self.rect)
        screen.blit(text_surf, text_rect)
