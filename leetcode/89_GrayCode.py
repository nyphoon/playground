# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given an integer n representing the total number of bits in the code, return any sequence of gray code.
#
# A gray code sequence must begin with 0.
#
# Example 1:
# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# [0,2,3,1] is also a valid gray code sequence.
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
# Example 2:
# Input: n = 1
# Output: [0,1]
#
# Constraints:
# 1 <= n <= 16

# code_seq(16) ---> 0.71s user 0.03s system 95% cpu 0.769 total
class BitMachineOld:
    def __init__(self, n):
        self.count = 0
        self.expand = 2 ** (n-1)
        self.repeat = 2 ** n
    
    def step(self):
        # print('-----', self.expand, self.repeat, self.count)
        inv = self.count // self.repeat % 2
        m = self.count % self.repeat
        inv2 = 1 if m >= self.expand else 0
        self.count += 1
        return (0, 1, 0)[inv + inv2]


# code_seq(16) --->  0.73s user 0.02s system 98% cpu 0.765 total
class BitMachine:
    def __init__(self, n):
        self.count = 0
        self.n = n
        self.expand = 2 ** (n-1)
        self.repeat = self.expand * 2
    
    def step(self):
        # print('-----', self.expand, self.repeat, self.count)
        inv = ( self.count // self.repeat ) & 1

        if self.count % self.repeat >= self.expand:
            inv = ~inv & 1

        self.count += 1
        return inv

# bm = BitMachine(3)
# print(bm.step())
# print(bm.step())
# print(bm.step())
# print(bm.step())
# print(bm.step())
# print(bm.step())
# print(bm.step())
# print(bm.step())

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        machines = [BitMachine(i) for i in range(1, n+1)]
        for _ in range(2**n):
            number = 0
            for i,m in enumerate(machines):
                b = m.step()
                number |= b<<i
            # print('{0:080b}'.format(number), number)
            result.append(number)
        return result

s = Solution()
# print(s.grayCode(16))
# print(s.grayCode(10))
print(s.grayCode(5))


# Runtime: 1172 ms, faster than 5.15% of Python3 online submissions for Gray Code.
# Memory Usage: 21.7 MB, less than 11.17% of Python3 online submissions for Gray Code.