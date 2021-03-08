# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical 
# and the nodes have the same value.

# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:
# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        same = True
        def traversal(p, q):
            nonlocal same
            if same is False:
                return

            if p is None and q is None:
                return
            
            if (p is None or q is None) or p.val != q.val:
                same = False
                return
            
            traversal(p.left, q.left)
            traversal(p.right, q.right)
        traversal(p, q)

        return same

# Runtime: 16 ms, faster than 99.86% of Python3 online submissions for Same Tree.
# Memory Usage: 14.4 MB, less than 35.42% of Python3 online submissions for Same Tree.

    def isSameTree_Wrong(self, p: TreeNode, q: TreeNode) -> bool:
        def traverser(node):
            way = [node]
            while len(way) != 0:
                cur = way.pop()
                if cur is not None:
                    yield cur.val
                    way.append(cur.right)
                    way.append(cur.left)

        tq = traverser(q)
        for v in traverser(p):
            try:
                if v != next(tq):
                    return False
            except StopIteration:
                return False
        return True
        


        
s = Solution()

p = TreeNode(1,
    TreeNode(2, None,None),
    None
)
q = TreeNode(1,
    None,
    TreeNode(2, None,None)
)
assert s.isSameTree(p, q) is False
print('-----')

p = TreeNode(1,
    TreeNode(2, None,None),
    TreeNode(1, None,None)
)
q = TreeNode(1,
    TreeNode(1, None,None),
    TreeNode(2, None,None)
)
assert s.isSameTree(p, q) is False
print('-----')

p = TreeNode(1,
    TreeNode(2, None,None),
    TreeNode(1, None,None)
)
q = TreeNode(1,
    TreeNode(2, None,None),
    TreeNode(1, None,None)
)
assert s.isSameTree(p, q) is True
