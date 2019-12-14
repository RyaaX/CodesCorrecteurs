import numpy as np
from random import *


# Permet de générer des mots aléatoirement de taille "complexite".
# les mots sont généré avec comme condition de contenir au moin 2 bits à 1
def generateMot(complexite):
    mot = np.array([])
    compteur = 0
    while compteur <= 1:  # au moin 2 bits à 1
        mot = np.array([])
        compteur = 0
        for k in range(0, complexite):  # tirage aléatoire des bits
            bit = randint(0, 1)
            mot = np.insert(mot, k, bit)
            if bit == 1:
                compteur = compteur + 1
    return mot


# cette fonction permet d'ajouter 1 à un mots binaire
# elle nous permet de parcourir tous les mots binaire d'une certaine taille pour calculer la distance de hamming
def ajoutUnBinaire(mot):
    for k in range(1, mot.size + 1):
        var = mot[-k]
        if var == [1]:
            mot[-k] = [0]
        else:
            mot[-k] = [1]
            break
    return mot


# cette fonction calcul la distance de hamming entre 2 mots binaire de taille "nbBit"
def calculHamming(Mot1, Mot2, nbBit):
    distance = 0
    lenght = np.size(Mot1)
    for n in range(0, round(lenght / nbBit)):
        mot1 = Mot1[n]
        mot2 = Mot2[n]
        for k in range(0, nbBit):
            if mot1[k] != mot2[k]:
                distance = distance + 1
    return distance


# Cette fonction génére aléatoire une matrice de contrôle
# pour cela elle verifie plusieur condition:
#   Tous les mots doivent étre différent les un des autres en ligne
#   Tous les mots doivent être différent des un des autres et avoir au moins 2 bits à 1 en colone
def generateMatriceAleatoire(ligne, complexite):
    mot = generateMot(ligne)
    M = np.array([mot])
    bon = True
    nbEssaie = 0
    while bon:  # tant que l'on obtient pas une matrice valide on en créer une nouvelle
        nbEssaie += 1
        if nbEssaie == 1000:  # securité si aucune solution existe
            raise TimeoutError("Pas de solution trouvé")
        mot = generateMot(ligne)
        M = np.array([mot])
        for nb in range(1, complexite):  # Ajout aléatoire de tous les mots de la matrice
            bool = True
            while bool:
                mot = generateMot(ligne)
                dedans = False

                for l in M:  # on évite les doubles
                    dedans = dedans or np.equal(l, mot).all()

                if not dedans:
                    M = np.vstack([M, mot])
                    bool = False
        M = np.transpose(M)
        c = 0
        bon = False
        for l in M:  # aprés avoir transposé la matrice on verifie à nouveaux que chaque mot est différent des autres et qu'il ont aux moin 2 bits à 1.
            g = 0
            compteur = 0
            for bit in l:
                if bit == 1:
                    compteur = compteur + 1
            if compteur <= 1:  # si un mot a moin de 2 bits a 1, la matrice est fausse
                bon = True
                break
            for p in M:  # on compare le mot à tous les autres.
                if g != c:
                    bon = bon or np.equal(l, p).all()
                g += 1
            c += 1
    return M


# Cette fonction verifie si une matrice est génératrice
# matrice, la matrice génératrice
# nbBit, le nombre de bit des mots non codé
# complexite, le nombre de bit des mots de la matrice de controle
def verifierGenerateur(matrice, nbBit, complexite):
    init = np.array([[0]])
    listMot = 0
    minHam = -1
    for k in range(0, nbBit - 1):  # mot non codé initiale
        init = np.vstack([init, 0])
    for k in range(1, 2 ** nbBit + 1):  # pour chaque mot non codé
        motCode = init * matrice  # on le code

        if k == 1:
            listMot = np.array([motCode])  # initialisation de la liste des mots codé
        else:
            for g in range(1,
                           k - 1):  # on effectue la distance de hamming entre le nouveaux mot codé et tous ceux déjà créé
                distance = calculHamming(motCode, listMot[g], nbBit + complexite)
                if minHam == -1 or minHam > distance:  # on garde la plus petite distance
                    minHam = distance
            listMot = np.vstack([listMot, [motCode]])  # on ajoute le mot codé à la liste des mots codé

        init = ajoutUnBinaire(init)
    return minHam


# cette fonction permet de lié entre elles les matrices de parité et de controle.
# ligne, le nombre de bits des mot non codé
# complexite, le nombre de bits des mots de la matrice de controle
def generateMatriceGeneratrice(ligne, complexite):
    MG = "Pas assez de complexite"
    if (ligne <= complexite ** 2):
        M = np.identity(ligne)
        G = generateMatriceAleatoire(ligne, complexite)
        MG = np.concatenate((M, G), 1)
    return MG


ligne = 4 # le nombre de bits des mot non codé
complexite = 3 # le nombre de bits des mots de la matrice de controle
M = generateMatriceGeneratrice(ligne, complexite) # Generation de la matrice génératrice
print(M)
print("Distance de Hamming min :", verifierGenerateur(M, ligne, complexite)) # Calcul de la distance de hamming minimal
