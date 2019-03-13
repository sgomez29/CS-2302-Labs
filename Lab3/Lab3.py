# -*- coding: utf-8 -*-
"""
Created on Wed March 6 19:26:29 2019
@author: Sebastian Gomez
Course: Data Structure 2302
Assignment: Lab 3
Instructor: Olac Fuentes
T.A: Anindita Nath and Maliheh Zargaran
Purpose: Binary search tree operations
"""

import numpy as np
import matplotlib.pyplot as plt


def draw_BStree(ax, n, deltaX, deltaY, x, y, Tr):
    if n>0:
        #changing the center x to right and left. y changes always downwards
        left = np.array([[x, y], [x - deltaX, y - deltaY]])
        right = np.array([[x, y], [x + deltaX, y - deltaY]])
        ax.plot(right[:,0],right[:,1],color='k')
        ax.plot(left[:,0],left[:,1],color='k')
        np.array(plt.Circle((x,y),20,color = 'k',fill=False))
        plt.text(x,y,Tr.item, fontdict = None, withdash = False, fontsize = 25)

        draw_BStree(ax, n-1, deltaX / 2, deltaY, x - deltaX, y - deltaY,Tr.left)#Draws the left side
        draw_BStree(ax, n-1, deltaX / 2, deltaY, x + deltaX, y - deltaY,Tr.right)#Draws the right side


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')

                        
def PrintAtDepth(Tr,d):
    if Tr is None:
        return Tr
    if d == 0:
        print(Tr.item, end = ' ')
    else:
        PrintAtDepth(Tr.left,d-1)
        PrintAtDepth(Tr.right,d-1)
 
def BSTToList(Tr):
   sort = []
   if Tr is None:
       return sort
   else:
       sort = BSTToList(Tr.left)+[Tr.item] + BSTToList(Tr.right)
   return sort
    
def Search(Tr,searchee):
    if Tr is None:
        return Tr
    else:
        while Tr is not None:
            if searchee == Tr.item:
                return True
            elif searchee < Tr.item:
                Tr = Tr.left
            elif searchee > Tr.item:
                Tr = Tr.right
        print('Element not found')
        return False


def ListToBST(B):
    if len(B) == 0:
        return None
    median = len(B)//2
    Tree = BST(B[median])
    Tree.left = ListToBST(B[:median])
    Tree.right = ListToBST(B[median+1:])
    return Tree

def Height(Tr):
    if Tr is None:
        return 0
    return max(Height(Tr.left), Height(Tr.right)) + 1#using max to know which side is longer

B = [1,2,3,4,5,7,8,9,10,12,15,18]
Tr = ListToBST(B)
plt.close("all")
fig, ax = plt.subplots()
ax.axis('on')
draw_BStree(ax, 3, 50, 50, 0, 0,Tr)
ax.set_aspect(1.0)
plt.show()
fig.savefig('BST.png')
wantedElement = int(input('What element would you like to search?'))
print('Element found: ',Search(Tr, wantedElement))
InOrder(Tr)
print()
sortedList = BSTToList(Tr)
h = Height(Tr)
for i in range(h):
    print('Keys at depth ', i, ': ', end = ' ')
    PrintAtDepth(Tr,i)
    print()
print()
i =0   
while i <= len(sortedList) - 1:
    print(sortedList[i], end = ' ')
    i +=1
print()
print()
print()
InOrderD(Tr, ' ')

  


