# exercice 1

def occurence_lettres(phrase):
        """str -> dic
        prend un paramètre une variable phrase de type str, et renvoie un dictionnaire constitué des occurences des caractères présents dans la phrase
        les clés du dictionnaire sont les caractères de la phrase et les valeurs sont l'occurence de ces caractères"""
        dico={}
        for i in range(len(phrase)):
                if phrase[i] not in dico.keys():
                        compteur=1
                        for j in range(len(phrase)):
                                if phrase[j]==phrase[i] and i!=j:
                                        compteur+=1
                        dico[phrase[i]]=compteur
        return dico


def occurence_lettres2(phrase):
    """str -> dic
    prend un paramètre une variable phrase de type str, et renvoie un dictionnaire constitué des occurences des caractères présents dans la phrase
    les clés du dictionnaire sont les caractères de la phrase et les valeurs sont l'occurence de ces caractères
    cette fonction a une complexité plus faible que la fonction précédente"""
    dico={}
    for e in phrase:
        if e not in dico:
            dico[e]=1
        else:
            dico[e]+=1
    return dico


# exercice 2

def fusion(L1,L2):
    """list, list -> list
    prend en entrée deux listes L1 et L2 triées par ordre croissant, renvoie la
    liste L12 qui est la fusion des deux listes, triée par ordre croissant"""
    
    assert L1 == sorted(L1) and L2 == sorted(L2), 'les listes ne sont pas triées'
    
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    while i1 < n1:
    	L12[i] = L1[i1]
    	i1 = i1 + 1
    	i += 1
    while i2 < n2:
    	L12[i] = L2[i2]
    	i2 = i2 + 1
    	i += 1
    return L12








