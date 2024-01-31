# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    res = None
    my_head = head
    while my_head is not None:
        temp = my_head
        my_head = my_head.next
        temp.next = res
        res = temp
    return res