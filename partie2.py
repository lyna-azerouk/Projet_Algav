from  partie1 import decomposition 
from  partie1 import table 
class Arbre():
    def __init__(self,nom=''):
        self.label = nom
        self.mot_luka=''
        self.G = None
        self.D = None

def cons_arbre   ( T):
    liste =decomposition (len (T))
    arbre=[]
    for j in range (3) : 
        i=0
        while i <len( T)-1 : 
            if j==0 : 
                noeudR=Arbre ("x"+str(j+1))
                noeudd=Arbre(T[i+1])
                noeudd.D=None
                noeudd.G=None
                noeudg=Arbre(T[i])
                noeudg.D=None
                noeudg.G=None
                noeudR.G=noeudg
                noeudR.D=noeudd
            else :
                noeudR=Arbre ("x"+str(j+1))
                noeudR.G=T[i]
                noeudR.D=T[i+1]
                
            arbre.append(noeudR)
            i=i+2
        T.clear()
        T=arbre.copy()
        arbre.clear()
    return T[0]


resultat = table (38,8)

def affiche(arbre ):
    if  arbre !=None :
        return  (  print (arbre.label), affiche( arbre.G)  ,affiche( arbre.D) )
#print("parcours prefefixe de l'arbre ")      
arbre_decision=(cons_arbre(resultat)) 

def luka ( arbre ) : 
    if arbre ==None  :  return  arbre
    else :
        if arbre.G==None and arbre.D==None :
                 arbre.mot_luka=arbre.label       
                 return arbre 
        else :
           arbre.mot_luka= '(' + arbre.label + arbre.mot_luka+ str( (luka(arbre.G)).mot_luka )+ str( luka(arbre.D).mot_luka ) + ')'
           return arbre


arbre_luka = luka(arbre_decision)
affiche(arbre_luka)


