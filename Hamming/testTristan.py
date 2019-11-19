import numpy as np
H=np.matrix([[0,0,0,1,1,1,1],[0,1,1,0,0,1,1],[1,0,1,0,1,0,1]])
m=np.array([[0],[1],[1],[0],[0],[1],[1]])
mavecerreur=np.array([[0],[1],[1],[0],[1],[1],[1]])
print(H.dtype)
print("H=",H)
print("m=",m)
R=np.mod(np.dot(H,m),2)
print("H*m=",R)
R=np.mod(np.dot(H,mavecerreur),2)
print("Avec une erreur H*m=",R)

for i in range (H.shape[1]) :
    if np.allclose(R,H[:,i]):
        print("erreur sur le bit ,",i+1)
    
