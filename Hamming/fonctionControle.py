import numpy as np

def bitErreur(message,matriceControle):
    for i in range (matriceControle.shape[1]) :
        if np.allclose(message,matriceControle[:,i]):
            print("erreur sur le bit : ",i+1)

matriceControle=np.matrix([[0,0,0,1,1,1,1],[0,1,1,0,0,1,1],[1,0,1,0,1,0,1]])
