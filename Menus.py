import pygame

import sys

pygame.font.init()
green = (255, 255, 255)
inside_pause_menu = False
inside_death_menu = False

# Define the rectangle properties
rectangle_pos = pygame.Rect(300, 200, 200, 100)
rectangle_color = pygame.Color(27, 168, 133)
width, height = 800, 600

# Define the button properties
button_width, button_height = 200, 50
button_color = pygame.Color(100, 100, 100)
button_font = pygame.font.Font(None, 30)
bottom_button_rect = pygame.Rect(width // 2 - button_width // 2,
                                 height // 2 - button_height // 2 + 100, button_width,
                                 button_height)

top_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 - button_height // 2,
                              button_width, button_height)

game_over_font = pygame.font.Font(None, 100)
game_over_text = game_over_font.render('Game Over', True, green)

game_over_Rect = game_over_text.get_rect()

# set the center of the rectangular object.
game_over_Rect.center = (width // 2, height // 2)


def event_happener(method_to_run):
    global inside_pause_menu
    global inside_death_menu
    while True:
        method_to_run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if inside_death_menu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if bottom_button_rect.collidepoint(mouse_pos):
                        inside_death_menu = not inside_death_menu
                        return False
            if inside_pause_menu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        inside_pause_menu = not inside_pause_menu
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if bottom_button_rect.collidepoint(mouse_pos):
                        sys.exit()
                    if top_button_rect.collidepoint(mouse_pos):
                        inside_pause_menu = not inside_pause_menu
                        return

        pygame.display.update()


def pause_menu(screen):
    global inside_pause_menu
    inside_pause_menu = not inside_pause_menu
    pygame.draw.rect(screen, button_color, bottom_button_rect)
    pygame.draw.rect(screen, button_color, top_button_rect)

    quit_button_text = button_font.render("Quit", True, (255, 255, 255))

    screen.blit(quit_button_text, (bottom_button_rect.centerx - quit_button_text.get_width() // 2,
                                   bottom_button_rect.centery - quit_button_text.get_height() // 2))

    resume_button_text = button_font.render("Resume", True, (255, 255, 255))

    screen.blit(resume_button_text, (top_button_rect.centerx - resume_button_text.get_width() // 2,
                                     top_button_rect.centery - resume_button_text.get_height() // 2))


def death_menu(screen):
    global inside_death_menu
    inside_death_menu = not inside_death_menu

    screen.blit(game_over_text, game_over_Rect)
    pygame.draw.rect(screen, button_color, bottom_button_rect)

    new_game_button_text = button_font.render("New Run", True, (255, 255, 255))

    screen.blit(new_game_button_text, (bottom_button_rect.centerx - new_game_button_text.get_width() // 2,
                                       bottom_button_rect.centery - new_game_button_text.get_height() // 2))
