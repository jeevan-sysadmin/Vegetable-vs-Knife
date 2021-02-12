import random

import math
import pygame
from pygame import mixer

pygame.init()
pygame.font.init()

# intialize the pygame
pygame.get_init()
fps = pygame.time.Clock()
# create the screen
display = pygame.display.set_mode((800, 600))

# background
backgroung = pygame.image.load('abcdef.jpg').convert()
x = 0
mixer.music.load("Tobu.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Vegetable vs Knif")
icon = pygame.image.load('harvest.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('poijk.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy1
enemy1Img = pygame.image.load('carrot.png')
enemy1X = random.randint(0, 735)
enemy1Y = random.randint(50, 150)
enemy1X_change = 0.3
enemy1Y_change = 40

# enemy2
enemy2Img = pygame.image.load('cabbage.png')
enemy2X = random.randint(0, 735)
enemy2Y = random.randint(50, 150)
enemy2X_change = 0.3
enemy2Y_change = 40

# enemy3
enemy3Img = pygame.image.load('chili.png')
enemy3X = random.randint(0, 735)
enemy3Y = random.randint(50, 150)
enemy3X_change = 0.3
enemy3Y_change = 40

# enemy4
enemy4Img = pygame.image.load('eggplant.png')
enemy4X = random.randint(0, 735)
enemy4Y = random.randint(50, 150)
enemy4X_change = 0.3
enemy4Y_change = 40

# enemy5
enemy5Img = pygame.image.load('tomato.png')
enemy5X = random.randint(0, 735)
enemy5Y = random.randint(50, 150)
enemy5X_change = 0.3
enemy5Y_change = 40

# Bullet
bulletImg = pygame.image.load('bnm.png')
bulletX = 0
bulletY = 400
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

# SCORE

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 0, 153))
    display.blit(score, (x, y))

def game_over_text(x,y):
    over_text = over_font.render("GAME OVER ", True, (0, 0, 0))
    display.blit(over_text, (x, y))

def player(X, y):
    display.blit(playerImg, (playerX, playerY))

def enemy1(X, Y, ):
    display.blit(enemy1Img, (enemy1X, enemy1Y))


def enemy2(X, Y):
    display.blit(enemy2Img, (enemy2X, enemy2Y))


def enemy3(X, Y):
    display.blit(enemy3Img, (enemy3X, enemy3Y))


def enemy4(X, Y):
    display.blit(enemy4Img, (enemy4X, enemy4Y))


def enemy5(x, Y):
    display.blit(enemy5Img, (enemy5X, enemy5Y))


def fire_bullet(X, Y):
    global bullet_state
    bullet_state = "fire"
    display.blit(bulletImg, (X + 16, Y + 10))

def iscollision(enemy1X, bulletX, enemy1Y, bulletY):
    distance = math.sqrt(math.pow(enemy1X - bulletX, 2) + (math.pow(enemy1Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def iscollision(enemy2X, bulletX, enemy2Y, bulletY):
    distance = math.sqrt(math.pow(enemy2X - bulletX, 2) + (math.pow(enemy2Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def iscollision(enemy3X, bulletX, enemy3Y, bulletY):
    distance = math.sqrt(math.pow(enemy3X - bulletX, 2) + (math.pow(enemy3Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def iscollision(enemy4X, bulletX, enemy4Y, bulletY):
    distance = math.sqrt(math.pow(enemy4X - bulletX, 2) + (math.pow(enemy4Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def iscollision(enemy5X, bulletX, enemy5Y, bulletY):
    distance = math.sqrt(math.pow(enemy5X - bulletX, 2) + (math.pow(enemy5Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Grame Loop
def main():
    run = True

running = True
while running:

    # Backgroung image
    rel_x = x % backgroung.get_rect().width
    display.blit(backgroung, (rel_x - backgroung.get_rect().width, 0))
    if int(x):
        display.blit(backgroung, (rel_x, 0))
    x -= 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# if keystrike is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('allwin.wav')
                    bullet_sound.play()
                    bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # checking for boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    # enemy movement
    enemy1X += enemy1X_change
    enemy2X += enemy2X_change
    enemy3X += enemy3X_change
    enemy4X += enemy4X_change
    enemy5X += enemy5X_change
    # Game Over
    if enemy1Y > 400:
        for i in range(enemy1X, enemy1Y):
            enemy1Y = 2000
            game_over_text()
            break

    if enemy2Y > 400:
        for i in range(enemy2X, enemy2Y):
            enemy2Y = 2000
            game_over_text()
            break

    if enemy3Y > 400:
        for i in range(enemy3X, enemy3Y):
            enemy3Y = 2000
            game_over_text()
            break

    if enemy4Y > 400:
        for i in range(enemy4X, enemy4Y):
            enemy4Y = 2000
            game_over_text()
            break

    if enemy5Y > 500:
        for i in range(enemy5X, enemy5Y):
            enemy5Y = 2000
            game_over_text()
            break

    # enemy1 movement
    if enemy1X <= 0:
        enemy1X_change = 0.5
        enemy1Y += enemy1Y_change
    elif enemy1X >= 736:
        enemy1X_change = -0.5
        enemy1Y += enemy1Y_change

    # enemy2 movement
    if enemy2X <= 0:
        enemy2X_change = 0.5
        enemy2Y += enemy2Y_change
    elif enemy2X >= 736:
        enemy2X_change = -0.5
        enemy2Y += enemy2Y_change

        # enemy3 movement
    if enemy3X <= 0:
        enemy3X_change = 0.5
        enemy3Y += enemy3Y_change
    elif enemy3X >= 736:
        enemy3X_change = -0.5
        enemy3Y += enemy3Y_change

        # enemy4 movement
    if enemy4X <= 0:
        enemy4X_change = 0.5
        enemy4Y += enemy4Y_change
    elif enemy4X >= 736:
        enemy4X_change = -0.5
        enemy4Y += enemy4Y_change

        # enemy5 movement
    if enemy5X <= 0:
        enemy5X_change = 0.5
        enemy5Y += enemy5Y_change
    elif enemy5X >= 736:
        enemy5X_change = -0.5
        enemy5Y += enemy5Y_change

        # collision 1
        collision1 = iscollision(enemy1X, enemy1Y, bulletX, bulletY)
        if collision1:
            explosion_sound = mixer.Sound('sugan.wav')
            explosion_sound.play()
            bulletY = 400
            bullet_state = "ready"
            score_value += 1
            enemy1X = random.randint(0, 735)
            enemy1Y = random.randint(50, 150)

        # collision 2
    collision2 = iscollision(enemy2X, enemy2Y, bulletX, bulletY)
    if collision2:
        bulletY = 400
        bullet_state = "ready"
        score_value += 1
        enemy2X = random.randint(0, 735)
        enemy2Y = random.randint(50, 150)

        # collision 3
    collision3 = iscollision(enemy3X, enemy3Y, bulletX, bulletY)
    if collision3:
        bulletY = 400
        bullet_state = "ready"
        score_value += 1
        enemy3X = random.randint(0, 735)
        enemy3Y = random.randint(50, 150)

        # collision 4
    collision4 = iscollision(enemy4X, enemy4Y, bulletX, bulletY)
    if collision4:
        bulletY = 400
        bullet_state = "ready"
        score_value += 1
        enemy4X = random.randint(0, 735)
        enemy4Y = random.randint(50, 150)

        # collision 5
    collision5 = iscollision(enemy5X, enemy5Y, bulletX, bulletY)
    if collision5:
        bulletY = 400
        bullet_state = "ready"
        score_value += 1
        enemy5X = random.randint(0, 735)
        enemy5Y = random.randint(50, 150)
        pygame.display.update()

    player(playerX, playerY)
    enemy1(enemy1X, enemy1Y)
    enemy2(enemy2X, enemy2Y)
    enemy3(enemy3X, enemy3Y)
    enemy4(enemy4X, enemy4Y)
    enemy5(enemy5X, enemy5Y)
    show_score(textX, textY)
    pygame.display.update()
