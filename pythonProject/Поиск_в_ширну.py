from collections import deque
spisok = {}
spisok['you'] = ['alice', 'tom', 'bob']
spisok['alice'] = ['anuj', 'pegg']
spisok['tom'] = ['andr', 'alice']
spisok['bob'] = ['meny']
spisok['anuj'] = []
spisok['pegg'] = []
spisok['andr'] = []
spisok['meny'] = []

def person(name):
    prodov_or_net = {}
    prodov_or_net['alice'] = False
    prodov_or_net['tom'] = False
    prodov_or_net['bob'] = False
    prodov_or_net['anuj'] = False
    prodov_or_net['pegg'] = True
    prodov_or_net['andr'] = True
    prodov_or_net['meny'] = True
    return prodov_or_net[name]


def mango(spisok):
    naity = deque()
    naity += spisok['you']
    prov = []
    while naity:
        pesona = naity.popleft()
        if pesona not in prov:
            if person(pesona):
                return pesona
                break
            else:
                naity += spisok[pesona]
                prov.append(pesona)
    return 'govno'


print(mango(spisok))
