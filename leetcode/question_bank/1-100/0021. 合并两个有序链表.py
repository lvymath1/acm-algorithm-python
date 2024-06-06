# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        pre = dummy
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val <= p2.val:
                pre.next = p1
                pre = p1
                p1 = p1.next
            else:
                pre.next = p2
                pre = p2
                p2 = p2.next
        pre.next = p1 if p1 else p2
        return dummy.next