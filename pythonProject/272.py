f = open('C:\\Users\\Никита\\Desktop\\test.txt')
nn = list(map(int, f.readline().split()))
n = nn[0]
a = []
for i in range(999):
    a.append(0)
s = 0
con = []
for j in range(n):
    bb = list(map(int, f.readline().split()))
    b = bb[0]
    s += b
    ost = s % 5
    if a[ost - 1] == 0 and ost != 0:
        a.pop(ost - 1)
        a.insert(ost - 1, s)
    p = s - a[s % 5 - 1]
    if p != 0:
        con.append(p)
print(a)
print(con)
print(len(con))



