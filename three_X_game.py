import pygame  # 1. pygame 선언
import os

# 현재 위치 정의
current_path = os.path.dirname(__file__)
# 이미지 폴더 위치 정의
image_path = os.path.join(current_path, "images")
# 불러올 이미지 로드
background = pygame.image.load(os.path.join(image_path, "background.png"))

pygame.init()  # 2. pygame 초기화
# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

Corn_silk = (255, 248, 220)  # white
Alice_Blue = (240, 248, 255)  # white
Light_turquoise = (224, 255, 255)  # YELLOW

large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
size = [600, 550]
screen = pygame.display.set_mode(size)
turn = 0
grid = [' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ']
done = False
clock = pygame.time.Clock()


def is_valid_position(grid, position):
    if grid[position] == ' ':
        return True
    else:
        return False


def is_winner(grid, mark):
    if (grid[0] == mark and grid[1] == mark and grid[2] == mark and grid[3] == mark) or \
            (grid[4] == mark and grid[5] == mark and grid[6] == mark and grid[7] == mark) or \
            (grid[8] == mark and grid[9] == mark and grid[10] == mark and grid[11] == mark) or \
            (grid[12] == mark and grid[13] == mark and grid[14] == mark and grid[15] == mark) or \
            (grid[0] == mark and grid[4] == mark and grid[8] == mark and grid[12] == mark) or \
            (grid[1] == mark and grid[5] == mark and grid[9] == mark and grid[13] == mark) or \
            (grid[2] == mark and grid[6] == mark and grid[10] == mark and grid[14] == mark) or \
            (grid[3] == mark and grid[7] == mark and grid[11] == mark and grid[15] == mark) or \
            (grid[0] == mark and grid[5] == mark and grid[10] == mark and grid[15] == mark) or \
            (grid[3] == mark and grid[6] == mark and grid[9] == mark and grid[12] == mark):
        return True
    else:
        return False


def is_grid_full(grid):
    full = True
    for mark in grid:
        if mark == ' ':
            full = False
            break
    return full


turn = 0


def runGame():
    # 게임 활용 변수
    CELL_SIZE = 100
    COLUMN_COUNT = 4
    ROW_COUNT = 4
    X_WIN = 1
    O_WIN = 2
    DRAW = 3
    game_over = 0
    global done, turn, grid
    while not done:
        clock.tick(30)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 0:
                    column_index = event.pos[0] // CELL_SIZE
                    row_index = event.pos[1] // CELL_SIZE
                    position = column_index + 4 * row_index
                    if is_valid_position(grid, position):
                        grid[position] = 'X'
                        if is_winner(grid, 'X'):
                            print('X 가 이겼습니다.')
                            game_over = X_WIN
                            # break
                        elif is_grid_full(grid):
                            print('무승부 입니다.')
                            game_over = DRAW
                            # break
                        turn += 1
                        turn = turn % 2
                else:
                    column_index = event.pos[0] // CELL_SIZE
                    row_index = event.pos[1] // CELL_SIZE
                    position = column_index + 4 * row_index
                    if is_valid_position(grid, position):
                        grid[position] = 'O'
                        if is_winner(grid, 'O'):
                            print('O 가 이겼습니다.')
                            game_over = O_WIN
                            # break
                        elif is_grid_full(grid):
                            print('무승부 입니다.')
                            game_over = DRAW
                            # break
                        turn += 1
                        turn = turn % 2
            # 화면 그리기
            for column_index in range(COLUMN_COUNT):
                for row_index in range(ROW_COUNT):
                    rect = (CELL_SIZE * column_index, CELL_SIZE * row_index, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, Corn_silk, rect, 1)
            for column_index in range(COLUMN_COUNT):
                for row_index in range(ROW_COUNT):
                    position = column_index + 4 * row_index
                    mark = grid[position]
                    if mark == 'X':
                        X_image = small_font.render('{}'.format('X'), True, Light_turquoise)
                        screen.blit(X_image, (CELL_SIZE * column_index + 10, CELL_SIZE * row_index + 10))
                    elif mark == 'O':
                        O_image = small_font.render('{}'.format('O'), True, Alice_Blue)
                        screen.blit(O_image, (CELL_SIZE * column_index + 10, CELL_SIZE * row_index + 10))
            if not game_over:
                pass
            else:
                if game_over == X_WIN:
                    game_over_image = large_font.render('X wins', True, RED)
                elif game_over == O_WIN:
                    game_over_image = large_font.render('O wins', True, RED)
                else:
                    game_over_image = large_font.render('Draw', True, RED)
                screen.blit(game_over_image,
                            (600 // 2 - game_over_image.get_width() // 2, 600 // 2 - game_over_image.get_height() // 2))
            pygame.display.update()  # 모든 화면 그리기 업데이트


runGame()
pygame.quit()
