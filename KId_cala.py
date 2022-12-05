###Bibliothèques
import numpy as giroud



###Variables
dic = {1:'Pomme' , 2:'Orange' , 3:'Banane' , 4:'Fraise'}
dic2 = {1:'🍏' , 2:'🍊' , 3:'🍌' , 4:'🍓'}
###Fonctions
def crea_vide(c = 2, l= 7):
    return [[[] for _ in range(l)] for _ in range(c)]

def rempli(tab):
    a = [i for i in range(4)]
    for i in range(len(tab)):
        for j in range(1, len(tab[0])-1):
            tab[i][j] += a
    return tab

def impression(tab):
    for i in range(len(tab[0])):
        print(tab[0][i], tab[1][i])



def case_jouee(tab, j):
    ca_roule = False
    while not ca_roule :
        case = input("Au tour du joueur "+str(j+1)+". Choissisez une case: \n")
        while ord(case) not in [i for i in range(49, 54)]:
            case = input("Votre nombre n'était pas jouable, veuillez recommencer: \n")
        case = int(case)
        ca_roule = est_jouable(tab, j, case)
    return (j, case)


def est_jouable(tab, j, case):
    if case > 0 and case < 6:
        if tab[j][case] != []:
            return True
    return False

def contenue(tab, ind):
    return tab[ind[0]][ind[1]]

def vide_case(tab, ind):
    tab[ind[0]][ind[1]] = []
    return tab



def tour(tab, case):
    liste_fruits  = contenue(tab, case)
    i, j = case
    cote = i
    while liste_fruits != []:
        while cote == 0:
            if j > 6 or j <0 or liste_fruits == []:
                None
            else :
                tab[0][j+1] += [liste_fruits[0]]
                liste_fruits.pop(0)
            j += 1
            cote = j//6
        while cote == 1:
            if j <= 0 or j > 6 or liste_fruits ==[]:
                if j ==-1:
                    cote = 0
            else :
                tab[1][j-1] += [liste_fruits[0]]
                liste_fruits.pop(0)
            j -= 1
        if cote == 0:
            j = 0
        else :
            j =6
    return tab

def fini(tab):
    a, b = True, True
    for i in range(5):
        if tab[0][i+1] != []:
            a *= False
        if tab[1][i+1] != []:
            b *= False
    return a , b


def rapatriement(tab):
    a, b = fini(tab)
    if a == 1:
        for i in range(5):
            tab[0][6] += tab[0][i+1]
            tab[0][i+1] = []
    if b == 1:
        for i in range(5):
            tab[1][0] += tab[1][i+1]
            tab[1][i+1] = []
    return tab

def comptage(tab):
    dica = {}
    dicb = {}
    L = [0 for _ in range(4)]
    L2 = [0 for _ in range(4)]
    for el in tab[0][6]:
            L[el] += 1
    for el in tab[1][0]:
            L2[el] += 1
    for i in range(4):
        dica[dic2[i+1]] = L[i]
        dicb[dic2[i+1]] = L[i]
    return [dica, L], [dicb, L2]


def win(tab):
    a, b = comptage(tab)
    i, j = sum(a[1]), sum(b[1])
    if i > j:
        print("Le joueur 1 gagne avec "+str(i)+" fruits! Il cumule :"+str(a[1][0])+" "+dic2[1]+", "+str(a[1][1])+\
        ", "+dic2[2]+", "+str(a[1][2])+" "+dic2[3]+", "+str(a[1][3])+" "+dic2[4]+" .")
        print("Le joueur 2 cumule: "+str(b[1][0])+" "+dic2[1]+", "+str(b[1][1])+", "+dic2[2]+\
        ", "+str(b[1][2])+" "+dic2[3]+", "+str(b[1][3])+" "+dic2[4]+" .")
    else :
        print("Le joueur 2 gagne avec "+str(j)+" fruits! Il cumule: "+str(b[1][0])+" "+dic2[1]+", "+str(b[1][1])+", "+dic2[2]+", "\
        +str(b[1][2])+" "+dic2[3]+", "+str(b[1][3])+" "+dic2[4]+", ")
        print("Le joueur 1 cumule: "+str(a[1][0])+" "+dic2[1]+", "+str(a[1][1])+", "+dic2[2]+", "+\
        str(a[1][2])+" "+dic2[3]+", "+str(a[1][3])+" "+dic2[4]+" .")


def demo():
    count= 0
    tab= rempli(crea_vide())
    impression(tab)
    while fini(tab) == (0,0) :
        j = case_jouee(tab, count%2)
        tab = tour(tab, j)
        impression(tab)
        count += 1
    tab = rapatriement(tab)
    win(tab)

