import math

import pygame
import random


class Enemy:

    def __init__(self, health, shootSpead, X, Y, vel):
        self.health = health
        self.shootSpead = shootSpead
        self.X = X
        self.Y = Y
        self.sizeX = 10
        self.color = (255, 0, 3)
        self.flagX = True
        self.flagY = Y
        self.vel = vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.X, self.Y), self.sizeX)

    def sine_swing_motion(self):

        if self.X >= 760:
            self.flagX = False
        if self.X <= 0:
            self.flagX = True

        # Movement
        if self.flagX:
            self.X += 1
        else:
            self.X -= 1

        self.Y = int(math.sin(self.X / self.vel) * 102 + self.flagY)
        self.flagY += 1
    def border_pop(enemies):
        for enemy in enemies:
            if enemy.Y > 800 or enemy.Y < 0:
                enemies.pop(enemies.index(enemy))
    def enemy_spawn(enemies):
        if len(enemies) < 10:
            enemies.append(
                Enemy(300, 300, random.randint(0, 500), random.randint(0, 500), random.randint(60, 150)))
