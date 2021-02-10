# Given a list of non-overlapping axis-aligned rectangles rects, 
# write a function pick which randomly and uniformily picks an integer point 
# in the space covered by the rectangles.

# Note:

# An integer point is a point that has integer coordinates. 
# A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.

# Example 1:
# Input: 
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output: 
# [null,[4,1],[4,1],[3,3]]

# Example 2:
# Input: 
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output: 
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

# Explanation of Input Syntax:
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

from typing import List
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.node_num = 0
        self.section_idx = []
        for r in rects:
            n = (abs(r[2] - r[0]) + 1) * (abs(r[3] - r[1]) + 1)
            self.section_idx.append(self.node_num + n)
            self.node_num += n
        print(rects)
        print(self.section_idx)

    def get_rect(self, n):
        # print('get_rect', n)
        idx = self.section_idx

        def _search(l, r, n):
            # print(l, r)
            nonlocal idx
            if l == r:
                return l

            i = (l + r) // 2

            if idx[i] >= n:
                return _search(l, i, n)
            else:
                return _search(i+1, r, n)

        at = _search(0, len(idx)-1, n)
        return at
        

    def pick(self) -> List[int]:
        r = random.randint(1, self.node_num)
        print('pick', r)
        rect_idx = self.get_rect(r)
        if rect_idx > 0:
            r = r - self.section_idx[rect_idx-1]
        r -= 1
        print('at', rect_idx)
        rect = self.rects[rect_idx]
        width = abs(rect[2] - rect[0]) + 1
        return (rect[0] + (r % width),
                rect[1] + (r // width))

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# rects = [[1,1,5,5]]
rects = [[-2,-2,-1,-1],[3,0,3,0]]
# rects = [[-2,-2,-1,-1],[1,0,3,0]]
# rects = [[1,1,1,1]]

obj = Solution(rects)

# param_1 = obj.pick()
print('-----------')
print(obj.pick())
print('-----------')
print(obj.pick())
print('-----------')
print(obj.pick())
print('-----------')
print(obj.pick())
print('-----------')
print(obj.pick())
print('-----------')
print(obj.pick())

# Runtime: 200 ms, faster than 54.17% of Python3 online submissions for Random Point in Non-overlapping Rectangles.
# Memory Usage: 18.2 MB, less than 76.79% of Python3 online submissions for Random Point in Non-overlapping Rectangles.