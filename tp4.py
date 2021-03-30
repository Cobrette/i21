import random
def rand_table(n,a,b):
    l=[]
    for i in range(n):
        l+=[random.randint(a,b)]
    return l

    def tri_bulle(t):
    n=len(t)
    d=n
    cpt=0
    echange=True
    while echange==True:
        i=0
        echange=False
        while i<d-1:
            cpt=cpt+1
            if t[i]>t[i+1]:
                t[i],t[i+1]=t[i+1],t[i]
                echange=True
            i=i+1
        d=d-1
    return cpt


    def tri_insertion(T):
    cpt=0
    for i in range(1,len(T)):
        j=i
        while j>0 and T[j-1]>T[j]:
            cpt=cpt+1
            T[j-1],T[j]=T[j],T[j-1]
            j=j-1
        cpt=cpt+1
    return cpt

    def tri_selection(T):
    cpt=0
    i=0
    n=len(T)
    while i<=n-2:
        imin=i
        j=i+1
        while j<=n-1:
            cpt=cpt+1
            if T[j]<T[imin]:
                imin=j
            j=j+1
        T[i],T[imin]=T[imin],T[i]
        i=i+1
    return cpt
