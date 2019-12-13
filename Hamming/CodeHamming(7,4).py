import numpy as np
from termcolor import colored
# Simule le fonctionnement de la transmission d'un message  avec un code correcteur de Hamming(7,4)
# Le programme demande le nombre d'erreurs à insérer, le code de Hamming(7,4) ne détecte qu'une seule erreur.

def messageAlea(): #génére et renvoie un message de données de 4 bits à transmettre
    return np.random.randint(2, size=(4, 1))


def genererMessage(message): #génére le message de 7 bits à envoyer
    G = np.matrix([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) # matrice génératrice
    M = np.mod(np.dot(G, message), 2)
    return M


def genererErreur(message, s): #permet de simuler un nombre s d'erreurs
    res = np.copy(message)
    if s > 0:
        for i in range(s):
            b = np.random.randint(len(message))
            res[b] = (res[b] + 1) % 2
    return res


def bitErreur(message): #renvoie le bit sur lequel il ya une erreur
    matriceControle = np.matrix([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]]) #matrice de controle
    R = np.mod(np.dot(matriceControle, message), 2)
    if (R == np.zeros([1, 3])).all(): #si il n'y a pas d'erreurs, R est une matrice nulle
        return -1
    else:
        for i in range(matriceControle.shape[1]):
            if np.allclose(R, matriceControle[:, i]):
                return i    #renvoie le n° de bit sur lequel une erreur à été trouvé


def corrigerErreur(message, i): #permet d'inverser le bit n°i du message
    res = np.copy(message)
    res[i] = (res[i] + 1) % 2
    return res


def decodeMessage(message): # decode le message, prend 7 bits en entrée et renvoie 4 bits
    D = np.matrix([[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
    return np.mod(np.dot(D, message), 2)


def differenceMatrice(matrice1, matrice2): #affichage de différence de 2 matrices, les bit équivalents sont en vert, les différents sont en rouge
    for i in range(matrice1.shape[0]):
        if matrice1[i] == matrice2[i]:
            print(colored(str(matrice2[i]).strip('[]'), 'green'), " ", end='')
        else:
            print(colored(str(matrice2[i]).strip('[]'), 'red'), " ", end='')
    print()


def afficheMatrice(matrice): #permet un affichage propre de matrices colonnes
    res = np.copy(matrice)
    res.shape = (1, res.shape[0])
    for i in range(matrice.shape[0]):
        print(str(matrice[i]).strip('[]'), " ", end='')
    print()
    return res


def commentEstTrouveLeBitDErreur(message): #explique le fonctionnement du programme
    matriceControle = np.matrix([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])
    R = np.mod(np.dot(matriceControle, message), 2)
    print("La matrice de controle :")
    affichageMatriceComplete(matriceControle)
    print("Le message")
    afficheMatrice(message)
    print("Le message * la matrice de controle")
    affichageMatriceComplete(R)
    affichageMatriceBitErreur(matriceControle, bitErreur(message))


def affichageMatriceComplete(matrice): #permet d'afficher des matrices
    for i in range(matrice.shape[0]):
        for j in range(matrice.shape[1]):
            print(str(matrice.item((i, j))), " ", end='')
        print()


def affichageMatriceBitErreur(matrice, bit):
    print("  1  2  3  4  5  6  7")
    print(" --------------------")
    for i in range(matrice.shape[0]):
        print('| ', end='');
        for j in range(matrice.shape[1]):
            if (j == bit):
                print(colored(str(matrice.item((i, j))), 'green'), " ", end='')
            else:
                print(str(matrice.item((i, j))), " ", end='')
        print('| ', end='');
        print()
    print(" ---------------------")


C = messageAlea()
print("Donnée a transmettre = ")
afficheMatrice(C)
M = genererMessage(C)
print("Message a envoyer = ")
afficheMatrice(M)
s = input('Nombre erreurs a inserer (entier entre 0 et 7) : ')
K = genererErreur(M, int(s))
print("Message reçu (avec erreurs) = ")
afficheMatrice(K)
print("Affichage difference (erreurs en rouge) = ")
differenceMatrice(M, K)
i = bitErreur(K)
if(i==-1) :
    print("Pas d'erreurs dans le message reçu")
    L = K
else:
    print("Erreur sur le bit = ", i + 1)
    L = corrigerErreur(K, i)
    print("Message corrigé = ")
    differenceMatrice(M, L)
P = decodeMessage(L)
print("Message Décodé = ")
differenceMatrice(C, P)
commentEstTrouveLeBitDErreur(K)
