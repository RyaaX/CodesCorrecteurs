import numpy as np
import OutilsCodeLineaire as OCL

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
                distance = OCL.calculHamming(motCode, listMot[g], nbBit+complexite)
                if minHam == -1 or minHam > distance:
                    minHam = distance

        init = OCL.ajoutUnBinaire(init)
    return minHam

def generateMatriceGeneratrice(ligne, complexite):
    MG = "Pas assez de complexite"
    if (ligne <= complexite ** 2):
        M = np.identity(ligne)
        G = OCL.generateMatriceAleatoire(ligne, complexite)
        MG = np.concatenate((M, G), 1)
    return MG   

M = generateMatriceGeneratrice(5, 30)
H = OCL.verifierGenerateur(M, 5, 30)

print("Matrice : ")
print(M)
print("Distance de hamming minimal : ")
print(H)