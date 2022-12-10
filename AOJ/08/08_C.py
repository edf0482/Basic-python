a_z = {}
for i in range(ord('a'), ord('z')+1):
    a_z[chr(i)] = 0
    # ord:char→ASCII
    # chr:ASCII→char

# i-end
while True:
    try:
        str = input()
        str = str.replace(" ", "")  # 空白消去
        for c in str:
            num = ord(c)
            # A~Z:65~90
            # a~z:97~122
            if 65 <= num and num <= 90:
                a_z[chr(num+32)] += 1
            elif 97 <= num and num <= 122:
                a_z[c] += 1
        # c-end
    except EOFError:
        break

for c in a_z:
    print(c, ':', a_z[c])
