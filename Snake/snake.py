# import library
import pygame
import random

from pygame import mixer
mixer.init()
pygame.init()
# veloc=100
# Color
red = pygame.Color(255, 0, 0)
blue = pygame.Color(65, 105, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(128, 128, 128)
# Window display
x = 800
y = 600
# Set display
Screen = pygame.display.set_mode((x, y))
# Set Name
pygame.display.set_caption('Snake Game')
# kích thước chiều cao và chiều rộng
m = 20
n = 10
#Load and set Background of Game
# load hình ảnh
gameIcon = pygame.image.load('snake.jpg')
# Set gameicon
pygame.display.set_icon(gameIcon)

Intro = pygame.image.load('intro.png')
Intro = pygame.transform.scale(Intro, (x, y))

Background = pygame.image.load('background.jpg')
Background = pygame.transform.scale(Background, (x, y))

Background1 = pygame.image.load('background1.jpg')
Background1 = pygame.transform.scale(Background1, (x, 56))

wall = pygame.image.load('wall.png')
wall = pygame.transform.scale(wall, (x, n))

wall1 = pygame.image.load('wall1.png')
wall1 = pygame.transform.scale(wall1, (n, y))

head = pygame.image.load('head.png')
head = pygame.transform.scale(head, (m, m))

body = pygame.image.load('body.png')
body = pygame.transform.scale(body, (m, m))

food = pygame.image.load('apple.png')
food = pygame.transform.scale(food, (m, m))


# Load music
# sound=pygame.mixer.Sound('no6.wav')
mixer.music.load('no6.wav')
mixer.music.play(-1)
sound1 = pygame.mixer.Sound('vacham.wav')

score = 0
pause = False

# Hàm tạo button
def button(msg, x, y, l, w, oc, bc, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + l and y < mouse[1] < y + w:
        # pygame.mixer.Sound.play(sound1)
        pygame.draw.rect(Screen, bc, (x, y, l, w))
        if click[0] == 1 and action != None:
            action()
    else:
        # pass
        pygame.draw.rect(Screen, oc, (x, y, l, w))
    text = pygame.font.SysFont("bahnschrift", 30).render(msg, True, black)
    text_rect = text.get_rect(center=((x + (l / 2)), (y+(w/2))))
    Screen.blit(text, text_rect)
#  Hàm bỏ pause game
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
# Hàm thoát game
def quitgame():
    pygame.quit()
    quit()

# Hàm pause game
def paused():
    # pygame.mixer.music.pause()
    text = pygame.font.SysFont("bahnschrift", 100).render("PAUSED", True, black)
    text_rect = text.get_rect(center=((x / 2), (y / 2)))
    Screen.blit(text, text_rect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Screen.fill(white)
        button("Menu", 80, 450, 100, 50, gray, red, game_intro)
        button("Continue", 250, 450, 130, 50, gray, red, unpause)
        button("Play again", 450, 450, 150, 50, gray, red, game)
        button("Quit", 680, 450, 100, 50, gray, red, quitgame)
        pygame.display.update()
# Hàm Start game
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                # Screen.blit(Background1, (0, 0))
        Screen.blit(Intro, (0, 0))
        button("Play", 300, 300, 100, 50, gray, red, game)
        button("Quit", 300, 380, 100, 50, gray, red, quitgame)
        pygame.display.update()
# hàm gameover
def game_over(score):
   # pygame.mixer.Sound.play(sound1)
   #  pygame.mixer.music.stop()

    text = pygame.font.SysFont('consolas', 40).render('Game over!', True, red)
    Screen.blit(text, [300, 300])
    font = pygame.font.SysFont('consolas', 28).render('Score:' + str(score), True, white)
    rect = font.get_rect()
    rect.midtop = (390, 230)
    Screen.blit(font, rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again", 150, 450, 160, 50, gray, red, game)
        button("Menu", 380, 450, 100, 50, gray, red, game_intro)
        button("Quit", 550, 450, 100, 50, gray, red, quitgame)
        pygame.display.update()
def draw():
    # Nền khung rắn di chuyển
    Screen.blit(Background, (0, 56))
    # nền khung điểm
    Screen.blit(Background1, (0, 0))
    # rào chắn
    # biên trên
    Screen.blit(wall, (0, 56))
    # biên dưới
    Screen.blit(wall, (0, 590))
    # biên dọc trái
    Screen.blit(wall1, (0, 56))
    # biên dọc phải
    Screen.blit(wall1, (790, 56))
    # draw food score
    Screen.blit(food, (128, 15))
def game():
    # game_over()
    # pygame.mixer.Sound.play(sound)
    global pause
    snakepos = [200, 100]
    snakebody = [[200, 100], [180, 80]]
    veloc= 100

    foodx = round(random.randrange(40, x - 40) / 10)
    foody = round(random.randrange(80, y - 40) / 10)

    if foodx % 2 != 0:
        foodx += 1
    if foody % 2 != 0:
        foody += 1
    foodpos = [foodx * 10, foody * 10]
    foodflat = True
    direction = 'RIGHT'
    changeto = direction
    score = 0
    # button("Quit", 550, 450, 100, 50, gray, red, quitgame)
    play = True
    while play:
        # pygame.mixer.Sound.play(sound1)
        # tốc độ chơi
        pygame.time.delay(int(veloc))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # xử lý phím
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    changeto = 'LEFT'
                if event.key == pygame.K_UP:
                    changeto = 'UP'
                if event.key == pygame.K_DOWN:
                    changeto = 'DOWN'
                if event.key == pygame.K_SPACE:
                    # time.sleep(10)
                    pause = True
                    paused()
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        # hướng đi
        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        # cập nhật vị trí mới
        if direction == 'RIGHT':
            snakepos[0] += m
        if direction == 'LEFT':
            snakepos[0] -= m
        if direction == 'UP':
            snakepos[1] -= m
        if direction == 'DOWN':
            snakepos[1] += m
        #cơ chế thêm khúc dài ra
        snakebody.insert(0, list(snakepos))
        if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
            score += 1
            veloc=veloc*0.98
            print(veloc)
            pygame.mixer.Sound.play(sound1)
            # pygame.display.update()
            foodflat = False
        else:
            snakebody.pop()
        # food
        if foodflat == False:
            foodx = round(random.randrange(30, x - 40) / 10)
            foody = round(random.randrange(80, y - 40) / 10)
            if foodx % 2 != 0:
                foodx += 1
            if foody % 2 != 0:
                foody += 1
            foodpos = [foodx * 10, foody * 10]
            foodflat = True
        #  cập nhật lên cửa sổ
            print(foodpos)
        draw()
        for pos in snakebody:
            Screen.blit(body, pygame.Rect(pos[0], pos[1], m, m))
        Screen.blit(head, pygame.Rect(snakebody[0][0], snakebody[0][1], m, m))
        Screen.blit(food, pygame.Rect(foodpos[0], foodpos[1], m, m))

        # Các trường hợp game_over
        # 1. Đâm vào tường
        if snakepos[0] > 770 or snakepos[0] < 15:
            game_over(score)
        if snakepos[1] > 575 or snakepos[1] < 60:
            game_over(score)
        # 2. Snake tự cắn vào cơ thể
        for bodysnake in snakebody[5:]:
            if snakepos[0] == bodysnake[0] and snakepos[1] == bodysnake[1]:
                game_over(score)
        # In ra điểm trong khi game chạy
        font = pygame.font.SysFont('consolas', 28)
        Score = font.render("Score:" + str(score), True, red)
        Screen.blit(Score, (5, 15))
        pygame.display.flip()
        # print(snakebody)
        # print(score)

game_intro()
game()
