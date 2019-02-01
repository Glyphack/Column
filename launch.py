import pygame

from main import main
from utils import draw_text_middle, read_file
from config import s_width, s_height


def main_menu(win):
    moves = read_file("moves.txt")
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle(win, 'Press Any Key To Play', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win, moves)

    pygame.display.quit()


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Column')
main_menu(win)