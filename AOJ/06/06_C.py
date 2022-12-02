room = [[[0 for i in range(10)] for j in range(3)]for k in range(4)]
n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    room[b-1][f-1][r-1] += v
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(f" {room[i][j][k]}", end="")
        # k-end
        print("", end="\n")
    # j-end
    if (i != 3):
        print("####################")
