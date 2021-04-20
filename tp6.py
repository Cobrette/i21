#QUESTION N°1:

from random import randint

'''EXERCICE N°1:'''
#question n°1:
def gen_tableau(n):
    l=[0]*n
    i=0
    while i<n:
        l[i]=randint(1,2*n)
        i+=1
    l=sorted[l]
    return l
  
  '''
    moodle question 1 :
'''
  
  from random import *
def rand_table(n,a,b):
    l=[0 for i in range(n)]
    i=0
    while i<n:
        l[i]=randint(a,b)
        i+=1
    l=sorted(l)
    return l
  
#QUESTION N°2:
def recherche_binaire(T,x):
    g=0
    d=len(T)-1
    i=0
    while g<=d:
        m=(g+d)//2
        if T[m]==x:
            i+=1
            return m,i
        elif T[m]>x:
            d=m-1
        else:
            g=m+1
            i+=2
    return -1
        

'''
  moodle
'''
def recherche_binaire(T,x):
    g=0
    d=len(T)-1
    i=0
    while g<=d:
        m=(g+d)//2
        if T[m]==x:
            i+=1
            return m,i
        elif T[m]>x:
            d=m-1
            i+=2
        else:
            g=m+1
            i+=2
    return -1,i

def recherche_ternaire(T,x):
    g=0
    d=len(T)-1
    i=0
    while g<=d:
        m1=(g+d)//3
        m2=(g+d)*2//3
        if T[m1]>x:
            d=m1-1
            i+=1
        elif t[m2]>x:
            d=m2-1
            g=m1+1
            i+=2
        elif T[m1]==x:
            i+=3
            return m,i
        elif T[m2]==x:
            i+=4
            return m2,i
        else:
            g=m2+1
            i+=4
    return-1,i

'''moodle'''
def recherche_ternaire(T,x):
    g=0
    d=len(T)-1
    i=0
    while g<=d:
        x1=(2*g+d)//3
        x2=(g+2*d)//3
        if T[x1]==x:
            i+=1
            return x1,i
        elif T[x2]==x:
            i+=2
            return x2,i
        elif T[x1]>x:
            d=x1-1
            i+=3
        elif T[x2]>x:
            d=x2-1
            g=x1+1
            i+=3
        else:
            g=x2+1
            i+=3
    return-1,i
        
#question n°3:

def complexité_binaire(T):
    somme=0
    for element in T:
        somme+=recherche_binaire(T,element)[1]
    return somme/len(T)


def complexité_ternaire(T):
    somme=0
    for element in T:
        somme+=recherche_ternaire(T,element)[1]
    return somme/len(T)


'''Exercice n°2:'''
#question n°1:
def recherche_zero(a,b,prec):
    l=[]
    while(b-a)>=prec:
        m=(a+b)/2
        if sin(m)==0:
            l+=[a,b]
            return l
        elif (sin(m)>0 and sin(b)>sin(a)) or (sin(m)<0 and sin(b)<sin(a)):
            b=m
            l+=[(a,b)]
        else:
            a=m
            l+=[(a,b)]
    return l
                     
'''Exercice n°3:'''
def recherche_max(a,b,prec):
    l=[[a,b]]
    g,d=a,b
    while(d-g)>=prec:
        x1=(2*g+d)/3
        x2=(2*d+g)/3
        if sin(x1)>sin(x2):
               d=x2
        elif sin(x1)<sin(x2):
               g=x1
        l+=[[g,d]]
    return l
