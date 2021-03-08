# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between 
# a letter in pattern and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false
 

# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lower-case English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        pl = len(pattern)
        w2c = {}
        for w in s.split():
            if i == pl:
                return False
            a = pattern[i]
            c = w2c.get(w)

            # print(i, w, a, c, w2c)

            if c == a:
                i += 1
                continue

            if c is None and a not in pattern[:i]:
                w2c[w] = a
                i += 1
                continue

            return False

        if i != pl:
            return False

        return True

# Runtime: 32 ms, faster than 56.46% of Python3 online submissions for Word Pattern.
# Memory Usage: 14.4 MB, less than 27.58% of Python3 online submissions 

s = Solution()
assert s.wordPattern('abba', 'dog cat cat dog') is True
assert s.wordPattern('aaaa', 'dog cat cat fish') is False
assert s.wordPattern('aaaa', 'dog cat cat dog') is False
assert s.wordPattern('abba', 'dog dog dog dog') is False

assert s.wordPattern('aaa', 'dog dog') is False
assert s.wordPattern('aaa', 'dog dog dog dog') is False
assert s.wordPattern('', '') is True
assert s.wordPattern('', 'dog dog dog dog') is False