

# node created
class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next=None
        
class LinkedList:
    def __init__(self) -> None:
        # empty linked list
        self.head = None
        self.n=0 #n tells the number of nodes in the linked list
    
    # counting the number of nodes in linked list   
    def __len__(self):
        return self.n
    
    
    # Insertion operation in Linked List
    
    # 1. Inserting from head
    
    def insert_head(self,value):
        #new node
        new_node=Node(value)
        
        #create connection
        new_node.next=self.head
        #reassingning head
        self.head=new_node
        self.n=self.n+1
        
    def traverse(self):
        curr= self.head
        
        while curr!=None:
            print(curr.data)
            curr=curr.next
            
    # 2.Inserting at the end
    
    def insert_at_end(self,value):
        
        new_node = Node(value)
        #resolving empty list problem/error
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return
            
        curr = self.head
        
        while curr.next!=None:
            curr=curr.next
        
        #now loop will end then curr is at last node
        curr.next=new_node #assigned last node as new node
        self.n= self.n+1
        
        
    def insert_after(self,after,value):
        new_node = Node(value)
        curr = self.head
        
        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next
            
            # Here we have two cases
            # 1. if condition breaks it means item found in the linked list -> curr -> not none
        if curr != None:
            new_node.next=curr.next
            curr.next=new_node
            self.n=self.n+1
        else:
            print( 'item not found') # 2. if condition does not breaks means loop pura chala-> item does not found in the linked List ->curr->none
            
    # clear the Linked List
    
    def clear(self):
        self.head=None
        self.n=0

    # Deleting the head
    
    def delete_head(self):
        if self.head==None:
            return 'empty linked list'
        self.head=self.head.next
        self.n = self.n-1
            
           #Pop operation on liked list Deleting at last 
    def pop(self):
        if self.head==None:
            return 'empty linked list'
        
        curr=self.head
        if curr.next == self.head:
            return self.delete_head()
            pass
        while curr.next.next != None:
            curr = curr.next
        
        curr.next=None
        self.n = self.n-1
        self.n = self.n-1
        
        
        # remove by item in Linked List
    def remove(self,value):
        if self.head==None:
            return 'empty linked list'
        curr = self.head
        
        if self.head.data==value:
            return self.delete_head()
        while curr.next != None:
            if curr.next.data == value:
                break
            curr= curr.next
            
        # 2 cases 
        # b. if item does not found
        if curr.next==None:
            return 'not found'

        # a. if item found
        else:
            curr.next=curr.next.next
        
        # searching item in Linked List and getting its index
        
    def search(self,item):
        curr = self.head
        pos=0
        while curr!=None:
            if curr.data==item:
                return pos
            curr=curr.next
            pos=pos+1
        return 'not found'
        
        
        # search by index
        
    def __getitem__(self,index):
        curr=self.head
        pos=0
        while curr!=None:
            if pos==index:
                return curr.data
            curr=curr.next
            pos=pos+1
            
            

LL= LinkedList()
LL.insert_head(1)
LL.insert_head(2)
LL.insert_head(3)
LL.insert_head(4)
LL.insert_at_end(5)
LL.insert_after(5,40)
print(LL[4])
# LL.pop() 
# print(LL.delete_head())
# print(LL.traverse())  
# LL.pop()

# print(LL.clear())
        
        
        
        
        
        
# a=Node(1)
# b=Node(2)
# c=Node(3)

# # connected manually
# a.next=b
# b.next=c

# print(c.next)
# print(int(0x00000185D2354F40))