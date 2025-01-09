import pygame
import sys

# Initialize the game
pygame.init()

# Set up display

width, height = 400, 400
line_width = 10
board_rows = 3
board_cols = 3
square_size = width // board_cols
circle_radius = square_size // 3
circle_width = 15
cross_width = 25
space = square_size // 4

# Colors
bg_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(bg_color)

# Board
board = [[0 for _ in range(board_cols)] for _ in range(board_rows)]

# Player stats
player1_wins = 0
player2_wins = 0

# Player names
player1_name = input("Enter Player 1 name: ")
player2_name = input("Enter Player 2 name: ")

# Draw lines
def draw_lines():
    for row in range(1, board_rows):
        pygame.draw.line(screen, line_color, (0, row * square_size), (width, row * square_size), line_width)
        pygame.draw.line(screen, line_color, (row * square_size, 0), (row * square_size, height), line_width)

# Draw figures
def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_width)

# Check win
def check_win(player):
    for row in range(board_rows):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(board_cols):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True
    return False

# Display winner
def display_winner(player):
    font = pygame.font.SysFont("comicsansms", 40)
    if player == 1:
        text = font.render(f"{player1_name} wins!", True, circle_color)
    else:
        text = font.render(f"{player2_name} wins!", True, cross_color)
    screen.blit(text, (width // 6, height // 3))
    pygame.display.update()
    pygame.time.wait(2000)

# Display stats
def display_stats():
    font = pygame.font.SysFont("comicsansms", 20)
    player1_text = font.render(f"{player1_name}: {player1_wins} wins", True, circle_color)
    player2_text = font.render(f"{player2_name}: {player2_wins} wins", True, cross_color)
    screen.blit(player1_text, (10, 10))
    screen.blit(player2_text, (width - player2_text.get_width() - 10, 10))

# Restart game
def restart():
    screen.fill(bg_color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

draw_lines()

# Main loop
player = 1
game_over = False

while True:
    pygame.event.pump()  # Ensure the window remains responsive
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // square_size
            clicked_col = mouseX // square_size

            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    game_over = True
                    display_winner(player)
                    if player == 1:
                        player1_wins += 1
                    else:
                        player2_wins += 1
                player = 3 - player

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    screen.fill(bg_color)
    draw_lines()
    draw_figures()
    display_stats()
    pygame.display.update()
