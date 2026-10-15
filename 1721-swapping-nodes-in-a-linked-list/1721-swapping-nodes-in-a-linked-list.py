# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=1
        temp=head
        curr=head
        while temp is not None:
            n+=1
            temp=temp.next
        temp=head
        for i in range(1, k):
            temp=temp.next
        
        curr=head
        for i in range(1,n-k):
            curr=curr.next
        
        value=curr.val
        curr.val=temp.val
        temp.val=value
        
        return head
        
        