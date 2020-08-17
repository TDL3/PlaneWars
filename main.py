import pygame
import definitions


class PlaneWars():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(definitions.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
        pygame.display.set_caption("Plane wars")
        pygame.time.set_timer(definitions.ENEMY_INIT_EVENT, definitions.ENEMY_INIT_TIME)
        self.__create_sprites()
        
    def start_game(self):
        while True:
            self.clock.tick(definitions.GAME_FRAME)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprite()
            # render(text, antialias, color, background=None) -> Surface
            text = self.font.render("HP: " + str(self.hero.hp), True, (255, 55, 0))
            self.screen.blit(text,(0,0))
            
            pygame.display.set_caption("Plane wars | FPS: " + str("{:.2f}".format(self.clock.get_fps())))
            
            pygame.display.update()

    def __create_sprites(self):
        bg1 =definitions.BgSprite("./images/background.png")
        bg2 = definitions.BgSprite("./images/background.png",True)
        self.hero = definitions.Hero("./images/me1.png")
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        self.hero_group = pygame.sprite.Group(self.hero)
        self.enemy_group = pygame.sprite.Group()

    # Player movement control is retarded, needs improvements
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            if event.type == definitions.HERO_FIRE_EVENT:
                self.hero.fire()
            if event.type == definitions.ENEMY_INIT_EVENT:
                enemy1 = definitions.Enemy("./images/enemy1.png")
                self.enemy_group.add(enemy1)

        keys_pressed = pygame.key.get_pressed()
        if not keys_pressed[pygame.K_SPACE]:
            pygame.time.set_timer(definitions.HERO_FIRE_EVENT,definitions.HERO_FIRE_TIME)
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.hero.speed = -4
        elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.hero.speed = 4
        elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.hero.speed_x = -4
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.hero.speed_x = 4
        else:
            self.hero.speed_x = self.hero.speed = 0
            
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.hp -= 20
            if self.hero.hp <= 0:
                self.hero.kill()
                self.__game_over()
                

    def __update_sprite(self):
        for group in [self.bg_group, self.hero_group, self.enemy_group,self.hero.bullet_group]:
                group.update()
                group.draw(self.screen)
        

    def __game_over(self):
        print("正在退出游戏...")
        pygame.quit()
        exit(0)

def main():
    PlaneWars().start_game()

if __name__ == "__main__":
    main()