# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]

# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Runtime: 128 ms, faster than 23.25% of Python3 online submissions for Majority Element II.
        # Memory Usage: 15.4 MB, less than 67.41% of Python3 online submissions for Majority Element II.
        stat = {}
        a1 = None
        a2 = None
        t1 = 0
        t2 = 0
        stage = None

        def stage2(num):
            nonlocal a1, a2, t2
            nonlocal stat
            if num == a1:
                return stage2

            if num in stat:
                stat[num] += 1
                c = stat[num]
            else:
                stat[num] = 1
                c = 1

            if c > t2:
                t2 = c
            if t2 > t:
                a2 = num
                return None
            return stage2

        def stage1(num):
            nonlocal a1, t1, t2
            nonlocal stat
            nonlocal stage
            nonlocal stage2

            if num in stat:
                stat[num] += 1
                c = stat[num]
            else:
                stat[num] = 1
                c = 1

            if c > t2:
                if c > t1:
                    t2 = t1
                    t1 = c
                else:
                    t2 = c
            if t1 > t:
                a1 = num
                return stage2
            return stage1

        stage = stage1

        t = len(nums) // 3

        for num in nums:
            stage = stage(num)
            if stage is None:
                break
        #     print(num, a1, a2, t1, t2)
        # print('---', t, nums)
        r = []
        if a1 is not None:
            r.append(a1)
            if a2 is not None:
                r.append(a2)
        return r

    def majorityElement_one(self, nums: List[int]) -> List[int]:
        # Runtime: 120 ms, faster than 48.42% of Python3 online submissions for Majority Element II.
        # Memory Usage: 15.6 MB, less than 27.51% of Python3 online submissions for Majority Element II.
        stat = {}
        a1 = None
        a2 = None
        t1 = 0
        t2 = 0
        stage = None

        t = len(nums) // 3

        for num in nums:
            if a1 is None:
                if num in stat:
                    stat[num] += 1
                    c = stat[num]
                else:
                    stat[num] = 1
                    c = 1

                if c > t2:
                    if c > t1:
                        t2 = t1
                        t1 = c
                    else:
                        t2 = c
                if t1 > t:
                    a1 = num
            else:
                if num == a1:
                    continue

                if num in stat:
                    stat[num] += 1
                    c = stat[num]
                else:
                    stat[num] = 1
                    c = 1

                if c > t2:
                    t2 = c
                if t2 > t:
                    a2 = num
                    break

        r = []
        if a1 is not None:
            r.append(a1)
            if a2 is not None:
                r.append(a2)
        return r
                        

s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([1,1,1,3,3,2,2,2]))
print(s.majorityElement([1,1,1,3,3,2,2,2,2]))
print(s.majorityElement([]))
print(s.majorityElement([1,1,1]))
print(s.majorityElement([1,2,3]))
print(s.majorityElement([2,2,2,2,2,2,2,21,1,1,3,9,9,3,2,2,2,2,32,21,43,54,65,89,76,1,2,3,4,5,6,7,8,9,0,2,2,2]))
