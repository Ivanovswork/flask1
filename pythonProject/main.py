a = int(input())
summ = 0
s = 1000000
for i in range(a):
    b = []
    b = input().split()
    b = list(map(int, b))
    summ += max(b)
    if abs(b[0] - b[1]) < s:
        s = abs(b[0] - b[1])
if summ % 3 != 0:
    print(summ)
else:
    print(summ + s)

