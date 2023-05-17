import pygame 
import moderngl
import json 


pygame.init()


class Game:

    def __init__(self) -> None:
        self.run = True
        self.load_settings()
        self.screen = pygame.display.set_mode(self.screen_params)
        self.clock = pygame.time.Clock()    
        self.ran()
    
    def load_settings(self) -> None:
        with open('settings.json') as file:
            settings = json.loads(file.read())
        self.screen_params = (settings["screen"]["width"], settings["screen"]["height"])
        file.close()

    def ran(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.screen.fill("purple")
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()



Game()
