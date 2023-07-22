

# node created
class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next=None
        
a=Node(1)
b=Node(2)
c=Node(3)

# connected manually
a.next=b
b.next=c

print(c.next)
print(int(0x00000185D2354F40))