'''
^ XOR
| or
~ not
& and
'''
#exo 1 :Operateurs bit a bit
#question 1:
#retourne la valeur dui-`eme bit de l’entiern.

def bit(n,i):
    x= n & 2**i
    return x>>i
"""
ou en 1 ligne :

def bit(n,i):
    return (n&2**i)>>i
"""
#question 2 :
#retourne l’entier x pour lequel le bit de poids i a  été modifier en val

def set_bit(x,i,val):
    u=bit(x,i)
    if u==val:
        return x
    else:
        if val ==0:
         j=x^2**i
         return j
        if val ==1:
             j=n|2**i
             return j

#question 3 :
#retourne le nombre de bits a 1 de l'entier x

def pop_count(n):
    c=0
    while n!=0:
        val=bit(n,0)
        if val==1:
            c+=1
        n=n>>1
    return c

#exo 2:Exponentiation rapide
#question 1:
# La fonction devra renvoyer la liste des valeurs intermediaires (et non pas seulement le resultat)

def expo_gd(x,k):
    n=k
    pdt=1
    l=[]
    l2=[pdt]
    while n !=0 :
        if n%2==0:
            n=n/2
            l=[0]+l
        else :
            n=n-1
            l=[1]+l

    for i in l:
        if i==0:
            pdt=pdt*pdt
            l2+=[pdt]
        else:
            pdt=pdt*x
            l2+=[pdt]
    return l2
    
#question 2:
def expo_dg(x,k):
    pdt=1
    l=[pdt]
    n=1
    while n <=k:
        if k&n:
            pdt=pdt*x
            l+=[x,pdt]
        else:
            l+=[x]
        n=n*2
        x=x*x
    return l
#exo 3: Nombres de Fibonacci
#question 1 :
def fibo(n):
    f0 = 0
    f1 = 1
    fn = -1
    if (n == 0):
        fn = f0
    if (n == 1):
        fn = f1
    for k in range(2,n+1):
        fn = f1 + f0
        f0,f1 = f1,fn
    return fn
