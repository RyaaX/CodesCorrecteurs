import numpy as np
from termcolor import colored


def messageAlea():
    return np.random.randint(2, size=(4, 1))


def genererMessage(message):
    G = np.matrix([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    M = np.mod(np.dot(G, message), 2)
    return M


def genererErreur(message, s):
    res = np.copy(message)
    if s > 0:
        for i in range(s):
            b = np.random.randint(len(message))
            res[b] = (res[b] + 1) % 2
    return res



def bitErreur(message):
    matriceControle = np.matrix([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])
    R = np.mod(np.dot(matriceControle, message), 2)
    for i in range(matriceControle.shape[1]):
        if np.allclose(R, matriceControle[:, i]):
            return i


def corrigerErreur(message, i):
    res = np.copy(message)
    res[i] = (res[i] + 1) % 2
    return res


def decodeMessage(message):
    D = np.matrix([[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
    return np.mod(np.dot(D, message), 2)


def differenceMatrice(matrice1, matrice2):
    for i in range(matrice1.shape[0]):
        if matrice1[i] == matrice2[i]:
            print(colored(str(matrice2[i]).strip('[]'), 'green'), " ", end='')
        else:
            print(colored(str(matrice2[i]).strip('[]'), 'red'), " ", end='')
    print()


def afficheMatrice(matrice):
    res = np.copy(matrice)
    res.shape = (1, res.shape[0])
    for i in range(matrice.shape[0]):
        print(str(matrice[i]).strip('[]'), " ", end='')
    print()
    return res


def commentEstTrouveLeBitDErreur(message):
    matriceControle = np.matrix([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])
    R = np.mod(np.dot(matriceControle, message), 2)
    print("La matrice de controle :")
    affichageMatriceComplete(matriceControle)
    print("Le message")
    afficheMatrice(message)
    print("Le message * la matrice de controle")
    affichageMatriceComplete(R)
    affichageMatriceBitErreur(matriceControle, bitErreur(message))


def affichageMatriceComplete(matrice):
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
print("Message reçu = ")
afficheMatrice(K)
print("Affichage difference = ")
differenceMatrice(M, K)
i = bitErreur(K)
print("Erreur sur le bit = ", i + 1)
L = corrigerErreur(K, i)
print("Message corrigé = ")
differenceMatrice(M, L)
P = decodeMessage(L)
print("Message Décodé = ")
differenceMatrice(C, P)
commentEstTrouveLeBitDErreur(K)
