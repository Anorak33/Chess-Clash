import pygame
import math
import time

from model.square import Square
from model.chessman import *


class Game:
    
    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        
        
        self.line_number = 0
        self.grid = []                  # x,y coords, from top left (0,0) to bottom right (8,16)
        # for i in range(12):
        #     temp_line = []
        #     for i in range(8):
        #         # x coords
        #         x_coords = 11 - len(self.grid)
                
        #         temp_line.append(Square(len(temp_line), x_coords))    # Create Square with coordinate
        #         print(x_coords)
                
                
        #     # y coords        
        #     self.grid.append(temp_line)
        
        self.chessman = []
        # self.chessman.append(ChessMan("white", "none", (2, 2)))
            
    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            if event.type == pygame.MOUSEBUTTONUP:
                self.mous_cliked = pygame.mouse.get_pos()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE] :
            self.running = False       
             
    def mouse_checking(self):
        self.mouse_pos = (pygame.mouse.get_pos())   
        self.mouse_pressed = pygame.mouse.get_pressed()
     
    def update(self):
        if self.line_number < 12:
            temp_line = []
            for i in range(8):
                # x coords
                x_coords = len(self.grid)
                
                temp_line.append(Square(len(temp_line), x_coords))    # Create Square with coordinate
                print(x_coords)
                
                
            # y coords        
            self.grid.append(temp_line)
            self.line_number += 1
            
                    
    def display(self):
        self.screen.fill("dimgrey") 
          
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].draw(self.screen)
                
        for i in range(len(self.chessman)):
            self.chessman[i].draw(self.screen)

        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handling_event()
            self.mouse_checking()
            self.update()
            self.display()
            self.clock.tick(60)
            time.sleep(2)
            
            
            
            

screen_widht = 340
screen_height = 640

pygame.init()

screen = pygame.display.set_mode((screen_widht , screen_height))
game = Game(screen)
game.run()

pygame.quit()