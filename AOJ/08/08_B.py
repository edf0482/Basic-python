while True:
    x = input()
    if x != '0':
        sum = 0
        for c in x:
            sum += int(c)
        # c-end
        print(sum)
    else:
        break
