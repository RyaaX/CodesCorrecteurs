import numpy as np
import sys
from termcolor import colored, cprint

def bitErreur(message,matriceControle):
    R=np.mod(np.dot(matriceControle,message),2)
    for i in range (matriceControle.shape[1]) :
        if np.allclose(R,matriceControle[:,i]):
            print("erreur sur le bit : ",i+1)


def differenceMatrice(matrice1,matrice2):
    for i in range(matrice1.shape[1]):
        if np.allclose(matrice1[i],matrice2[i]):
            print(colored(i,'red'))
        else:
            print(colored(i, 'green'))




matriceControle=np.matrix([[0,0,0,1,1,1,1],[0,1,1,0,0,1,1],[1,0,1,0,1,0,1]])
