import pygame


class Projectile:

    def __init__(self, x, y, vel):
        bullets = []
        self.X = x
        self.Y = y
        self.sizeX = 3
        self.sizeY = 15
        self.color = (223, 235, 9)
        self.vel = vel
        self.body = None

    def draw(self, screen):
        s = pygame.Surface((self.sizeX * 2, self.sizeY * 2))  # the size of your rect
        s.set_alpha(20)  # alpha level
        s.fill((255, 255, 255))  # this fills the entire surface
        screen.blit(s, (self.X - (self.sizeX / 2), self.Y - (self.sizeY / 2)))
        self.body = pygame.Rect(self.X, self.Y, self.sizeX, self.sizeY)
        pygame.draw.rect(screen, self.color, self.body)

    def bullet_spawn(bullets, frameLimiter, shooter, vel):

        shoot = frameLimiter % shooter.shootSpead
        for bullet in bullets:
            # Handle spawning
            if bullet.Y < 800 and bullet.Y > 0:
                bullet.Y += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        if shoot == 0:
            bullets.append(
                Projectile(shooter.X + 20, shooter.Y, vel))
