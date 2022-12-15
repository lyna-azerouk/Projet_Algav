#qst 3.10
class Arbre():
    def __init__(self,nom=''):
        self.label = nom #nom du noeud
        self.mot_luka=''
        self.G = None #sous arbre gauche
        self.D = None #sous arbre droit
        self.p=None

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o,Arbre):
            return NotImplemented
        return self.mot_luka == __o.mot_luka
    
    def __str__(self):
        return self.label


def new_compression(liste,h):
    if liste[h][0].G!=None:
        for arbre in liste[h]:
            if arbre.G==arbre.D:
                if arbre.p.G==arbre:
                    arbre.p.G=arbre.G
                else:
                    arbre.p.D=arbre.G

                #ajoute a la liste    
                if len(liste)==(h+1):
                    liste.append([arbre.G])
                else:
                    liste[h+1].append(arbre.G)

            else:
                if len(liste)==(h+1):
                    liste.append([arbre.G,arbre.D])
                else:
                    trouveG=False
                    trouveD=False
                    for other_tree in liste[h+1]:
                        if arbre.G==other_tree:
                            arbre.G=other_tree
                            trouveG=True
                            break
                    for other_tree in liste[h+1]:
                        if arbre.D==other_tree:
                            arbre.D=other_tree
                            trouveD=True
                            break

                    if not trouveG:
                        liste[h+1].append(arbre.G)
                    if not trouveD:
                        liste[h+1].append(arbre.D)

        new_compression(liste,(h+1))
                        


def new_compression_init(root):
    if root.G != None:
        if root.G!=root.D:
            liste=[[root][root.G,root.D]]
            h=1
            new_compression(liste,h)
        else:
            root=new_compression_init(root.G)
    return root
