"""
write a program to find the maximum value in linked list and replace it with a given value.
Assume that the linked list is populated with whole number and there is only one maximum value in the
linked list
"""

    # def replace_max(self,value):
    #     temp = self.head
    #     max = temp
        
    #     while temp!=None:
    #         if temp.data>max.data:
    #             max=temp
    #         temp=temp.next
    #     max.data=value
#  LL.replace_max(21)


"""
Write a program to add item in the linked List present at the odd index
"""

    # def sum_of_odd(self):
    #     curr = self.head
    #     pos=0
    #     result = 0
        
    #     while curr != None:
    #         if pos%2 !=0:
    #             result = result+curr.data
    #         pos+=1
    #         curr=curr.next
    #     print(result)
    
    
"""
Write a program to reverse a linked list without creating new linked list(inplace reversal )
"""              
#     def reverse(self):
#         prev_node = None
#         curr = self.head
        
#         while curr!=None:
#             next_node = curr.next
#             curr.next=prev_node
#             prev_node=curr
#             curr=next_node
#         self.head=prev_node
# LL.reverse()
# print(LL.traverse())

#    def change_sent(self):
#         curr = self.head
        
#         while curr != None:
#             if curr.data=='*' or curr.data=='/':
#                 curr.data=" "
#                 if curr.next.data =='*' or curr.next.data=='/':
#                     curr.next.next.data = curr.next.next.data.upper()   
#                     curr.next = curr.next.next
#             curr = curr.next     
