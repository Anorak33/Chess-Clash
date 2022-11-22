import pygame

class Square():
    
    def __init__(self, x, y):
        self.grid_coords = (x, y)
        self.screen_coords = (x * 8, y * 16)
        
        self.image = pygame.image.load("model/image/none.png") 
        self.image_factor_x = int(pygame.display.get_window_size()[0] / 8)
        self.image_factor_y = int(pygame.display.get_window_size()[1] / 16)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.image_factor_x, self.image.get_height() * self.image_factor_y))
        
          
    def draw(self, screen):
        screen.blit(self.image, self.screen_coords)    