# Problem:

# A robot is located at the top-left corner of a m x n grid (marked ‘Start’ in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach 
# the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).
# How many possible unique paths are there?

# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# Example 3:
# Input: m = 7, n = 3
# Output: 28

# Example 4:
# Input: m = 3, n = 3
# Output: 6
 
# Constraints:
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 109.


def combination(m, n):
    a = b = 1
    for i in range(m, m-n, -1):
        a *= i
    for i in range(1, n+1):
        b *= i
    # print(m, n, a, b, a/b)
    return a//b


def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    # print(n, '->', a)
    return a


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            a = m
            b = n - 1
        else:
            a = n
            b = m - 1

        # H(m,n)
        return combination(a+b-1,b)

# Runtime: 28 ms, faster than 87.99% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.4 MB, less than 40.91% of Python3 online submissions for Unique Paths.

s = Solution()

assert 28   == s.uniquePaths(3,7)
assert 3    == s.uniquePaths(3,2)
assert 28   == s.uniquePaths(7,3)
assert 6    == s.uniquePaths(3,3)
assert 1    == s.uniquePaths(1,1)