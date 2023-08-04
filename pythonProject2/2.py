cor = int(input())
dlin = int(input())
stup = int(input())
a = cor + dlin
if stup % a > dlin:
    b = 2 * (stup // a)
    print(b + 2)
elif stup % a == 0:
    b = 2 * (stup // a)
    print(b)
else:
    b = 2 * (stup // a)
    print(b + 1)