"""
@author: Sebastian Gomez
Course: Data Structure 2302
Assignment: Lab 4
Instructor: Olac Fuentes
T.A: Anindita Nath and Maliheh Zargaran
Purpose: Create operations for a B-Tree
"""

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    else:
        return 1 + height(T.child[-1])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
def BTToList(T):
    sort = []
    if T.isLeaf:
        sort = [T.item]
    else:
        sort = BTToList(T.child[0]) + [T.item] + BTToList(T.child[-1])
    return sort

def MinElementAtDepth(T,d,h):
    if d > h:
        return -1
    if d == 0:
        return T.item[0]
    else:
        return MinElementAtDepth(T.child[0],d - 1,h)
        
def MaxElementAtDepth(T,d,h):
    if d > h:
        return -1
    if d == 0:
        return T.item[-1]
    else:
        return MaxElementAtDepth(T.child[-1],d - 1,h)
    

def NumOfNodesAtDepth(T,d,h):
    if d > h:
        return -1
    if d == 0:
        return len(T.item)
    else:
        num = NumOfNodesAtDepth(T.child[0],d-1,h) + NumOfNodesAtDepth(T.child[-1],d-1,h)
        
    return num
       
           
def PrintAtDepth(T,d,h):
    if d > h:
        return -1
    if d == 0:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.child)):
            PrintAtDepth(T.child[i],d-1,h)
     
    
def NumOfNodesFull(T):
    if T.isLeaf:
        return 0
    else:
        if IsFull(T):
            return 1 + NumOfNodesFull(T.child[0]) + NumOfNodesFull(T.child[-1])
        else:
            return 0
    

def NumOfLeavesFull(T):
    if T.isLeaf:
        if IsFull(T):
            return 1 + NumOfLeavesFull(T.child[0]) + NumOfLeavesFull(T.child[-1])
        else:
            return 0
    else:
        return 0
    
def FindAtDepth(T,k):
    if T.isLeaf:
        if k in T.item:
            return 0
        else:
            return -1
    if k in T.item:
        return 0
    if k > T.item[len(T.item)-1]:
        d = FindAtDepth(T.child[-1],k)
    else:
        d = FindAtDepth(T.child[0],k)
    if d == -1:
        return -1
    else:
        return d + 1 
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120,123,122,121,201,202,205,206,53, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6,51,52,116]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    Print(T)
    print('\n####################################')
          
    

h = height(T)
print(h)
sortedList = BTToList(T)
i = 0
while i < len(sortedList):
    print(sortedList[i], end = ' ')
    i +=1
print()
print('Minimum Element at Depth: ',MinElementAtDepth(T,1,h))
print('Max Element at Depth: ',MaxElementAtDepth(T,1,h))
print('Number Of Leaves Full: ',NumOfLeavesFull(T))
print('Number of Nodes Full: ',NumOfNodesFull(T))
print('Number of Nodes at Depth: ',NumOfNodesAtDepth(T,1,h))
PrintAtDepth(T,1,h)
print()
print(FindAtDepth(T,202))


