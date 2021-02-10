# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# Example 1:

# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
# For the left two athletes, you just need to output their relative ranks according to their scores.
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.

from typing import List

class Solution:
    def findRelativeRanks_slow_heavy(self, nums: List[int]) -> List[str]:
        result = []
        scores = []
        winners = []
        for i in range(len(nums)):
            scores.append(0)
            winners.append([])

            c = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    c += 1
                    if j < i:
                        c += scores[j]
                        for w in winners[j]:
                            if nums[i] > nums[w]:
                                c += 1
                            else:
                                winners[i].append(w)
                        break
                if nums[i] < nums[j]:
                    winners[i].append(j)

            scores[i] = c

            rank = len(nums) - scores[i]
            if rank == 1:
                result.append('Gold Medal')
            elif rank == 2:
                result.append('Silver Medal')
            elif rank == 3:
                result.append('Bronze Medal')
            else:
                result.append(str(rank))

        # print(scores)
        # import pprint
        # pprint.pprint(winners)
        return result
# Runtime: 5896 ms, faster than 5.01% of Python3 online submissions for Relative Ranks.
# Memory Usage: 105.8 MB, less than 6.47% of Python3 online submissions for Relative Ranks.

    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        n = len(nums)
        rank = [0]
        for i in range(1,n):
            for j in range(len(rank)):
                if nums[rank[j]] < nums[i]:
                    rank.insert(j, i)
                    break
            if len(rank) == i:
                rank.append(i)

        result = [None] * n

        if n > 0:
            result[rank[0]] = 'Gold Medal'
        if n > 1:
            result[rank[1]] = 'Silver Medal'
        if n > 2:
            result[rank[2]] = 'Bronze Medal'
        if n > 3:
            for i in range(3,n):
                result[rank[i]] = str(i + 1)
        return result
# Runtime: 1364 ms, faster than 5.02% of Python3 online submissions for Relative Ranks.
# Memory Usage: 15 MB, less than 95.61% of Python3 online submissions for Relative Ranks.

s = Solution()
# print(s.findRelativeRanks([5, 4, 3, 2, 1]))
# print(s.findRelativeRanks([5]))
print(s.findRelativeRanks([5, 4, 3, 2, 1, 6 ,7, 8]))
