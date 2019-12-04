import numpy as np
import OutilsCodeLineaire as OCL

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