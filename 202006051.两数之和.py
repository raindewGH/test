#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-06-05 16:10:02
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

#  

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k, v in enumerate(nums):
            if target - v in nums[k+1:]:
                return [k, nums[k+1:].index(target - v)+k+1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for k, v in enumerate(nums):
            if target - v in sum_dict:
                return [sum_dict[target - v], k]
            sum_dict[v] = k
