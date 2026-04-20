def annuitaet(kw,z,j):
    ann = kw*((((1+z)**j)*z)/(((1+z)**j)-1))
    return ann

def effJahresZins(p_nom, m):
    effJZ= (1+p_nom/m)**m-1
    return effJZ
