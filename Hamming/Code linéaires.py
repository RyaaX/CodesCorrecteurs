import numpy as np
from random import *


def generateMot(complexite):
    mot = np.array([])
    for k in range(0, complexite):
        mot = np.insert(mot, k, randint(0, 1))
    return mot


def generateMatriceAleatoire(ligne, complexite):
    mot = generateMot(complexite)
    M = np.array([mot])
    for nb in range(1, ligne):
        bool = True
        while bool:
            mot = generateMot(complexite)
            dedans = False

            for l in M:
                dedans = dedans or np.equal(l, mot).all()

            if not dedans:
                M = np.vstack([M, mot])
                bool = False
    return M


def verifierGenerateur(matrice, nbBit):
    init = np.array([])
    for k in range(0, nbBit):
        init = np.insert(init, k, 0)
    for k in range(1, 2 ** nbBit+1):
        print(init)
        init = ajoutUnBinaire(init)


def ajoutUnBinaire(mot):
    for k in range(1, mot.size+1):
        var = mot[-k]
        if var == 1:
            mot[-k] = 0
        else:
            mot[-k] = 1
            break
    return mot


def generateMatriceGeneratrice(ligne, complexite):
    MG = "Pas assez de complexite"
    if (ligne <= complexite ** 2):
        M = np.identity(ligne)
        G = generateMatriceAleatoire(ligne, complexite)
        MG = np.concatenate((M, G), 1)
    return MG

verifierGenerateur([], 2)
# print(generateMatriceGeneratrice(5, 4))
