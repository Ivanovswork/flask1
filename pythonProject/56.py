a = list(map(int, input().split()))
spisok_chisel = []
spisok_podhodyashih = []
for i in range(a[1]):
    spisok_chisel.append(int(input()))
spisok_chisel.sort()
for elm in spisok_chisel:
    if sum(spisok_podhodyashih) > a[0]:
        del spisok_podhodyashih[-1]
        break
    else:
        spisok_podhodyashih.append(elm)
k = sum(spisok_podhodyashih)
razn = sum(spisok_chisel) - k
c = max(spisok_podhodyashih)
def maximal(raz):
    global c, spisok_podhodyashih
    if raz == 0:
        return sum(spisok_podhodyashih)
    elif (raz + c) in spisok_podhodyashih:
        spisok_podhodyashih.remove(c)
        spisok_podhodyashih.append(raz + c)
        return sum(spisok_podhodyashih)
    else:
        return maximal(raz - 1)
print(maximal(razn))