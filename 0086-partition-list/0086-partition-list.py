# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        


        lesserhead=ListNode(-1)
        lessertail=lesserhead

        greaterhead=ListNode(-1)
        greatertail=greaterhead
        curr=head 
        while curr is not None:#alga list bani hai hai choti wali
            if curr.val<x:
                nodetoinsert=curr
                curr=curr.next
                nodetoinsert.next=None
                lessertail.next=nodetoinsert
                lessertail=nodetoinsert
            else:#alga list bani hai hai badi wali
                nodetoinsert=curr
                curr=curr.next
                nodetoinsert.next=None
                greatertail.next=nodetoinsert
                greatertail=nodetoinsert
            #dono sublist rady join karo

        lessertail.next=greaterhead.next
        greaterhead.next=None 

        lesserhead=lesserhead.next       


        return lesserhead


