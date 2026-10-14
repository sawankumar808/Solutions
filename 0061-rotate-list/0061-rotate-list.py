# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or k ==0:
            return head
        temp=head
        n=1
        

        while temp.next is not None:
            n+=1
            temp=temp.next

        temp.next=head
        k=k%n
        temp=head
        for i in range(1,n-k-1+1):
            temp=temp.next
            
        forward=temp.next
        temp.next=None
        return forward
