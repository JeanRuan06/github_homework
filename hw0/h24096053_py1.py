# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:57:52 2021

@author: jeeea
"""

#處理輸入
A=input('Input the polynomials: ')   

#處理輸入進來的字串像是(A+2*B^2)(B+3*C^3) 變成{1: ['A', '+2*B^2'], 2: ['B', '+3*C^3']}
AA=A.split(')(')
#print(AA)
DAt={}
for i in range(len(AA)):
    if (AA[i]. startswith('(')==True):
        DAt[i+1]=AA[i].replace('(','',1).replace('-',' -').replace('+',' +')
    elif (AA[i]. endswith(')')==True):
        DAt[i+1]=AA[i].replace(')','',1).replace('-',' -').replace('+',' +')
    else:
        DAt[i+1]=AA[i].replace('-',' -').replace('+',' +')
#print(DAt)
for i in range(len(AA)):
    adj=DAt[i+1].split(' ')
    DAt[i+1]=adj
for i in DAt.values():
    if (i[0]==''):
        del i[0]
#print(DAt)


# 運算前將那一項整理成可以計算的list然後用在計算中 ['係數','xx','yyy','zzz']
def an(egg): 
    #XYZ
    if (egg.find('X')!=-1 and egg.find('Y')!=-1 and egg.find('Z')!=-1):
        if (egg.find('X^')!=-1 and egg.find('Y^')!=-1 and egg.find('Z^')!=-1):
            fi=egg.replace('X','')
            sec=fi.replace('Y','')
            th=sec.replace('Z','')
            #print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'X'*int(five[1]),'Y'*int(five[2]),'Z'*int(five[3])]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','X'*int(fo[1]),'Y'*int(fo[2]),'Z'*int(fo[3])]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','X'*int(fo[1]),'Y'*int(fo[2]),'Z'*int(fo[3])]
            else:
                fo=th.split('^')
                return['+1','X'*int(fo[1]),'Y'*int(fo[2]),'Z'*int(fo[3])]
        
        elif (egg.find('Y^')!=-1 and egg.find('Z^')!=-1):
            fi=egg.replace('X','^')
            sec=fi.replace('Y','')
            th=sec.replace('Z','')
           # print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
            #    print(fo)
                five=fo.split('^')
             #   print(five)
                return [five[0],'X'*1,'Y'*int(five[2]),'Z'*int(five[3])]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','X'*1,'Y'*int(fo[2]),'Z'*int(fo[3])]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','X'*1,'Y'*int(fo[2]),'Z'*int(fo[3])]
            else:
                fo=th.split('^')
                return['+1','X'*1,'Y'*int(fo[2]),'Z'*int(fo[3])]
        
        elif (egg.find('X^')!=-1 and egg.find('Z^')!=-1):
            fi=egg.replace('X','')
            sec=fi.replace('Y','^')
            th=sec.replace('Z','')
            #print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                #print(fo)
                five=fo.split('^')
                #print(five)
                return [five[0],'X'*int(five[1]),'Y'*1,'Z'*int(five[3])]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','X'*int(fo[1]),'Y'*1,'Z'*int(fo[3])]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','X'*int(fo[1]),'Y'*1,'Z'*int(fo[3])]
            else:
                fo=th.split('^')
                return['+1','X'*int(fo[1]),'Y'*1,'Z'*int(fo[3])]
        
        elif (egg.find('X^')!=-1 and egg.find('Y^')!=-1):
            fi=egg.replace('X','')
            sec=fi.replace('Y','')
            th=sec.replace('Z','^')
            #print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'X'*int(five[1]),'Y'*int(five[2]),'Z'*1]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','X'*int(fo[1]),'Y'*int(fo[2]),'Z'*1]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','X'*int(fo[1]),'Y'*int(fo[2]),'Z'*1]
            else:
                fo=th.split('^')
                return['+1','X'*int(fo[1]),'Y'*int(fo[2]),'Z'*1]
        
        elif (egg.find('Z^')!=-1):
            fi=egg.replace('X','^')
            sec=fi.replace('Y','^')
            th=sec.replace('Z','')
           # print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'X'*1,'Y'*1,'Z'*int(five[3])]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','X'*1,'Y'*1,'Z'*int(fo[3])]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','X'*1,'Y'*1,'Z'*int(fo[3])]
            else:
                fo=th.split('^')
                return['+1','X'*1,'Y'*1,'Z'*int(fo[3])]
        
        elif (egg.find('Y^')!=-1):
            fi=egg.replace('X','^')
            sec=fi.replace('Y','')
            th=sec.replace('Z','^')
          #  print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'X'*1,'Y'*int(five[2]),'Z'*1]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','X'*1,'Y'*int(fo[2]),'Z'*1]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','X'*1,'Y'*int(fo[2]),'Z'*1]
            else:
                fo=th.split('^')
                return['+1','X'*1,'Y'*int(fo[2]),'Z'*1]
            
        elif (egg.find('X^')!=-1):
            fi=egg.replace('X','')
            sec=fi.replace('Y','^')
            th=sec.replace('Z','^')
           # print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'X'*int(five[1]),'Y'*1,'Z'*1]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','X'*int(fo[1]),'Y'*1,'Z'*1]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','X'*int(fo[1]),'Y'*1,'Z'*1]
            else:
                fo=th.split('^')
                return['+1','X'*int(fo[1]),'Y'*1,'Z'*1]
            
        else:
            fi=egg.replace('X','^')
            sec=fi.replace('Y','^')
            th=sec.replace('Z','^')
           #print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'X'*1,'Y'*1,'Z'*1]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','X'*1,'Y'*1,'Z'*1]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','X'*1,'Y'*1,'Z'*1]
            else:
                fo=th.split('^')
                return['+1','X'*1,'Y'*1,'Z'*1]

    #ABC
    if (egg.find('A')!=-1 and egg.find('B')!=-1 and egg.find('C')!=-1):
        if (egg.find('A^')!=-1 and egg.find('B^')!=-1 and egg.find('C^')!=-1):
            fi=egg.replace('A','')
            sec=fi.replace('B','')
            th=sec.replace('C','')
           # print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'A'*int(five[1]),'B'*int(five[2]),'C'*int(five[3])]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','A'*int(fo[1]),'B'*int(fo[2]),'C'*int(fo[3])]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','A'*int(fo[1]),'B'*int(fo[2]),'C'*int(fo[3])]
            else:
                fo=th.split('^')
                return['+1','A'*int(fo[1]),'B'*int(fo[2]),'C'*int(fo[3])]
        
        elif (egg.find('B^')!=-1 and egg.find('C^')!=-1):
            fi=egg.replace('A','^')
            sec=fi.replace('B','')
            th=sec.replace('C','')
           # print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
            #    print(fo)
                five=fo.split('^')
             #   print(five)
                return [five[0],'A'*1,'B'*int(five[2]),'C'*int(five[3])]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','A'*1,'B'*int(fo[2]),'C'*int(fo[3])]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','A'*1,'B'*int(fo[2]),'C'*int(fo[3])]
            else:
                fo=th.split('^')
                return['+1','A'*1,'B'*int(fo[2]),'C'*int(fo[3])]
        
        elif (egg.find('A^')!=-1 and egg.find('C^')!=-1):
            fi=egg.replace('A','')
            sec=fi.replace('B','^')
            th=sec.replace('C','')
            #print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                #print(fo)
                five=fo.split('^')
                #print(five)
                return [five[0],'A'*int(five[1]),'B'*1,'C'*int(five[3])]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','A'*int(fo[1]),'B'*1,'C'*int(fo[3])]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','A'*int(fo[1]),'B'*1,'C'*int(fo[3])]
            else:
                fo=th.split('^')
                return['+1','A'*int(fo[1]),'B'*1,'C'*int(fo[3])]
        
        elif (egg.find('A^')!=-1 and egg.find('B^')!=-1):
            fi=egg.replace('A','')
            sec=fi.replace('B','')
            th=sec.replace('C','^')
            #print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'A'*int(five[1]),'B'*int(five[2]),'C'*1]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','A'*int(fo[1]),'B'*int(fo[2]),'C'*1]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','A'*int(fo[1]),'B'*int(fo[2]),'C'*1]
            else:
                fo=th.split('^')
                return['+1','A'*int(fo[1]),'B'*int(fo[2]),'C'*1]
        
        elif (egg.find('C^')!=-1):
            fi=egg.replace('A','^')
            sec=fi.replace('B','^')
            th=sec.replace('C','')
           # print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'A'*1,'B'*1,'C'*int(five[3])]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','A'*1,'B'*1,'C'*int(fo[3])]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','A'*1,'B'*1,'C'*int(fo[3])]
            else:
                fo=th.split('^')
                return['+1','A'*1,'B'*1,'C'*int(fo[3])]
        
        elif (egg.find('B^')!=-1):
            fi=egg.replace('A','^')
            sec=fi.replace('B','')
            th=sec.replace('C','^')
          #  print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'A'*1,'B'*int(five[2]),'C'*1]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','A'*1,'B'*int(fo[2]),'C'*1]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','A'*1,'B'*int(fo[2]),'C'*1]
            else:
                fo=th.split('^')
                return['+1','A'*1,'B'*int(fo[2]),'C'*1]
            
        elif (egg.find('A^')!=-1):
            fi=egg.replace('A','')
            sec=fi.replace('B','^')
            th=sec.replace('C','^')
           # print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'A'*int(five[1]),'B'*1,'C'*1]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','A'*int(fo[1]),'B'*1,'C'*1]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','A'*int(fo[1]),'B'*1,'C'*1]
            else:
                fo=th.split('^')
                return['+1','A'*int(fo[1]),'B'*1,'C'*1]
            
        else:
            fi=egg.replace('A','^')
            sec=fi.replace('B','^')
            th=sec.replace('C','^')
           #print(th)
            if (egg.find('*')!=-1):
                fo=th.replace('*','')
                five=fo.split('^')
                return [five[0],'A'*1,'B'*1,'C'*1]
            elif (egg.find('-')!=-1):
                fo=th.split('^')
                return['-1','A'*1,'B'*1,'C'*1]
            elif (egg.find('+')!=-1):
                fo=th.split('^')
                return['+1','A'*1,'B'*1,'C'*1]
            else:
                fo=th.split('^')
                return['+1','A'*1,'B'*1,'C'*1]
    
    #YZ
    elif (egg.find('Y')!=-1 and egg.find('Z')!=-1):
        if (egg.find('Y^')!=-1 and egg.find('Z^')!=-1):
            fi=egg.replace('Y','')
            sec=fi.replace('Z','')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'','Y'*int(fo[1]),'Z'*int(fo[2])]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','','Y'*int(th[1]),'Z'*int(th[2])]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','','Y'*int(th[1]),'Z'*int(th[2])]
            else:
                th=sec.split('^')
                return['+1','','Y'*int(th[1]),'Z'*int(th[2])]
        elif (egg.find('Z^')!=-1):
            fi=egg.replace('Y','^')
            sec=fi.replace('Z','')
            #print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'','Y'*1,'Z'*int(fo[2])]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','','Y'*1,'Z'*int(th[2])]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','','Y'*1,'Z'*int(th[2])]
            else:
                th=sec.split('^')
                return['+1','','Y'*1,'Z'*int(th[2])]
        elif (egg.find('Y^')!=-1):
            fi=egg.replace('Y','')
            sec=fi.replace('Z','^')
            #print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'','Y'*int(fo[1]),'Z'*1]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','','Y'*int(th[1]),'Z'*1]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','','Y'*int(th[1]),'Z'*1]
            else:
                th=sec.split('^')
                return['+1','','Y'*int(th[1]),'Z'*1]
        else:
            fi=egg.replace('Y','^')
            sec=fi.replace('Z','^')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
                #print(fo)
                return [fo[0],'','Y'*1,'Z'*1]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','','Y'*1,'Z'*1]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','','Y'*1,'Z'*1]
            else:
                th=sec.split('^')
                return['+1','','Y'*1,'Z'*1]
            
    #BC
    elif (egg.find('B')!=-1 and egg.find('C')!=-1):
        if (egg.find('B^')!=-1 and egg.find('C^')!=-1):
            fi=egg.replace('B','')
            sec=fi.replace('C','')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'','B'*int(fo[1]),'C'*int(fo[2])]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','','B'*int(th[1]),'C'*int(th[2])]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','','B'*int(th[1]),'C'*int(th[2])]
            else:
                th=sec.split('^')
                return['+1','','B'*int(th[1]),'C'*int(th[2])]
        elif (egg.find('C^')!=-1):
            fi=egg.replace('B','^')
            sec=fi.replace('C','')
            #print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'','B'*1,'C'*int(fo[2])]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','','B'*1,'C'*int(th[2])]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','','B'*1,'C'*int(th[2])]
            else:
                th=sec.split('^')
                return['+1','','B'*1,'C'*int(th[2])]
        elif (egg.find('B^')!=-1):
            fi=egg.replace('B','')
            sec=fi.replace('C','^')
            #print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'','B'*int(fo[1]),'C'*1]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','','B'*int(th[1]),'C'*1]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','','B'*int(th[1]),'C'*1]
            else:
                th=sec.split('^')
                return['+1','','B'*int(th[1]),'C'*1]
        else:
            fi=egg.replace('B','^')
            sec=fi.replace('C','^')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
                #print(fo)
                return [fo[0],'','B'*1,'C'*1]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','','B'*1,'C'*1]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','','B'*1,'C'*1]
            else:
                th=sec.split('^')
                return['+1','','B'*1,'C'*1]
    #XZ
    elif (egg.find('X')!=-1 and egg.find('Z')!=-1):
        if (egg.find('X^')!=-1 and egg.find('Z^')!=-1):
            fi=egg.replace('X','')
            sec=fi.replace('Z','')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
             #   print(fo)
                return [fo[0],'X'*int(fo[1]),'','Z'*int(fo[2])]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','X'*int(th[1]),'','Z'*int(th[2])]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','X'*int(th[1]),'','Z'*int(th[2])]
            else:
                th=sec.split('^')
                return['+1','X'*int(th[1]),'','Z'*int(th[2])]
        elif (egg.find('Z^')!=-1):
            fi=egg.replace('X','^')
            sec=fi.replace('Z','')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
              #  print(fo)
                return [fo[0],'X'*1,'','Z'*int(fo[2])]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','X'*1,'','Z'*int(th[2])]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','X'*1,'','Z'*int(th[2])]
            else:
                th=sec.split('^')
                return['+1','X'*1,'','Z'*int(th[2])]
        elif (egg.find('X^')!=-1):
            fi=egg.replace('X','')
            sec=fi.replace('Z','^')
          #  print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
              #  print(fo)
                return [fo[0],'X'*int(fo[1]),'','Z'*1]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','X'*int(th[1]),'','Z'*1]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','X'*int(th[1]),'','Z'*1]
            else:
                th=sec.split('^')
                return['+1','X'*int(th[1]),'','Z'*1]
        else:
            fi=egg.replace('X','^')
            sec=fi.replace('Z','^')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'X'*1,'','Z'*1]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','X'*1,'','Z'*1]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','X'*1,'','Z'*1]
            else:
                th=sec.split('^')
                return['+1','X'*1,'','Z'*1]    
            
    #AC
    elif (egg.find('A')!=-1 and egg.find('C')!=-1):
        if (egg.find('A^')!=-1 and egg.find('C^')!=-1):
            fi=egg.replace('A','')
            sec=fi.replace('C','')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
             #   print(fo)
                return [fo[0],'A'*int(fo[1]),'','C'*int(fo[2])]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','A'*int(th[1]),'','C'*int(th[2])]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','A'*int(th[1]),'','C'*int(th[2])]
            else:
                th=sec.split('^')
                return['+1','A'*int(th[1]),'','C'*int(th[2])]
        elif (egg.find('C^')!=-1):
            fi=egg.replace('A','^')
            sec=fi.replace('C','')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
              #  print(fo)
                return [fo[0],'A'*1,'','C'*int(fo[2])]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','A'*1,'','C'*int(th[2])]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','A'*1,'','C'*int(th[2])]
            else:
                th=sec.split('^')
                return['+1','A'*1,'','C'*int(th[2])]
        elif (egg.find('A^')!=-1):
            fi=egg.replace('A','')
            sec=fi.replace('C','^')
          #  print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
              #  print(fo)
                return [fo[0],'A'*int(fo[1]),'','C'*1]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','A'*int(th[1]),'','C'*1]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','A'*int(th[1]),'','C'*1]
            else:
                th=sec.split('^')
                return['+1','A'*int(th[1]),'','C'*1]
        else:
            fi=egg.replace('A','^')
            sec=fi.replace('C','^')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'A'*1,'','C'*1]
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','A'*1,'','C'*1]
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','A'*1,'','C'*1]
            else:
                th=sec.split('^')
                return['+1','A'*1,'','C'*1]   
            
    #XY
    elif (egg.find('X')!=-1 and egg.find('Y')!=-1):
        if (egg.find('X^')!=-1 and egg.find('Y^')!=-1):
            fi=egg.replace('X','')
            sec=fi.replace('Y','')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
            #    print(fo)
                return [fo[0],'X'*int(fo[1]),'Y'*int(fo[2]),'']
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','X'*int(th[1]),'Y'*int(th[2]),'']
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','X'*int(th[1]),'Y'*int(th[2]),'']
            else:
                th=sec.split('^')
                return['+1','X'*int(th[1]),'Y'*int(th[2]),'']
        elif (egg.find('Y^')!=-1):
            fi=egg.replace('X','^')
            sec=fi.replace('Y','')
          #  print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
           #     print(fo)
                return [fo[0],'X'*1,'Y'*int(fo[2]),'']
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','X'*1,'Y'*int(th[2]),'']
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','X'*1,'Y'*int(th[2]),'']
            else:
                th=sec.split('^')
                return['+1','X'*1,'Y'*int(th[2]),'']
        elif (egg.find('X^')!=-1):
            fi=egg.replace('X','')
            sec=fi.replace('Y','^')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
            #    print(fo)
                return [fo[0],'X'*int(fo[1]),'Y'*1,'']
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','X'*int(th[1]),'Y'*1,'']
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','X'*int(th[1]),'Y'*1,'']
            else:
                th=sec.split('^')
                return['+1','X'*int(th[1]),'Y'*1,'']
        else:
            fi=egg.replace('X','^')
            sec=fi.replace('Y','^')
            #print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'X'*1,'Y'*1,'']
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','X'*1,'Y'*1,'']
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','X'*1,'Y'*1,'']
            else:
                th=sec.split('^')
                return['+1','X'*1,'Y'*1,'']    
    
    #AB
    elif (egg.find('A')!=-1 and egg.find('B')!=-1):
        if (egg.find('A^')!=-1 and egg.find('B^')!=-1):
            fi=egg.replace('A','')
            sec=fi.replace('B','')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
            #    print(fo)
                return [fo[0],'A'*int(fo[1]),'B'*int(fo[2]),'']
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','A'*int(th[1]),'B'*int(th[2]),'']
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','A'*int(th[1]),'B'*int(th[2]),'']
            else:
                th=sec.split('^')
                return['+1','A'*int(th[1]),'B'*int(th[2]),'']
        elif (egg.find('B^')!=-1):
            fi=egg.replace('A','^')
            sec=fi.replace('B','')
          #  print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
           #     print(fo)
                return [fo[0],'A'*1,'B'*int(fo[2]),'']
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','A'*1,'B'*int(th[2]),'']
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','A'*1,'B'*int(th[2]),'']
            else:
                th=sec.split('^')
                return['+1','A'*1,'B'*int(th[2]),'']
        elif (egg.find('A^')!=-1):
            fi=egg.replace('A','')
            sec=fi.replace('B','^')
           # print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
            #    print(fo)
                return [fo[0],'A'*int(fo[1]),'B'*1,'']
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','A'*int(th[1]),'B'*1,'']
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','A'*int(th[1]),'B'*1,'']
            else:
                th=sec.split('^')
                return['+1','A'*int(th[1]),'B'*1,'']
        else:
            fi=egg.replace('A','^')
            sec=fi.replace('B','^')
            #print(sec)
            if (egg.find('*')!=-1):
                th=sec.replace('*','')
                fo=th.split('^')
               # print(fo)
                return [fo[0],'A'*1,'B'*1,'']
            elif (egg.find('-')!=-1):
                th=sec.split('^')
                return['-1','A'*1,'B'*1,'']
            elif (egg.find('+')!=-1):
                th=sec.split('^')
                return['+1','A'*1,'B'*1,'']
            else:
                th=sec.split('^')
                return['+1','A'*1,'B'*1,'']    
   
    #X
    elif (egg.find('X')!=-1):
        egg=egg.split('X')
        #print(egg)
        if (egg[1].find('^')!=-1):
            egg[1]=egg[1].split('^')
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'X'*int(egg[1][1]),'','']
            elif(egg[0].find('-')!=-1):
                return ['-1','X'*int(egg[1][1]),'','']
            elif(egg[0].find('+')!=-1):
                return ['+1','X'*int(egg[1][1]),'','']
            else:
                return ['+1','X'*int(egg[1][1]),'','']
        else:
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'X'*1,'','']
            elif(egg[0].find('-')!=-1):
                return ['-1','X'*1,'','']
            elif(egg[0].find('+')!=-1):
                return ['+1','X'*1,'','']
            else:
                return ['+1','X'*1,'','']
    #A
    elif (egg.find('A')!=-1):
        egg=egg.split('A')
        #print(egg)
        if (egg[1].find('^')!=-1):
            egg[1]=egg[1].split('^')
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'A'*int(egg[1][1]),'','']
            elif(egg[0].find('-')!=-1):
                return ['-1','A'*int(egg[1][1]),'','']
            elif(egg[0].find('+')!=-1):
                return ['+1','A'*int(egg[1][1]),'','']
            else:
                return ['+1','A'*int(egg[1][1]),'','']
        else:
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'A'*1,'','']
            elif(egg[0].find('-')!=-1):
                return ['-1','A'*1,'','']
            elif(egg[0].find('+')!=-1):
                return ['+1','A'*1,'','']
            else:
                return ['+1','A'*1,'','']
    #Y
    elif (egg.find('Y')!=-1):
        egg=egg.split('Y')
        #print(egg)
        if (egg[1].find('^')!=-1):
            egg[1]=egg[1].split('^')
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'','Y'*int(egg[1][1]),'']
            elif(egg[0].find('-')!=-1):
                return ['-1','','Y'*int(egg[1][1]),'']
            elif(egg[0].find('+')!=-1):
                return ['+1','','Y'*int(egg[1][1]),'']
            else:
                return ['+1','','Y'*int(egg[1][1]),'']
        else:
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'','Y'*1,'']
            elif(egg[0].find('-')!=-1):
                return ['-1','','Y'*1,'']
            elif(egg[0].find('+')!=-1):
                return ['+1','','Y'*1,'']
            else:
                return ['+1','','Y'*1,'']
    
    #B
    elif (egg.find('B')!=-1):
        egg=egg.split('B')
        #print(egg)
        if (egg[1].find('^')!=-1):
            egg[1]=egg[1].split('^')
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'','B'*int(egg[1][1]),'']
            elif(egg[0].find('-')!=-1):
                return ['-1','','B'*int(egg[1][1]),'']
            elif(egg[0].find('+')!=-1):
                return ['+1','','B'*int(egg[1][1]),'']
            else:
                return ['+1','','B'*int(egg[1][1]),'']
        else:
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'','B'*1,'']
            elif(egg[0].find('-')!=-1):
                return ['-1','','B'*1,'']
            elif(egg[0].find('+')!=-1):
                return ['+1','','B'*1,'']
            else:
                return ['+1','','B'*1,'']
    #Z
    elif (egg.find('Z')!=-1):
        egg=egg.split('Z')
        #print(egg)
        if (egg[1].find('^')!=-1):
            egg[1]=egg[1].split('^')
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'','','Z'*int(egg[1][1])]
            elif(egg[0].find('-')!=-1):
                return ['-1','','','Z'*int(egg[1][1])]
            elif(egg[0].find('+')!=-1):
                return ['+1','','','Z'*int(egg[1][1])]
            else:
                return ['+1','','','Z'*int(egg[1][1])]
        else:
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'','','Z'*1]
            elif(egg[0].find('-')!=-1):
                return ['-1','','','Z'*1]
            elif(egg[0].find('+')!=-1):
                return ['+1','','','Z'*1]
            else:
                return ['+1','','','Z'*1]
    
    #C
    elif (egg.find('C')!=-1):
        egg=egg.split('C')
        #print(egg)
        if (egg[1].find('^')!=-1):
            egg[1]=egg[1].split('^')
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'','','C'*int(egg[1][1])]
            elif(egg[0].find('-')!=-1):
                return ['-1','','','C'*int(egg[1][1])]
            elif(egg[0].find('+')!=-1):
                return ['+1','','','C'*int(egg[1][1])]
            else:
                return ['+1','','','C'*int(egg[1][1])]
        else:
            if (egg[0].find('*')!=-1):
                egg[0]=egg[0].split('*')
                return [egg[0][0],'','','C'*1]
            elif(egg[0].find('-')!=-1):
                return ['-1','','','C'*1]
            elif(egg[0].find('+')!=-1):
                return ['+1','','','C'*1]
            else:
                return ['+1','','','C'*1]
    #none                
    else:
        return [egg,'','','']
    
    
    
#一層的計算，會存到c中，用在while迴圈裡將多項試算出來
c=[]
def secal(x,y):
    for i in x:
        for j in y:
            fir=an(i)
            se=an(j)
            #print(fir)
            #print(se)
            A=str(int(fir[0])*int(se[0]))
            if (A.startswith('-')==False):
                A = '+' + A
            B=str((fir[1]+se[1]).count('X'))       
            BB='^'.join(['X',B])
            C=str((fir[2]+se[2]).count('Y'))
            CC='^'.join(['Y',C])
            D=str((fir[3]+se[3]).count('Z'))
            DD='^'.join(['Z',D])
            ALL=BB+CC+DD
            c.append('*'.join([A,ALL]))
    return c

def secalll(x,y):
    for i in x:
        for j in y:
            fir=an(i)
            se=an(j)
            #print(fir)
            #print(se)
            A=str(int(fir[0])*int(se[0]))
            if (A.startswith('-')==False):
                A = '+' + A
            B=str((fir[1]+se[1]).count('A'))       
            BB='^'.join(['A',B])
            C=str((fir[2]+se[2]).count('B'))
            CC='^'.join(['B',C])
            D=str((fir[3]+se[3]).count('C'))
            DD='^'.join(['C',D])
            ALL=BB+CC+DD
            c.append('*'.join([A,ALL]))
    return c



#利用while將一層一層完成
x=len(DAt)
two=2
if (A.find('X')!=-1 or A.find('Y')!=-1 or A.find('Z')!=-1 ):
    while (x!=1):
        x=x-1
        secal(DAt[1],DAt[two])
        # print('*',c)
        DAt[1]=c
        c=[]
        two=two+1
    #print('DAt',DAt)
    for i in range(len(DAt[1])):
         DAt[1][i]=DAt[1][i].replace('X^0','').replace('Y^0','').replace('Z^0','')
         if (DAt[1][i].find('X^1Y')!=-1 or DAt[1][i].find('X^1Z')!=-1 ):
             DAt[1][i]=DAt[1][i].replace('X^1','X')
         if (DAt[1][i].find('Y^1Z')!=-1 or DAt[1][i].endswith('Y^1')):
             DAt[1][i]=DAt[1][i].replace('Y^1','Y')
         if (DAt[1][i].endswith('Z^1')):
             DAt[1][i]=DAt[1][i].replace('Z^1','Z')
         if (DAt[1][i].startswith('+1*')):
             DAt[1][i]=DAt[1][i].replace('+1*','+')
         if (DAt[1][i].startswith('-1*')):
             DAt[1][i]=DAt[1][i].replace('-1*','-')
         
    print('Output result:',''.join(DAt[1]))

else:
    while (x!=1):
        x=x-1
        secalll(DAt[1],DAt[two])
       # print('*',c)
        DAt[1]=c
        c=[]
        two=two+1
    #print('DAt',DAt)
    for i in range(len(DAt[1])):
         DAt[1][i]=DAt[1][i].replace('A^0','').replace('B^0','').replace('C^0','')
         if (DAt[1][i].find('A^1B')!=-1 or DAt[1][i].find('A^1C')!=-1 ):
             DAt[1][i]=DAt[1][i].replace('A^1','A')
         if (DAt[1][i].find('B^1C')!=-1 or DAt[1][i].endswith('B^1')):
             DAt[1][i]=DAt[1][i].replace('B^1','B')
         if (DAt[1][i].endswith('C^1')):
             DAt[1][i]=DAt[1][i].replace('C^1','C')
         if (DAt[1][i].startswith('+1*')):
             DAt[1][i]=DAt[1][i].replace('+1*','+')
         if (DAt[1][i].startswith('-1*')):
             DAt[1][i]=DAt[1][i].replace('-1*','-')
    print('Output result:',''.join(DAt[1]))

    

    


