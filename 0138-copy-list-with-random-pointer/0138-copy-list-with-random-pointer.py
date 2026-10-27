"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        temp=head
        while temp is not None:
            cloneNode=Node(temp.val)
            cloneNode.next=temp.next
            temp.next=cloneNode
            temp=cloneNode.next

        temp=head
        while temp is not None:
            oldnode=temp
            newnode=temp.next

            if oldnode.random is not None:
                newnode.random=oldnode.random.next

            temp=newnode.next
        #detach karna hai
        temp=head
        anslist=head.next

        while temp is not None:
            oldnode=temp
            clonenode=temp.next

            oldnode.next=clonenode.next
            if clonenode.next is not None:
                clonenode.next=clonenode.next.next

            #temp ko move karna hai

            temp=temp.next
        return anslist
