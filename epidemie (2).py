#!/usr/bin/env python
# coding: utf-8

# ### Epidémie Matteo Smith

# In[2]:


"""
Projet épidémie Matteo Smith
Ce programme modélise, par la succession de journées, une épidémie non nocive par la représentation graphique
par nuage de points, représentant une centaine d'individus dont les états peuvent être 'sain', 'malade', 'guéri' ou 'immunisé'.
Deux individus seront immunisés.

Le programme permet le déplacement de tous les individus : chaque individu a chaque jour une chance sur 2 de se déplacer
de jusqu'à dix unités verticalement ou horizontalement.

Les malades ont chaque jour une chance sur deux de contaminer chaque individu dans un rayon de 2 d'eux,
et une chance sur trois de contaminer ceux dans un rayon entre 2 et 6 d'eux.

La guérison d'un malade peut se dérouler quotidiennement également. Les malades ont chance sur dixde guérir chaque jour,
et sont sinon guéris le 14ème jour de leur maladie.

Après chaque journée, le programme affiche la modélisation de l'épidémie sous forme de graphique.
Les individus sains sont représentés en vert, les malades en rouge, les guéris en bleu et les immunisés en jaune.

Le programme se termine lorsqu'il ne reste plus de malades, et affiche alors le nombre de jours qu'a duré l'épidémie,
ainsi que les statistiques concernant la population."""


import matplotlib.pyplot as plot
import math
import random
import time

## initialisation

positions_initiales = []
x = random.sample([i for i in range(1, 101)], 100)
y = random.sample([i for i in range(1, 101)], 100)
for i in range(len(x)):
    positions_initiales.append((x[i], y[i]))


class individu():
    def __init__(self, x, y, statut, jours_malade):
        self.x = x
        self.y = y
        self.statut = statut
        self.jours_malade = 0
        
    def affiche_infos(self):
        '''affiche les informations relatives à un individu'''
        print(self.x, selx.y, self.statut, self.jours_malade)
        return

    
def population():
    """
    crée une liste d'instances de la classe individu, dont le statut est sain
    choisit deux individus au hasard et les immunise"""
    pop=[]
    for i in positions_initiales:
        pop.append(individu(i[0], i[1], 'sain', 0))
    immunisés = random.sample(range(100), 2)
    for i in immunisés:
        pop[i].statut = 'immunisé'
    return pop


def status(population):
    """renvoie la liste des statuts des individus"""
    status = []
    for ind in population:
        status.append(ind.statut)
    return status


def affiche_statistiques(population):
    """permet d'obtenir les quantités d'individus de chaque statut"""
    print('sains : ' + str(status(population).count('sain')))
    print('malades : ' + str(status(population).count('malade')))
    print('guéris : ' + str(status(population).count('guéri')))
    print('immunisés : ' + str(status(population).count('immunisé')))
    print()
    return


## fonctions

def debut_epidemie(population): 
    '''
    prend en entrée une liste d'instances de la classe individu
    modifie le statut d'un des individus au hasard à 'malade' pour démarrer l'épidémie'''
    malade = random.sample(range(100), 1)
    population[malade[0]].statut='malade'
    return


def deplacement(population):
    """
    prend en entrée une liste d'instances de la classe individu
    chaque individu a une chance sur 2 de se déplacer
    ils peuvent se déplacer de jusqu'à dix unités verticalement ou horizontalement"""
    for ind in population:
        chances_bouge = random.sample(range(2),1)
        if chances_bouge[0] == 1:
            deplacement_x = random.sample([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) #choisit au hasard une distance
            if deplacement_x[0] < 0:
                while ind.x+deplacement_x[0] < 0: #recherche une nouvelle abscisse si l'acbscisse devient négative
                    deplacement_x = random.sample([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
            deplacement_y = random.sample([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
            if deplacement_y[0] < 0:
                while ind.y+deplacement_y[0] < 0:#recherche une nouvelle ordonnée si l'ordonnée devient négative
                    deplacement_y = random.sample([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
            ind.x += deplacement_x[0]
            ind.y+=deplacement_y[0]
    return

    
def contamination(population):
    """
    prend en entrée une liste d'instances de la classe individu, fait contaminer les sains par les malades
    les malades ont chaque jour 0,5 chances de contaminer un individu dans un rayon de 2
    et dans un rayon de 6, un individu a 1/3 d'être contaminé
    les guéris sont immunisés
    """
    for ind in population:
        if ind.statut == 'malade':
                liste_proches=[el for el in population if el is not ind and abs(el.x-ind.x) <=2 and abs(el.y-ind.y)<=2]
                #selectionne les individus dans un rayon de 2 du malade
                for individu in liste_proches:
                    contaminer_proche = random.sample(range(2), 1)
                    if contaminer_proche == [2] and individu.statut == 'sain': #seuls les individus sains peuvent tomber malades
                        individu.statut = 'malade'
                        individu.jours_malade +=1

                liste_loin = [el for el in population if el is not ind                               and abs(el.x - ind.x) > 2 and abs(el.x - ind.x) <= 6                               and abs(el.y - ind.y) > 2 and abs(el.y-ind.y) <=6]                               #selectionne les individus dans un rayon entre 2 et 6 du malade
                for individu in liste_loin:
                        contaminer_loin = random.sample(range(3), 1)
                        if contaminer_loin == [1] and individu.statut == 'sain':
                            individu.statut = 'malade'
                            individu.jours_malade +=1
    return


def guerison(population):
    '''
    prend en entrée une liste d'instances de la classe individu 
    permet aux individus malades de guérir
    les malades ont 1/10 chance de guérir chaque jour, sinon sont guéris le 14ème jour de leur maladie'''
    liste_malades = [el for el in population if el.statut == 'malade']
    for ind in liste_malades:
        if ind.jours_malade == 14 and status(population).count('guéri')+status(population).count('malade')>1:
            ind.statut = 'guéri'
        chance_guerir = random.sample(range(10), 1)
        #print(chance_guerir)
        if chance_guerir == [2] and status(population).count('guéri')+status(population).count('malade')>1:
            ind.statut = 'guéri'
    return


def actualisation(population):
    """
    prend en entrée une liste d'instances de la classe individu
    actualise et affiche le graphique des positions des individus
    les sains sont représentés en vert, les malades en rouge, les guéris en bleu et les immunisés en jaune"""
    x=[ind.x for ind in population if ind.statut == 'sain']
    y=[ind.y for ind in population if ind.statut == 'sain']
    plot.scatter(x, y, c = 'g', marker = 'x', s=10)
    x=[ind.x for ind in population if ind.statut == 'malade']
    y=[ind.y for ind in population if ind.statut == 'malade']
    plot.scatter(x, y, c = 'r', marker = 'x', s=10)
    x=[ind.x for ind in population if ind.statut == 'guéri']
    y=[ind.y for ind in population if ind.statut == 'guéri']
    plot.scatter(x, y, c = 'b', marker = 'x', s=10)
    x=[ind.x for ind in population if ind.statut == 'immunisé']
    y=[ind.y for ind in population if ind.statut == 'immunisé']
    plot.scatter(x, y, c = 'y', marker = 'x', s=10)
    plot.show()
    return


def jour(population, jour_total):
    """
    prend en entrée une liste d'instances de la classe individu
    actualise jours_malade pour les individus malades
    génère le déplacement, la contamination et la guérison des individus se déroulant en une journée
    actualise enfin pour afficher le graphique"""
    #print('Jour '+str(jour_total))
    #time.sleep(0.2)
    for ind in population:
        if ind.statut=='malade':
            ind.jours_malade+=1
    deplacement(population)
    #actualisation(population)
    #time.sleep(0.3)
    contamination(population)
    #actualisation(population)
    #time.sleep(0.3)
    guerison(population)
    actualisation(population)
    #time.sleep(0.3)
    return


def main():
    """initialise et affiche la population initiale
    démarre l'épidémie et fait se dérouler les journées jusqu'à ce qu'il n'y ait plus de malades
    affiche à la fin de l'épidémie le nombre de jours qu'elle a duré,
    ainsi que les statistiques concernant la population"""
    popu = population()
    actualisation(popu)
    debut_epidemie(popu)
    i=1
    while status(popu).count('malade')>0:
        jour(popu, i)
        i+=1
    time.sleep(0.3)
    print('Fin')
    print()
    print('Jour '+str(i-1))
    return affiche_statistiques(popu)
    
main()


# In[ ]:




