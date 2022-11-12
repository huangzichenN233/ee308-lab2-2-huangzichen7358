import pygame


class BoTTon:
    def __init__(self):
        self.start = pygame.image.load("fig/start.png")
        self.stop = pygame.image.load("fig/end.png")
        self.end = pygame.image.load("fig/exit.png")
        self.rule = pygame.image.load("fig/rule.png")
        self.startRect = self.start.get_rect().move(100, 0)
        self.stopRect = self.stop.get_rect().move(300, 0)
        self.endRect = self.end.get_rect().move(500, 0)
        self.ruleRect = self.rule.get_rect().move(550, 250)
