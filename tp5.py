""" Retourne la liste des indices des cases à
échanger pour obtenir un tableau à trois couleurs
trié en bleu/blanc/rouge"""

'''Pas opti mais marche sur moodle'''
#exo1
#question 1
def bbr(T):
    b=0
    w=0
    r=len(T)-1
    l=[]

    while w <=r :
        if T[w]== 'white':
            w += 1
            
        elif T[w]=='red':
                T[w],T[r]=T[r],T[w]
                l+=[(w,r)]
                r-=1

        elif T[w]=='blue':          
            T[w],T[b]= T[b],T[w]
            l+=[(w,b)]
            b+=1
            w+=1
            
    return l

''' opti mais marche pas sur moodle'''
def bbr(t):
    b=0
    w=0
    r=len(t)-1
    l=[]

    while w <=r :
        if t[w]== 'white':
            w += 1
            
        elif t[w]=='red':
            if t[r]=='red':
                r-=1
            else:
                t[w],t[r]=t[r],t[w]
                l+=[(w,r)]
                r-=1

        else:          
            t[w],t[b]= t[b],t[w]
            l+=[(w,b)]
            b+=1
            w+=1
            
    return l
#exo2
#question 1
def fusionner(T1,T2):
    T3=[]
    i=0
    j=0
    cpt=0
    while len(T3)!=len(T1)+len(T2):
        if T1[i]<T2[j]:
            T3+=[T1[i]]
            cpt+=1
            i+=1
        else:
            T3+=[T2[j]]
            cpt+=1
            j+=1
        if i==len(T1):
            T3+=T2[j:]

        elif j==len(T2):
            T3+=T1[i:]

    return T3,cpt
#question 2
def tri_partiel(T,a,b):
    cpt=0
    i=a+1
    while i<b:
        j=i
        while j>a and T[j-1]>T[j]:
            T[j-1],T[j]=T[j],T[j-1]
            j-=1
            cpt+=1
        cpt+=1
        i+=1
    return cpt
#question 3
def fusion_partielle(T,a,b):
    temps,cpt=fusionner(T[:a],T[a:b])
    T[:b]=temps
    return cpt
