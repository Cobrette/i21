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
'''
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
'''
def fibo(n):
    i=2
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        l=[0,1]
        while i<=n:
            l+=[l[i-l]+l[i-2]]
            i+=l
        return l[-l]



#question 2:
def matmult(m1,m2):
    l=[[0,0],[0,0]]
    l[0][0]=m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0]
    l[0][1]=m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1]
    l[1][0]=m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0]
    l[1][1]=m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1]
    return l

def matcarre(m):
    chips=matmult(m,m)
    return chips

#question 3:
def fibo2(n):
    l=[]
    while n!=0:
        if n%2==0:
            n=n/2
            l=[1]+l
        else:
            n=n-1
            l=[0]+l
    m=[[1,0],[0,1]]
    f=[[1,1],[1,0]]
    for element in l:
        if element==0:
            m=matmult(m,f)
        else:
            m=matcarre(m)
    return m[0][1]

