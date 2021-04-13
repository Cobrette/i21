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
        
#question n°3:

def complexité_binaire(T):



    
def complexité_ternaire(T):





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
                     
