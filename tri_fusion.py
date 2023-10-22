#ex 1

def est_trie(t):
    for i in range(1, len(t)):
        if t[i]<t[i-1]:
            return False
    return True

def fusion(t1, t2):
    assert est_trie(t1), "le tableau t1 n'est pas trié"
    assert est_trie(t2), "le tableau t2 n'est pas trié"
    new_t=[]
    while len(t1) > 0 and len(t2) > 0:
        if t1[0]>t2[0]:
            new_t.append(t2[0])
            t2.remove(t2[0])

        else:
            new_t.append(t1[0])
            t1.remove(t1[0])

    for e in t1:
        new_t.append(e)
    for e in t2:
        new_t.append(e)
            
    assert est_trie(new_t), "le tableau new_t n'est pas trié"
    return new_t

print(fusion([1,2,5],[3,5,9]))


def tri_fusion(t):
    if len(t)==1:
        return t
    return fusion(tri_fusion(t[:len(t)//2]), tri_fusion(t[len(t)//2:]))
