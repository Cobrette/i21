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


def multiplication (n1,n2):
    liste=[0]*(len(n1)+len(n2))

    for i in range (len(n2)):
        for j in range (len(n1)):
            liste[i+j]+=n1[j]*n2[i]
            if liste [i+j]>9:
                liste[i+j+1] += liste[i+j]//10
                liste [i+j]=liste[i+j]%10
    return liste

#question n°2:
lim = 10**20
# on cree  une  liste  contenant  des  paires  de  nombres  aleatoire
stest = []
for i in  range (10000):
     n1=randrange(lim)
     n2=randrange(lim)
     test +=[(n1 ,n2)]
# on  stocke l’heure de  depart
start=time()
    for n1 ,n2 in test:
        n3=n1*n2
# on  recupere l’heure de fin et on  affiche  le  resultat
end=time()
print(end -start)



    
