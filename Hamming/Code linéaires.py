import numpy as np
from random import *

def generateMot(complexite):
    mot = np.array([])
    for k in range(0,complexite):
        mot = np.insert(mot,k,randint(0,1))
    return mot


def generateMatriceUnique(ligne, complexite):
    mot = generateMot(complexite)
    M = np.array(mot)
    for ligne in M:
        print(np.equal(ligne,mot).all())
    return M


def generateMatriceGeneratrice(ligne, complexite):
    MG = 0
    if(ligne <= complexite**2):
        M = np.identity(ligne)
        G = generateMatriceUnique(ligne, complexite)
        MG = np.concatenate((M,G),1)
        print(M)
        print(G)
    return MG


print(generateMatriceGeneratrice(2,5))