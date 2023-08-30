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

""" Linked List Cycle"""

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         slwpntr = head
#         fastpntr = head

#         while fastpntr and fastpntr.next:
#             slwpntr = slwpntr.next
#             fastpntr = fastpntr.next.next

#             if slwpntr == fastpntr:
#                 return True
#         return False


#add two numbers in linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
            
            