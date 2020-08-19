import pygame

# 1.该类是一个游戏元素的基类（子弹，背景图，我方飞机，敌方飞机所有类都继承该类）该基类继承精灵类
#   将精灵添加到精灵组中，统一管理的
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
GAME_FRAME = 60
HERO_FIRE_EVENT = pygame.USEREVENT + 1  # USEREVENT：PYGAME模块中让用户自定义事件的编号起始点
HERO_FIRE_TIME = 200  # 定义开火时间的间隔
ENEMY_INIT_EVENT =  pygame.USEREVENT + 2
ENEMY_INIT_TIME = 1000

ENEMY_SPEED_MIN = 1
ENEMY_SPEED_MAX = 5


