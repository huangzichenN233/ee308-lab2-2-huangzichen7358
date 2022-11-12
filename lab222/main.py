import random
import sys
import pygame
from Dice import Dice
from BoTTon import BoTTon


class Game:
    def __init__(self):
        pygame.init()
        size = 1200, 900
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.BoTTon = BoTTon()
        self.Dice1 = Dice(100, 100)
        self.Dice2 = Dice(200, 100)
        self.Dice3 = Dice(300, 100)
        self.Dice4 = Dice(400, 100)
        self.Dice5 = Dice(500, 100)
        self.Dice6 = Dice(600, 100)
        self.zyuan, self.duit, self.sanh, self.sijin, self.erju, self.yixiu = 1, 2, 4, 8, 16, 32
        self.background = pygame.image.load("fig/bgb.jpg").convert()
        self.TxtFont = pygame.font.SysFont('微软雅黑', 40)
        self.stop = False
        self.start = False
        self.run()
        pygame.quit()

    def rewrdcacl(self, oneres):
        count_four = 0
        count_two  = 0
        oneplus = [i+1 for i in oneres]
        for item in oneplus:
            if item==4:
                count_four+=1
            elif item==2:
                count_two+=1
        if count_four>=4 and self.zyuan>0:
            self.zyuan -= 1
            return 0
        elif 0 in oneplus and 1 in oneplus and 2 in oneplus and 3 in oneplus and 4 in oneplus and 5 in oneplus and self.duit>0:
            self.duit -= 1
            return 1
        elif count_four>=3 and self.sanh>0:
            self.sanh -= 1
            return 2
        elif count_two >=4 and self.sijin>0:
            self.sijin -= 1
            return 3
        elif count_four>=2 and self.erju>0:
            self.erju -= 1
            return 4
        elif count_four>=1 and self.yixiu>0:
            self.yixiu -= 1
            return 5
        elif self.yixiu<0 and self.duit<0 and self.zyuan<0 and self.sijin<0 and self.erju<0 and self.sanh<0:
            return -2
        else:
            return -1

    def creatmap1(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.BoTTon.start, self.BoTTon.startRect)
        self.screen.blit(self.BoTTon.stop, self.BoTTon.stopRect)
        self.screen.blit(self.BoTTon.end, self.BoTTon.endRect)
        self.screen.blit(self.BoTTon.rule, self.BoTTon.ruleRect)

        if not self.stop and not self.start:
            pygame.display.update()

    def creatmap2(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.BoTTon.start, self.BoTTon.startRect)
        self.screen.blit(self.BoTTon.stop, self.BoTTon.stopRect)
        self.screen.blit(self.BoTTon.end, self.BoTTon.endRect)
        self.screen.blit(self.BoTTon.rule, self.BoTTon.ruleRect)
        self.screen.blit(self.Dice1.diceSpin[self.Dice1.SpinStatus], self.Dice1.diceRect)
        self.screen.blit(self.Dice2.diceSpin[self.Dice2.SpinStatus], self.Dice2.diceRect)
        self.screen.blit(self.Dice3.diceSpin[self.Dice3.SpinStatus], self.Dice3.diceRect)
        self.screen.blit(self.Dice4.diceSpin[self.Dice4.SpinStatus], self.Dice4.diceRect)
        self.screen.blit(self.Dice5.diceSpin[self.Dice5.SpinStatus], self.Dice5.diceRect)
        self.screen.blit(self.Dice6.diceSpin[self.Dice6.SpinStatus], self.Dice6.diceRect)
        self.Dice1.move()
        self.Dice2.move()
        self.Dice3.move()
        self.Dice4.move()
        self.Dice5.move()
        self.Dice6.move()
        if not self.stop and self.start:
            pygame.display.update()

    def creatmap3(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.BoTTon.start, self.BoTTon.startRect)
        self.screen.blit(self.BoTTon.stop, self.BoTTon.stopRect)
        self.screen.blit(self.BoTTon.end, self.BoTTon.endRect)
        self.screen.blit(self.BoTTon.rule, self.BoTTon.ruleRect)
        self.screen.blit(self.Dice1.diceStop[self.Dice1.StopStatus], self.Dice1.diceRect)
        self.screen.blit(self.Dice2.diceStop[self.Dice2.StopStatus], self.Dice2.diceRect)
        self.screen.blit(self.Dice3.diceStop[self.Dice3.StopStatus], self.Dice3.diceRect)
        self.screen.blit(self.Dice4.diceStop[self.Dice4.StopStatus], self.Dice4.diceRect)
        self.screen.blit(self.Dice5.diceStop[self.Dice5.StopStatus], self.Dice5.diceRect)
        self.screen.blit(self.Dice6.diceStop[self.Dice6.StopStatus], self.Dice6.diceRect)
        if self.stop and not self.start:
            pygame.display.update()

    def creatmap4(self, res, res111):
        for i in range(len(res)):
            tmp_st = 'Player{0}:{1}, {2}, {3}, {4}, {5}, {6}'.format(i+1, res[i][0]+1, res[i][1]+1, res[i][2]+1, res[i][3]+1, res[i][4]+1, res[i][5]+1)
            paly_res_tx = self.TxtFont.render(tmp_st, True, (255, 40, 40))
            self.screen.blit(paly_res_tx, (150, 200+(i*35)))
        zyuanb = self.TxtFont.render(str(self.zyuan), True, (0, 0, 0))
        self.screen.blit(zyuanb, (1050, 260))
        duitb = self.TxtFont.render(str(self.duit), True, (0, 0, 0))
        self.screen.blit(duitb, (1050, 310))
        sanhb = self.TxtFont.render(str(self.sanh), True, (0, 0, 0))
        self.screen.blit(sanhb, (1050, 360))
        sijinb = self.TxtFont.render(str(self.sijin), True, (0, 0, 0))
        self.screen.blit(sijinb, (1050, 410))
        erjub = self.TxtFont.render(str(self.erju), True, (0, 0, 0))
        self.screen.blit(erjub, (1050, 460))
        yixiub = self.TxtFont.render(str(self.yixiu), True, (0, 0, 0))
        self.screen.blit(yixiub, (1050, 510))

        for j in range(len(res111)):
            paer_st = 'palyer{0}: zhuangyuan:{1},duitang:{2},sanhong:{3},sijin:{4},erju:{5},yixiu:{6}'.format(j+1,
                res111[j][0], res111[j][1], res111[j][2], res111[j][3], res111[j][4], res111[j][5])
            paer_res_tx = self.TxtFont.render(paer_st, True, (0, 0, 0))
            self.screen.blit(paer_res_tx, (150, 580+(j*40)))
        pygame.display.update()

    def gameover(self, res111):
        GameOverFont = pygame.font.SysFont('微软雅黑', 80)
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.BoTTon.end, self.BoTTon.endRect)
        gameover_text = GameOverFont.render('Game Over', True, (0, 0, 0))
        self.screen.blit(gameover_text, (150, 100))
        for j in range(len(res111)):
            paer_st = 'palyer{0}: zhuangyuan:{1},duitang:{2},sanhong:{3},sijin:{4},erju:{5},yixiu:{6}'.format(j+1,
                res111[j][0], res111[j][1], res111[j][2], res111[j][3], res111[j][4], res111[j][5])
            paer_res_tx = self.TxtFont.render(paer_st, True, (0, 0, 0))
            self.screen.blit(paer_res_tx, (150, 580+(j*40)))
        pygame.display.update()

    def run(self):
        res = []
        tmp = []
        res111 = [[0 for i in range(6)] for j in range(8)]
        while True:
            self.clock.tick(20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT \
                        or (event.type == pygame.MOUSEBUTTONDOWN
                            and 0 <= event.pos[1] <= 86
                            and 500 <= event.pos[0] <= 900):
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and 100 <= event.pos[0] <= 300 and 0 <= event.pos[1] <= 86:
                    self.start = True
                    self.stop = False
                if event.type == pygame.MOUSEBUTTONDOWN and 300 <= event.pos[0] <= 500 and 0 <= event.pos[1] <= 87:
                    self.stop = True
                    self.start = False
                    self.Dice1.StopStatus = random.randint(0, 5)
                    self.Dice2.StopStatus = random.randint(0, 5)
                    self.Dice3.StopStatus = random.randint(0, 5)
                    self.Dice4.StopStatus = random.randint(0, 5)
                    self.Dice5.StopStatus = random.randint(0, 5)
                    self.Dice6.StopStatus = random.randint(0, 5)
                    tmp.append([self.Dice1.StopStatus, self.Dice2.StopStatus, self.Dice3.StopStatus, self.Dice4.StopStatus
                                ,self.Dice5.StopStatus, self.Dice6.StopStatus])
                    res.append(
                        [self.Dice1.StopStatus, self.Dice2.StopStatus, self.Dice3.StopStatus, self.Dice4.StopStatus
                            , self.Dice5.StopStatus, self.Dice6.StopStatus])
                    j = len(tmp)
                    if j > 0:
                        flageres = self.rewrdcacl(tmp[j - 1])
                        if flageres > -1:
                            res111[j - 1][flageres] += 1
                        if flageres == -2:
                            self.gameover(res111)
                    if len(tmp) == 8:
                        tmp = []
                if not self.start and not self.stop:
                    self.creatmap1()
                if self.start and not self.stop:
                    self.creatmap2()
                if not self.start and self.stop:
                    self.creatmap3()
                self.creatmap4(tmp, res111)


if __name__ == '__main__':
    Game()
