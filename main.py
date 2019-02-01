import pygame
import random

from utils import *
from config import file_play
pygame.font.init()


def main(win, moves):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_faller = False
    run = True
    current_faller = get_shape()
    next_faller = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3
    score = 0
    cursor = 0
    play = True
    freeze = False
    print(moves)
    while run:
        if file_play:
            if cursor >= len(moves) and run:
                play = False
            grid = create_grid(locked_positions)
            fall_time += clock.get_rawtime()
            clock.tick()

            if fall_time / 1000 > fall_speed:
                fall_time = 0
                current_faller.y += 1
                if not (valid_space(current_faller, grid)) and current_faller.y > 0:
                    current_faller.y -= 1
                    change_faller = True

            if play:
                while not freeze:
                        move = moves[cursor].rstrip()
                        cursor += 1
                        if move == "SPACE":
                            current_faller.rotation += 1
                            print("rotated")
                            if not (valid_space(current_faller, grid)):
                                current_faller.rotation -= 1
                        if move == "RIGHT":
                            current_faller.x += 1
                            print("right")
                            if not (valid_space(current_faller, grid)):
                                current_faller.x -= 1
                        if move == "LEFT":
                            current_faller.x -= 1
                            print('left')
                            if not (valid_space(current_faller, grid)):
                                current_faller.x += 1
                        if move == "DOWN":
                            current_faller.y += 1
                            if not (valid_space(current_faller, grid)):
                                current_faller.y -= 1
                        if move == "FREEZE":
                            print('freezed')
                            freeze = True
                        if cursor >= len(moves):
                            play = False
                            break

            shape_pos = convert_shape_format(current_faller)

            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    grid[y][x] = current_faller.color

            if change_faller:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_faller.color
                    freeze = False
                current_faller = next_faller
                next_faller = get_shape()
                change_faller = False
                freeze = False
                score += clear_rows(grid, locked_positions) * 1

            draw_window(win, grid, score)
            draw_next_shape(next_faller, win)
            pygame.display.update()

            if check_lost(locked_positions):
                draw_text_middle(win, "YOU LOST!", 80, (255, 255, 255))
                pygame.display.update()
                pygame.time.delay(1500)
                run = False



        else:
            grid = create_grid(locked_positions)
            fall_time += clock.get_rawtime()
            clock.tick()

            if fall_time / 1000 > fall_speed:
                fall_time = 0
                current_faller.y += 1
                if not (valid_space(current_faller, grid)) and current_faller.y > 0:
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

            draw_window(win, grid, score)
            draw_next_shape(next_faller, win)
            pygame.display.update()

            if check_lost(locked_positions):
                draw_text_middle(win, "YOU LOST!", 80, (255, 255, 255))
                pygame.display.update()
                pygame.time.delay(1500)
                run = False
