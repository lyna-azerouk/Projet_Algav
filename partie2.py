from  partie1 import decomposition 
from  partie1 import table 
class Arbre():
    def __init__(self,nom=''):
        self.label = nom
        self.mot_luka=''
        self.G = None
        self.D = None
        self.p=None 

def cons_arbre   ( T):
    liste =decomposition (len (T))
    arbre=[]
    for j in range (3) :   # 3 == nbr de bit a a dans taille (T)
        i=0
        while i <len( T)-1 : 
            if j==0 : 
                noeudR=Arbre ("x"+str(j+1))
                noeudd=Arbre(T[i+1])
                noeudd.D=None
                noeudd.G=None
                noeudd.p=noeudR
                noeudg=Arbre(T[i])
                noeudg.D=None
                noeudg.G=None
                noeudg.p=noeudR
                noeudR.G=noeudg
                noeudR.D=noeudd
            
            else :
                noeudR=Arbre ("x"+str(j+1))
                T [i].p=noeudR
                T[i+1].p=noeudR
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
        return  (  print ( str ( arbre.mot_luka) + str ( arbre)), affiche( arbre.G)  ,affiche( arbre.D) )
print("parcours prefefixe de l'arbre ")      
arbre_decision=(cons_arbre(resultat)) 
#affiche(arbre_decision)
def luka ( arbre ) : 
    if arbre ==None  :  return  arbre
    else :
        if arbre.G==None and arbre.D==None :
                 arbre.mot_luka= arbre.label     
                 return arbre 
        else :
           arbre.mot_luka= arbre.label + '('+ arbre.mot_luka+ str( (luka(arbre.G)).mot_luka ) + ')'+ '('+ str( luka(arbre.D).mot_luka )  +')'
           return arbre


arbre_luka = luka(arbre_decision)
#affiche(arbre_luka) 


#qst 2.8
def compression (arbre, liste):
    #arbre vide
    if arbre == None :
        return arbre
    #arbre pas vide
    else: 
        #initialisation de la liste si vide 
        if liste == []:
            liste.append  (   [ False  , Arbre(False ) ]) 
            liste.append ( [True , Arbre(True )  ]) 
        #parcours de la liste a la recherche du mot luka
        #liste [[1,2][1,2][1,2][1,2]]
        #liste [mot_luka][arbre]
        i=0
        sim=-1
        for i in range(len(liste)):
            if liste[i][0]==arbre.mot_luka:
                sim=i

        #arbre pas dans la table
        if sim == -1:
            liste.append (  [arbre.mot_luka  , arbre  ]) 
            arbre.D = compression(arbre.D, liste)
            arbre.G = compression(arbre.G, liste)
                
        #arbre dans la table
        else :
            arbre = liste [sim][1]
            compression ( arbre.G,liste ) 
            compression(arbre.D,liste )
        return arbre 

liste =[] 
result_compresion=compression ( arbre_luka , liste )
affiche(result_compresion)
# l'affichage des adresses des noeud "true" et "false " sont tjr les mme   
# adresse noeud true==>  0x00000225B40D0A10  
#   adrsse du noeud false ==>0x00000225B40D09D0
# adresse du noeud x1(False) (true)==> x1(False)(True)<__main__.Arbre object at 0x00000209CB940950>




#qst 2.8
def compression (arbre, liste):
    #arbre vide
    if arbre == None :
        return arbre
    #arbre pas vide
    else: 
        #initialisation de la liste si vide 
        if liste == None:
            liste[0][0] = False
            liste[0][1] = arbre("False")
            liste[1][0] = True
            liste[1][1] = arbre("True")
        #parcours de la liste a la recherche du mot luka
        #liste [[1,2][1,2][1,2][1,2]]
        #liste [mot_luka][arbre]
        i=0
        sim=-1
        for i in range(len(liste)):
            if liste[i][0]==arbre.mot_luka:
                sim=i

        #arbre pas dans la table
        if sim == -1:
            liste[i][0] = arbre.mot_luka
            liste[i][1] = arbre
            arbre.D = compression(arbre.D, liste)
            arbre.G = compression(arbre.G, liste)
                
        #arbre dans la table
        else :
            arbre = liste [sim][1]


            return arbre
                




#qst 3.10
def compression_2 ( arbre , liste ):
   if arbre==None : return  arbre 
   else :
    #1ere regle
    if  arbre.G!=None and arbre.G.mot_luka ==False  :
        arbre.G=liste[1]  ;   compression_2(arbre.D,liste) ;   compression_2(arbre.G,liste)
    if arbre.D!=None and arbre.D.mot_luka==False :
        arbre.D=liste[1];   compression_2(arbre.G,liste)  ;    compression_2(arbre.D,liste) 
    if arbre.G!=None and arbre.G.mot_luka ==True  :
        arbre.G=liste[0] ;   compression_2(arbre.D,liste)  ;compression_2(arbre.G,liste)
    if arbre.D!=None and arbre.D.mot_luka ==True  :
        arbre.D=liste[0]  ; compression_2(arbre.G,liste);  compression_2(arbre.D,liste) 
    #2eme regle
    if arbre.G!=None and arbre.G.G!=None and arbre.G.D!=None   and   arbre.G.G.mot_luka==arbre.G.D.mot_luka  :
        arbre.G=arbre.G.G ;  compression_2 ( arbre.D,liste)  ;  compression_2 ( arbre.G,liste) 
    if arbre.D!=None and arbre.D.G!=None and arbre.D.D!=None   and   arbre.D.G.mot_luka==arbre.D.D.mot_luka  :
        arbre.D=arbre.D.G  ; compression_2( arbre.G ,liste) ; compression_2 ( arbre.D,liste) 
    else :
        compression_2 ( arbre.G, liste )  ; compression_2 ( arbre.D, liste )
    
    return arbre 
    


def  compression_bdd ( arbre  ):
    if arbre ==None : return  arbre 
    noeudf= Arbre (False )
    noeudt=Arbre(True)
    noeudf.mot_luka=False 
    noeudt.mot_luka=True 
    noeudf.label=False 
    noeudt.label=True 
    noeudf.D=None
    noeudf.G=None 
    noeudt.G=None 
    noeudt.D=None
    l=[]
    l.append(noeudt)
    l.append(noeudf)

    resultat=compression_2(arbre ,l)
    return resultat

#arbre_Robdd= compression_bdd(arbre_luka)
#affiche(arbre_Robdd) 







