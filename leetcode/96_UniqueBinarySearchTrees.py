# Given n, how many structurally unique BST’s (binary search trees) that store values 1 … n?

# Example:

# Input: 3
# Output: 5

# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3



# I Google this question and found this is a famous Catalan number
# So I wrote this Caltalan function
# cache = {0:1}
# def catalan(n):
#     if n in cache:
#         return cache[n]
#     r = 0
#     for k in range(n):
#         r += catalan(k) * catalan(n-1-k)
#     cache[n] = r
#     return r


class Solution:
    # Runtime: 28 ms, faster than 81.59% of Python3 online submissions for Unique Binary Search Trees.
    # Memory Usage: 14.3 MB, less than 13.88% of Python3 online submissions for Unique Binary Search Trees.
    def numTrees(self, n: int) -> int:
        cache = {0:1}
        def catalan(n):
            if n in cache:
                return cache[n]
            r = 0
            for k in range(n):
                r += catalan(k) * catalan(n-1-k)
            cache[n] = r
            return r
        return catalan(n)

    def numTrees_wrong(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            for j in range(0, n-i):
                dp[i] += (dp[j] + dp[i-j-1])

        return dp[n-1]

s = Solution()
print(s.numTrees(1), 1)
print(s.numTrees(2), 2)
print(s.numTrees(3), 5)
print(s.numTrees(4), 14)
