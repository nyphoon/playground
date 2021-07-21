# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2
 
# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000

from typing import List

class Solution:
    # Runtime: 4132 ms, faster than 16.70% of Python3 online submissions for Jump Game II.
    # Memory Usage: 15.2 MB, less than 58.52% of Python3 online submissions for Jump Game II.
    def jump(self, nums: List[int]) -> int:
        ans  =[None] * len(nums)
        ans[0] = 0
        for cur in range(len(nums)):
            for s in range(1, nums[cur]+1):
                front = cur+s
                if front >= len(nums):
                    continue
                # print(ans, '-',front)
                if ans[front] is None:
                    ans[front] = ans[cur] + 1

        return ans[-1]



s = Solution()
print(s.jump([2,3,0,1,4]))
print(s.jump([2,3,1,1,4]))
