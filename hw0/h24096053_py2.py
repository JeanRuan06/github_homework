# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:45:54 2021

@author: jeeea
"""
fin = open('IMDB-Movie-Data.csv','r')
s = fin.readlines()

for i in range(len(s)):
    s[i]=s[i].split(',')

#print(s[0],type(s[0]))
#用來比較大小
def test(thing):
        return thing[1]

#first question
def one(sets):
    dictone={}
    for i in range(len(sets)):
        for j in range(len(sets[i])):
            if (sets[i][j]=='2016'):
                dictone[sets[i][1]]=float(sets[i][7])
    dictone=sorted(dictone.items(), key=test,reverse=True)
    return dictone       
a=one(s)
print('Top-3 movies with the highest ratings in 2016: ')
print('  1.',a[0][0],' 2.',a[1][0],' 3.',a[2][0])

#second question
def two(sets):
    actor_set=set()
    dicttwo={}
    for i in range(1,len(sets)):
        each=sets[i][4].split('|')
        for j in each:
            j=j.strip()
            actor_set.add(j)
    #print(actor_set)
    for i in actor_set:
        income=[]
        for j in range(1,len(sets)):
            each=sets[j][4].split('|')
            for k in each:
                k=k.strip()
                if (k==i):
                    each_income=sets[j][9]
                    if (each_income==''):
                        each_income=0
                    income.append(float(each_income))
        dicttwo[i]=income
    return dicttwo   
b=two(s) 
for i in b.keys():
    b[i]=sum(b[i])/len(b[i])
b=sorted(b.items(), key=test,reverse=True)
print('\n','The actor generating the highest average revenue:',b[0][0],',',b[1][0])

#third 
def three(sets):
    rate=[]
    for i in range(1,len(sets)):
        each=sets[i][4].split('|')
        for j in each:
            j=j.strip()
            if (j=='Emma Watson'):
                if (sets[i][7]==''):
                    rate.append(0)
                else:
                    rate.append(float(sets[i][7]))
    return sum(rate)/len(rate)
print('\n','The average rating of Emma Watson’s movies:',three(s))
                
   
#forth question
def four(sets):
    dictfo={}
    director_set=set()
    for i in range(1,len(sets)):
        director_set.add(sets[i][3])
    for i in director_set:
        each_collab=set()
        for j in range(1,len(sets)):
            if(sets[j][3]==i):
                devi=sets[j][4].split('|')
                for k in devi:
                    k=k.strip()
                    each_collab.add(k)
                
        dictfo[i]=len(each_collab)
    return dictfo
d=four(s)
d=sorted(d.items(), key=test,reverse=True)
#print(d)
print('\n','Top-3 directors who collaborate with the most actors: ')
print('  1.',d[0][0],' 2.',d[1][0],' 3.',d[2][0],',',d[3][0]) 

#fifth question
def five(sets):
    dictfive={}
    dictcal={}
    for i in range(1,len(sets)):
        act=sets[i][4].split('|')
        gen=sets[i][2].split('|')
        for j in act:
            j=j.strip()
            if (list(dictfive.keys()).count(j)==0):
                dictfive[j]=set()
                for k in gen:
                    dictfive[j].add(k)
            else:
                for k in gen:
                    dictfive[j].add(k)
    for x,y in dictfive.items():
        dictcal[x]=len(y)
    return dictfive,dictcal
e=five(s)[1]
e=sorted(e.items(), key=test,reverse=True)
print('\n','Top-2 actors playing in the most genres of movies:','\n  1.',e[0][0],'\n  2.',e[1][0],',',e[2][0],',',e[3][0],',',e[4][0],',',e[5][0])
                
#sixth question         
def six(sets):
    dictsix={}
    dictcall={}
    for i in range(1,len(sets)):
        act=sets[i][4].split('|')
        for j in act:
            j=j.strip()
            if (list(dictsix.keys()).count(j)==0):
                dictsix[j]=[]
                dictsix[j].append(int(sets[i][5]))
            else:
                dictsix[j].append(int(sets[i][5]))
    for x,y in dictsix.items():
        y.sort()
        minu=len(y)-1
        bi=y[minu]
        sma=y[0]
        ress=bi-sma
        dictcall[x]=ress
    return dictcall
f=six(s)
f=sorted(f.items(), key=test,reverse=True)
print('\n','Top-3 actors whose movies lead to the largest maximum gap of years:')
print('  1.',f[0][0],f[0][1],'years') 
print('  2.',f[1][0],f[1][1],'years') 
print('  3.',f[2][0],f[2][1],'years') 
mi=3 
for i in range(3,len(f)):
    mi=mi+1
    if (f[i][1]==10): 
        print(' ',mi,'.',f[i][0],'10years')     
        
#seventh question 
def seven(sets):
    actor_set=set()
    dictseven={}
    for i in range(1,len(sets)):
        each=sets[i][4].split('|')
        for j in each:
            j=j.strip()
            actor_set.add(j)
    
    for i in actor_set:
        co_set=set()
        for j in range(1,len(sets)):
            co=sets[j][4].split('|')
            for k in range(len(co)):
                co[k]=co[k].strip()
           # print(co)
            if (co.count(i)==1):
                for p in co:
                    co_set.add(p)
        co_set.remove(i)
        dictseven[i]=co_set
    return dictseven
g=seven(s)
setone=g['Johnny Depp']
settwo=set()
cal=[settwo,setone]
setthree=setone-settwo
nu=1
while(len(setthree)!=0):
    nu=nu+1
    mid=set()
    for i in setthree:
        if (list(g.keys()).count(i)==0):
            continue
        else:
            for j in g[i]:
                mid.add(j)   
    cal.append(mid | cal[nu-1])
    setthree=cal[nu]-cal[nu-1]
print('Find all actors who collaborate with Johnny Depp in direct and indirect ways:' )
for i in cal[nu]:
    print(i,end=',')
     
            
        
    
fin.close()
