# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head == None or  head.next==None:
            return head
        
        currnode=head
        forward=head.next
        
        while forward is not None:
            if currnode.val!=forward.val:
                currnode=currnode.next
                forward=forward.next
            else:
                currnode.next=forward.next
                forward=forward.next

        return head

        