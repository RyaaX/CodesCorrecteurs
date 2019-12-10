import time

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
            for g in range(1,k-1):
                distance = OCL.calculHamming(motCode, listMot[g], nbBit+complexite)
                if minHam == -1 or minHam > distance:
                    minHam = distance
            listMot = np.vstack([listMot, [motCode]])

        init = OCL.ajoutUnBinaire(init)
    return minHam

def generateMatriceGeneratrice(ligne, complexite):
    MG = "Pas assez de complexite"
    if (ligne <= complexite ** 2):
        M = np.identity(ligne)
        G = OCL.generateMatriceAleatoire(ligne, complexite)
        MG = np.concatenate((M, G), 1)
    return MG


def test(minimal, nb, bool):
    compteur = 0
    nombre = 0
    M = 0
    H = 0
    while(nombre < minimal and compteur < nb):
        compteur += 1
        M = generateMatriceGeneratrice(4, 3)
        H = verifierGenerateur(M, 4, 3)
        nombre = H

    if bool == True:
        if(H < minimal):
            print("Pas de solution trouvée")
        else:
            print("Matrices testées : %s" %compteur)
            print("Matrice : ")
            print(M)
            print("Distance de hamming minimal : %s" %H)
    return compteur

def moyenne(minimal, nb, nb2):
    somme = 0
    for k in range(1,nb2-1):
        somme += test(minimal, nb, False)
    somme += test(minimal,nb,True)
    return somme/nb2

start_time = time.time()
nbtest = 10000
moy = moyenne(3,1000, nbtest)
temps_final = time.time() - start_time
print("Moyenne : %s" %moy)
print("temps : %ss" %(round(temps_final*100)/100))
print("tempsMoyen : %ss" %(round((temps_final/nbtest)*100)/100))
