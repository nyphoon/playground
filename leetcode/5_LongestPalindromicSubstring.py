# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"
 
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),

def get_palindrome(s, l, r):
    p = s[l:r+1]
    while s[l] == s[r]:
        p = s[l:r+1]
        l -= 1
        r += 1
        if l < 0 or r >= len(s):
            break
    return p

class Solution:
    # Runtime: 1392 ms, faster than 44.52% of Python3 online submissions for Longest Palindromic Substring.
    # Memory Usage: 14.3 MB, less than 60.60% of Python3 online 
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                cand = get_palindrome(s, i, i+2)
                if len(cand) > len(ans):
                    ans = cand
            if s[i] == s[i+1]:
                cand = get_palindrome(s, i, i+1)
                if len(cand) > len(ans):
                    ans = cand

        if len(s) >= 2 and s[-1] == s[-2]:
            cand = s[-2:]
            if len(cand) > len(ans):
                ans = cand
        return ans
        
s = Solution()
print(s.longestPalindrome('babad'), 'bab/aba')
print(s.longestPalindrome('cbbd'), 'bb')
print(s.longestPalindrome('a'), 'a')
print(s.longestPalindrome('acc'), 'cc')
print(s.longestPalindrome('ccc'), 'ccc')
print(s.longestPalindrome('cccc'), 'cccc')
print(s.longestPalindrome('ccccc'), 'ccccc')
print(s.longestPalindrome('cccccca'), 'cccccc')
print(s.longestPalindrome('28a3773arterzfi8ifzehrwgg'), 'zfi8ifz')
