# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
from typing import List

class Solution:
    # Made Wrong Question: longestCommonSubstring
    def longestCommonPrefix_bad(self, strs: List[str]) -> str:
        ans = ''
        d = {}
        for s in strs:
            parts = set()
            for i in range(len(s)):
                l = len(s) - i
                for j in range(0, i+1):
                    # print(s[j:j+l])
                    part = s[j:j+l]
                    if part in parts:
                        continue
                    parts.add(part)

                    if part in d:
                        d[part] += 1
                        if len(strs) == d[part]:
                            if len(ans) < len(part):
                                ans = part
                    else:
                        d[part] = 1
        return ans

        
    def longestCommonPrefix_wrong(self, strs: List[str]) -> str:
        ac = {c: [] for c in 'abcdefghijklmnopqrstuvwxyz'} # alphabet count

        for i in range(len(strs)):
            for c in strs[i]:
                acl = len(ac[c])
                if acl == i:
                    ac[c].append(i)
        cs = []
        for k,v in ac.items():
            if len(v) == len(strs):
                cs.append(k)
        
        s = strs[0]
        cand = []
        for c in cs:
            h = s.find(c)
            for i in range(1, len(cs)):
                if s[h+i] not in cs:
                    break
            else:
                print(s[h:h+len(cs)])

    # Runtime: 36 ms, faster than 57.21% of Python3 online submissions for Longest Common Prefix.
    # Memory Usage: 14.2 MB, less than 93.46% of Python3 online submissions for Longest Common Prefix.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sample = strs[0]
        for i in range(len(sample)):
            c = sample[i]
            for s in strs[1:]:
                try:
                    if s[i] != c:
                        return s[:i]
                except IndexError:
                    return s[:i]
        return sample

        
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]), 'fl')
print(s.longestCommonPrefix(["dog","racecar","car"]), '""')
print(s.longestCommonPrefix(["dog","dooo","do"]), 'do')
print(s.longestCommonPrefix(["sax","saxxxfl","saxxxxxxaa"]), 'sax')
print(s.longestCommonPrefix(["a","a","a"]), 'a')