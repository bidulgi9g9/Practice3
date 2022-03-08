#https://www.youtube.com/watch?v=rtwtOcfYKqc 출처 이수안컴퓨터연구소 유튜브


import pygame

import sys

import time

import random # import함수로 이미 만들어진 복잡한 함수를 끌어옴

 

 

from pygame.locals import *

 

WINDOW_WIDTH = 800

WINDOW_HEIGHT = 600

GRID_SIZE = 20

GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE

GID_HEIGHT= WINDOW_HEIGHT / GRID_SIZE #게임화면의 크기설정

 

WHITE = (255, 255, 255)

GREEN = (0, 50, 0)

ORANGE = (250, 150, 0) #게임속 오브젝트의 색상 설정

 

UP = (0, -1)

DOWN = (0, 1)

LEFT = (-1, 0)

RIGHT = (1, 0) #게임의 메인오브젝트인 지렁이의 움직임 값 설정

 

FPS = 10 #게임화면 프레임 설정

 

class Python(object): #object라는 클래스를 class함수로 설정 -지렁이

    def __init__(self): #def함수로 사용할self함수를 만듬

        self.create()

        self.color = GREEN #object개체의 색상설정

 

    def create(self):

        self.length = 2

        self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2))]

        self.direction = random.choice([UP, DOWN, LEFT, RIGHT]) #object의 움직임 설정

 

    def contorl(self, xy): #contorl함수 설정

        if (xy[0] * -1, xy[1] * -1) == self.direction:

            return

        else:

            self.direction = xy

 

    def move(self): #move함수 설정

        cur = self.positions[0]

        x, y = self.direction

        new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGHT)

        if new in self.positions[2:]:

            self.create()

        else:

            self.positions.insert(0, new)

            if len(self.positions) >self.length:

                self.positions.pop()

 

    def eat(self): #eat 함수설정

        self.length += 1

 

    def draw(self, surface): #draw함수설정

        for p in self.positions:

            draw_object(surface, self.color, p) 

 

class Feed(object): #Feed라는객체생성 -지렁이가먹을 점

    def __init__(self):

        self.position = (0, 0)

        self.color = ORANGE

        self.create()

 

    def create(self): #랜덤하게 생성되도록 random 모듈을 불러와서 설정해줌

        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GID_HEIGHT - 1) *GRID_SIZE)

 

    def draw(self, surface):

        draw_object(surface, self.color, self.position)

            

def draw_object(surface, color, pos):

    r = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(surface, color, r)

 

def check_eat(python, feed):

    if python.positions[0] == feed.position:

        python.eat()

        feed.create()

   

    

 

if __name__ == '__main__':

    python = Python() #지렁이

    feed = Feed() #점

 

 

    

    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

    pygame.display.set_caption('Python Game')

    surface = pygame.Surface(window.get_size())

    surface = surface.convert()

    surface.fill(WHITE)

    clock = pygame.time.Clock()

    pygame.key.set_repeat(1, 40)

    window.blit(surface, (0, 0))

 

    while True: #반복문을 사용해줌으로써 게임을 중지하기전까지 계속됨

 

        for event in pygame.event.get():

            if event.type == QUIT:

                pygame.quit()

                sys.exit()

            elif event.type == KEYDOWN:

                if event.key == K_UP: #방향키를 누르면 움직이도록 방향키에 함수를 할당해줌

                    pygame.control(UP)

                elif event.key == K_DOWN:

                    pygame.control(DOWN)

                elif event.key == K_LEFT:

                    pygame.control(LEFT)

                elif event.key == K_RIGHT:

                    pygame.control(RIGHT)

 

        surface.fill(WHITE) #배경화면 색 설정

        python.move() #지렁이가 움직일 때 사용할 함수 할당

        check_eat(python, feed) #지렁이가 점을 먹을떄마다 길어지도록 할당

        speed = (FPS + python.length) / 2 #지렁이가 길어질때마다 속도가 올라가도록 할당

        python.draw(surface) #화면에 지렁이가 나타나게 해줌

        feed.draw(surface) #화면에 점이 나타나게 해줌

        window.blit(surface, (0, 0))

        pygame.display.flip()

        pygame.display.update()

        clock.tick(speed)