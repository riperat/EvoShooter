import random

import pygame

import sys

from Collision import Collision
from Enemy import Enemy
from Player import Player
from Projectile import Projectile

flagX = True
flagY = True

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

pygame.mouse.set_visible(0)
icon = pygame.image.load("img/rocket.png")
pygame.display.set_caption('Evo Shooter')
pygame.display.set_icon(icon)

player = Player(300, 80)

run = True

frameLimiter = 0
enemies = []
bullets = []
stars = []


def star_spawn():
    global frameLimiter
    shoot = frameLimiter % 160
    # if frameLimiter == 159:
    #     stars.pop(0)
    # if shoot == 0:
    #     stars.append(
    #         Stars(random.randrange(800), random.randrange(800)))


def redrawGameWindow():
    # UPDATE
    screen.fill((41, 40, 38))

    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    # Draw entity's
    player.draw(screen)

    pygame.display.update()


def enemy_event_handler():
    # Enemy event checker
    for enemy in enemies:
        for bullet in bullets:
            if Collision.bullet_hit_check(enemy, bullet):
                enemies.pop(enemies.index(enemy))
                bullets.pop(bullets.index(bullet))
                break

        Collision.border_colission_check(enemy)
        enemy.sine_swing_motion()
    Enemy.border_pop(enemies)

black = (0, 0, 0)
white = (255, 255, 255)
star_pixels = [(320, 230), (310, 240), (320, 250), (330, 240), (320, 250)]


while run:

    clock.tick(160)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    Enemy.enemy_spawn(enemies)
    star_spawn()
    # Player movement
    frameLimiter = (frameLimiter + 1) % 160

    player.X += ((keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 1)
    player.Y += ((keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 1)

    for pixel in star_pixels:
        pygame.draw.rect(screen, white, (pixel[0], pixel[1], 10, 10), 0)

    # Collision check
    Collision.border_colission_check(player)
    Projectile.bullet_spawn(bullets, frameLimiter, player)

    enemy_event_handler()

    redrawGameWindow()

pygame.quit()
exit()
