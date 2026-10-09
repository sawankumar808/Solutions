# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

  def getIntersectionNode(
      self, headA: ListNode, headB: ListNode
  ) -> Optional[ListNode]:
    if not headA or not headB:
      return None

    a = headA
    b = headB

    # Dono pointers ko ek sath aage badhao jab tak koi ek khatam na ho
    while a is not None and b is not None:
      a = a.next
      b = b.next

    # Agar 'a' pehle None ho gaya, matlab List B lambi hai
    if a is None:
      bExtralen = 0
      while b is not None:
        bExtralen += 1
        b = b.next

      while bExtralen > 0:
        headB = headB.next
        bExtralen -= 1

    # Agar 'b' pehle None ho gaya, matlab List A lambi hai
    else:
      aExtralen = 0
      while a is not None:
        aExtralen += 1
        a = a.next

      while aExtralen > 0:
        headA = headA.next
        aExtralen -= 1

    # Ab dono pointers ko barabar lamba karke intersection check karo
    while headA is not None and headB is not None:
      if headA == headB:
        return headA
      headA = headA.next
      headB = headB.next

    return None