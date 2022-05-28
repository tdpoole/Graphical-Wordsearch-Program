import pygame

# button class
class Button:
    def __init__(
        self, position, size, col, hovercol, text, font, fontsize=16, fontcol=(0, 0, 0)
    ):
        self.def_clr = col
        self.clr = col
        self.hoverclr = hovercol
        self.size = size
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect(center=position)

        if len(col) == 4:
            self.surface.set_alpha(col[3])

        self.can_be_pressed = False

        self.font = pygame.font.SysFont(font, fontsize)
        self.text = text
        self.fontcol = fontcol
        self.text_surface = self.font.render(self.text, 1, self.fontcol)
        self.text_rect = self.text_surface.get_rect(
            center=[wh // 2 for wh in self.size]
        )

    def draw(self, screen):
        self.mouseover()

        self.surface.fill(self.clr)
        self.surface.blit(self.text_surface, self.text_rect)
        screen.blit(self.surface, self.rect)
        return self.pressed

    def mouseover(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 0:
            self.can_be_pressed = True
            self.clr = self.hoverclr

        if self.rect.collidepoint(pos):

            if pygame.mouse.get_pressed()[0] == 1 and self.can_be_pressed:
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.clr = self.def_clr
            self.pressed = False
            self.can_be_pressed = False
