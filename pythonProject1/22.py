a = list(input())
count = 0
b = []
c = 0
v = 'v'
print(a)
for elem in a:
    c += 1
    if c == len(a):
        break
    elif elem == v:
        b.append(count)
        count = 1
    else:
        count += 1
    v = elem
print(b)
print(max(b))

