import pygame


class Life:
    def __init__(self, screen):
        self.x = 400 - 28 * 4
        self.y = 0
        self.screen = screen
        self.init_blood = 4
        self.now_blood = 4
        self.blood = pygame.image.load("./feiji/blood.png").convert()
        self.blood1 = pygame.image.load("./feiji/blood1.png").convert()

    def hurt(self):
        self.now_blood -= 1
        if self.now_blood == 0:
            return True
        return False

    def display(self):
        for i in range(self.now_blood):
            self.screen.blit(self.blood, (self.x, self.y))
            self.x += 28
        for i in range(self.init_blood - self.now_blood):
            self.screen.blit(self.blood1, (self.x, self.y))
            self.x += 28
        self.x = 400 - 28 * 4
