#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-07 11:09:20
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

# 示例:

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 

#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  

# 提示：

# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         return [max(nums[l:l+k]) for l in range(len(nums)-k+1)] if nums else []

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k <= 1: return nums # 特殊情况判断

        deque, res = [], [] # 初始化
        for v in nums[:k]: # 窗口初始位置
            while deque and deque[-1] < v: deque.pop()
            deque.append(v)
        res.append(deque[0])

        for i, v in enumerate(nums[k:]): # 窗口往后滑动
            if deque[0] == nums[i]: deque.pop(0)
            while deque and deque[-1] < v: deque.pop()
            deque.append(v)
            res.append(deque[0])

        return res

if __name__ == '__main__':
    tt = Solution()
    # tt.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    tt.maxSlidingWindow([7, 2, 4], 2)
