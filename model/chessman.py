import pygame

class ChessMan():
    
    def __init__(self, player, name, grid_coords): 
        self.player = player
        self.name = name 
        self.image = pygame.image.load(f"model/image/chessman/{player}/{name}.png")  # Modif with screen resolution
        
        self.grid_coords = grid_coords
        self.screen_coords = (grid_coords[0] * 40+10, grid_coords[1] * 40+10)
        
    def draw(self, screen):
        screen.blit(self.image, self.grid_coords)    
        
    