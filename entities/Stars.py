import pygame


class Stars:

    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.sizeX = 10
        self.sizeY = 10
        self.color = (255, 255, 255)
        self.vel = 1

    def draw(self, screen):
        # s = pygame.Surface((self.sizeX * 2, self.sizeY * 2))  # the size of your rect
        # s.set_alpha(20)  # alpha level
        # s.fill((255, 255, 255))  # this fills the entire surface
        # pygame.draw.circle(s, (0, 0, 255), (30, 30), 5)
        # screen.blit(s, (self.X - (self.sizeX / 2), self.Y - (self.sizeY / 2)))
        # surface1 = pygame.Surface((50, 50))
        # surface1.set_colorkey((0, 0, 0))
        # surface1.set_alpha(20)
        # pygame.draw.circle(surface1, (255, 255, 255), (25, 25), 10)
        # screen.blit(surface1, 50,50)
        pygame.draw.circle(screen, self.color, (self.X, self.Y), 5)
