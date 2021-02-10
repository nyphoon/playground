# Given a binary tree, return the inorder traversal of its nodes’ values.

# For example:
# Given binary tree [1,null,2,3],

#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def traversal(node):
            nonlocal result
            if node.left is not None:
                traversal(node.left)
            result.append(node.val)
            if node.right is not None:
                traversal(node.right)
                
        if root is not None:
            traversal(root)
        return result


s = Solution()

# Input: root = [1,null,2,3]
# Output: [1,3,2]
root = \
TreeNode(1,
    None,
    TreeNode(2,
        TreeNode(3, None, None),
        None
    )
)
print(s.inorderTraversal(root))

# 3 1 2
# 1 3 2
root = \
TreeNode(3,
    TreeNode(1, None, None),
    TreeNode(2, None, None)
)
print(s.inorderTraversal(root))


print(s.inorderTraversal(None))


print(s.inorderTraversal(TreeNode(1, None, None)))


# Runtime: 32 ms, faster than 58.74% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 14.3 MB, less than 47.35% of Python3 online submissions for Binary Tree Inorder Traversal.