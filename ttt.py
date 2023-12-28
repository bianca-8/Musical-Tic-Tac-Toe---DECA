import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
BUTTON_COLOR = (200, 200, 200)
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 40

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Fonts
font = pygame.font.SysFont(None, 40)

# Game state
BLANK_STATE = 'blank_state'

# Initial game state
game_state = BLANK_STATE

# Variable to control player turns
can_make_move = False

# Function to display buttons for symbol choice
def draw_blank_state():
    screen.fill((255, 255, 255))

    # Display options for the player
    text = font.render("Was your move correct?", True, LINE_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(text, text_rect)

    yes_button_rect = pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 4 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT))
    yes_text = font.render('Yes', True, LINE_COLOR)
    yes_text_rect = yes_text.get_rect(center=yes_button_rect.center)
    screen.blit(yes_text, yes_text_rect)

    no_button_rect = pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 4 * 3 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT))
    no_text = font.render('No', True, LINE_COLOR)
    no_text_rect = no_text.get_rect(center=no_button_rect.center)
    screen.blit(no_text, no_text_rect)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if game_state == BLANK_STATE:
                yes_button_rect = pygame.Rect(WIDTH // 4 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
                no_button_rect = pygame.Rect(WIDTH // 4 * 3 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

                if yes_button_rect.collidepoint(event.pos):
                    can_make_move = True
                    game_state = 'playing'
                elif no_button_rect.collidepoint(event.pos):
                    can_make_move = False
                    game_state = 'losing'

    if game_state == BLANK_STATE:
        draw_blank_state()
        print("can_make_move:", can_make_move)  # Add this line to print the value

    pygame.display.flip()
