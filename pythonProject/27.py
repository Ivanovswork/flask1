f = open('C:\\Users\\Никита\\Desktop\\27-B.txt')
n = int(str(f.readline()))
a = []
c = 0
print(n)
maximum = 0
b = []
for i in range(n):
    chislo = int(str(f.readline()))
    b.append((chislo))
    if chislo > 0 and chislo % 2 != 0:
        c += 1
    if c % 30 == 0:
        a.append(i)
print(a)
print(len(a))
for el in a:
    for elem in a:
       if elem - el < 30:
           continue
       elif sum(b[el:elem + 1]) > maximum:
            maximum = sum(b[el:elem + 1])
print(maximum)
