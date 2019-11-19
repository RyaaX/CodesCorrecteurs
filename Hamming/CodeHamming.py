import numpy as np


def messagealea():
    return np.random.randint(2, size=(4,1))

G=np.matrix([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print("G=",G)
C=messagealea()
print("C=",C)
M=np.mod(np.dot(G,C),2)
print("M=",M)
