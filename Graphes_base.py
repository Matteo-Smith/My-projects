import random

class Graphe_mat:
    """ représentation par une matrice d'adjacence, où
    les sommets sont les entiers 0, 1, ..., n-1 """

    def __init__(self,n):
        self.n = n
        self.adj= [[0] * n for i in range(n)]

    def ajouter_arc(self, s1, s2):
        self.adj[s1][s2] = 1

    def arc(self, s1, s2):
        return self.adj[s1][s2] == 1

    def voisins(self, s):
        v = []
        for i in range(self.n):
            if self.adj[s][i]:
                v.append(i)
        return v

    def afficher(self):
        for s1 in range(self.n):
            print(s1, ' -> ', end = '')
            for s2 in range(self.n):
                if self.arc(s1, s2) :
                    print(s2, end = ' ')
            print('')

    def degre(self, s):
        if s < self.n :
            return sum(self.adj[s])

    def nb_arcs(self):
        nb = 0
        for s in range(self.n):
           nb += self.degre(s)
        return nb

    def supprimer_arc(self, s1, s2):
        if self.arc(s1, s2):
            self.adj[s1][s2] = 0
        
            

class Graphe_dict:
    """ représentation par un dictionnaire d'adjacence"""

    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self, s):
        if s not in self.adj :
            self.adj[s] = []

    def ajouter_arc(self, s1, s2) :
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].append(s2)

    def arc(self, s1, s2):
        return s2 in self.adj[s1] 

    def sommets(self):
        return list(self.adj.keys())

    def voisins(self, s):
        return self.adj[s]

    def afficher(self):
        for s in self.adj:
            print(s, self.adj[s])
            
    def nb_sommets(self):
        return len(self.adj)

    def degre(self, s):
        return len(self.adj[s])

    def nb_arcs(self, s):
        nb = 0
        for s in self.adj:
            nb += self.degre(s)
        return nb

    def supprimer_arc(self, s1, s2):
        if self.arc(s1, s2):
            self.adj[s1].pop(s2)


def matrix_to_dict(gm):
    """ gm étant une instance de la classe Graphe_mat, la fonction
    renvoie le même graphe représenté par une instance de la classe
    Graphe_dict """

    gd = Graphe_dict()
    for s in range(gm.n):
        gd.ajouter_sommet(s)
    for s1 in range(gm.n):
        for s2 in range(gm.n):
            if gm.arc(s1,s2) :
                gd.ajouter_arc(s1, s2)
    return gd


class Pile:
    """ classe Pile
    création d’une instance Pile avec une liste
    """
    
    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def depiler(self):
        assert not self.vide(),"Pile vide"
        return self.L.pop()

    def sommet(self):
        assert not self.vide(),"Pile vide"
        return self.L[len(self.L)-1]

    def empiler(self,x):
        self.L.append(x)


class File:
    """classe File
    création d’une instance File avec une liste 
    """
    
    def __init__(self):
        self.L = []
        
    def vide(self):
        return self.L == []

    def defiler(self):
        assert not self.vide(), "file vide"
        return self.L.pop(0)

    def enfiler(self,x):
        self.L.append(x)

    def taille(self):
        return len(self.L)

    def sommet(self):
        return self.L[0]

    def present(self,x):
        return x in self.L

def parcours_largeur(g,s):
    '''prend en argument un graphe de Graphe_dict et un sommet s, le départ
    renvoie une liste des sommets visités en parcours largeur'''
    visités=[]
    f=File()
    visités.append(s)
    f.enfiler(s)
    while not f.vide():
        u=f.defiler()
        for v in g.voisins(u):
            if v not in visités:
                visités.append(v)
                f.enfiler(v)
    return visités

import random

def parcours_profondeur(g,s):
    '''prend en argument un graphe, un sommet s de départ'''
    visites=[s]
    p=Pile()
    p.empiler(s)
    while not p.vide():
        u=p.sommet()
        #print(u)
        voisins_u = [v for v in g.voisins(u) if v not in visites]
        if voisins_u == []:
            p.depiler()
        else:
            v=random.choice(voisins_u) #attention ! random.sample renvoie un élément sous forme de liste, ce qui ne marche pas ici!
            visites.append(v)
            p.empiler(v)
    return visites


def parcours_profondeur2(g,s, visités):
    """prend en entrée un graphe g, un sommet s de départ et une liste vide"""
    if s not in visités:
        visités.append(s)
        for v in g.voisins(s):
            if v not in visités:
                parcours_profondeur2(g, v, visités)
    return visités


g=Graphe_dict()
g.ajouter_arc('Rennes', 'Toulouse')
g.ajouter_arc('Rennes', 'Paris')
g.ajouter_arc('Paris', 'Toulouse')
g.ajouter_arc('Paris', 'Rennes')
g.ajouter_arc('Paris','Lyon')
g.ajouter_arc('Paris','Nancy')
g.ajouter_arc('Toulouse', 'Rennes')
g.ajouter_arc('Toulouse', 'Paris')
g.ajouter_arc('Toulouse', 'Montpellier')
g.ajouter_arc('Nancy', 'Paris')
g.ajouter_arc('Nancy', 'Lyon')
g.ajouter_arc('Lyon', 'Marseille')
g.ajouter_arc('Lyon', 'Nice')
g.ajouter_arc('Lyon', 'Paris')
g.ajouter_arc('Lyon', 'Nancy')
g.ajouter_arc('Nice', 'Marseille')
g.ajouter_arc('Nice', 'Lyon')
g.ajouter_arc('Marseille', 'Nancy')
g.ajouter_arc('Marseille', 'Lyon')
g.ajouter_arc('Marseille', 'Montpellier')
g.ajouter_arc('Montpellier', 'Marseille')
g.ajouter_arc('Montpellier', 'Toulouse')


#ex 5

graphe_5 = Graphe_dict()
graphe_5.ajouter_arc('A', 'B')
graphe_5.ajouter_arc('A', 'D')
graphe_5.ajouter_arc('D', 'E')
graphe_5.ajouter_arc('E', 'B')
graphe_5.ajouter_arc('B', 'C')
graphe_5.ajouter_arc('C', 'E')
graphe_5.ajouter_arc('C', 'F')
graphe_5.ajouter_arc('G', 'C')
#print(parcours_largeur(graphe_5, 'A'))
#print(parcours_profondeur(graphe_5, 'A'))


#ex 6

def est_connexe(g, s):
    visites=parcours_profondeur(g, s)
    condition=True
    for v in visites:
        if v not in g.adj:
            return True
    return condition and len(visites) == len(g.adj)


#ex 7

"""def  parcours_ch(g, dic_visites, origine, s):
     #parcours depuis le sommet s, en venant de origine
     #origine est le sommet qui a permis d'atteindre s en empruntant l'arc origine -> s
     #dic_visites est le dico qui associe à chaque sommet visité le sommet qui a permis de l’atteindre \n
     #pendant le parcours en profondeur
    p=Pile()
    p.empiler(s)
    parcours=[]
    while not p.vide():
        u=p.sommet()
        voisins_u = [v for v in g.voisins(u) if v not in dic_visites] #v doit ne pas être origine? à quoi sert origine
        if voisins_u == []:
            p.depiler()
        else:
            v=random.choice(voisins_u) #attention ! random.sample renvoie un élément sous forme de liste, ce qui ne marche pas ici!
            parcours.append(v)
            p.empiler(v)
    return parcours

#dic_visites pour graphe_5 : dic={'B':'A', 'D':'A', 'C':'B', 'E':'D', 'F':'C'}"""

def parcours_ch(g, dic_visites, origine, s):
    if s not in dic_visites:
        dic_visites.append(origine)
        for v in g.voisins(s):
            if v not in dic_visites:
                parcours_ch(g, v, visités)
    return visités

#pas checké

