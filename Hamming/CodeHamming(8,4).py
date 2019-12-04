import numpy as np
from termcolor import colored


def messageAlea():
    return np.random.randint(2, size=(4, 1))


def genererMessage(message):
    G = np.matrix([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
                   [1, 1, 1, 0]])
    M = np.mod(np.dot(G, message), 2)
    return M


def genererErreur(message,s):
    res = np.copy(message)
    for i in range(s):
        b = np.random.randint(len(message))
        res[b] = (res[b] + 1) % 2
    return res


def bitErreur(message):
    matriceControle = np.matrix([[0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0]])
    R = np.mod(np.dot(matriceControle, message), 2)
    if (R == np.zeros([1, 3])).all():
        return -1
    else:
        if parite(message)!=message[7] :
            print('erreur bit parite')
            for i in range(matriceControle.shape[1]):
                if np.allclose(R, matriceControle[:, i]):
                    return i
        else :
            return -2

def parite(message):
    cpt=0
    for i in range(message.shape[0]-1):
        cpt +=message[i]
    return cpt%2



def corrigerErreur(message, i):
    res = np.copy(message)
    res[i] = (res[i] + 1) % 2
    return res


def decodeMessage(message):
    D = np.matrix(
        [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]])
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


C = messageAlea()
print("Donnée a transmettre = ")
afficheMatrice(C)
M = genererMessage(C)
print("Message a envoyer = ")
afficheMatrice(M)
s = input('Nombre erreurs a inserer')
K = genererErreur(M, int(s))
print("Message reçu = ")
afficheMatrice(K)
print("Affichage difference = ")
differenceMatrice(M, K)
i = bitErreur(K)
if i == -1:
    print("Pas d'erreurs dans le message reçu")
    L = K
elif i==-2 :
    print('Au moins deux erreurs')
    print('On ne peut pas decoder le message, il faut le renvoyer')
else :
    print("Erreur sur le bit = ", i + 1)
    L = corrigerErreur(K, i)
    print("Message corrigé = ")
    differenceMatrice(M, L)
if i!=-2 :
    P = decodeMessage(L)
    print("Message Décodé = ")
    differenceMatrice(C, P)
