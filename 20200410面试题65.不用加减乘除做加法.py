#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 13:09:09
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

#  

# 示例:

# 输入: a = 1, b = 1
# 输出: 2
#  

# 提示：

# a, b 均可能是负数或 0
# 结果不会溢出 32 位整数

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def add(self, a: int, b: int) -> int:
        return (a if a <= 0x7fffffff else -((a - 1) ^ 0xffffffff)) if b == 0 else self.add((a^b) & 0xffffffff, ((a&b)<<1) & 0xffffffff)
