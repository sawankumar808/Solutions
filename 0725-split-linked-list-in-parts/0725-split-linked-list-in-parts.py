# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        ans=[]

        temp=head
        n=0
        while temp is not None:

            n+=1
            temp=temp.next

        baseSize=n//k
        extraNodes=n%k

        
        curr=head
        

        for part in range(k):
            #insert curr into arr
            if curr is None:
                ans.append(None)
                continue
            ans.append(curr)
           

            width=baseSize+( 1 if extraNodes>0 else 0)

            extraNodes-=1

            prev=None
            for i in range(width):
                prev=curr
                curr=curr.next

            if prev is not None:
                prev.next=None

        return ans


              