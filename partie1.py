def  decomposition ( n ) : 
    q = -1
    res = "" 
    liste = []
    while q != 0:
        q = n // 2
        r = n % 2
        if r ==0 : 
            liste.append ( True ) 
        else :
            liste.append ( False  ) 
        n = q
    liste.reverse()
    return liste 
resultat = decomposition ( 38)

def completion ( liste , n ) :
    if ( len( liste )>=n) : 
        return liste [0:n]
    else :
        for  i in range (  n -len( liste )) :
            liste.append(False)
    return liste 
#print ( completion ( resultat ,8))

def table ( x ,n ) :
    liste=decomposition(x)
    result_final =completion( liste , n )
    return result_final

#print( table (38,8))