import pygame as pg

import random

from sys import exit

# initialise pygame
pg.init()

# screen set

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("new game")

icon = pg.image.load("gamepad.png")

pg.display.set_icon(icon)

# player class for generating player


class player(pg.sprite.Sprite):

    player_image = pg.image.load("spaceship1.png")
    player_x = 350
    player_y = 480

    def player_display(x, y):
        screen.blit(player.player_image, (x, y))

# enemy class to generate variable enemies


class enemy(pg.sprite.Sprite):

    enemy1_icon = pg.image.load("alien1.png")
    e_pos_x = random.randint(0, 745)
    enemy1_x = e_pos_x
    enemy1_y = 20

    def enemy_display(x, y):
        screen.blit(enemy.enemy1_icon, (x, y))

# Game over


game_over_image = pg.image.load("game-over.png")

def game_over_display():
    screen.blit(game_over_image, (150, 75))

x = False

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            if player.player_x < 735:
                player.player_x += 0.1
            else:
                player.player_x = 15

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            if player.player_x > 0:
                player.player_x -= 0.1
            else:
                player.player_x = 735

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
            if player.player_y > 25:
                player.player_y -= 0.1

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_DOWN:
            if player.player_y < 520:
                player.player_y += 0.1

    if running:
        enemy.enemy1_y += 0.1

    if running:
     if ((enemy.enemy1_y == (player.player_y))):
        x = True

    if (x):
        game_over_display()

    player.player_display(player.player_x, player.player_y)

    enemy.enemy_display(enemy.enemy1_x, enemy.enemy1_y)

    pg.display.update()
