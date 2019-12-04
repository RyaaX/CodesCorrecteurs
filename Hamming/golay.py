import numpy as np
from termcolor import colored


MatGeneratrice = np.matrix([
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
               [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
               [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
               [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
               [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
               [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
               [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
               [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
               [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
               ])


def genererMessage(message):
    M = np.mod(np.dot(MatGeneratrice, message), 2)
    return M


def messageAlea():
    return np.random.randint(2, size=(12, 1))

def afficheMatrice(matrice):
    res = np.copy(matrice)
    res.shape = (1, res.shape[0])
    for i in range(matrice.shape[0]):
        print(str(matrice[i]).strip('[]'), " ", end='')
    print()
    return res

def genererErreur(message, s):
    res = np.copy(message)
    for i in range(s):
        b = np.random.randint(len(message))
        res[b] = (res[b] + 1) % 2
    return res

def differenceMatrice(matrice1, matrice2):
    for i in range(matrice1.shape[0]):
        if matrice1[i] == matrice2[i]:
            print(colored(str(matrice2[i]).strip('[]'), 'green'), " ", end='')
        else:
            print(colored(str(matrice2[i]).strip('[]'), 'red'), " ", end='')
    print()

def partie(message,a):
    retour = np.matrix('0;0;0;0;0;0;0;0;0;0;0;0')
    for k in range(a,a+12):
        retour[k-a]=message[k]
    return retour

def affichageMatriceComplete(matrice):
    for i in range(matrice.shape[0]):
        for j in range(matrice.shape[1]):
            print(str(matrice.item((i, j))), " ", end='')
        print()

print("la matrice génératrice = ")
affichageMatriceComplete(MatGeneratrice)
message = messageAlea()
message=np.matrix('1;0;1;1;1;0;0;1;1;0;1;1')
print("Donnée a transmettre = ")
afficheMatrice(message)
M = genererMessage(message)
print("Message a envoyer = ")
afficheMatrice(M)
K = genererErreur(M, 1)
print("Message reçu = ")
afficheMatrice(K)
print("Affichage difference = ")
differenceMatrice(M, K)
partieDonnees=partie(K,0)
partiePartie=partie(K,11)
print(" Partie données = ")
afficheMatrice(partieDonnees)
print(" Partie parité = ")
afficheMatrice(partiePartie)


