# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        p = ''
        for c in s:
            i = p.rfind(c)
            if i == -1:
                p += c
            else:
                p = p[i+1:] + c
            m = max(len(p), m)

        return m
        

s = Solution()
assert s.lengthOfLongestSubstring('abcabcbb') == 3
assert s.lengthOfLongestSubstring('bbbbb') == 1
assert s.lengthOfLongestSubstring('pwwkew') == 3
assert s.lengthOfLongestSubstring('') == 0
assert s.lengthOfLongestSubstring('pwwkeww') == 3
assert s.lengthOfLongestSubstring('dvdf') == 3
assert s.lengthOfLongestSubstring("aabaab!bb") == 3

# Runtime: 60 ms, faster than 78.07% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.5 MB, less than 27.19% of Python3 online submissions for Longest Substring Without Repeating Characters.