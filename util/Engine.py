import importlib
import random

import pygame

import sys

from screen import Menus, UpdateShop
from entities.Enemy import Enemy
from entities.Player import Player
from entities.Projectile import Projectile
from util import LevelSelect
from util.Collision import Collision

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

shooting_enemies = False

# Initial Player settings
player_health = 30
player_shoot_speed = 100
player_dmg = 10

player = Player(player_health, player_shoot_speed, player_dmg)

tower_one = Player(player_health, player_shoot_speed, player_dmg)
tower_one.sizeX = 20
tower_one.sizeY = 20
tower_one.X = 330
tower_two = Player(player_health, player_shoot_speed, player_dmg)
tower_two.X = 410
tower_two.sizeX = 20
tower_two.sizeY = 20

enemies = []
playerBullets = []
tower_one_Bullets = []
tower_two_Bullets = []
enemyBullets = []

black = (0, 0, 0)
white = (255, 255, 255)

enemy_direction = lambda x: 0 if x == 0 else SCREEN_WIDTH if x == 1 else None


def restart_game():
    global flagX, flagY, started_game, pause, clock, frameLimiter, player, enemies, playerBullets, enemyBullets, \
        total_play_time, player_dmg, player_shoot_speed, player_health, tower_one, tower_two, clock

    module = importlib.import_module("screen.UpdateShop")
    importlib.reload(module)
    clock = pygame.time.Clock()
    total_play_time = 0

    flagX = True
    flagY = True
    started_game = True
    pause = False

    frameLimiter = 0
    player = Player(player_health, player_shoot_speed, player_dmg)

    tower_one = Player(player_health, player_shoot_speed, player_dmg)
    tower_one.sizeX = 20
    tower_one.sizeY = 20
    tower_one.X = 330
    tower_two = Player(player_health, player_shoot_speed, player_dmg)
    tower_two.X = 410
    tower_two.sizeX = 20
    tower_two.sizeY = 20

    enemies = []
    playerBullets = []
    enemyBullets = []
    LevelSelect.reset()


def level_Reset():
    global enemies, playerBullets, enemyBullets
    enemies = []
    playerBullets = []
    enemyBullets = []


def redraw_game_window():
    # UPDATE
    screen.fill((41, 40, 38))

    for bullet in playerBullets:
        bullet.draw(screen)
    for bullet in tower_one_Bullets:
        bullet.draw(screen)
    for bullet in tower_two_Bullets:
        bullet.draw(screen)
    for bullet in enemyBullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    # Draw entity's
    if player.tower_one:
        tower_one.draw(screen)
    if player.tower_two:
        tower_two.draw(screen)

    player.draw(screen)

    LevelSelect.draw_time_left(total_play_time, screen)

    pygame.display.update()


def entity_hit(bullet_list, enemy):
    for bullet in bullet_list:
        if Collision.bullet_hit_check(enemy, bullet):
            enemy.take_damage(player.dmg)
            if enemy.health <= 0:
                enemies.pop(enemies.index(enemy))
                player.coins += enemy.coins
            bullet_list.pop(bullet_list.index(bullet))
            break


def enemy_event_handler():
    # Enemy event checker
    for enemy in enemies:
        try:
            if player.tower_one and Collision.player_hit_check(enemy, tower_one):
                player.damage_player(enemy.dmg)
                enemies.pop(enemies.index(enemy))
            if player.tower_two and Collision.player_hit_check(enemy, tower_two):
                player.damage_player(enemy.dmg)
                enemies.pop(enemies.index(enemy))
            if Collision.player_hit_check(enemy, player):
                player.damage_player(enemy.dmg)
                enemies.pop(enemies.index(enemy))
        except:
            print("None existing enemy")
        entity_hit(playerBullets, enemy)
        entity_hit(tower_one_Bullets, enemy)
        entity_hit(tower_two_Bullets, enemy)
        for bullet in enemyBullets:
            if Collision.bullet_hit_check(player, bullet):
                player.damage_player(enemy.dmg)
                enemyBullets.pop(enemyBullets.index(bullet))
                break
        if shooting_enemies:
            if random.randint(0, 1):
                Projectile.bullet_spawn(enemyBullets, frameLimiter, enemy, 1)
        enemy.movement_method()
    Enemy.border_pop(enemies)


def spawn_difficulty_tracker():
    global time_elapsed_since_last_action, total_play_time, clock
    if LevelSelect.level_finished_check(total_play_time, screen, player):
        clock = pygame.time.Clock()
        total_play_time = 0
    if time_elapsed_since_last_action > 900 - (LevelSelect.current_level * 100):
        Enemy.enemy_spawn(enemies, 60, 10 + (LevelSelect.current_level * 10))
        time_elapsed_since_last_action = 0


def start_engine():
    global started_game, time_elapsed_since_last_action, pause, frameLimiter, total_play_time
    redraw_game_window()
    while started_game:
        if started_game == 0:
            break
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

        frameLimiter = (frameLimiter + 1) % FPS

        # player movement
        player.move_X(keys)
        Collision.border_colission_check(player, 1, 1)

        # Bullet spawn
        Projectile.bullet_spawn(playerBullets, frameLimiter, player, -1)
        if player.tower_one:
            tower_one.move_X(keys)
            Collision.border_colission_check(tower_one, 1, 1)
            Projectile.bullet_spawn(tower_one_Bullets, frameLimiter, tower_one, -1)
        if player.tower_two:
            tower_two.move_X(keys)
            Collision.border_colission_check(tower_two, 1, 1)
            Projectile.bullet_spawn(tower_two_Bullets, frameLimiter, tower_two, -1)

        spawn_difficulty_tracker()
        enemy_event_handler()
        redraw_game_window()
    restart_game()
