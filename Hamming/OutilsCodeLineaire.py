import numpy as np
from random import *

def generateMot(complexite):
    mot = np.array([])
    compteur = 0
    while compteur <= 1:
        mot = np.array([])
        compteur = 0
        for k in range(0, complexite):
            bit = randint(0, 1)
            mot = np.insert(mot, k, bit)
            if bit == 1:
                compteur = compteur+1
    return mot

def ajoutUnBinaire(mot):
    for k in range(1, mot.size+1):
        var = mot[-k]
        if var == [1]:
            mot[-k] = [0]
        else:
            mot[-k] = [1]
            break
    return mot

def calculHamming(Mot1, Mot2, nbBit):
    distance = 0
    lenght = np.size(Mot1)
    for n in range(0, round(lenght/nbBit)):
        mot1 = Mot1[n]
        mot2 = Mot2[n]
        for k in range(0, nbBit):
            if mot1[k] != mot2[k]:
                distance = distance + 1
    return distance

def generateMatriceAleatoire(ligne, complexite):
    mot = generateMot(ligne)
    M = np.array([mot])
    bon = True
    nbEssaie = 0
    while bon:
        nbEssaie += 1
        if nbEssaie == 1000:
            raise TimeoutError("Pas de solution trouvé")
        mot = generateMot(ligne)
        M = np.array([mot])
        for nb in range(1, complexite):
            bool = True
            while bool:
                mot = generateMot(ligne)
                dedans = False

                for l in M:
                    dedans = dedans or np.equal(l, mot).all()

                if not dedans:
                    M = np.vstack([M, mot])
                    bool = False
        M = np.transpose(M)
        c = 0
        bon = False
        for l in M:
            g = 0
            compteur = 0
            for bit in l:
                if bit == 1:
                    compteur = compteur+1
            if compteur <= 1:
                bon = True
                break
            for p in M:
                if g != c:
                    bon = bon or np.equal(l, p).all()
                g += 1
            c += 1
    return M