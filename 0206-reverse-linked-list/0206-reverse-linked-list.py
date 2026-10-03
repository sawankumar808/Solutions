# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        # recursion approach 
        prev=None
        curr=head
        ans=self.solve(prev,curr)
        return ans

    def solve (self,prev, curr):
        if curr==None:
            return prev

        forward=curr.next
        curr.next=prev
        prev=curr
        curr=forward
        return self.solve(prev,curr)





        #iterrative approach
        '''
        prev=None
        curr=head
        while(curr is not None):
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward
        return prev
    '''
   
    

