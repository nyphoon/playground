# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        idx = []

        while cur is not None:
            idx.append(cur)
            cur = cur.next
        
        for i in range(n-1, m-1, -1):
            idx[i].next = idx[i-1]

        if n == len(idx):
            idx[m-1].next = None
        else:
            idx[m-1].next = idx[n]
        
        if m >= 2:
            idx[m-2].next = idx[n-1]
            ans = head
        else:
            ans = idx[n-1]

        # for i in idx:
        #     print(i.val, '->', 'null' if i.next is None else i.next.val)
        
        return ans

def print_list(head: ListNode):
    cur = head
    print(cur.val)
    while cur.next is not None:
        cur = cur.next
        print(cur.val)
    print('---------------------')

test_data =  ListNode(1,         #1
        ListNode(2,         #2
        ListNode(3,         #3
        ListNode(4,         #4
        ListNode(5, None)   #5
        )
        )
        )
        )
import copy

head = copy.deepcopy(test_data)
print('2 4')
s = Solution()
ans = s.reverseBetween(head, 2, 4)
print_list(ans)


head = copy.deepcopy(test_data)
print('1 4')
s = Solution()
ans = s.reverseBetween(head, 1, 4)
print_list(ans)


head = copy.deepcopy(test_data)
print('2 5')
s = Solution()
ans = s.reverseBetween(head, 2, 5)
print_list(ans)


head = copy.deepcopy(test_data)
print('3 3')
s = Solution()
ans = s.reverseBetween(head, 3, 3)
print_list(ans)


head = copy.deepcopy(test_data)
print('1 1')
s = Solution()
ans = s.reverseBetween(head, 1, 1)
print_list(ans)


head = copy.deepcopy(test_data)
print('5 5')
s = Solution()
ans = s.reverseBetween(head, 5, 5)
print_list(ans)


# Runtime: 52 ms, faster than 5.10% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14.3 MB, less than 89.38% of Python3 online submissions for Reverse Linked List II.