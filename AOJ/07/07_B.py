while True:
    n, x = map(int, input().split())
    if n != 0 or x != 0:
        count = 0
        for i in range(1, n+1):  # 1~n
            for j in range(i+1, n+1):  # i+1~n
                for k in range(j+1, n+1):  # j+1~n
                    if i+j+k == x:
                        count += 1
                # k-end
            # j-end
        # i-end
        print(count)
    else:
        break
