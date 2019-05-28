import pygame


class Bullet:
    def __init__(self, x, y, screen):
        self.x = x + 26
        self.y = y - 30
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet.png").convert()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 12

    def judge(self):
        if self.y < 0:
            return True
        return False


class EnemyBullet:
    def __init__(self, x, y, screen):
        self.x = x + 30
        self.y = y + 80
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet1.gif").convert()
        self.image1 = pygame.image.load("./feiji/bullet.gif").convert()

    def move(self):
        self.y += 2

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def display1(self):
        self.screen.blit(self.image1, (self.x, self.y))

    def judge(self):
        if self.y > 700:
            return True
        return False
