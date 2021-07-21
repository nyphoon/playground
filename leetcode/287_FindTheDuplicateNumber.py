# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [1,1]
# Output: 1

# Example 4:
# Input: nums = [1,1,2]
# Output: 1

# Constraints:
# 2 <= n <= 3 * 104
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
# Follow up:
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem without modifying the array nums?
# Can you solve the problem using only constant, O(1) extra space?
# Can you solve the problem with runtime complexity less than O(n2)?
from typing import List
from collections import Counter

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        # Runtime: 612 ms, faster than 65.59% of Python3 online submissions for Find the Duplicate Number.
        # Memory Usage: 36.2 MB, less than 5.66% of Python3 online submissions for Find the Duplicate Number.
        return Counter(nums).most_common(1)[0][0]

    def findDuplicate_misunderstand(self, nums: List[int]) -> int:
        n = len(nums)-1
        n_sum = (1 + n) * n // 2
        return sum(nums) - n_sum
        
s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
print(s.findDuplicate([1,1]))
print(s.findDuplicate([1,1,2]))
print(s.findDuplicate([2,2,2]))
