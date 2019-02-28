# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:26:29 2019
@author: Sebastian Gomez
Course: Data Structure 2302
Assignment: Lab 2
Instructor: Olac Fuentes
T.A: Anindita Nath and Maliheh Zargaran
Purpose: Sort a list and return the middle element of a sorted list
"""

import random

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
    
def Prepend(L,x):
    #Inserts x at the beggining of the list
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        temp = L.head
        L.head = Node(x)
        L.head.next = temp
    
def getLength(L):
    temp = L.head
    count = 0
    while temp is not None:
        count = count + 1
        temp = temp.next
    return count
    
def BubbleSort(L):
    done = True
    counter = 0
    while done:
        done = False
        temp = L.head
        n = 0
        while temp.next is not None and n < getLength(L):
            if temp.item > temp.next.item:
                counter = counter + 1
                value = temp.item
                value2 = temp.next.item
                temp.item = value2
                temp.next.item = value
                done = True
            temp = temp.next 
            n = n + 1
    print('Number of comparisons: ',counter)

def QuickSort(L):
    if getLength(L) > 1:
        counter = 0
        pivot = L.head.item
        L1 = List()
        L2 = List()
        temp = L.head.next
        
        while temp is not None:
            if temp.item < pivot:
                Append(L1,temp.item)
            else:
                Append(L2,temp.item) 
            counter = counter + 1
            temp = temp.next
            
        QuickSort(L1)
        QuickSort(L2)
        
        if IsEmpty(L1):
            Append(L1,pivot)
        else:
            Prepend(L2,pivot)
            
        if IsEmpty(L1):
            L.head = L2.head
            L.tail = L2.tail
        else:
            L1.tail.next = L2.head
            L.head = L1.head
            L.tail = L2.tail
        
        print('Number of comparisons: ',counter)
        
def QuickSortOptimized(L):
    if getLength(L) > 1:
        counter = 0
        pivot = L.head.item
        L1 = List()
        temp = L.head.next
        
        while temp is not None:
            if temp.item < pivot:
                Append(L1,temp.item)
            else:
                Prepend(L1,temp.item) 
            counter = counter + 1
            temp = temp.next
            
        QuickSort(L1)
        Append(L1,pivot)
        L.head = L1.head
        L.tail = L1.tail

def Merge(L1,L2):
    merged = List()
    temp = L1.head
    temp2 = L2.head
    
    if temp is None:
        return temp2
    if temp2 is None:
        return temp
    
   
    if temp.item <= temp.item:
           Append(merged,temp.item)
           Merge(temp.next,temp2)
        
    else:
        Append(merged,temp2.item)
        Merge(temp,temp2.next)
        
    return merged   


def MergeSort(L):
    if getLength(L) > 1:
       L1 = List()
       L2 = List()
       temp = L.head
       i = 0
       count = 0
       if i < getLength(L)//2:
          Append(L1,temp.item)
       elif i > getLength(L)//2 and i < getLength(L):
          Append(L2,temp.item)
       temp = temp.next
       i = i + 1
       count = count + 1
          
       print(count)
       MergeSort(L1)
       MergeSort(L2)
       L = Merge(L1,L2)
        
def Copy(L):
    copy = List()
    temp = L.head
    while temp is not None:
        Append(copy,temp.item)
        temp = temp.next
    return copy
    
def ElementAt(C,median):
    if IsEmpty(C):
        return None
    else:
        temp = C.head
        i = 0
        while temp is not None and i < median:
            temp = temp.next
            i = i + 1
        return temp.item
            
def Median(L):
    C = Copy(L)
    BubbleSort(C)
    Print(C)
    med = ElementAt(C,getLength(C)//2)
    return med
    print()

def Median2(L):
    C = Copy(L)
    MergeSort(C)
    Print(C)
    med = ElementAt(C,getLength(C)//2)
    return med
    print()

def Median3(L):
    C = Copy(L)
    QuickSort(C)
    Print(C)
    med = ElementAt(C,getLength(C)//2)
    return med
    print()

def Median4(L):
    C = Copy(L)
    QuickSortOptimized(C)
    Print(C)
    med = ElementAt(C,getLength(C)//2)
    return med
    print()

L = List()
n = random.randint(0,50)
for i in range(n):
    rand = random.randint(0,n*2)
    Append(L,rand)

Print(L)
print('The middle element is',Median(L))
print('--------------------------------------------------------------')
print('The middle element is',Median2(L))
print('--------------------------------------------------------------')
print('The middle element is',Median3(L))
print('--------------------------------------------------------------')
print('The middle element is',Median4(L))
