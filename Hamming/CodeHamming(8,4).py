import numpy as np
from termcolor import colored
# Simule le fonctionnement de la transmission d'un message  avec un code correcteur de Hamming(8,4)
# Le programme demande le nombre d'erreurs à insérer, le code de Hamming(8,4) détecte une erreur, ou un nombre pair d'erreurs.

def messageAlea(): #génére et renvoie un message de données de 4 bits à transmettre
    return np.random.randint(2, size=(4, 1))


def genererMessage(message): #génére le message de 7 bits à envoyer
    G = np.matrix([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
                   [1, 1, 1, 0]])
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
    matriceControle = np.matrix([[0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0]])
    R = np.mod(np.dot(matriceControle, message), 2)
    if (R == np.zeros([1, 3])).all():
        return -1   #si il n'y a pas d'erreurs, R est une matrice nulle
    else:
        if parite(message) != message[7]: # Si le bit de parité global n'est pas bon, il y un nombre impair d'erreur
            print('erreur bit parite')
            for i in range(matriceControle.shape[1]):
                if np.allclose(R, matriceControle[:, i]):
                    return i # on renvoie donc le bit sur lequel il ya une erreur (le code renvoie un bit aleatoire si il y a 3 ou plus erreur)
        else:
            return -2 # Si le bit de parité global est bon, il y un nombre pair d'erreur, on ne peut pas le corriger


def parite(message): #permet de determiner la parite d'un message
    cpt = 0
    for i in range(message.shape[0] - 1):
        cpt += message[i]
    return cpt % 2


def corrigerErreur(message, i): #permet d'inverser le bit n°i du message
    res = np.copy(message)
    res[i] = (res[i] + 1) % 2
    return res


def decodeMessage(message): # decode le message, prend 8 bits en entrée et renvoie 4 bits
    D = np.matrix(
        [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]])
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


C = messageAlea()
print("Donnée a transmettre = ")
afficheMatrice(C)
M = genererMessage(C)
print("Message a envoyer = ")
afficheMatrice(M)
s = input('Nombre erreurs a inserer (entier entre 0 et 8) : ')
K = genererErreur(M, int(s))
print("Message reçu (avec erreurs) = ")
afficheMatrice(K)
print("Affichage difference (erreurs en rouge) = ")
differenceMatrice(M, K)
i = bitErreur(K)
if i == -1:
    print("Pas d'erreurs dans le message reçu")
    L = K
elif i == -2:
    print('Au moins deux erreurs')
    print('On ne peut pas decoder le message, il faut le renvoyer')
else:
    print("Erreur sur le bit = ", i + 1)
    L = corrigerErreur(K, i)
    print("Message corrigé = ")
    differenceMatrice(M, L)
if i != -2:
    P = decodeMessage(L)
    print("Message Décodé = ")
    differenceMatrice(C, P)
