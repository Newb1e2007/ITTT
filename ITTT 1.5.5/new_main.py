import pygame
import Field
import Player3
import time

# import Colors

fps = 60
# break_flag = True

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 72)

Field.drawing_field()
pygame.display.update()


def main():
    player_num = 1
    # break_flag = True
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                condition = Player3.players_lst[player_num].motion()
                pygame.display.update()
                if condition == 1:
                    print('again')
                    pass
                elif condition == 2:
                    time.sleep(1)
                    Field.game_finish()
                    text = font.render(f'Player number {player_num + 1} win!', True, (255, 255, 255))
                    Field.screen.blit(text, (500, 325))
                    print('finish')
                    pygame.display.update()
                    # break_flag = False
                    break
                elif condition == 3:
                    player_num = (player_num + 1) % 3
                    print(player_num)

        # pygame.display.update()
        clock.tick(fps)


main()
