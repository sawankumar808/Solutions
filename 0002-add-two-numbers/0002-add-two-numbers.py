# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        anshead=ListNode(-1)
        anstail=anshead
        curr=l1
        curr2=l2

        carry=0
        
        while curr is not None or curr2 is not None or carry!=0:
            count=0
            if curr is not None:
                count+=curr.val
                curr=curr.next
            if curr2 is not None:
                count+=curr2.val
                curr2=curr2.next

            count+= carry
            digit=count%10
            
            carry=count//10
            newnode=ListNode(digit)
            anstail.next=newnode
            anstail=newnode
        anshead=anshead.next
        return anshead





