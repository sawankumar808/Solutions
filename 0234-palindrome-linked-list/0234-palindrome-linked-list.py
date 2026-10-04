# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        #slow or fast se midle niklo
        # last wala part reverse karo
        #comapre karo
        if head==None or head.next==None:
            return True
        slow=head
        fast=head #slow fast middle nikla
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #ab list todo

        head2=slow.next
        slow.next=None

        #second half reverse
        prev2=None
        curr=head2

        while curr is not None :

            forward=curr.next

            curr.next=prev2
            prev2=curr
            curr=forward

        
        

        #prev2 is second half  ka head 

        p1=head
        p2=prev2

        while p2 is not None:
            if p1.val!=p2.val:
                return False

            p1=p1.next
            p2=p2.next
        return True










    
        