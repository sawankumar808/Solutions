# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        n=0
        curr=head
        prev=None

        while curr is not None:
            n+=1
            curr=curr.next
        if n<k:
            return head
            
        curr=head
        prev=None
        for i in range(k):
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward
            

        ans=self.reverseKGroup(curr,k)
        head.next=ans

        return prev
        


                

        