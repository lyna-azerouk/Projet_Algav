from partie1 import *
from p2ori import *

#test partie 1
table0=table(38,8)
print(table0)
arbre0=cons_arbre(table0)

#attention affichage non correcte car meme nom
digraph_in_dot(arbre0)



#creation d une table
table1=[True,True,True,False,True,True,True,False]

#construction de l arbre
arbre1=cons_arbre(table1)
luka(arbre1)
#sauvegarder en dot
digraph_in_dot(arbre1)
