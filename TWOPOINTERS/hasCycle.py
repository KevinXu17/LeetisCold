# https://leetcode.com/problems/linked-list-cycle/description/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def hasCycle(head: Optional[ListNode]) -> bool:
    # if head == None or head.next == None:
    #     return False
    # head_next = head.next
    # head_next_next = head_next.next
    # while head_next_next != None:
    #     if head == head_next_next:
    #         return True
    #     head = head.next
    #     head_next = head_next_next.next
    #     if head_next == None:
    #         break
    #     head_next_next = head_next.next
    # return False

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False