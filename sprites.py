import pygame
import random
import definitions

SCREEN_RECT = definitions.SCREEN_RECT

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_dir, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_dir)
        self.rect = self.image.get_rect()
        self.speed = speed
    
    def update_image(self, img):
        self.image = img

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, image_dir, is_second=False):
        super().__init__(image_dir)
        if is_second:
            self.rect.y = - self.rect.height

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - self.rect.height


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet2.png",-3)

    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()


class Hero(GameSprite):
    def __init__(self,hero_dir):
        super().__init__(hero_dir,0)
        self.change_time = 1
        self.changed_flag = False
        self.hp = 100
        self.speed_x = 0
        self.rect.centerx = int(SCREEN_RECT.width/2)
        self.rect.centery = SCREEN_RECT.height - 120 - int(self.rect.height/2)
        self.bullet_group = pygame.sprite.Group()
        #pygame.time.set_timer(HERO_IMAGE_UPDATE_EVENT, HERO_IMAGE_INTERVAL)

    def update(self):
        self.change_time += 1
        #update image every 10 tick
        if self.change_time % 10 == 0:
            if self.changed_flag:
                self.image = pygame.image.load("./images/me1.png")
                self.changed_flag = False
            else:
                self.image = pygame.image.load("./images/me2.png")
                self.changed_flag = True
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed
        # Ensure plane stay inside the window
        # head
        if self.rect.y <= 0:
            self.rect.y = 0
        # tail
        if self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height
        # left wing
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        # right wing
        if self.rect.centerx > SCREEN_RECT.width:
            self.rect.centerx = SCREEN_RECT.width

    def fire(self):
        bullet1 = Bullet()
        bullet1.rect.centerx = self.rect.centerx
        bullet1.rect.bottom = self.rect.top
        self.bullet_group.add(bullet1)


class Enemy(GameSprite):
    def __init__(self,enemy_dir):
        super().__init__(enemy_dir)
        self.speed = random.randint(definitions.ENEMY_SPEED_MIN,definitions.ENEMY_SPEED_MAX)
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.enemy_group = pygame.sprite.Group()

    def update(self):
        super().update()
        if self.rect.top == SCREEN_RECT.height:
            self.kill()

