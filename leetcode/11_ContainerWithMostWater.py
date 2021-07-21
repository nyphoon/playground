# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Example 2:
# Input: height = [1,1]
# Output: 1

# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16

# Example 4:
# Input: height = [1,2,1]
# Output: 2
 
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
from typing import List

class Solution:
    # After Google the solution
    # Runtime: 664 ms, faster than 92.53% of Python3 online submissions for Container With Most Water.
    # Memory Usage: 27.5 MB, less than 50.22% of Python3 online submissions for Container With Most Water.
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        big = 0
        l = 0
        r = n-1
        while l < r:
            if height[l] > height[r]:
                water = (r - l) * height[r]
                r -= 1
            else:
                water = (r - l) * height[l]
                l += 1
            if water > big:
                big = water
        return big


    # Time Limit Exceeded
    def maxArea_stupid(self, height: List[int]) -> int:
        n = len(height)
        good_right = []
        good_left = []
        for i in range(n):
            for j in range(i+1, n):
                if height[j] >= height[i]:
                    break
            else:
                good_right.append(i)

        for i in reversed(range(n)):
            for j in range(i-1, -1, -1):
                if height[j] >= height[i]:
                    break
            else:
                good_left.append(i)

        bigs = [0]
        for l in good_left:
            for r in good_right:
                w = r-l
                h = height[l] if height[l] < height[r] else height[r]
                bigs.append(w * h)

        return max(bigs)


        
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
print(s.maxArea([4,3,2,1,4]))
print(s.maxArea([1,2,1]))
print(s.maxArea([1,1,1,1,9,9,1]))
print(s.maxArea([]))