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

C=messageAlea()
print("C = ",C)
M=genererMessage(C)
print("M = ",M)
K=genererErreur(M)
print("K = ",K)
bitErreur(K)