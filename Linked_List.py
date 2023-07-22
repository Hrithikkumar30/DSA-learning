class Node:
    def __init__(self,value,next=None):
        self.data = value
        self.next = next
        
class Linked_list:
    def __init__ (self):
        self.head = None
        
    def insert_at_begining(self,data):
        node = Node(data , self.head) 
        self.head=node

        
    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        llstr=''
        while itr:
            llstr += str(itr.data) +'--->'
            itr=itr.next
        
        print(llstr)
        
        
    def insert_at_end(self,data):
        if self.data is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data , None)
        
if __name__ == '__main__':
    ll = Linked_list()
    ll.insert_at_begining(5)
    ll.insert_at_begining(23)
    ll.insert_at_end(45)
    ll.print()