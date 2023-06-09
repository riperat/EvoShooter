import random

import pygame

import sys

from screen import Menus
from Collision import Collision
from entities.Enemy import Enemy
from entities.Player import Player
from entities.Projectile import Projectile

# screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
FPS = 160
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mouse.set_visible(0)
icon = pygame.image.load("img/rocket.png")
pygame.display.set_caption('Evo Shooter')
pygame.display.set_icon(icon)

flagX = True
flagY = True
started_game = True
pause = False

time_elapsed_since_last_action = 0
total_play_time = 0
clock = pygame.time.Clock()
frameLimiter = 0
# Initial Player settings
player_health = 10
player_shoot_speed = 30
player_dmg = 10

player = Player(player_health, player_shoot_speed, player_dmg)
enemies = []
playerBullets = []
enemyBullets = []
stars = []
black = (0, 0, 0)
white = (255, 255, 255)

black = (0, 0, 0)
white = (255, 255, 255)

enemy_direction = lambda x: 0 if x == 0 else SCREEN_WIDTH if x == 1 else None


def restart_game():
    global flagX, flagY, started_game, pause, clock, frameLimiter, player, enemies, playerBullets, enemyBullets, total_play_time
    flagX = True
    flagY = True
    started_game = True
    pause = False

    frameLimiter = 0
    total_play_time = 0
    player = Player(player_health, player_shoot_speed, player_dmg)

    enemies = []
    playerBullets = []
    enemyBullets = []


def spawn_difficulty_tracker():
    global time_elapsed_since_last_action
    if time_elapsed_since_last_action > 900:
        Enemy.enemy_spawn(enemies, 60, 10)
        time_elapsed_since_last_action = 0


def redraw_game_window():
    # UPDATE
    screen.fill((41, 40, 38))

    for bullet in playerBullets:
        bullet.draw(screen)
    for bullet in enemyBullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    # Draw entity's
    player.draw(screen)

    pygame.display.update()


def enemy_event_handler():
    # Enemy event checker
    for enemy in enemies:
        if (Collision.player_hit_check(enemy, player)):
            player.damage_player(enemy.dmg)
            enemies.pop(enemies.index(enemy))
        for bullet in playerBullets:
            if Collision.bullet_hit_check(enemy, bullet):
                enemy.take_damage(player.dmg)
                if enemy.health <= 0:
                    enemies.pop(enemies.index(enemy))
                    player.score += enemy.score
                playerBullets.pop(playerBullets.index(bullet))
                break
        for bullet in enemyBullets:
            if Collision.bullet_hit_check(player, bullet):
                player.damage_player(enemy.dmg)
                enemyBullets.pop(enemyBullets.index(bullet))
                break

        if (random.randint(0, 1)):
            Projectile.bullet_spawn(enemyBullets, frameLimiter, enemy, 1)
        enemy.movement_method()
    Enemy.border_pop(enemies)


def start_engine():
    global started_game, time_elapsed_since_last_action, pause, frameLimiter, total_play_time
    redraw_game_window()
    while started_game:
        dt = clock.tick(FPS)
        total_play_time += dt
        time_elapsed_since_last_action += dt
        keys = pygame.key.get_pressed()
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_r:
                    started_game = not started_game
        if pause:
            Menus.event_happener(Menus.pause_menu(screen))
            pause = not pause

        if player.health <= 0:
            started_game = Menus.event_happener(Menus.death_menu(screen))

        if started_game == 0:
            break
        # player movement
        frameLimiter = (frameLimiter + 1) % FPS

        player.X += ((keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 1)
        player.Y += ((keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 1)

        # Collision check
        Collision.border_colission_check(player, 1, 1)
        Projectile.bullet_spawn(playerBullets, frameLimiter, player, -1)
        spawn_difficulty_tracker()
        enemy_event_handler()
        redraw_game_window()
    print(total_play_time // 1000)
    restart_game()
