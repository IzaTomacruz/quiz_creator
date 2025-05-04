import pygame

# Setup the GUI
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quiz Game")

    #Colors
color_white = (255, 255, 255)
color_green = (36, 115, 57)
color_yellowbrown = (213, 167, 40)

    # Backgrounds
background_img = pygame.image.load("graphics/background1.jpg")
background_img = pygame.transform.scale(background_img, (width, height))

quiz_background = pygame.image.load("graphics/background2.jpg")  
quiz_background = pygame.transform.scale(quiz_background, (width, height))

    # Fonts
title_font= pygame.font.Font("graphics/font.ttf", 34)
button_font= pygame.font.Font("graphics/font.ttf", 26)

    # Button
start_button = pygame.Rect(300, 280, 200, 60)
exit_button = pygame.Rect(300, 380, 200, 60)

home_screen = True
running = True
while running:
    if home_screen:
        screen.blit(background_img, (0, 0))
    else:
        screen.blit(quiz_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                home_screen = False       
            elif exit_button.collidepoint(event.pos):
                running = False 

    if home_screen:
        title_text = title_font.render("Welcome to Quiz Game!", True, color_yellowbrown)
        title_rect = title_text.get_rect(center=(width // 2, 150))
        screen.blit(title_text, title_rect)

        pygame.draw.rect(screen, color_green, start_button)
        pygame.draw.rect(screen, color_green, exit_button)

        start_text = button_font.render("START", True, color_white)
        exit_text = button_font.render("EXIT", True, color_white)

        screen.blit(start_text, (start_button.x + 40, start_button.y + 17))
        screen.blit(exit_text, (exit_button.x + 48, exit_button.y + 17))

    pygame.display.flip()

# Check answer
    # if correct, show correct!
    # if not correct, show the correct answer
# show score
# ask if try again

# close if done
pygame.quit()
