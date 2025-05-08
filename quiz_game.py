import pygame
import json
import random
import textwrap

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
quiz_font = pygame.font.Font("graphics/font.ttf", 13)

    # Button
start_button = pygame.Rect(300, 280, 200, 60)
exit_button = pygame.Rect(300, 380, 200, 60)

choice_buttons = {
    "A": pygame.Rect(100, 180, 60, 60),
    "B": pygame.Rect(100, 260, 60, 60),
    "C": pygame.Rect(100, 340, 60, 60),
    "D": pygame.Rect(100, 420, 60, 60)
    }

play_again_button = pygame.Rect(220, 280, 350, 60)
back_menu_button = pygame.Rect(245, 380, 300, 60)

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
        question_text = current_question["question"]
        wrapped_lines = textwrap.wrap(question_text, width=45)  
        question_y = 100 

        for line in wrapped_lines:
            question = quiz_font.render(line, True, color_white)
            screen.blit(question, (100, question_y))
            question_y += 25
        # choices
        for key, rect in choice_buttons.items():
            pygame.draw.rect(screen, color_yellowbrown, rect)
            label = button_font.render(key, True, color_white)
            screen.blit(label, (rect.x + 17, rect.y + 17))

            choice_text = current_question["choices"][key]
            wrapped_choice_lines = textwrap.wrap(choice_text, width=40)
            choice_y = rect.y + 5

            for line in wrapped_choice_lines:
                choice_line = quiz_font.render(line, True, color_white)
                screen.blit(choice_line, (rect.x + 80, choice_y))  
                choice_y += 24

    if feedback_text:
        feedback = quiz_font.render(feedback_text, True, color_white)
        screen.blit(feedback, (100, 500))

# show score
def draw_score_screen():
    screen.blit(background_img, (0, 0))
    title_text = title_font.render(f"Your score is {score}/10", True, color_yellowbrown)
    title_rect = title_text.get_rect(center=(width // 2, 150))
    screen.blit(title_text, title_rect)

    pygame.draw.rect(screen, color_green, play_again_button)
    pygame.draw.rect(screen, color_green, back_menu_button)

    again_text = button_font.render("PLAY AGAIN", True, color_white)
    menu_text = button_font.render("MAIN MENU", True, color_white)

    screen.blit(again_text, (play_again_button.x + 47, play_again_button.y + 17))
    screen.blit(menu_text, (back_menu_button.x + 37, back_menu_button.y + 17))

home_screen = True
quiz_screen = False
score_screen = False
running = True
feedback_text = ""
next_question = False
used_questions = []
score = 0

while running:
    if home_screen:
        draw_home_screen()
    elif quiz_screen:
        draw_quiz_screen()
    elif score_screen:
        draw_score_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if home_screen:
                if start_button.collidepoint(event.pos):
                    home_screen = False
                    quiz_screen = True
                    current_question = random.choice(questions) 
                    used_questions.append(current_question)      
                elif exit_button.collidepoint(event.pos):
                    running = False 
# ask if try again
            elif score_screen:
                    if play_again_button.collidepoint(event.pos):
                        used_questions = []
                        score = 0
                        feedback_text = ""
                        next_question = False
                        score_screen = False
                        quiz_screen = True
                        current_question = random.choice(questions)
                        used_questions.append(current_question)
                    elif back_menu_button.collidepoint(event.pos):
                        # Return to main menu
                        used_questions = []
                        score = 0
                        feedback_text = ""
                        next_question = False
                        score_screen = False
                        home_screen = True

            elif next_question:
                feedback_text = ""
                next_question = False

                if len(used_questions) == 10:
                    quiz_screen = False
                    score_screen = True
                else:
                    while True:
                        next_q = random.choice(questions)
                        if next_q not in used_questions:
                            current_question = next_q
                            used_questions.append(current_question)
                            break
# Check answer
            else:
                for key, rect in choice_buttons.items():
                    if rect.collidepoint(event.pos):
                        # if correct, show correct!
                        if key == current_question["answer"]:
                            feedback_text = "Correct!"
                            score += 1
                        # if not correct, show the correct answer
                        else:
                            correct_key = current_question["answer"]
                            feedback_text = f"Incorrect! Correct answer is: {correct_key}"
                        next_question = True
                        break

    pygame.display.flip()

# close if done
pygame.quit()
