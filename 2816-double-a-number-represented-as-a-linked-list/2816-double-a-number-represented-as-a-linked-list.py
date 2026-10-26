# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=self.reverse(head)        
        count=0
        carry=0
        node=ListNode(-1)
        nodetail=node
        newhead=prev
        while newhead is not None:
            count=newhead.val+newhead.val+carry

            digit=count%10
            nodetail.next=ListNode(digit)
            nodetail=nodetail.next
            carry=count//10
            newhead=newhead.next
            
        if newhead == None and carry !=0:

            nodetail.next=ListNode(carry)

        node=node.next
        head=self.reverse(node)
        return head

    def reverse(self,head):
        prev=None
        curr=head
        while curr is not None:
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward
        return prev

        

        



              

        
        

        

            
        