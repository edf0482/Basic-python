W, H, x, y, r = map(int, input().split())
flag_x = False
flag_y = False
if (0 <= x-r and x+r <= W):
    flag_x = True
else:
    flag_x = False
if (0 <= y-r and y+r <= H):
    flag_y = True
else:
    flag_y = False
if (flag_x and flag_y):
    print("Yes")
else:
    print("No")
