import numpy as np

motGenerateur = np.array([1, 0, 0, 0, 0, 1])


def ArraytoPolynomial(array):
    size = np.size(array)
    expo = [0x2070, 0x00B9, 0x00B2, 0x00B3, 0x2074, 0x2075, 0x2076, 0x2077, 0x2078, 0x2079]
    print(array)
    if array[0] == 1:
        print("1 ", end='')
    else:
        print("0 ", end='')
    for i in range(1, size):
        if array[i] == 1:
            print('+ x' + chr(expo[i]), end='')
    print()


def shifting(array):
    size = np.size(array)
    print('Matrice avant décalage : ')
    ArraytoPolynomial(array)
    i = size - 1
    while i > 0:
        if array[i] == 1:
            if i != 0:
                array[i] = 0
                if array[i - 1] == 1:
                    array[i - 1] = 0
                else:
                    array[i - 1] = 1
            else:
                array[0] = 0
                if array[size - 1] == 1:
                    array[size - 1] = 0
                else:
                    array[size - 1] = 1
            i = i - 1
        i = i - 1
    print('Matrice après décalage : ')
    ArraytoPolynomial(array)


shifting(motGenerateur)
