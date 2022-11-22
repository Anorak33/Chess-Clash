import pygame
from model.square import Square
class Game:
    
    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        
        self.grid = []                  # x,y coords, from top left (0,0) to bottom right (8,16)
        for i in range(16):
            temp_line = []
            for i in range(8):
                # y coords
                temp_line.append(Square(len(temp_line), len(self.grid)))    # Create Square with coordinate
            # x coords        
            self.grid.insert(0, temp_line)

        for i in self.grid:
            print(i)
            
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
        pass
                    
    def display(self):
        self.screen.fill("black") 
          
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].draw(self.screen)

        pygame.display.flip()
    
    def run(self):
        print(pygame.display.get_window_size())
        while self.running:
            self.handling_event()
            self.mouse_checking()
            self.update()
            self.display()
            self.clock.tick(60)
            
            
            

screen_widht = 300
screen_height = 600

pygame.init()

screen = pygame.display.set_mode((screen_widht , screen_height))
game = Game(screen)
game.run()

pygame.quit()