import pygame


class Player:

    def __init__(self, health, shootSpead):
        self.health = health
        self.shootSpead = shootSpead
        self.X = 300
        self.Y = 300
        self.sizeX = 40
        self.sizeY = 40
        self.color = (27, 168, 133)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.X, self.Y, self.sizeX, self.sizeY))
