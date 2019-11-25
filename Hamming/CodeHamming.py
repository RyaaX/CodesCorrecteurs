import numpy as np
from termcolor import colored


def messageAlea():
    return np.random.randint(2, size=(4,1))

def genererMessage(message):
    G=np.matrix([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    M=np.mod(np.dot(G,message),2)
    return M

def genererErreur(message):
    b=np.random.randint(len(message))
    message[b]=(message[b]+1)%2
    return message

def bitErreur(message):
    matriceControle = np.matrix([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])
    for i in range (matriceControle.shape[1]) :
        if np.allclose(message,matriceControle[:,i]):
            print("erreur sur le bit : ",i+1)

def bitErreur(message):
    matriceControle = np.matrix([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])
    R=np.mod(np.dot(matriceControle,message),2)
    for i in range (matriceControle.shape[1]) :
        if np.allclose(R,matriceControle[:,i]):
            return i

def corrigerErreur(message,i):
    message[i]=(message[i]+1)%2
    return message

def decodeMessage(message):
    D = np.matrix([[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
    return np.mod(np.dot(D, message), 2)

def differenceMatrice(matrice1,matrice2):
    for i in range(matrice1.shape[0]):
        if matrice1[i]==matrice2[i]:
            print(colored(matrice1[i],'green'))
        else:
            print(colored(matrice1[i], 'red'))


C=messageAlea()
print("Donnée a transmettre = ",C)
M=genererMessage(C)
print("Message a envoyer = ",M)
K=genererErreur(M)
print("Message reçu = ",K)
print("Affichage difference = ")
differenceMatrice(M,K)
i=bitErreur(K)
print("Erreur sur le bit = ",i+1)
L=corrigerErreur(K,i)
print("Message corrigé = ",L)
P=decodeMessage(L)
print("Message Décodé = ",P)
