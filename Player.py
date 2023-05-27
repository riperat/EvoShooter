import pygame


class Player:
    X = 360
    Y = 400
    sizeX = 40
    sizeY = 40
    color = pygame.Color(0, 168, 133)
    def __init__(self, health, shootSpead, dmg):
        self.body = None
        self.health = health
        self.shootSpead = shootSpead
        self.dmg = dmg

    def draw(self, screen):
        self.body = pygame.Rect(self.X, self.Y, self.sizeX, self.sizeY)
        pygame.draw.rect(screen, self.color, self.body)
