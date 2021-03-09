import  matplotlib.pyplot  as plt
from math import cos,sin,pi
import math as math
from  time  import  time
from  random  import  randrange

#question n°1:
# On cree la liste  des  abscisses  des  point  que l’on veut  tracer
abscisse = []
for i in  range (10):
    abscisse += [i]

# On cree la liste  des  ordonnees  des  points  que l’on veut  tracer:
carre = []
for i in  range(len(abscisse )):
    carre += [abscisse[i]**2]

cube = []
for i in  range(len(abscisse )):
    cube += [abscisse[i]**3]

# plot() trace  les  courbes  correspondantes  et show() les  affiche
# a l’ecran.

plt.plot(abscisse , carre , abscisse , cube)


#question n°2:
#liste des values comprise en a et +b
def intervalle(a,b,inc):
    values=[]
    values +=[a]
    while values[len(values)-1]+inc <=b:
        last=values[len(values)-1]
        values += [last+inc]
    return values

'''
premier courbe avec matplotlib
'''

#question n°3:
#prends la liste des valeurs grace au fonction cos/sin  aux point donnés par la liste t
def valeur_sin(t):
    return [math.sin(x) for x in t]

def valeur_cos(t):
    return [math.cos(x) for x in t]

abscisse=intervalle(-2*pi,2*pi,pi/100)
liste1=valeur_sin(abscisse)
liste2=valeur_cos(abscisse)
plt.plot(abscisse,liste1,label="sin")
plt.plot(abscisse,liste2,label="cos")
plt.legend()
plt.show()
'''
etude de la multiplication en python
'''
#question n°1:
# [::-1] signifie vide : vide : -1

def multiplication(n1,n2):
    n1,n2=n1[::-1], n2[::-1]

    n=len(n1)
    n3=[0]*2*n

    j=0
    while j<n:
        i,r = 0, 0
        while i<n:
            p=n3[i+j]+n1[i]*n2[j]+r
            n3[i+j]=p%10
            r=p//10
            i+=1
        n3[i+j]=r
        j+=1

    return n3[::-1]



    
