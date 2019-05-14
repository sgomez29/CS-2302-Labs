# -*- coding: utf-8 -*-
"""
@author: Sebastian Gomez
Course: Data Structure 2302
Assignment: Lab 8
Instructor: Olac Fuentes
T.A: Anindita Nath and Maliheh Zargaran
Purpose: Learn how randomizing algorithms are useful and how backtracking works
"""

import random
from math import *
import numpy as np
import math
from mpmath import *
import time

def equal(f1, f2,limit,tries=1000,tolerance=0.0001):
    for i in range(tries):
        t = random.uniform(-limit,limit)
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True

def partition(S,total_sum,first,last,goal1,goal2):
    if total_sum%2!=0:
        return False,[],[]
    if goal1==0 and goal2==0:
        return True,[],[]
    if first>len(S)-1 or last<0:
        return False,[],[]
    if goal1<0 and goal2<0:
        return False,[],[]
    res,subset1,subset2 = partition(S,total_sum,first+1,last-1,goal1-S[last],goal2-S[first])
    if res:
        subset1.append(S[last])
        subset2.append(S[first])
        return True,subset1,subset2
    else:
        return partition(S,total_sum,first+1,last-1,goal1,goal2) 
    
limit = math.pi
func = []
f1 = 'sin(t)'
f2 = 'cos(t)'
f3 = 'tan(t)'
f4 = 'sec(t)'
f5 = '-sin(t)'
f6 = '-cos(t)'
f7 = '-tan(t)'
f8 = 'sin(-t)'
f9 = 'cos(-t)'
f10 = 'tan(-t)'
f11 = 'sin(t)/cos(t)'
f12 = '2*sin(t/2)*cos(t/2)'
f13 = 'math.pow(sin(t),2)'
f14 = '1-math.pow(cos(t),2)'
f15 = '(1-cos(2*t))/2'
f16 = '1/cos(t)'
f = ['sin(t)','cos(t)','tan(t)','sec(t)','-sin(t)','-cos(t)','-tan(t)','sin(-t)','cos(-t)','tan(-t)','sin(t)/cos(t)','2*sin(t/2)*cos(t/2)','math.pow(sin(t),2)','1-math.pow(cos(t),2)','(1-cos(2*t))/2','1/cos(t)']
ff = []
start = time.time()
for i in range(len(f)):
    y = f[i]
    iden = equal(f1,y,limit)
    if iden==True and f1!=f[i]:
        ff.append([f1,y])
    iden = equal(f2,y,limit)
    if iden==True and f2!=f[i]:
        ff.append([f2,y])
    iden = equal(f3,y,limit)
    if iden==True and f3!=f[i]:
        ff.append([f3,y])
    iden = equal(f4,y,limit)
    if iden==True and f4!=f[i]:
        ff.append([f4,y])
    iden = equal(f5,y,limit)
    if iden==True and f5!=f[i]:
        ff.append([f5,y])
    iden = equal(f6,y,limit)
    if iden==True and f6!=f[i]:
        ff.append([f6,y])
    iden = equal(f7,y,limit)
    if iden==True and f7!=f[i]:
        ff.append([f7,y])
    iden = equal(f8,y,limit)
    if iden==True and f8!=f[i]:
        ff.append([f8,y])
    iden = equal(f9,y,limit)
    if iden==True and f9!=f[i]:
        ff.append([f9,y])
    iden = equal(f10,y,limit)
    if iden==True and f10!=f[i]:
        ff.append([f10,y])
    iden = equal(f11,y,limit)
    if iden==True and f11!=f[i]:
        ff.append([f11,y])
    iden = equal(f12,y,limit)
    if iden==True and f12!=f[i]:
        ff.append([f12,y])
    iden = equal(f13,y,limit)
    if iden==True and f13!=f[i]:
        ff.append([f13,y])
    iden = equal(f14,y,limit)
    if iden==True and f14!=f[i]:
        ff.append([f14,y])
    iden = equal(f15,y,limit)
    if iden==True and f15!=f[i]:
        ff.append([f15,y])
    iden = equal(f16,y,limit)
    if iden==True and f16!=f[i]:
        ff.append([f16,y])
end = time.time()
print('Running time:',end-start)
print(ff)
print()
F1 = f2
F2 = f9
start = time.time()
identity = (equal(F1,F2,limit))
if identity == True:
    print('There is an identity between',F1, 'and',F2)
    func.append([F1,F2])
else:
    print('They are not an identity')
end = time.time()
print('Running time:',end-start) 
func.append([f1,f12])
func.append([f2,f9])
func.append([f3,f11])
func.append([f4,f16])
func.append([f5,f8])
func.append([f7,f10])
func.append([f13,f14])
func.append([f13,f15])
func.append([f14,f15])
print(func)
print()

S = []
for i in range(60):
    x = random.randint(0,100)
    S.append(x)
print(S)
total_sum = 0
for i in range(len(S)):
    total_sum += S[i]
print('Total sum =',total_sum)
goal1 = total_sum//2
goal2 = goal1
print('Sum of each subset =',goal2)
first = 0
last = len(S)-1
start = time.time()
a,s1,s2 = partition(S,total_sum,first,last,goal1,goal2)
end = time.time()
print('Running time:',end-start)
if a:
    print('Partition:',s1,' ',s2)
else:
    print('Partition not possible')