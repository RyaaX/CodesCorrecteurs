import numpy as np
G=np.matrix([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print("G=",G)
C=np.matrix([[1],[0],[1],[1]])
print("C=",C)
M=np.mod(np.dot(G,C),2)
print("M=",M)