import numpy as np

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


C=messageAlea()
print("Donnée a transmettre = ",C)
M=genererMessage(C)
print("Message a envoyer = ",M)
K=genererErreur(M)
print("Message reçu = ",K)
i=bitErreur(K)
print("Erreur sur le bit = ",i+1)
L=corrigerErreur(K,i)
print("Message corrigé = ",L)
P=decodeMessage(L)
print("Message Décodé = ",P)