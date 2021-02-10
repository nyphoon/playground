from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sn = sorted(nums)
        for i in range(1, len(sn), 2):
            print('i',i)
            if sn[i] != sn[i-1]:
                print('i', sn[i], 'i-1', sn[i-1])
                return sn[i-1]
        print('last')
        return sn[-1]
s = Solution()
nums = [2,2,5,5,3,4,1,1,3]
print(s.singleNumber(nums))
