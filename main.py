import pygame
import random
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60
VEL = 6
BALL_VEL = 6

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (112,112,112)

POINTS_FONT = pygame.font.SysFont('arial', 40)

PLAYER_WIDTH, PLAYER_HEIGHT = 10, 50
BALL_SIZE = 10

player1_points = 0
player2_points = 0

def player1_handle_movement(keys_pressed, player1):
    if keys_pressed[pygame.K_w] and player1.y - VEL - 10 > 0:
        player1.y -= VEL
    if keys_pressed[pygame.K_s] and player1.y + VEL + 10 + PLAYER_HEIGHT < HEIGHT:
        player1.y += VEL

def player2_handle_movement(keys_pressed, player2):
    if keys_pressed[pygame.K_UP] and player2.y - VEL - 10 > 0:
        player2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and player2.y + VEL + 10 + PLAYER_HEIGHT < HEIGHT:
        player2.y += VEL

def draw_window(player1, player2, ballX, ballY, ball):
    WIN.fill(WHITE)
    points_separator = POINTS_FONT.render(":", 1, GREY)
    player1_points_text = POINTS_FONT.render(str(player1_points), 1, GREY)
    player2_points_text = POINTS_FONT.render(str(player2_points), 1, GREY)
    WIN.blit(points_separator, ((WIDTH - points_separator.get_width()) / 2, 8))
    WIN.blit(player1_points_text, (WIDTH / 2 - player1_points_text.get_width() - 10, 10))
    WIN.blit(player2_points_text, (WIDTH / 2 + 10, 10))
    pygame.draw.rect(WIN, BLACK, player1)
    pygame.draw.rect(WIN, BLACK, player2)
    pygame.draw.circle(WIN, BLACK, (ballX + BALL_SIZE, ballY + BALL_SIZE), BALL_SIZE)
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    player1 = pygame.Rect(20, (HEIGHT - PLAYER_HEIGHT)/2, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = pygame.Rect(WIDTH - 20 - PLAYER_WIDTH, (HEIGHT - PLAYER_HEIGHT)/2, PLAYER_WIDTH, PLAYER_HEIGHT)

    global player1_points
    global player2_points

    ballX = WIDTH / 2 - BALL_SIZE
    ballY = (HEIGHT + 145) / 2 - BALL_SIZE

    random_ball_momentum = random.randrange(2)
    
    if random_ball_momentum == 0:
        ballXMomentum = -1

    if random_ball_momentum == 1:
        ballXMomentum = 1
    
    ballYMomentum = 1

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

        ballY = ballY + ballYMomentum * BALL_VEL

        ballX = ballX + ballXMomentum * BALL_VEL

        ball = pygame.Rect(ballX, ballY, BALL_SIZE * 2, BALL_SIZE * 2)

        if ball.colliderect(player1): 
            ballXMomentum = 1
        
        if ball.colliderect(player2):
            ballXMomentum = -1

        if ballY < BALL_SIZE * 2:
            ballYMomentum = 1
        if ballY > HEIGHT - BALL_SIZE * 2:
            ballYMomentum = -1

        if ballX > WIDTH:
            player1_points += 1
            main()

        if ballX + BALL_SIZE * 2 < 0:
            player2_points += 1
            main()

        keys_pressed = pygame.key.get_pressed()

        player1_handle_movement(keys_pressed, player1)
        player2_handle_movement(keys_pressed, player2)
        draw_window(player1, player2, ballX, ballY, ball)


if __name__ == "__main__":
    main()