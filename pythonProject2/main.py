v = 100
while v < 10000:
    a, b = 0, 1
    v += 1
    x = v
    a = a + 1
    b = b * (x % 10)
    x = x // 10
    if a == 4 and b == 24:
        print(v)
        break

