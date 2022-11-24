import pygame

class Square():
    
    def __init__(self, x, y):
        self.grid_coords = (x, y)
        self.screen_coords = (x * 40+10, y * 40+10)    #* screen whidth / 3 and screen height / 6
        self.color = "none"
        
        
        if x % 2 == y % 2:
            self.color = "black"
        else:
            self.color = "white"
        
        
        if x == 0 and y == 11:
            self.color = "none"
        
        if x == 7 and y == 0:
            self.color = "none"
                
        self.image = pygame.image.load(f"model/image/square/{self.color}.png") 
        
          
    def draw(self, screen):
        screen.blit(self.image, self.screen_coords)    