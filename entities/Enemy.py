import math

import pygame
import random


class Enemy:
    sizeX = 10
    flagX = True
    flagY = 0

    def __init__(self, X, Y, vel, health, shoot_speed, dmg, coins):
        self.max_health = health
        self.health = health
        self.shootSpead = shoot_speed
        self.X = X
        self.Y = Y
        self.dmg = dmg
        self.vel = vel
        self.color = pygame.Color(255, 0, 3)
        self.movement_method = self.choose_movement_method()
        self.body = None
        self.coins = coins

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.X, self.Y), self.sizeX)
        self.body = self.get_rect()

    def get_rect(self):
        rect_width = self.sizeX * 2
        rect_height = self.sizeX * 2
        rect_x = self.X - self.sizeX
        rect_y = self.Y - self.sizeX
        return pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    def sine_swing_motion(self):
        if self.X >= 800:
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

    def moon_swing_motion(self):

        if self.X >= 800:
            self.flagX = False
        if self.X <= 0:
            self.flagX = True

        # Movement
        if self.flagX:
            self.X += 1
        else:
            self.X -= 1

        self.Y += (self.vel % 10) + 1

    def border_pop(enemies):
        for enemy in enemies:
            if enemy.Y >= 800:
                enemy.Y = 0
                enemy.flagY = 0

    def choose_movement_method(self):
        # Randomly choose between method 1 and method 2 during initialization
        if random.randint(0, 1) == 0:
            print("sine")
            return self.sine_swing_motion
        else:
            print("moon")
            return self.moon_swing_motion

    def movement_method(self):
        # Call the chosen movement method
        self.movement_method()

    def take_damage(self, dmg):
        self.health -= dmg
        self.color.r -= max(int(self.color.r * 0.2), 0)

    def enemy_spawn(enemies, vel, enemiesOnScreen):
        enemy_direction = lambda x: 0 if x == 0 else 800 if x == 1 else None

        if len(enemies) < enemiesOnScreen:
            enemies.append(
                Enemy(enemy_direction(random.randint(0, 1)), random.randint(0, 500), vel, 50, 300, 10, 10))
