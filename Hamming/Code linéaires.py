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


def verifierGenerateur(matrice, nbBit, complexite):
    init = np.array([[0]])
    listMot = 0
    minHam = -1
    for k in range(0, nbBit-1):
        init = np.vstack([init, 0])
    for k in range(1, 2 ** nbBit+1):
        motCode = init * matrice

        if k == 1:
            listMot = np.array([motCode])
        else:
            listMot = np.vstack([listMot, [motCode]])
            for g in range(1,k-1):
                distance = calculHamming(motCode, listMot[g], nbBit+complexite)
                if minHam == -1 or minHam > distance:
                    minHam = distance

        init = ajoutUnBinaire(init)
    return minHam

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

def ajoutUnBinaire(mot):
    for k in range(1, mot.size+1):
        var = mot[-k]
        if var == [1]:
            mot[-k] = [0]
        else:
            mot[-k] = [1]
            break
    return mot


def generateMatriceGeneratrice(ligne, complexite):
    MG = "Pas assez de complexite"
    if (ligne <= complexite ** 2):
        M = np.identity(ligne)
        G = generateMatriceAleatoire(ligne, complexite)
        MG = np.concatenate((M, G), 1)
    return MG   

M = generateMatriceGeneratrice(3, 10)
H = verifierGenerateur(M, 3, 10)

print("Matrice : ")
print(M)
print("Distance de hamming minimal : ")
print(H)