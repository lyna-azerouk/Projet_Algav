import numpy as np
import matplotlib.pyplot as plt
from  partie1 import decomposition 
from  partie1 import table 
import time
#definition de notre stucture d arbre
class Arbre():
    def __init__(self,nom=''):
        self.label = nom
        self.mot_luka=''
        self.G = None
        self.D = None
        self.p=None


   # def __eq__(self, __o: object) -> bool:
     #   return self.mot_luka == __o.mot_luka
    
  #  def __str__(self):
       # return self.label


def cons_arbre   ( T):
    liste =decomposition (len (T))
    arbre=[]
    for j in range (2) :   # 3 == nbr de bit a a dans taille (T) ou le nobre de variable 8=2^3
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


#resultat = table (38, 8)
resultat =[False ,  False ,False ,False ,False , False ,False ,False  ]
def affiche(arbre ):
    if  arbre !=None :
        return  (  print ( str ( arbre.label) + str ( arbre)), affiche( arbre.G)  ,affiche( arbre.D) )


#print("parcours prefefixe de l'arbre ")      
#arbre_decision=(cons_arbre(resultat)) 
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


#arbre_luka = luka(arbre_decision)


#QUESTION 2.8
def compression (arbre, liste):
    #arbre vide
    if arbre == None :
        return arbre
    #arbre pas vide
    else: 
        #initialisation de la liste si vide 
        if liste == []:
            arbref=Arbre(False ) 
            arbref.G=None 
            arbref.D=None
            arbref.mot_luka=False
            arbret=Arbre(True ) 
            arbret.G=None 
            arbret.D=None
            arbret.mot_luka=True
            liste.append  (   [ False  ,arbref ]) 
            liste.append ( [True , arbret ]) 
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
#result_compresion=compression ( arbre_luka , liste )
#affiche(result_compresion)
# l'affichage des adresses des noeud "true" et "false " sont tjr les mme   
# adresse noeud true==>  0x00000225B40D0A10  
#   adrsse du noeud false ==>0x00000225B40D09D0
# adresse du noeud x1(False) (true)==> x1(False)(True)<__main__.Arbre object at 0x00000209CB940950>

#QUESTION 2.9
def get_liste_dot(arbre):
    #creation liste vide
    liste=[]
    if arbre.G is not None:
        liste.append(str(arbre.label)+'->'+str(arbre.G.label)+';')
        liste.extend(get_liste_dot(arbre.G))
    if arbre.D is not None:
        liste.append(arbre.label+'->'+str(arbre.D.label)+';')
        liste.extend(get_liste_dot(arbre.D))
    return liste

#Input est la racine de l arbre
#le resultat est un fichier {nom_arbre}.dot
def digraph_in_dot(arbre):
    #creation liste vide
    liste=get_liste_dot(arbre)
    #write file
    f = open(str(arbre.label )+".dot", "w")
    f.write('digraph G {')
    for i in liste:
        f.write("\n\t")
        f.write(i)
    f.write("\n}")
    f.close()
    return liste

#digraph_in_dot(arbre_decision)




"""

DEBUT PARTIE 3

"""
#qst 3.10
def compression_2 ( arbre  ):
   if arbre==None : 
    return  arbre 
   else :
        
    #2eme regle
    if arbre.G!=None and arbre.G.G!=None and arbre.G.D!=None   and   str (arbre.G.G.mot_luka)==str ( arbre.G.D.mot_luka ) :
        arbre.G=arbre.G.G ;  return  compression_2 ( arbre)  ;  return arbre 

    if arbre.D!=None and arbre.D.G!=None and arbre.D.D!=None   and   str (arbre.D.G.mot_luka) ==str ( arbre.D.D.mot_luka ) :
        arbre.D=arbre.D.G  ;  return  compression_2( arbre ) ;   return arbre 

    if arbre.G!=None and arbre.D!=None and str (arbre.G.mot_luka)==str ( arbre.D.mot_luka ): 
         if  arbre.p != None and (arbre.p).G==arbre :
            arbre.p.G=arbre.G  ; compression_2( arbre )  
         if  arbre.p != None and (arbre.p).D==arbre :
            arbre.p.D=arbre.G  ; compression_2( arbre) 
         if arbre.p==None :
                 return arbre.G 
    else :
         compression_2 ( arbre.G )  ;   compression_2 ( arbre.D ) ; return arbre 

     

def  compression_bdd ( arbre  ): 
    if arbre ==None : return  arbre 
    else :
        liste =[]
        #1ere regle et 3 eme regle 
        arbre_c =  compression (arbre, liste) 
        #2eme regle 
        resultat=compression_2(arbre_c )
        return resultat 

print ("arbre bodd ")
#arbre_Robdd= compression_bdd(arbre_luka)
#affiche(arbre_Robdd) 

#On peut voir que les noeud x1 (False) (True) ont la meme adresse x1(False)(True)<__main__.Arbre object at 0x00000254D0C3A050>
# le parcour du dernieud x2 affiche x2 , x1(False)(True)<__main__.Arbre object at 0x00000254D0C3A050>False<__main__.Arbre object at 0x00000254D0C3A3D0>True<__main__.Arbre object at 0x00000254D0C3A390> False<__main__.Arbre object at 0x00000254D0C3A3D0>
# c a dire que le dernier False a eté suprimer 
# les adresses dez tout les noeuds false sont les meme   False<__main__.Arbre object at 0x00000254D0C3A3D0>
# les adresses dez tout les noeuds True sont les meme True<__main__.Arbre object at 0x00000254D0C3A390>


#start = time.time()
#print (start)
#arbre_Robdd= compression_bdd(arbre_luka)
#end = time.time()
#print ( end )
#elapsed = end - start

#print(f'Temps d\'exécution : {elapsed:.2}ms')



# Partie 4 

#Temps d'xecution pour la compression de 20 variables est: 3.5 ms   ( 1670526028.7819424-   1670526026.9136066 ) 
#Temps d'exceution de la  compression de 27 variables est : infi 
def nb_noeud ( arbre , l ):
    if arbre ==None: return 0 
    else  :
        if l ==[]:
            l.append (arbre )
            return 1  + nb_noeud(arbre.G,nb)+ nb_noeud (arbre.D,nb)
        else :  
            if arbre not in l:
                 l.append (arbre )
                 return 1  + nb_noeud(arbre.G,nb)+ nb_noeud (arbre.D,nb)
            else : 
                return  nb_noeud(arbre.G ,nb)+ nb_noeud (arbre.D,nb)
nb=[]

def points  ( variable ):
    L=[]
    v=[]
    table=[0 ]* ((2)**variable )
    t=[]
    for i in range ((2**2)**variable ) :        
        for k in  range(2**variable ) : 
            if table[k]==0 : 
                t.append ( True )
            else : t.append ( False)
        print("--------------------new  ")
        robdd= compression_bdd (luka (  cons_arbre( t)))
        affiche(robdd)
        nb=[]
        taille=(nb_noeud(robdd , nb))
        if L==[] :    
            L.append (taille)
            v.append ( 1)
        else : 
            if taille  not in L :
                L.append(taille)
                v.append ( 1)
            else : 
                 v[L.index(taille)]=v[L.index(taille )] +1
        j=0
        while  j<((2)**variable ) and  table[j]==1 :
             table [j]=0 
             j=j+1
        table [j %(2**variable ) ]=1
    print (L)
    print (v)        
    return [L, v]


def dessin (points ) : 
    plt.scatter(points[0] , points[1])
    plt.show()

dessin ( points ( 2))





