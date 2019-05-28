import pygame
from bullet import Bullet, EnemyBullet
from random import randint
from life import Life


class HeroPlane:
    t = 0

    def __init__(self, screen):
        self.x = 230
        self.y = 500
        self.screen = screen
        self.image_name = "./feiji/hero.gif"
        self.image_name1 = "./feiji/hero1.gif"
        self.image = pygame.image.load(self.image_name).convert()
        self.image1 = pygame.image.load(self.image_name1).convert()
        self.t = 0
        self.bullet_list = []
        self.bload = []
        for i in range(70):
            self.bload.append([])
        self.life = Life(screen)
        for i in range(70):
            for j in range(76):
                self.bload[i].append(False)
        self.block()

    def is_hurt(self, bad_bullet_list):
        for bad_bullet in bad_bullet_list:
            if bad_bullet.x - self.x < 0 or bad_bullet.x - self.x > 69 or bad_bullet.y - self.y < 0 or bad_bullet.y - self.y >75:
                continue
            if self.bload[bad_bullet.x - self.x][bad_bullet.y - self.y]:
                if not self.life.hurt():
                    return bad_bullet
                else:
                    return "game over"
        return None

    # 简单把飞机分成3块，以飞机的x, y为参照点，这3个范围可以被击中。
    # (32, 0)->(37, 17)
    # (0, 25)->(70, 46)
    # (20, 46)->(52, 63)
    def block(self):
        for i in range(32, 37):
            for j in range(0, 17):
                self.bload[i][j] = True
        for i in range(0, 70):
            for j in range(25, 46):
                self.bload[i][j] = True
        for i in range(20, 52):
            for j in range(46, 63):
                self.bload[i][j] = True

    def boundary_x(self):
        if self.x < -70:
            self.x = 400
        elif self.x > 400:
            self.x = -70

    def boundary_y(self):
        if self.y < 0:
            self.y = 0
        if self.y > 624:
            self.y = 624

    def launch_bullet(self):
        new_bullet = Bullet(self.x, self.y, self.screen)
        self.bullet_list.append(new_bullet)

    def display(self):
        if HeroPlane.t % 10 < 5:
            self.screen.blit(self.image, (self.x, self.y))
        else:
            self.screen.blit(self.image1, (self.x, self.y))
        HeroPlane.t += 1
        if HeroPlane.t > 1000000:
            HeroPlane.t -= 1000000
        need_del_list = []
        for item in self.bullet_list:
            if item.judge():
                need_del_list.append(item)
        for def_item in need_del_list:
            self.bullet_list.remove(def_item)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
        self.life.display()

    def move_left(self):
        self.x -= 20
        self.boundary_x()

    def move_right(self):
        self.x += 20
        self.boundary_x()

    def move_up(self):
        self.y -= 20
        self.boundary_y()

    def move_down(self):
        self.y += 20
        self.boundary_y()


class EnemyPlane:
    def __init__(self, screen):
        self.x = randint(80, 240)
        self.y = 0
        self.screen = screen
        self.image_name = "./feiji/enemy.gif"
        self.image_name1 = "./feiji/enemy1.gif"
        self.image = pygame.image.load(self.image_name).convert()
        self.image1 = pygame.image.load(self.image_name1).convert()
        self.bullet_list = []
        self.direction = "right" if randint(1, 2) == 1 else "left"
        self.life = randint(24, 36)
        self.score = self.life * randint(1326, 1570)
        self.flag = False

    def move(self):
        self.y += 1
        if self.direction == "right":
            self.x += 6
        elif self.direction == "left":
            self.x -= 6
        if self.x > 300:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def launch_bullet(self):
        number = randint(1, 100)
        if number < 6:
            new_bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(new_bullet)

    def is_hurt(self, bullet):
        if 0 < bullet.x - self.x < 110 and 0 < bullet.y - self.y < 100:
            self.life -= 1
            return_1 = (1, (self, bullet), self.score)
            return_2 = (2, bullet)
            if self.life <= 0:
                return return_1
            return return_2
        return_3 = (0, 0)
        return return_3

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        need_del_list = []
        for i in self.bullet_list:
            if i.judge():
                need_del_list.append(i)
        for i in need_del_list:
            self.bullet_list.remove(i)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def display1(self):
        if not self.flag:
            self.life += 10
            self.score += 20000
            self.flag = True
        self.screen.blit(self.image1, (self.x, self.y))
        need_del_list = []
        for i in self.bullet_list:
            if i.judge():
                need_del_list.append(i)
        for i in need_del_list:
            self.bullet_list.remove(i)
        for bullet in self.bullet_list:
            bullet.display1()
            bullet.move()
