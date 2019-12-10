import numpy as np

motGenerateur = np.array([1, 0, 0, 1, 0, 0])


def ArraytoPolynomial(array):
    size = np.size(array)
    expo = [0x2070, 0x00B9, 0x00B2, 0x00B3, 0x2074, 0x2075, 0x2076, 0x2077, 0x2078, 0x2079]
    print(array)
    if array[0] == 1:
        print("1", end='')
    for i in range(1, size):
        if array[i] == 1:
            print(' + x' + chr(expo[i]), end='')
    print()

def shifting(array):
    poly = np.polynomial.Polynomial(array)
    x =np.polynomial.Polynomial(0,1)
    print(poly)
    np.polynomial.polymul(poly,x)




ArraytoPolynomial(motGenerateur)
shifting(motGenerateur)
