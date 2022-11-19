a, b, c = map(int, input().split())
if a > b:
    s = a
    a = b
    b = s
if b > c:
    s = b
    b = c
    c = s
if a > b:
    s = a
    a = b
    b = s
print(a, b, c)
