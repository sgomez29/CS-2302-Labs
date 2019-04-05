# -*- coding: utf-8 -*-
"""
@author: Sebastian Gomez
Course: Data Structure 2302
Assignment: Lab 5
Instructor: Olac Fuentes
T.A: Anindita Nath and Maliheh Zargaran
Purpose: Binary search tree and hash implemenatation of reading a file to compute similarities of a given file
"""

# Implementation of hash tables with chaining using strings
import time
import numpy as np
import math
global start
global end

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T


def Height(Tr):
    if Tr is None:
        return 0
    return max(Height(Tr.left), Height(Tr.right)) + 1#using max to know which side is longer

def NumOfNodes(T):
    if T is None:
        return 0
    return NumOfNodes(T.left) + NumOfNodes(T.right) + 1

def Search(T,k):
    if T is None:
        return T
    temp = T
    while temp is not None:
        if temp.item[0] == k:
            return temp.item[1]
        elif temp.item[0] < k:
            temp = temp.right
        else:
            temp = temp.left
    return None


def BuildBST(f,pairsOfWords):
    print('Building binary search tree')
    print()
    T = None
    start = float(time.time())
    for line in f:
        info = line.split(' ')
        T = Insert(T,[info[0],np.array(info[1:]).astype(np.float)])
    end = float(time.time())
    print('Binary Search Tree stats:')
    print()
    print('Number of Nodes: ',NumOfNodes(T))
    print('Height: ',Height(T))
    print('Running time for constructing binary search tree: ',round((end-start),2))
    print()
    print('Reading word file to determine similarities')
    print()
    start = float(time.time())
    print('Word Similarities Found:')
    for Line in pairsOfWords:
        infor = Line.split(' ')
    e0 = Search(T,infor[0])
    e1 = Search(T,infor[1])
    print('Similarity',infor[0:2], '= ', round(np.sum(e0 *e1) / (math.sqrt(np.sum(e0*e0)) * math.sqrt(np.sum(e1*e1))),4))
    end = float(time.time())
    print()
    print('Running time for binary search tree query processing: ',round((end-start),2))
    
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.num_items = 0
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    if H.num_items // len(H.item) == 1:
        H = double(H)
    b = h(k[0],len(H.item))
    H.item[b].append([k[0],np.array(k[1:]).astype(np.float)])
    H.num_items+=1
    return H
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return H.item[b][i][1]
    return -1

def double(H):
    size = 2 * len(H.item) + 1
    DoubleH = HashTableC(size)
    
    for i in H.item:
        if i != []:
            for j in i:
                DoubleH.item[h(j[0],len(DoubleH.item))].append([j[0],j[1]])
                DoubleH.num_items += 1
    return DoubleH

def emptyList(H):
    numOfEmptyLists = 0
    for h in H.item:
        if h == []:
            numOfEmptyLists +=1
    return numOfEmptyLists


def deviation(H):
    loadFactor = H.num_items / len(H.item) 
    deviation = 0
    for i in H.item:
        deviation += len(i) - loadFactor
    return deviation / len(H.item)
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def BuildHashTable(f,pairsOfWords):
    print('Building hash table with chaining')
    print()
    print('Hash Table Stats:')
    H = HashTableC(50)
    print('Initial Table size: ',len(H.item))
    start =  float(time.time())
    for line in f:
        info = line.split(' ')
        H = InsertC(H,info,1)
    end = float(time.time())
    print('Final table size: ',len(H.item))
    print('Load factor: ',H.num_items/len(H.item))
    e = emptyList(H)
    d = deviation(H)
    print('Percentage of empty lists: ',(e*100 / len(H.item)))
    print('Standard deviation of the lenghts of the lists: ',d)
    print('Running time for hash table construction: ',round((end-start),2))
    print()
    print('Reading word file to determine similarities')
    print()
    start = float(time.time())
    print('Word Similarities Found:')
    for Line in pairsOfWords:
        infor = Line.rstrip('\n').split(' ')
        e0 = FindC(H,infor[0])
        e1 = FindC(H,infor[1])
        print('Similarity',infor[0:2], '= ', round(np.sum(e0 *e1) / (math.sqrt(np.sum(e0*e0)) * math.sqrt(np.sum(e1*e1))),4))
    end = float(time.time())
    print()
    print('Running time for hash table query processing: ',round((end-start),6))
    
c = '1'
while c == '1' or c == '2':
    c = input('Choose table implementation Type 1 for binary search tree or 2 for hash table with chaining ')
    print('Choice:', c)
    print()
    f = open('glove.6B.50d.txt',encoding = 'utf-8')
    pairsOfWords = open('pairs.txt',encoding = 'utf-8',)
    if c == '1':
        BuildBST(f,pairsOfWords)
    elif c == '2':
        BuildHashTable(f,pairsOfWords)
    f.close()
    pairsOfWords.close()