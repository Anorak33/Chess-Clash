import pygame

class Square():
    
    def __init__(self, x, y):
        self.grid_coords = (x, y)
        
        self.image = pygame.image.load("None") 
        self.area_surface = pygame.Surface((int(pygame.display.get_window_size()[0] / 8), int(pygame.display.get_window_size()[1] / 16)))
        self.
        
          
    def draw(self, screen):
        screen.blit(self.area_surface, (self.coords[0] * 8, self.coords[1] * 16))    