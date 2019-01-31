import pygame
import random

from config import *
from utils import *
pygame.font.init()


def main(win):
    last_score = max_score()
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_faller = False
    run = True
    current_faller = get_shape()
    next_faller = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_faller.y += 1
            if not(valid_space(current_faller, grid)) and current_faller.y > 0:
                current_faller.y -= 1
                change_faller = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    pygame.display.quit()

                if event.key == pygame.K_LEFT:
                    current_faller.x -= 1
                    if not(valid_space(current_faller, grid)):
                        current_faller.x += 1
                
                if event.key == pygame.K_RIGHT:
                    current_faller.x += 1
                    if not(valid_space(current_faller, grid)):
                        current_faller.x -= 1
                
                if event.key == pygame.K_DOWN:
                    current_faller.y += 1
                    if not(valid_space(current_faller, grid)):
                        current_faller.y -= 1
                
                if event.key == pygame.K_SPACE:
                    current_faller.rotation += 1
                    if not(valid_space(current_faller, grid)):
                        current_faller.rotation -= 1

        shape_pos = convert_shape_format(current_faller)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_faller.color

        if change_faller:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_faller.color
            current_faller = next_faller
            next_faller = get_shape()
            change_faller = False
            score += clear_rows(grid, locked_positions) * 1

        draw_window(win, grid, score, last_score)
        draw_next_shape(next_faller, win)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
