# Problem:
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        h = len(nums) // 2
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            if d[n] > h:
                return n
        
        return None
        

nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
nums = [1]
s = Solution()
print(s.majorityElement(nums))\

# Runtime: 176 ms
# Memory Usage: 15.6 MB