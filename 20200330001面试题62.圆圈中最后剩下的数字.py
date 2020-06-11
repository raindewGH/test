#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-30 21:34:34
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

#  

# 示例 1：

# 输入: n = 5, m = 3
# 输出: 3
# 示例 2：

# 输入: n = 10, m = 17
# 输出: 2
#  

# 限制：

# 1 <= n <= 10^5
# 1 <= m <= 10^6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 直接计算法，超时
# class Solution:
    # def lastRemaining(self, n: int, m: int) -> int:
    #     r = list(range(0, n))
    #     l = []
    #     while len(r) > 1:
    #         l = l + r * (((m - len(l) - 1) // len(r)) + 1)
    #         print(l)

    #         i = l[m-1]
    #         print(i)
    #         r.remove(i)
    #         l = l[m:]

    #     return r[0]

# 数学公式法，推测下标
# 下标：0 1 2 3 4 
# 数据：
#      0 1 2 3 4 
#      3 4 0 1
#      1 3 4
#      1 3
#      3
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        p = 0;
        for i in range(2, n+1):
            p = (p+m) % i

        return p

if __name__ == '__main__':
    test = Solution()



