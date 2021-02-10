# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        shorest = None

        def traverse(node, lv):
            nonlocal shorest
            lv += 1

            if node.left is None and node.right is None:
                if shorest is None:
                    shorest = lv
                else:
                    shorest = min(shorest, lv)
                return

            if node.left is not None:
                traverse(node.left, lv)

            if node.right is not None:
                traverse(node.right, lv)

        traverse(root, 0)

        return shorest

s = Solution()


# 3,9,20,null,null,15,7
# Output: 2
root = \
TreeNode(3,
    TreeNode(9, None, None),
    TreeNode(20,
        TreeNode(15, None, None),
        TreeNode(7, None, None)
    )
)
print(s.minDepth(root))


# 3,9,20,15,7
# Output: 2
root = \
TreeNode(3,
    TreeNode(9,
        TreeNode(15, None, None),
        TreeNode(7, None, None)
    ),
    TreeNode(20, None, None)
)
print(s.minDepth(root))

# Input: root = [2,null,3,null,4,null,5,null,6]  right skew
# Output: 5
root = \
TreeNode(2,
    None,
    TreeNode(3,
        None,
        TreeNode(4,
            None,
            TreeNode(5,
                None,
                TreeNode(6, None, None)
            )
        )
    )
)
print(s.minDepth(root))

# Input: root = [2,3, null,4,null,5,null,6] left skew
# Output: 5
root = \
TreeNode(2,
    TreeNode(3,
        TreeNode(4,
            TreeNode(5,
                TreeNode(6, None, None),
                None
            ),
            None
        ),
        None
    ),
    None
)
print(s.minDepth(root))


print(s.minDepth(None))


# Runtime: 960 ms, faster than 5.09% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 55.6 MB, less than 9.99% of Python3 online submissions for Minimum Depth of Binary Tree.