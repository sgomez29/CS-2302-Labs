# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:35:14 2019
@author: Sebastian Gomez
Course: Data Structure 2302
Assignment: Lab 1
Instructor: Olac Fuentes
T.A: Anindita Nath and Maliheh Zargaran
Purpose: Use of recursive calls to plot and create complex figures
"""
import numpy as np
import matplotlib.pyplot as plt
import math 
import time

global start
global end

def draw_squares(ax,n,p,w,center,radius):
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        center = [0,0]
        radius = p[:,0] / 2
        draw_squares(ax,n-1,q,w,center,radius)
        

start = time.time()
plt.close("all") 
p = np.array([[-400,-400],[400,-400],[400,400],[-400,400],[-400,-400]])
fig, ax = plt.subplots()
center = [0,0]
draw_squares(ax,1,p,.2,center,50)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')
end = time.time()
print(end - start)

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,[center[0] - (radius*(1-w)),0],radius*w,w)

start = time.time()
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax,14,[200,0],200,.8)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')
end = time.time()
print(end - start)

start = time.time()
plt.close("all") 
fig, ax2 = plt.subplots() 
r = 200
center = [0,0]
draw_circles(ax2,1,center,200,.8)
draw_circles(ax2,1,[center[0] - (2/3)*r,0],r/3,.1)
draw_circles(ax2,1,[center[0] + (2/3)*r,0],r/3,.1)
draw_circles(ax2,1,[center[0],0],r/3,.1)
draw_circles(ax2,1,[center[0],center[0] - (2/3)*r ],r/3,.1)
draw_circles(ax2,1,[center[0],center[0] + (2/3)*r ],r/3,.1)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')
end = time.time()
print(end - start)

def draw_tree(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_tree(ax,n-1,q,w)
        

start = time.time()
plt.close("all") 
size = 100
p = np.array([[0,0],[size,-size],[0,0],[-size,-size],[0,0]])
p = np.array([[0,0],[size/2,-size/2],[0,0],[-size/2,-size/2],[0,0]])
fig, ax = plt.subplots()
draw_tree(ax,1,p,.1)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')
end = time.time()
print(end - start)