# -*- encoding: utf-8 -*-
'''
Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lena = 0
        p = headA
        while p:
            p = p.next
            lena += 1

        lenb = 0
        p = headB
        while p:
            p = p.next
            lenb += 1

        pa = headA; pb = headB
        if lena > lenb:
            for i in range(lena-lenb):
                pa = pa.next
        if lenb > lena:
            for i in range(lenb-lena):
                pb = pb.next
        while pa and pb:
            if pb == pa: return pa
            pa = pa.next
            pb = pb.next
        return None


if __name__ == '__main__':
    s = Solution()
    print 'PASS'
