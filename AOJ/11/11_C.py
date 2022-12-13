class Dice:
    def __init__(self, roll_numbers):  # 宣言
        self.frt = roll_numbers[0]  # 表面
        self.und = roll_numbers[1]  # 下面
        self.rit = roll_numbers[2]  # 右面
        self.lft = roll_numbers[3]  # 左面
        self.top = roll_numbers[4]  # 上面
        self.bak = roll_numbers[5]  # 裏面

    def roll(self, direction):  # 転がす
        # 保存
        sav_frt = self.frt
        sav_und = self.und
        sav_rit = self.rit
        sav_lft = self.lft
        sav_top = self.top
        sav_bak = self.bak
        # 保存終わり
        if direction == 'E':  # 東
            self.frt = sav_lft
            self.lft = sav_bak
            self.bak = sav_rit
            self.rit = sav_frt
        if direction == 'W':  # 西
            self.frt = sav_rit
            self.rit = sav_bak
            self.bak = sav_lft
            self.lft = sav_frt
        if direction == 'S':  # 南
            self.frt = sav_top
            self.top = sav_bak
            self.bak = sav_und
            self.und = sav_frt
        if direction == 'N':  # 北
            self.frt = sav_und
            self.und = sav_bak
            self.bak = sav_top
            self.top = sav_frt

    def getTop(self):  # 表面の数字を表示
        return self.frt

    def rightSpin(self):
        sav_top = self.top
        sav_rit = self.rit
        sav_lft = self.lft
        sav_und = self.und

        self.top = sav_lft
        self.lft = sav_und
        self.und = sav_rit
        self.rit = sav_top

    def isSameDice(self, dice2):

        for i in range(4):
            dice2.roll("S")
            for j in range(4):
                dice2.rightSpin()
                if self.frt == dice2.frt and self.und == dice2.und and self.rit == dice2.rit and \
                   self.lft == dice2.lft and self.top == dice2.top and self.bak == dice2.bak:
                    return True
            # j-end
        # i-end
        # 右を見る
        dice2.roll("W")
        for i in range(4):
            dice2.rightSpin()
            if self.frt == dice2.frt and self.und == dice2.und and self.rit == dice2.rit and \
               self.lft == dice2.lft and self.top == dice2.top and self.bak == dice2.bak:
                return True
        # 左を見る
        dice2.roll("E")
        dice2.roll("E")
        for i in range(4):
            dice2.rightSpin()
            if self.frt == dice2.frt and self.und == dice2.und and self.rit == dice2.rit and \
               self.lft == dice2.lft and self.top == dice2.top and self.bak == dice2.bak:
                return True
        return False


roll_numbers1 = list(map(int, input().split()))
roll_numbers2 = list(map(int, input().split()))
dice1 = Dice(roll_numbers1)
dice2 = Dice(roll_numbers2)
if dice1.isSameDice(dice2):
    print("Yes")
else:
    print("No")
