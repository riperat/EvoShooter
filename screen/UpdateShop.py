import pygame

pygame.font.init()
white = (255, 255, 255)
inside_pause_menu = False
inside_death_menu = False
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)

font = pygame.font.Font("fonts/Grand9K Pixel.ttf", 20)
# Button Texts
speed_text = "Shoot Speed"
attack_text = "Attack"
health_text = "Health"
body_text = "Body"
# Button dimensions
button_width = 200
button_height = 40

# Button positions
button_x = 50
button_y = 100

speed_clicks = 0
attack_clicks = 0
health_clicks = 0
body_clicks = 0

# Clicked rectangles
speed_rects = []
attack_rects = []
health_rects = []
body_rects = []

rect_spacing = 6
cost_per_level = [10, 30, 80, 100, 150, 220, 360, "Sold out"]
cost_per_body = [250, 600, "Sold out"]


def shop_menu(screen, player):
    global speed_label, attack_label, health_label, body_label
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    screen.fill((41, 40, 38))
                    return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if buttons are clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if button_x <= mouse_x <= button_x + button_width:
                    if button_y <= mouse_y <= button_y + button_height and len(
                            speed_rects) < 7 and player.coins >= cost_per_level[len(speed_rects)]:
                        player.shootSpead -= 10
                        player.coins -= cost_per_level[len(speed_rects)]

                        rect_x = button_x + len(speed_rects) * (rect_spacing + 10)
                        speed_rects.append(pygame.Rect(rect_x, button_y - 10, 10, 10))

                    if button_y + 70 <= mouse_y <= button_y + 70 + button_height and len(
                            attack_rects) < 7 and player.coins >= cost_per_level[len(attack_rects)]:
                        player.dmg += 10
                        player.coins -= cost_per_level[len(attack_rects)]

                        rect_x = button_x + len(attack_rects) * (rect_spacing + 10)
                        attack_rects.append(pygame.Rect(rect_x, button_y + 70 - 10, 10, 10))

                    if button_y + 140 <= mouse_y <= button_y + 140 + button_height \
                            and len(health_rects) < 7 \
                            and player.coins >= cost_per_level[len(health_rects)]:
                        player.health += 10
                        player.coins -= cost_per_level[len(health_rects)]

                        rect_x = button_x + len(health_rects) * (rect_spacing + 10)
                        health_rects.append(pygame.Rect(rect_x, button_y + 140 - 10, 10, 10))

                    if button_y + 210 <= mouse_y <= button_y + 210 + button_height \
                            and len(body_rects) < 2 \
                            and player.coins >= cost_per_level[len(body_rects)]:
                        player.coins -= cost_per_body[len(body_rects)]
                        rect_x = button_x + len(body_rects) * (rect_spacing + 10)
                        body_rects.append(pygame.Rect(rect_x, button_y + 210 - 10, 10, 10))
                        if len(body_rects) == 1:
                            player.tower_one = True
                        if len(body_rects) == 2:
                            player.tower_two = True

        draw(screen, player)


def draw(screen, player):
    screen.fill((41, 40, 38))
    pygame.draw.rect(screen, GRAY, (button_x, button_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button_x, button_y + 70, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button_x, button_y + 140, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button_x, button_y + 210, button_width, button_height))

    [pygame.draw.rect(screen, GREEN, rect) for rect in attack_rects]
    [pygame.draw.rect(screen, GREEN, rect) for rect in health_rects]
    [pygame.draw.rect(screen, GREEN, rect) for rect in body_rects]
    [pygame.draw.rect(screen, GREEN, rect) for rect in speed_rects]

    # Render butons
    speed_label = font.render(speed_text + " : " + str(cost_per_level[len(speed_rects)]), True, WHITE)
    attack_label = font.render(attack_text + " : " + str(cost_per_level[len(attack_rects)]), True, WHITE)
    health_label = font.render(health_text + " : " + str(cost_per_level[len(health_rects)]), True, WHITE)
    body_label = font.render(body_text + " : " + str(cost_per_body[len(body_rects)]), True, WHITE)

    # Draw button labels
    screen.blit(speed_label, (button_x + 10, button_y + 10))
    screen.blit(attack_label, (button_x + 10, button_y + 80))
    screen.blit(health_label, (button_x + 10, button_y + 150))
    screen.blit(body_label, (button_x + 10, button_y + 220))

    player.draw(screen)
    pygame.display.update()
