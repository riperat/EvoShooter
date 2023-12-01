from entities.Enemy import Enemy
from screen import UpdateShop
import pygame

font = pygame.font.Font("fonts/Grand9K Pixel.ttf", 20)

level_time = [10, 30, 50, 300, 3000]

current_level = 0


def reset():
    global current_level
    current_level = 0

def level_finished_check(total_play_time, screen, player):
    global current_level
    if total_play_time // 1000 >= level_time[current_level]:
        UpdateShop.shop_menu(screen, player)
        current_level += 1
        return True


def draw_time_left(total_play_time, screen):
    time_left_text = font.render("Time left: " + str(level_time[current_level] - (total_play_time // 1000)), True, (255, 255, 255))
    time_left_rect = time_left_text.get_rect()
    time_left_rect.center = (400, 20)
    screen.blit(time_left_text, time_left_rect)


def boss_lvl(screen, player):
    UpdateShop.shop_menu(screen, player)
    # TODO add boss level
