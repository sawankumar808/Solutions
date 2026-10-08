# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        read=head.next
        write=head

        while read is not None:
            count=0
            while read.val!=0:
                count+=read.val
                read=read.next

            write.val=count# insert sum value
            write.next=read.next#delete faltu node

            read=read.next #read nad write ko move kro ek ek step
            write=write.next
        return head














        '''
        brute force approach
        anshead=None
        anstail=None

        count=0 
        curr=head.next # phela zero skip ke liye

        while curr is not None:

           
            if curr.val==0:
                newnode=ListNode(count)
                if anshead is None:

                    anshead=newnode
                    anstail=newnode
            
                
                else:
                #agar phele se node hai to tail ke aage jodo
                    anstail.next=newnode
                    anstail=newnode
                count=0
            else:
                count+=curr.val
            curr=curr.next

        return anshead
        '''
        


                             



        