n = int(input())  # nを入力
cards = [[True for i in range(13)] for j in range(4)]  # 4*13の二次元配列(初期値:True→未所持)
pattern = ["S", "H", "C", "D"]  # S:0 H:1 C:2 D:3
for i in range(n):  # n回入力
    char, num = input().split()  # char:文字　num:数字
    num = int(num)  # num:を整数型に
    cards[pattern.index(char)][num-1] = False  # False:所持　num-1:1~13→0~12
for i in range(4):  # 柄の種類
    for j in range(13):  # 数字の数
        if cards[i][j]:  # Trueで動作
            print(pattern[i], j+1)
