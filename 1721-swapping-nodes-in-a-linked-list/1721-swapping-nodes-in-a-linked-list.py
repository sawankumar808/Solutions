# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #ye hai sliding window ek hi traverse mai ho jayga

        first=head
        for i in range(1,k):
            first=first.next

        temp=first.next
        second=head

        while temp is not None:
            temp=temp.next
            second=second.next
        first.val, second.val= second.val, first.val
        

        
        '''
        isme hume 2 barr traverse kr rhe hai lekin tm or sc dono code mai same hai
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
        '''
        
        return head
        
        