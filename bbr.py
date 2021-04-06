""" Retourne la liste des indices des cases à
échanger pour obtenir un tableau à trois couleurs
trié en bleu/blanc/rouge"""

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
        
            
            
