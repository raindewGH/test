#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 16:26:13
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

#  

# 示例 1：

# 输入: n = 3
# 输出: 6
# 示例 2：

# 输入: n = 9
# 输出: 45
#  

# 限制：

# 1 <= n <= 10000

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/qiu-12n-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def sumNums(self, n: int) -> int:
        # return n and n + self.sumNums(n-1)
        # return reduce(lambda x,y:x+y,range(1,n+1))
        return ((((n+1) & -(n>>0 & 1))<<0)
            +   (((n+1) & -(n>>1 & 1))<<1)
            +   (((n+1) & -(n>>2 & 1))<<2)
            +   (((n+1) & -(n>>3 & 1))<<3)
            +   (((n+1) & -(n>>4 & 1))<<4)
            +   (((n+1) & -(n>>5 & 1))<<5)
            +   (((n+1) & -(n>>6 & 1))<<6)
            +   (((n+1) & -(n>>7 & 1))<<7)
            +   (((n+1) & -(n>>8 & 1))<<8)
            +   (((n+1) & -(n>>9 & 1))<<9)
            +   (((n+1) & -(n>>10 & 1))<<10)
            +   (((n+1) & -(n>>11 & 1))<<11)
            +   (((n+1) & -(n>>12 & 1))<<12)
            +   (((n+1) & -(n>>13 & 1))<<13))>>1


