# Problem
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input:  [1,2,3,4,5,6,7] and k = 3 
# Output: [5,6,7,1,2,3,4]
# Explanation: rotate 1 steps to the right: [7,1,2,3,4,5,6] rotate 2 steps to the right: [6,7,1,2,3,4,5] 
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input:[-1,-100,3,99] and k = 2 
# Output: [3,99,-1,-100] 
# Explanation: rotate 1 steps to the right: [99,-1,-100,3] rotate 2 steps to the right: [3,99,-1,-100]

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
from typing import List

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [q : k] n
        n = len(nums)
        if n == 0:
            return

        k %= n
        q = n-k
        cp = nums[:q]
        for i in range(k):
            nums[i] = nums[q+i]
        for i in range(q):
            nums[k+i] = cp[i]


s = Solution()

l = [1,2,3,4,5,6,7]
s.rotate(l, 3)
print(l)

l = [-1,-100,3,99]
s.rotate(l, 2)
print(l)

l = []
s.rotate(l, 1)
print(l)

l = [1,2,3,4,5,6,7]
s.rotate(l, 0)
print(l)

l = [1,2,3,4,5,6,7]
s.rotate(l, 7)
print(l)

l = [1,2,3,4,5,6,7]
s.rotate(l, 6)
print(l)

l = [1,2,3,4,5,6,7]
s.rotate(l, 4)
print(l)

l = [-1]
s.rotate(l, 2)
print(l)

l = [1, 2]
s.rotate(l, 3)
print(l)  # expect  [2,1]


# Runtime: 60 ms, faster than 78.87% of Python3 online submissions for Rotate Array.
# Memory Usage: 15.4 MB, less than 96.49% of Python3 online submissions for Rotate Array.
