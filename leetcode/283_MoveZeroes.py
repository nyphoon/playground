# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
from typing import List
class Solution:
    def moveZeroes_old(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur] = nums[i]
                cur += 1
        for i in range(cur, len(nums)):
            nums[i] = 0

        print(nums)
# Runtime: 52 ms, faster than 55.21% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.5 MB, less than 20.11% of Python3 online submissions for Move Zeroes.

    def moveZeroes_bad(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur = i
            else:
                tmp = nums[cur]
                nums[cur] = nums[i]
                nums[i] = tmp
                cur += 1

        print(nums)
                
s = Solution()

l = [0,1,0,3,12]
s.moveZeroes(l)

l = [0,0]
s.moveZeroes(l)

l = [1,3,12]
s.moveZeroes(l)

l = []
s.moveZeroes(l)