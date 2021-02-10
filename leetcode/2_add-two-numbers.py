def print_list(l):
    if l is None:
        return
    cur = l
    while cur.next is not None:
        print(cur.val)
        cur = cur.next
    print(cur.val)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = None
        ca = None
        over_ten = False
        c1 = l1
        c2 = l2
        
        while c1 is not None or c2 is not None:
            a = 0
            a += 0 if c1 is None else c1.val
            a += 0 if c2 is None else c2.val
            if over_ten:
                a += 1
            over_ten = a >= 10
            a %= 10
            if ans is None:
                ans = ListNode(a, None)
                ca = ans
            else:
                new_node = ListNode(a, None)
                ca.next = new_node
                ca = new_node
            c1 = c1.next if c1 is not None else None
            c2 = c2.next if c2 is not None else None
        
        if over_ten:
            ca.next = ListNode(1, None)

        return ans

s = Solution()

l1 = ListNode(2,
        ListNode(4,
            ListNode(3, None)
        )
     )
l2 = ListNode(5,
        ListNode(6,
            ListNode(4, None)
        )
     )
la = s.addTwoNumbers(l1, l2)
print_list(la)
print('--------')

l1 = ListNode(5,None)
l2 = ListNode(5,None)
la = s.addTwoNumbers(l1, l2)
print_list(la)
print('--------')

l1 = ListNode(1,
        ListNode(8, None)
     )
l2 = ListNode(0)
la = s.addTwoNumbers(l1, l2)
print_list(la)
print('--------')