import pygame

from Collision import Collision


class Projectile:

    def __init__(self, x, y):
        bullets = []
        self.X = x
        self.Y = y
        self.sizeX = 3
        self.sizeY = 15
        self.color = (223, 235, 9)
        self.vel = -1

    def draw(self, screen):
        s = pygame.Surface((self.sizeX * 2, self.sizeY * 2))  # the size of your rect
        s.set_alpha(20)  # alpha level
        s.fill((255, 255, 255))  # this fills the entire surface
        screen.blit(s, (self.X - (self.sizeX / 2), self.Y - (self.sizeY / 2)))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.X, self.Y, self.sizeX, self.sizeY))

    def bullet_spawn(bullets, frameLimiter, shooter):

        shoot = frameLimiter % shooter.shootSpead
        for bullet in bullets:
            # Handle collision


            # Handle spawning
            if bullet.Y < 800 and bullet.Y > 0:
                bullet.Y += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        if shoot == 0:
            bullets.append(
                Projectile(shooter.X + 20, shooter.Y))
