#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-06-05 18:20:30
# @Author  : raind (848299610@qq.com)
# @Link    : http://raind.cc
# @Version : $Id$

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '': return 0
        res = 1

        # 存储字符的最新位置
        char_dict = {}
        cur = -1

        for k, v in enumerate(s):
            if v in char_dict and res < k - char_dict[v]:
                res = k - char_dict[v]
                cur = k
            else:
                res = k - cur

            char_dict[v] = k

            print(res)

        return res

if __name__ == '__main__':
    tt = Solution()
    tt.lengthOfLongestSubstring("abcabcbb")
    # tt.twoSum([2,7,11,15], 9)

