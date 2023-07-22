

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
        
LL= LinkedList()

LL.insert_head(1)
LL.insert_head(2)
LL.insert_head(3)
LL.insert_head(4)

print(LL.traverse())  

print(len(LL))
        
        
        
        
        
        
# a=Node(1)
# b=Node(2)
# c=Node(3)

# # connected manually
# a.next=b
# b.next=c

# print(c.next)
# print(int(0x00000185D2354F40))