#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 12:14:16
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

#  

# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

#  

# 示例 1:

# 输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
# 示例 2:

# 输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# f(n, m)：n个骰子，得到和m的情况数
# f(n, m) = f(n-1, m-1) + f(n-1, m-2) + f(n-1, m-3) + f(n-1, m-4) + f(n-1, m-5) + f(n-1, m-6)
# f(1, 1) = f(1, 2) = f(1, 3) = f(1, 4) = f(1, 5) = f(1, 6) = 1

class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [[0 for _ in range(n*6+1)] for _ in range(n+1)]
        for i in range(1, 7):
            dp[1][i] = 1
        for j in range(2, n+1):
            for k in range(j, j*6+1):
                for x in range(1, 7):
                    if k-x >= 1 and dp[j-1][k-x] != 0:
                        dp[j][k] = dp[j][k] + dp[j-1][k-x]
        return [dp[n][i] / 6**n for i in range(n, n*6+1)]

if __name__ == '__main__':
    test = Solution()


