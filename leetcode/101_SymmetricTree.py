# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def Traverser(node):
            way = [node]
            while len(way) != 0:
                n = way.pop()
                if n is None:
                    yield None
                else:
                    yield n.val
                    way.append(n.left)
                    way.append(n.right)

        def MirrorTraverser(node):
            way = [node]
            while len(way) != 0:
                n = way.pop()
                if n is None:
                    yield None
                else:
                    yield n.val
                    way.append(n.right)
                    way.append(n.left)

        if root is None:
            return True

        traverser = Traverser(root.left)
        mirror_traverser = MirrorTraverser(root.right)

        for l in traverser:
            try:
                r = next(mirror_traverser)
            except StopIteration:
                return False
            if l != r:
                return False
            # print('->', l, r)
        return True

s = Solution()

root = TreeNode(1,
    TreeNode(2,
        TreeNode(4, None, None),
        TreeNode(3, None, None)
    ),
    TreeNode(2,
        TreeNode(3, None, None),
        TreeNode(4, None, None)
    )
)
print(s.isSymmetric(root))

print('------------')

root = TreeNode(1,
    TreeNode(2,
        None,
        TreeNode(3, None, None)
    ),
    TreeNode(2,
        None,
        TreeNode(3, None, None)
    )
)
print(s.isSymmetric(root))



# Runtime: 36 ms, faster than 58.00% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 14.4 MB, less than 44.95% of Python3 online submissions for Symmetric Tree.