import random


def initialisation(n):
    return [['.' for i in range(n)] for j in range(n)]

def affichage():
    n = int(len(G))
    for i in range(n):
        for j in range(n):
            print(G[i][j],end=" ")
        print()

def position():
    n = int(len(G))
    pos = random.randint(0,n-1)
    return pos

def axe():
    rand = random.randint(0,1)
    if rand == 0:
        return 'vertical'
    else:
        return 'horizontal'

def sens():
    rand = random.randint(0,1)
    if rand == 0:
        return '+'
    else:
        return '-'

def controlPositionVide(maposX, maposY):
    if G[maposX][maposY] == '.':
        return True

def controlPositionnement(laposX, laposY, laaxe, lasens, lataille):
    cpt = 0
    n = int(len(G))
    if laaxe == 'vertical' and lasens == '+':
        if laposY + lataille < n:
            for i in range(lataille):
                if G[laposY + i][laposX] != '.':
                    break
                else:
                    cpt += 1
    elif laaxe == 'vertical' and lasens == '-':
        if laposY - lataille > 0:
            for i in range(lataille):
                if G[laposY - i][laposX] != '.':
                    break
                else:
                    cpt += 1
    elif laaxe == 'horizontal' and lasens == '+':
        if laposX + lataille < n:
            for i in range(lataille):
                if G[laposY][laposX + i] != '.':
                    break
                else:
                    cpt += 1
    elif laaxe == 'horizontal' and lasens == '-':
        if laposX - lataille > 0:
            for i in range(lataille):
                if G[laposY][laposX - i] != '.':
                    break
                else:
                    cpt +=1
    if cpt == lataille:
        return True
    else:
        return False

def placer(uneposX, uneposY, uneaxe, unesens, unetaille):
    if uneaxe == 'vertical' and unesens == '+':
            for i in range(unetaille):
                G[uneposY + i][uneposX] = '\u25A0'

    elif uneaxe == 'vertical' and unesens == '-':
            for i in range(unetaille):
                G[uneposY - i][uneposX] = '\u25A0'
    elif uneaxe == 'horizontal' and unesens == '+':
            for i in range(unetaille):
                G[uneposY][uneposX + i] = '\u25A0'
    elif uneaxe == 'horizontal' and unesens == '-':
            for i in range(unetaille):
                G[uneposY][uneposX - i] = '\u25A0'

def positionnement():
    # Placement du porte avion
    tab = [5,4,3,3,2]
    for i in range(4):
        while True:
            leposX = position()
            leposY = position()
            lesens = sens()
            leaxe = axe()
            letaille = tab[i]
            if controlPositionVide(leposX, leposY) == True and controlPositionnement(leposX, leposY, leaxe,lesens, letaille):
                placer(leposX, leposY, leaxe, lesens, letaille)
                break
    

G = initialisation(20)

positionnement()
affichage()
