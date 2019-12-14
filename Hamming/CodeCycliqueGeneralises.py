import numpy as np

motGenerateur = np.array([1, 1, 0, 1, 0, 0, 0])


# Affiche les matrices sous forme de polynôme
def ArraytoPolynomial(array):
    size = np.size(array)
    expo = [0x2070, 0x00B9, 0x00B2, 0x00B3, 0x2074, 0x2075, 0x2076, 0x2077, 0x2078, 0x2079]
    print(array)
    if array[0] == 1:
        print("1", end='')
    else:
        print("0", end='')
    for i in range(1, size):
        if array[i] == 1:
            print(' + x' + chr(expo[i]), end='')
    print()


# Permet d'effectuer une permutation circulaire
def shifting(array):
    size = np.size(array)
    # print('Matrice avant décalage : ')
    # ArraytoPolynomial(array)

    shifted = np.zeros(size, dtype=int)

    for i in range(size):
        if array[i] == 1:
            shifted[(i + 1) % 7] = 1

    # print('Matrice après décalage : ')         #Décommenter ces lignes pour voir s'afficher les matrices après
    # ArraytoPolynomial(shifted)                 # permutation circulaire
    return shifted


# Compare si deux matrices lignes sont identiques
def comparerMatrice(array1, array2):
    res = True
    for i in range(np.size(array1)):
        if array1[i] != array2[i]:
            res = False
    return res


# Affiche l'ensemble des permutations circulaires différentes d'un polynôme et retourne une matrice génératrice du code C
def permutations(array):
    ArraytoPolynomial(array)
    generator = array
    perm = shifting(array)
    print('Permutations du mot générateur : ')
    while not comparerMatrice(array, perm):
        generator = np.vstack([generator, perm])
        perm = shifting(perm)
    return generator


def permutationsmin(array):
    ArraytoPolynomial(array)
    generator = array
    perm = shifting(array)
    i = 0
    print('Permutations du mot générateur : ')
    while not comparerMatrice(array, perm) and i < 3:
        generator = np.vstack([generator, perm])
        perm = shifting(perm)
        i = i + 1
    return generator


# Permet le code d'un mot en mot du code
def codage(mot):
    generator = permutationsmin(motGenerateur)
    code = (np.dot(mot, generator)) % 2
    return code


mot = np.array([1, 1, 1, 0])
code = codage(mot)
print('Mot codé : ', code)
