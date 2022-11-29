#Question 2.9  ́Etant donne un graphe (arbre de decision ou DAG),  ́ecrire une fonction dot qui
#construit un fichier repr esentant le graphe en langage dot. Une fois un fichier dot construit, l’application
#graphviz permet d’en donner la visualisation.
#Des exemples de representation en dot sont pr ́esent ́es ici : https://graphs.grevian.org/example

class Arbre():
    def __init__(self,nom=''):
        self.label = nom #nom du noeud
        self.mot_luka=''
        self.G = None #sous arbre gauche
        self.D = None #sous arbre droit

def get_liste_dot(arbre):
    #creation liste vide
    liste=[]
    if arbre.G is not None:
        liste.append(arbre.label+'->'+arbre.G.label+';')
        liste.extend(get_liste_dot(arbre.G))
    if arbre.D is not None:
        liste.append(arbre.label+'->'+arbre.D.label+';')
        liste.extend(get_liste_dot(arbre.D))
    return liste

#input is root of tree
def digraph_in_dot(arbre):
    #creation liste vide
    liste=[]
    liste=get_liste_dot(arbre)
    #write file
    f = open(arbre.label+".dot", "w")
    f.write('digraph G {')
    for i in liste:
        f.write("\n\t")
        f.write(i)
    f.write("\n}")
    f.close()
    return liste
    

#creation de l'arbre
arbre=Arbre('A')
arbre.G=Arbre('B')
arbre.D=Arbre('C')
arbre.G.G=Arbre('D')
arbre.G.D=Arbre('E')
arbre.G.G.G=Arbre('F')

digraph_in_dot(arbre)
