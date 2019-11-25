import numpy as np
from random import *

def generateMot(complexite):
    mot = np.array([])
    for k in range(0,complexite):
        mot = np.insert(mot,k,randint(0,1))
    return mot


def generateMatriceAleatoire(ligne, complexite):
    mot = generateMot(complexite)
    M = np.array(mot)
    for nb in range(1,ligne):
        bool = True
        while bool:
            mot = generateMot(complexite)
            dedans = False

            for l in M:
                 dedans = dedans or np.equal(l,mot).all()

            if not dedans:
                M = np.vstack([M,mot])
                bool = False
    return M


def generateMatriceGeneratrice(ligne, complexite):
    MG = "Pas assez de complexite"
    if(ligne <= complexite**2):
        M = np.identity(ligne)
        G = generateMatriceAleatoire(ligne, complexite)
        MG = np.concatenate((M,G),1)
    return MG


print(generateMatriceGeneratrice(4,3))