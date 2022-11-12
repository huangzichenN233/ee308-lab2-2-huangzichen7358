import random
import pygame


class Dice:
    def __init__(self, pos_x, pos_y):
        self.dice = pygame.image.load("fig/asser03.png")
        self.diceRect = self.dice.get_rect().move(pos_x, pos_y)
        self.diceSpin = [pygame.image.load("fig/asser03.png"),
                         pygame.image.load("fig/asser02.png"),
                         pygame.image.load("fig/asser01.png")]
        self.diceStop = [pygame.image.load("fig/01.png"),
                         pygame.image.load("fig/02.png"),
                         pygame.image.load("fig/03.png"),
                         pygame.image.load("fig/04.png"),
                         pygame.image.load("fig/05.png"),
                         pygame.image.load("fig/06.png")]
        self.StopStatus = random.randint(0, 5)
        self.SpinStatus = 0

    def move(self):
        self.SpinStatus += 1
        if self.SpinStatus == 3:
            self.SpinStatus = 0
