import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
GRID_SIZE = 3
SQUARE_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
LINE_WIDTH = 15
BUTTON_COLOR = (200, 200, 200)
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 40

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Create the game board
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Fonts
font = pygame.font.SysFont(None, 40)

# Game states
SYMBOL_SELECTION = 'symbol_selection'
PLAYING = 'playing'
WINNER_SCREEN = 'winner_screen'
DRAW_SCREEN = 'draw_screen'
REPLAY_SCREEN = 'replay_screen'

# Initial game state
game_state = SYMBOL_SELECTION

# Player symbols
player1_symbol = ''
player2_symbol = ''
current_player = ''

# Function to draw the grid lines
def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw the X and O on the board
def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                draw_x(col, row)
            elif board[row][col] == 'O':
                draw_o(col, row)

# Function to draw X at a specific position
def draw_x(col, row):
    pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE),
                     ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE),
                     (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)

# Function to draw O at a specific position
def draw_o(col, row):
    pygame.draw.circle(screen, LINE_COLOR,
                       (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                       SQUARE_SIZE // 2, LINE_WIDTH)

# Function to check for a winner
def check_winner():
    # Check rows and columns
    for i in range(GRID_SIZE):
        if all(board[i][j] == 'X' for j in range(GRID_SIZE)) or all(board[j][i] == 'X' for j in range(GRID_SIZE)):
            return 'X'
        elif all(board[i][j] == 'O' for j in range(GRID_SIZE)) or all(board[j][i] == 'O' for j in range(GRID_SIZE)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(GRID_SIZE)) or all(board[i][GRID_SIZE - 1 - i] == 'X' for i in range(GRID_SIZE)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(GRID_SIZE)) or all(board[i][GRID_SIZE - 1 - i] == 'O' for i in range(GRID_SIZE)):
        return 'O'

    return None

# Function to check if the board is full
def is_board_full():
    return all(board[i][j] != '' for i in range(GRID_SIZE) for j in range(GRID_SIZE))

# Function to display the winning screen
def show_winning_screen(winner):
    screen.fill(WHITE)
    text = font.render(f'Player {winner} wins!', True, LINE_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    replay_button_rect = pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 50, BUTTON_WIDTH, BUTTON_HEIGHT))
    replay_text = font.render('Replay', True, LINE_COLOR)
    replay_text_rect = replay_text.get_rect(center=replay_button_rect.center)
    screen.blit(replay_text, replay_text_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if replay_button_rect.collidepoint(event.pos):
                    reset_game()
                    return

# Function to display the draw screen
def show_draw_screen():
    screen.fill(WHITE)
    text = font.render("It's a draw!", True, LINE_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    replay_button_rect = pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 50, BUTTON_WIDTH, BUTTON_HEIGHT))
    replay_text = font.render('Replay', True, LINE_COLOR)
    replay_text_rect = replay_text.get_rect(center=replay_button_rect.center)
    screen.blit(replay_text, replay_text_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if replay_button_rect.collidepoint(event.pos):
                    reset_game()
                    return

# Function to display buttons for symbol choice
def draw_symbol_buttons():
    x_button_rect = pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 4 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT))
    o_button_rect = pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 4 * 3 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT))

    x_text = font.render('X', True, LINE_COLOR)
    x_text_rect = x_text.get_rect(center=x_button_rect.center)
    screen.blit(x_text, x_text_rect)

    o_text = font.render('O', True, LINE_COLOR)
    o_text_rect = o_text.get_rect(center=o_button_rect.center)
    screen.blit(o_text, o_text_rect)

    return x_button_rect, o_button_rect

# Function to reset the game
def reset_game():
    global board, game_state, player1_symbol, player2_symbol, current_player
    board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    game_state = SYMBOL_SELECTION
    player1_symbol = ''
    player2_symbol = ''
    current_player = ''

# Main game loop
while True:
    screen.fill(WHITE)

    if game_state == SYMBOL_SELECTION:
        x_button_rect, o_button_rect = draw_symbol_buttons()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if x_button_rect.collidepoint(event.pos):
                    player1_symbol, player2_symbol = 'X', 'O'
                    current_player = player1_symbol
                    game_state = PLAYING
                elif o_button_rect.collidepoint(event.pos):
                    player1_symbol, player2_symbol = 'O', 'X'
                    current_player = player1_symbol
                    game_state = PLAYING

    elif game_state == PLAYING:
        draw_grid()
        draw_board()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE
                if board[row][col] == '':
                    board[row][col] = current_player
                    winner = check_winner()
                    if winner:
                        show_winning_screen(winner)
                        game_state = REPLAY_SCREEN
                    elif is_board_full():
                        show_draw_screen()
                        game_state = REPLAY_SCREEN
                    else:
                        current_player = player2_symbol if current_player == player1_symbol else player1_symbol

    elif game_state == REPLAY_SCREEN:
        replay_button_rect = pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 50, BUTTON_WIDTH, BUTTON_HEIGHT))
        replay_text = font.render('Replay', True, LINE_COLOR)
        replay_text_rect = replay_text.get_rect(center=replay_button_rect.center)
        screen.blit(replay_text, replay_text_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if replay_button_rect.collidepoint(event.pos):
                    reset_game()
                    game_state = SYMBOL_SELECTION

    pygame.display.flip()
