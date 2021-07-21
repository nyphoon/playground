# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true
 
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    # Runtime: 32 ms, faster than 63.89% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 14.2 MB, less than 62.43% of Python3 online submissions for Valid Parentheses.
    def isValid(self, s: str) -> bool:
        mapping = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []
        for c in s:
            if c in (']', '}', ')'):
                if len(stack) == 0 or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            if c in ('[', '{', '('):
                stack.append(c)
        return len(stack) == 0
        
s = Solution()
print(s.isValid('()'))
print(s.isValid('()[]{}'))
print(s.isValid('(]'))
print(s.isValid('([)]'))
print(s.isValid('{[]}'))

print(s.isValid(''))
