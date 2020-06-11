#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-11 10:41:22
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

#  

# 示例 1：

# 输入：nums = [3,4,3,3]
# 输出：4
# 示例 2：

# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
#  

# 限制：

# 1 <= nums.length <= 10000
# 1 <= nums[i] < 2^31

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # counter = collections.Counter(nums)
        # return [item[0] for item in counter.items() if item[1] == 1][0]
        return collections.Counter(nums).most_common()[-1][0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3 - sum(nums))//2

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in nums:
            b = ~a&(b^i)
            a = ~b&(a^i)

        return b - 2**32 if b > 2**32 - 1 else b

