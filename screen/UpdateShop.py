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
button_width = 160
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

# Render butons
speed_label = font.render(speed_text, True, WHITE)
attack_label = font.render(attack_text, True, WHITE)
health_label = font.render(health_text, True, WHITE)
body_label = font.render(body_text, True, WHITE)


def shop_menu(screen, playerEntity):
    global speed_label, attack_label, health_label, body_label
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if buttons are clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if button_x <= mouse_x <= button_x + button_width:
                    if button_y <= mouse_y <= button_y + button_height and len(speed_rects) < 7:
                        if len(speed_rects) == 6:
                            speed_label = font.render("Sold out", True, WHITE)
                        rect_x = button_x + len(speed_rects) * (rect_spacing + 10)
                        speed_rects.append(pygame.Rect(rect_x, button_y - 10, 10, 10))
                        playerEntity.shootSpead -= 10

                    if button_y + 70 <= mouse_y <= button_y + 70 + button_height and len(attack_rects) < 7:
                        if len(attack_rects) == 6:
                            attack_label = font.render("Sold out", True, WHITE)
                        rect_x = button_x + len(attack_rects) * (rect_spacing + 10)
                        attack_rects.append(pygame.Rect(rect_x, button_y + 70 - 10, 10, 10))
                        playerEntity.dmg += 10

                    if button_y + 140 <= mouse_y <= button_y + 140 + button_height and len(health_rects) < 7:
                        if len(health_rects) == 6:
                            health_label = font.render("Sold out", True, WHITE)
                        rect_x = button_x + len(health_rects) * (rect_spacing + 10)
                        health_rects.append(pygame.Rect(rect_x, button_y + 140 - 10, 10, 10))
                        playerEntity.health += 10

                    if button_y + 210 <= mouse_y <= button_y + 210 + button_height and len(body_rects) < 7:
                        if len(body_rects) == 6:
                            body_label = font.render("Sold out", True, WHITE)
                        rect_x = button_x + len(body_rects) * (rect_spacing + 10)
                        body_rects.append(pygame.Rect(rect_x, button_y + 210 - 10, 10, 10))

        draw(screen)


def draw(screen):
    pygame.draw.rect(screen, GRAY, (button_x, button_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button_x, button_y + 70, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button_x, button_y + 140, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button_x, button_y + 210, button_width, button_height))

    [pygame.draw.rect(screen, GREEN, rect) for rect in attack_rects]
    [pygame.draw.rect(screen, GREEN, rect) for rect in health_rects]
    [pygame.draw.rect(screen, GREEN, rect) for rect in body_rects]
    [pygame.draw.rect(screen, GREEN, rect) for rect in speed_rects]

    # Draw button labels
    screen.blit(speed_label, (button_x + 10, button_y + 10))
    screen.blit(attack_label, (button_x + 10, button_y + 80))
    screen.blit(health_label, (button_x + 10, button_y + 150))
    screen.blit(body_label, (button_x + 10, button_y + 220))

    pygame.display.update()
