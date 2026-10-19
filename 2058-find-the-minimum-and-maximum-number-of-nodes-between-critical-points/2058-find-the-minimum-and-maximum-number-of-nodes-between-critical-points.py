# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:

        prev=head
        curr=head.next
        i=1
        ans=[] 

        while curr.next is not None:

            if curr.val> prev.val and curr.val>curr.next.val:
                ans.append(i)

            if curr.val< prev.val and curr.val<curr.next.val:
                ans.append(i)

            prev=prev.next
            curr=curr.next
            i+=1

        if len(ans)<2:
            return [-1,-1]
        
        minvalue=100000
        

        for j in range(1,len(ans)):
            minvalue=min(minvalue, ans[j]-ans[j-1])

            
        maxvalue = ans[-1]-ans[0]

        return [minvalue, maxvalue]




        