#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-08 12:15:53
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

#  

# 示例 1：

# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]
# 示例 2：

# 输入：nums = [10,26,30,31,47,60], target = 40
# 输出：[10,30] 或者 [30,10]
#  

# 限制：

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in nums:
#             if i < target - nums[-1]:
#                 continue
#             elif i < target/2:
#                 # if nums.index(target-i): return [i, target-i]
#                 try:
#                     nums.index(target-i)
#                     return [i, target-i]
#                 except: pass
#                 finally: pass
#             else:
#                 return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in nums:
#             if target - i in nums:
#                 return [i, target - i]

#         return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         l, r = 0, len(nums) - 1 # list长度的复杂度为O(1)

#         while l < r:
#             tmp = nums[l] + nums[r]
#             if tmp > target: r -= 1
#             elif tmp < target: l += 1
#             else: return [nums[l], nums[r]]

#         return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums = set(nums)

#         for i in nums:
#             if target - i in nums:
#                 return [i, target - i]

#         return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1 # list长度的复杂度为O(1)

        while l < r:
            while nums[l] + nums[r] > target: r -= 1
            while nums[l] + nums[r] < target: l += 1
            if nums[l] + nums[r] == target: return [nums[l], nums[r]]

        return []

if __name__ == '__main__':
    tt = Solution()
    tt.twoSum([45,46,67,73,74,74,77,83,89,98], 147)
    # tt.twoSum([2,7,11,15], 9)

