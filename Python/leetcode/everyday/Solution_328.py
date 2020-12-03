# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        last = head.next
        tmp = last
        while not cur.next and not tmp.next:
            cur.next = cur.next.next
            tmp.next = tmp.next.next
            cur = cur.next
            tmp = tmp.next
        cur.next = last
        return head




