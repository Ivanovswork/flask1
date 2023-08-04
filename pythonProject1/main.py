a = []
m = 0
for i in range(5000):
    a.append(int(input()))
count = 0
s = 1
for i in range(len(a)):
    if i == len(a) - 1:
        break
    elif a[i] % 3 == 0 or a[i + 1] % 3 == 0:
        count += 1
        if a[i] + a[i + 1] > s:
            m = i
            b = a[i]
            c = a[i + 1]
            s = a[i] + a[i + 1]
print(count, s, b, c, m)
