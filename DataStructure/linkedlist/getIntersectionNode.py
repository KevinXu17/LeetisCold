# https://leetcode.com/problems/intersection-of-two-linked-lists/

"""
    Two linked list
    when two list Node has same node, they share the tail
    2 3 4 5           (len 4 + 3)
             8 3 2
        2 4           (len 2 + 3)
    A_diff + Same = B_diff + Same

    if they do not share the same node:
    A + B = B + A => both None end
    So loop A then B with B then A should get same object if has intersection;
    otherwise, both are None


    if only ask whether it has intersection:
    we can compute: connect the A's tail to B's head, then check circle => 2 pointers
                    or check both tails are the same object
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    ha = headA
    hb = headB
    while ha != hb:
        ha = headB if ha is None else ha.next
        hb = headA if hb is None else hb.next
    return ha