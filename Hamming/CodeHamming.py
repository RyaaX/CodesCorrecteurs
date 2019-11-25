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
    res= np.copy(message)
    res[b]=(res[b]+1)%2
    return res

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
    res = np.copy(message)
    res[i]=(res[i]+1)%2
    return res

def decodeMessage(message):
    D = np.matrix([[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
    return np.mod(np.dot(D, message), 2)

def differenceMatrice(matrice1,matrice2):
    for i in range(matrice1.shape[0]):
        if matrice1[i]==matrice2[i]:
            print(colored(matrice2[i],'green'),end='')
        else:
            print(colored(matrice2[i], 'red'),end='')
    print()

def afficheMatrice(matrice):
    res=np.copy(matrice)
    res.shape=(1,res.shape[0])
    return res

C=messageAlea()
print("Donnée a transmettre = ",afficheMatrice(C))
M=genererMessage(C)
print("Message a envoyer = ",afficheMatrice(M))
K=genererErreur(M)
print("Message reçu = ",afficheMatrice(K))
print("Affichage difference = ")
differenceMatrice(M,K)
i=bitErreur(K)
print("Erreur sur le bit = ",i+1)
L=corrigerErreur(K,i)
print("Message corrigé = ")
differenceMatrice(M,L)
P=decodeMessage(L)
print("Message Décodé = ",afficheMatrice(P))

