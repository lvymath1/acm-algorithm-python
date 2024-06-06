# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        p = head
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            x = v1 + v2 + carry
            p.next = ListNode(x % 10)
            p = p.next
            carry = x // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next