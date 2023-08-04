import math

b = int(input())
def ni(chislo):
    a = []
    n = 2
    while n < chislo:
        if math.gcd(n, chislo) == 1:
            a.append(n)
        n += 1
        print(a)
    for elem in a:
        print(elem, end=' ')

ni(b)