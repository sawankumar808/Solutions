class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        p = head
        while p is not None:
            if p.child is None:
                # Agar child nahi hai, toh seedha aage badho
                p = p.next
            else:
                # Step 1: Child sub-list ka aakhri node (tail) dhoondo
                temp = p.child
                while temp.next is not None:
                    temp = temp.next
                
                # Step 2: Child ke tail ko p.next se jodo (agar p.next None nahi hai)
                if p.next is not None:
                    temp.next = p.next
                    p.next.prev = temp
                
                # Step 3: Child ko p ke theek aage lagao
                p.next = p.child
                p.child.prev = p
                
                # Step 4: Child pointer ko None karna zaroori hai (Flattened list ka rule)
                p.child = None
                
                # p ko aage badha do
                p = p.next

        return head