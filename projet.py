from random import randint, shuffle


"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""


grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

"""
Les deux fonctions ci-dessous sont données à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""


def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1, 9+1):
        print("".join(n+s for (n, s)
              in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


def ligne(x, i):
    """
    Renvoie la liste de la ligne i de la grille de sudoku x
    """
    return x[i-1]


def unique(x):
    """
    Regard si la liste donnée a bien chaques chiffres unique"""
    s = set()
    for i in x:
        if i == 0:  # si 0 skip
            continue
        if i in s:
            return False
        s.add(i)
    return True

def colonne(x, i):
    """
    Renvoie la liste de la colonne j de la grille de sudoku x
    """
    return [r[i-1] for r in x]



def region(x, i):
    """
    Renvoie la liste de la region k de la grille de sudoku x
    """
    reg = []
    xrow = 3 * ((i-1) // 3)  # 0, 3, 6
    xcol = 3 * ((i-1) % 3)  # 0, 3, 6
    for k in range(len(x)):  # k: 0 -> 8
        reg.append(x[xrow + k // 3][xcol + k % 3])
    return reg


def ajouter(x, i, j, v):
    """
    Ajoute la valeur v dans la case correspondante 
    aux coordonnées (i,j) si celui ci lui est accordé
    """
    k = 3 * ((i - 1)//3) + ((j - 1)//3) + 1
    xrow = ligne(x, i)
    xcol = colonne(x, j)
    xreg = region(x, k)

    old_value = x[i-1][j-1]
    x[i-1][j-1] = v

    if not(unique(xrow) and unique(xcol) and unique(xreg)):
        x[i-1][j-1] = old_value
    


def verifier(x):
    """
    verifie si la grille x est complétée
    """
    for r in x:  # verifie ligne et zeros
        if 0 in r:
            return False
        if not unique(r):
            return False

    all_columns = [colonne(x, i) for i in range(1, 10)]
    for c in all_columns:  # verifie colonne
        if not unique(c):
            return False

    all_regions = [region(x, i) for i in range(1, 10)]
    for reg in all_regions:  # verifie region
        if not unique(reg):
            return False
    return True


def jouer(x):
    """Tant que la grille n'est pas complète continuer de jouer en donnant la ligne, la colonne ainsi que la valeur souhaiter"""
    while not(verifier(x)):
        afficher(x)
        entré = [1,2,3,4,5,6,7,8,9]
        i, j, v = map(int, input("Entrez la ligne, la colonne puis la valeur souohaité :\n").split())
        while not(i in entré and j in entré and (v in entré or v == 0)):
            print("Entrée incorrectes, veuillez reessayer :\n\n La ligne et la colonne doivent être comprise entre 1 et 9 \n\n La valeur doit être comprise entre 0 et 9\n")
            i, j, v = map(int, input("Entrez la ligne, la colonne puis la valeur souohaité :\n").split())
        ajouter(x, i, j, v)



def solutions(x):
    """Renvoi un dictionnaire (solution_dict) qui comprend la liste des valeurs solutionne pour ligne i et colonne j"""
    solution_dict = {}
    for k in range(10):  #Crée un dictionnaire
        solution_dict[k] = []

    for i, xrow in enumerate(x):
        for j, val in enumerate(xrow):
            if val != 0:  #Passer les celulles vides
                continue
            l = []
            k = 3 * ((i )//3) + ((j )//3) + 1

            xreg = region(x, k)
            xcol = colonne(x, j + 1)

            #Efface les valeurs qui sont déja dans la lignes, la colonne et la région de la case vide
            for n in range(10):
                if not((n in ligne(x, i+1)) or (n in xcol) or (n in xreg)):
                    l.append(n)

            #Dictionnaire apprend la tuple(i,j,l) qui correspond aux valeurs possible dans la case (i,j)
            solution_dict[len(l)].append((i, j, l))

    return solution_dict


def resoudre(x):
    """Resoud la grille x selon l'algorythme de resolution recursive en prenant la liste des solutions et en regardant pour chaque valeur si c'est possible d'aller plus loin jusqu'a ce que la grille soit remplis"""
    xsolutions =  list(solutions(x).values())
    print(xsolutions)
  

    if xsolutions == [[], [], [], [], [], [], [], [], [], []]:  #toutes les cellules sont remplies
        return x

    for num in range(len(xsolutions)):
        for val in range(len(xsolutions[num])):

            if xsolutions[num][val][2] == []:  #solution impossible
                return False

            for cell_s in xsolutions[num][val][2]: 
                ajouter(x, xsolutions[num][val][0]+1, xsolutions[num][val][1]+1, cell_s)
                   

                if resoudre(x):
                    return x

            return False





def generer(x):
    """Resoud la grille x selon l'algorythme de resolution recursive de manière aléatoir afin d'obtenir une nouvelle grille remplissable"""

    xsolutions =  list(solutions(x).values())

    if xsolutions == [[], [], [], [], [], [], [], [], [], []]:  #toutes les cellules sont remplies
        return x

    for num in range(len(xsolutions)):
        for val in range(len(xsolutions[num])):

            if xsolutions[num][val][2] == []:  #solution impossible
                return False
            shuffle(xsolutions[num][val][2])
            for cell_s in xsolutions[num][val][2]: 
                ajouter(x, xsolutions[num][val][0]+1, xsolutions[num][val][1]+1, cell_s)
                    

                if generer(x):
                    return x

            return False


def nouvelle(difficulty=1):
    '''
    La difficulté varie entre 1 et 5, plus elle est élevée plus il y aura des cases vides

    Difficulté -> Cases vides
        1    ->    66
        2    ->    54
        3    ->    42
        4    ->    30
        5    ->    17
    '''
    x = grille_0
    if difficulty not in range(1, 6):
        print("la difficulté doit etre comprise entre 1 et 5")
    difficulties = [66, 54, 42, 30, 17]
    cell_a_supp = 81 - difficulties[difficulty - 1]
    grille_pleine = generer(x)
    for i in range(cell_a_supp):
        cell_ligne = randint(0, 8)
        cell_colonne = randint(0, 8)
        while grille_pleine[cell_ligne][cell_colonne] == 0:
            cell_ligne = randint(0, 8)
            cell_colonne = randint(0, 8)
        grille_pleine[cell_ligne][cell_colonne] = 0
    return grille_pleine




jouer(nouvelle(5))




