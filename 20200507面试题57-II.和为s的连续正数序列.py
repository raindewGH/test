#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-07 18:11:35
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

#  

# 示例 1：

# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：

# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  

# 限制：

# 1 <= target <= 10^5

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target in (1, 2, 4): return [] # 特殊情况
        if target == 3: return [[1, 2]] # 特殊情况
        if target == 5: return [[2, 3]] # 特殊情况

        res = [] # 存储结果
        n = 3 # 连续序列的最大值
        l = [1, 2, 3] # 连续序列
        s = 6 # 连续序列的和

        while n*2 <= target + 1:
            if s == target: # 匹配序列后，减少一个增加一个
                res.append(l.copy())
                s -= l.pop(0)
                n += 1; l.append(n); s += n
            elif s < target: # 小于目标值，增加一个
                n += 1; l.append(n); s += n
            else: # 大于目标值，减少一个
                s -= l.pop(0)

        return res

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = [] # 存储结果

        for y in range(2, target//2+2):
            x = (y**2 + y - target*2 + 0.25)**(0.5) + 0.5
            if type(x) != complex and x - int(x) == 0:
                res.append(list(range(int(x), y+1)))

        return res


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, res = 1, [] # 存储结果

        while (i/2 + 1)*(i + 1) <= target:
            if not (target - i*(i+1)/2)%(i+1):
                x = int((target - i*(i+1)/2)/(i+1))
                res.append(list(range(x, x+i+1)))
            i += 1

        return res[::-1]









