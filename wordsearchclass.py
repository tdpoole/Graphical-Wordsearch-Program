import pygame
from support.settings import *
# The wordsearch class will contain the wordsearch itself as well as the solution to the wordsearch.
class Wordsearch:
    #   Initialising variables
    def __init__(self, data):
        self.grid = data
        self.row_count = len(data)
        self.column_count = len(data[0])

    #   A simple function that checks to see if a word is in a certain direction. Returns bool.
    def check_in_direction(
        self,
        direction,
        # Refer to the up and down directions to search in
        dirx,
        diry,
        looking_for_word_list,
        start_row_position,
        start_column_position,
        looking_for_word,
    ):
        for index, letter in enumerate(looking_for_word_list):
            try:
                if (
                    letter.upper()
                    != self.grid[start_row_position + index * diry][
                        start_column_position + index * dirx
                    ].upper()
                ):
                    return False
            except IndexError:
                return False
            if index == len(looking_for_word_list) - 1:
                self.wordlocation = str(start_column_position) + " , " + str(start_row_position)
                self.worddirection = direction
                return True
    
    def draw_on_surface(self,surface):
        surf=pygame.Surface((1000,1000))
        surf.fill((255,255,255))
        surface.blit(surf,(0,0))       
        
        
        longest_side=len(self.grid)
        if len(self.grid[0])>longest_side:
            longest_side=len(self.grid[0])
        
        SQUARE_SIZE=int(1000/longest_side)
        
        for ypos,row in enumerate(self.grid):            
            pygame.draw.line(surface,(0,0,0),(0,SQUARE_SIZE*ypos),(1000,SQUARE_SIZE*ypos))
            
            for xpos,letter in enumerate(row):
                pygame.draw.line(surface,(0,0,0),(SQUARE_SIZE*xpos,0),(SQUARE_SIZE*xpos,1000))
                
                font=pygame.font.SysFont(FONT,int(SQUARE_SIZE*1.25))
                img=font.render(letter,True,(0,0,0))
                surface.blit(img,((ypos*SQUARE_SIZE)+SQUARE_SIZE/4,(xpos*SQUARE_SIZE)+SQUARE_SIZE/4))
        

    
    #   The actual wordsearcher
    def find_word(self, word_to_search_for):
        self.worddirection=None
        self.wordlocation=None
        
        looking_for_word=word_to_search_for
        
        sucess = False
        looking_for_word_list = list(looking_for_word)

        # Iterate through every word in the grid
        for start_row_position, currentrow in enumerate(self.grid):
            for start_column_position, starting_letter in enumerate(currentrow):

                if (
                    starting_letter == looking_for_word_list[0]
                ):  # If so, it is worth checking

                    # Checks in each direction. Results are stored by the check_in_direction function
                    sucess = self.check_in_direction(
                        "NORTH",
                        0,
                        -1,
                        looking_for_word_list,
                        start_row_position,
                        start_column_position,
                        looking_for_word,
                    )

                    if not sucess:
                        sucess = self.check_in_direction(
                            "SOUTH",
                            0,
                            1,
                            looking_for_word_list,
                            start_row_position,
                            start_column_position,
                            looking_for_word,
                        )

                    if not sucess:
                        sucess = self.check_in_direction(
                            "WEST",
                            -1,
                            0,
                            looking_for_word_list,
                            start_row_position,
                            start_column_position,
                            looking_for_word,
                        )

                    if not sucess:
                        sucess = self.check_in_direction(
                            "EAST",
                            1,
                            0,
                            looking_for_word_list,
                            start_row_position,
                            start_column_position,
                            looking_for_word,
                        )

                    if not sucess:
                        sucess = self.check_in_direction(
                            "NORTHWEST",
                            -1,
                            -1,
                            looking_for_word_list,
                            start_row_position,
                            start_column_position,
                            looking_for_word,
                        )

                    if not sucess:
                        sucess = self.check_in_direction(
                            "NORTHEAST",
                            1,
                            -1,
                            looking_for_word_list,
                            start_row_position,
                            start_column_position,
                            looking_for_word,
                        )

                    if not sucess:
                        sucess = self.check_in_direction(
                            "SOUTHWEST",
                            -1,
                            1,
                            looking_for_word_list,
                            start_row_position,
                            start_column_position,
                            looking_for_word,
                        )

                    if not sucess:
                        sucess = self.check_in_direction(
                            "SOUTHEAST",
                            1,
                            1,
                            looking_for_word_list,
                            start_row_position,
                            start_column_position,
                            looking_for_word,
                        )
    
        return self.wordlocation,self.worddirection