x = int(input())
y = int(input())
n = int(input())
x1 = abs(x - y)
x2 = abs(x - y)
list1 = []
for q in range(n):
    k = int(input())
    list1.append(k)
    if abs(x - k) < x1:
        x1 = abs(x - k)
    if abs(y - k ) < x2:
        x2 = abs(y - k)
g = x1 + x2 + 1
h=abs(x - y)
if g < h:
    print(g)
else:
    print(h)