# -*- coding: utf-8 -*-
"""
@author: Sebastian Gomez
Course: Data Structure 2302
Assignment: Lab 7
Instructor: Olac Fuentes
T.A: Anindita Nath and Maliheh Zargaran
Purpose: Find the path from source to destination using different algorithmic searches.
"""

import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import interpolate
import time
import math


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
    
def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def NumSets(S):
    count =0
    for i in range(len(S)):
        if S[i]<0:
            count += 1
    return count

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def draw_dsf(S):
    scale = 30
    fig, ax = plt.subplots()
    for i in range(len(S)):
        if S[i]<0: # i is a root
            ax.plot([i*scale,i*scale],[0,scale],linewidth=1,color='k')
            ax.plot([i*scale-1,i*scale,i*scale+1],[scale-2,scale,scale-2],linewidth=1,color='k')
        else:
            x = np.linspace(i*scale,S[i]*scale)
            x0 = np.linspace(i*scale,S[i]*scale,num=5)
            diff = np.abs(S[i]-i)
            if diff == 1: #i and S[i] are neighbors; draw straight line
                y0 = [0,0,0,0,0]
            else:      #i and S[i] are not neighbors; draw arc
                y0 = [0,-6*diff,-8*diff,-6*diff,0]
            f = interpolate.interp1d(x0, y0, kind='cubic')
            y = f(x)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0[2]+2*np.sign(i-S[i]),x0[2],x0[2]+2*np.sign(i-S[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)
    
def mazeByUnion(S,walls,a):
    while a!=0:
        d = random.randint(0,len(walls)-1)
        c1 = find(S,walls[d][0])
        c2 = find(S,walls[d][1])
        if c1 != c2:
            union(S,walls[d][0],walls[d][1])
            walls.pop(d)
        a-=1

            
def draw_graph(G):
    fig, ax = plt.subplots()
    n = len(G)
    r = 30
    coords =[]
    for i in range(n):
        theta = 2*math.pi*i/n+.001 # Add small constant to avoid drawing horizontal lines, which matplotlib doesn't do very well
        coords.append([-r*np.cos(theta),r*np.sin(theta)])
    for i in range(n):
        for dest in G[i]:
            ax.plot([coords[i][0],coords[dest][0]],[coords[i][1],coords[dest][1]],
                     linewidth=1,color='k')
    for i in range(n):
        ax.text(coords[i][0],coords[i][1],str(i), size=10,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.set_aspect(1.0)
    ax.axis('off') 
     

def Breadth_first_search(G,v):
    visited = [False]*(len(G))
    prev = [-math.inf] *len(G)
    queue = []
    queue.append(v)
    visited[v] = True
    
    while queue:
        u = queue.pop()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                queue.append(t)
    return prev
    
def depthFirst_stack(G,source):
    visited = [False] *(len(G))
    prev = [-math.inf]*len(G)
    visited[source] = True
    S = Stack()
    S.push(source)
    
    while S:
        u = S.pop()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                S.push(t)
    return prev
        
    
def depthFirst_rec(G,source):
    visited = [False]*(len(G))
    prev = [-math.inf] *len(G)
    visited[source] = True
    for t in G[source]:
        if not visited[t]:
            prev[t] = source
        depthFirst_rec(G,t)
    
        
def adjList_fromMaze(S):
    G = [ [] for i in range(len(S)) ]
    for j in range(len(S)):
        if S[j] != -1:
            G[j].append(S[j])
    return G
    


plt.close("all") 
maze_rows = 11
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True)#displaying before creating the maze 
S = DisjointSetForest(maze_rows*maze_cols)
draw_dsf(S)#displaying before union

m = maze_rows*maze_cols
print('There are ', m-1 , 'cells')
a = int(input('How many walls would you like to remove? '))
if a < m-1:
    print('A path from source to destination is not guaranteed to exist')
elif a == m-1:
    print('There is a unique path from source to destination')
else:
    print('There is at least one path from source to destination')


mazeByUnion(S,walls,a)  
print(S)
G = adjList_fromMaze(S)    
print(G)     
start = time.time()
depthFirst_rec(G,3)
end = time.time()
print(end-start)

draw_graph(G)
draw_dsf(S)#to check if there is only one set
draw_maze(walls,maze_rows,maze_cols)#displaying the maze