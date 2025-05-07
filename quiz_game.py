import pygame
import json
import random

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
title_font = pygame.font.Font("graphics/font.ttf", 34)
button_font = pygame.font.Font("graphics/font.ttf", 26)
quiz_font = pygame.font.Font("graphics/font.ttf", 10)

    # Button
start_button = pygame.Rect(300, 280, 200, 60)
exit_button = pygame.Rect(300, 380, 200, 60)

choice_buttons = {
    "A": pygame.Rect(100, 180, 60, 60),
    "B": pygame.Rect(100, 260, 60, 60),
    "C": pygame.Rect(100, 340, 60, 60),
    "D": pygame.Rect(100, 420, 60, 60)
    }

# Load random questions (10 items)
with open("questions.json") as f:
    questions = json.load(f)

# Functions
def draw_home_screen():
    screen.blit(background_img, (0, 0))
    title_text = title_font.render("Welcome to Quiz Game!", True, color_yellowbrown)
    title_rect = title_text.get_rect(center=(width // 2, 150))
    screen.blit(title_text, title_rect)

    pygame.draw.rect(screen, color_green, start_button)
    pygame.draw.rect(screen, color_green, exit_button)

    start_text = button_font.render("START", True, color_white)
    exit_text = button_font.render("EXIT", True, color_white)

    screen.blit(start_text, (start_button.x + 40, start_button.y + 17))
    screen.blit(exit_text, (exit_button.x + 48, exit_button.y + 17))

def draw_quiz_screen():
    # question
    screen.blit(quiz_background, (0, 0))
    if current_question:
        question_text = quiz_font.render(current_question["question"], True, color_white)
        screen.blit(question_text, (100, 100))

        # choices
        for key, rect in choice_buttons.items():
            pygame.draw.rect(screen, color_yellowbrown, rect)
            label = button_font.render(key, True, color_white)
            screen.blit(label, (rect.x + 17, rect.y + 17))

            choice_text = quiz_font.render(current_question["choices"][key], True, color_white)
            screen.blit(choice_text, (rect.x + 80, rect.y + 15))  

    if feedback_text:
        feedback = quiz_font.render(feedback_text, True, color_white)
        screen.blit(feedback, (100, 500))

home_screen = True
running = True
feedback_text = ""
next_question = False
used_questions = []

while running:
    if home_screen:
        draw_home_screen()
    else:
        draw_quiz_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if home_screen:
                if start_button.collidepoint(event.pos):
                    home_screen = False
                    current_question = random.choice(questions) 
                    used_questions.append(current_question)      
                elif exit_button.collidepoint(event.pos):
                    running = False 

            elif next_question:
                feedback_text = ""
                next_question = False
                used_questions = []

                if len(used_questions) == 10:
                    current_question = None
                    home_screen = True

                else:
                    while True:
                        next_q = random.choice(questions)
                        if next_q not in used_questions:
                            current_question = next_q
                            used_questions.append(current_question)
                            break
                        
            else:
                for key, rect in choice_buttons.items():
                    if rect.collidepoint(event.pos):
                        if key == current_question["answer"]:
                            feedback_text = "Correct!"
                        else:
                            correct_key = current_question["answer"]
                            feedback_text = f"Incorrect! Correct answer is: {correct_key}"
                        next_question = True
                        break

# Check answer
    # if correct, show correct!
    # if not correct, show the correct answer

    pygame.display.flip()

# show score
# ask if try again

# close if done
pygame.quit()
