import numpy as np


def messageAlea():
    return np.random.randint(2, size=(4,1))

def genererMessage():
    G=np.matrix([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    C=messageAlea()
    M=np.mod(np.dot(G,C),2)
    print("M=",M)
    return M

genererMessage()