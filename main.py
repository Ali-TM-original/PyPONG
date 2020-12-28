# ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30)
# player1 = pygame.Rect(WIDTH+180, HEIGHT/2 - 70, 10, 140)
# player2 = pygame.Rect(10, HEIGHT/2 - 70, 10, 140)


# Import the pygame library and initialise the game engine
import pygame
import sys
from time import sleep
import random
from pygame import mixer

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
HEIGHT = 700
WIDTH = 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("PYPONG")

clock = pygame.time.Clock()

mixer.music.load('ping.mp3')


# collision method
def ball_collision_overall():
    global ballx_speed, bally_speed , player1_score, player2_score
    # collision with walls
    if ball.left <= 0:
        if_ball_hits_walls_behind()
        player1_score += 1
    if ball.right >= HEIGHT:
        if_ball_hits_walls_behind()
        player2_score += 1
    if ball.top <= 0 or ball.bottom >= WIDTH:
        bally_speed *= -1
    # collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        mixer.music.play(1)
        ballx_speed *= -1
        # bally_speed *= -1  this dosen't work as the y speed changes thus it bounces back in the same direction


# DETECTION IF PADDLE either OUT OF SCREEN
def detection():
    if paddle1.top <= 0:
        paddle1.top = 0
    if paddle1.bottom >= 500:
        paddle1.bottom = 500
    if paddle2.top <= 0:
        paddle2.top = 0
    if paddle2.bottom >= 500:
        paddle2.bottom = 500


def if_ball_hits_walls_behind():
    global ballx_speed
    global bally_speed
    sleep(.02)
    ball.center = (349, 250)
    ballx_speed = 2 * random.choice((-1, 1))
    bally_speed = 2 * random.choice((-1, 1))


# paddles
# paddle1 = pygame.Rect(680, HEIGHT/2-15, 10, 90)
# paddle2 = pygame.Rect(10, HEIGHT/2-15, 10, 90)
paddle1 = pygame.Rect(680, 250 - 25, 10, 90)
paddle2 = pygame.Rect(10, 250 - 25, 10, 90)

# ball
ball = pygame.Rect(349 - 15, 250, 30, 30)
ballx_speed = 2
bally_speed = 2

# PADDLE SPEEDS
paddle1_speed = 0
paddle2_speed = 0

# displaying score
player1_score = 0
player2_score = 0
font = pygame.font.Font('HanaleiFill-Regular.ttf', 40)


# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                paddle1_speed += 7
            if event.key == pygame.K_UP:
                paddle1_speed -= 7
            if event.key == pygame.K_w:
                paddle2_speed -= 7
            if event.key == pygame.K_s:
                paddle2_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                paddle1_speed -= 7
            if event.key == pygame.K_UP:
                paddle1_speed += 7
            if event.key == pygame.K_w:
                paddle2_speed += 7
            if event.key == pygame.K_s:
                paddle2_speed -= 7

    # ball speed
    ball.x += ballx_speed
    ball.y += bally_speed

    # collision method
    ball_collision_overall()

    # detection method
    detection()

    # paddle movement
    paddle1.y += paddle1_speed
    paddle2.y += paddle2_speed

    screen.fill(BLACK)
    # middle line
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 2)
    # paddles
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    # ball
    pygame.draw.ellipse(screen, WHITE, ball)
    # score text
    player1_text = font.render(f'{player1_score}', True, WHITE)
    player2_text = font.render(f'{player2_score}', True, WHITE)
    screen.blit(player2_text, (307, 250))
    screen.blit(player1_text, (350, 250))

    pygame.display.update()
    clock.tick(200)
