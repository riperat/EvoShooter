import pygame


class Player:
    X = 360
    Y = 400
    sizeX = 40
    sizeY = 40
    tower_one = False
    tower_two = False
    font = pygame.font.Font("fonts/Grand9K Pixel.ttf", 20)

    def __init__(self, health, shootSpead, dmg):
        self.body = pygame.Rect(self.X, self.Y, self.sizeX, self.sizeY)
        self.health = health
        self.shootSpead = shootSpead
        self.dmg = dmg
        self.color = pygame.Color(0, 168, 133)
        self.coins = 10000

    def draw(self, screen):
        self.body = pygame.Rect(self.X, self.Y, self.sizeX, self.sizeY)
        pygame.draw.rect(screen, self.color, self.body)
        self.HUD(screen)

    def damage_player(self, dmg):
        self.health -= dmg
        self.color.g -= max(int(self.color.g * 0.2), 0)
        self.color.b -= max(int(self.color.b * 0.2), 0)

    def HUD(self, screen):
        health_text = self.font.render("Health: " + str(self.health), True, (255, 255, 255))
        health_Rect = health_text.get_rect()
        health_Rect.center = (60, 20)
        screen.blit(health_text, health_Rect)

        coins_text = self.font.render("Coins: " + str(self.coins), True, (255, 255, 255))
        coins_rect = health_text.get_rect()
        coins_rect.center = (740, 20)
        screen.blit(coins_text, coins_rect)

    def move_X(self, keys):
        self.X += ((keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 1)
        self.Y += ((keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 1)