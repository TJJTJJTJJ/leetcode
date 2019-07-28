#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (30.77%)
# Total Accepted:    135.4K
# Total Submissions: 434.9K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
# method 1 作者这里是在末尾加入了第四个句号，形成了一个闭环，
# 比自己一开始想到的三个句号就判断结束的情况简洁了很多
# 并且用s作为断点开始结束，比自己用i,j要更简单很多
# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         if len(s)>12 or len(s)<4:
#             return []
#         res = list()
        
#         def dfs(index, path, s):
#             if index == 4:
#                 if not s:
#                     res.append(path[:-1])
#                 return None
#             if len(s)>=1:
#                 dfs(index+1, path+s[:1]+'.', s[1:])    
#             if len(s)>=2 and s[0]!='0':
#                 dfs(index+1, path+s[:2]+'.', s[2:])
#             if len(s)>=3 and s[0]!='0' and int(s[:3])<=255:
#                 dfs(index+1, path+s[:3]+'.', s[3:])
#         dfs(0, '', s)
#         return res

# method 2 相比用递归的method1，是简单粗暴的循环
# class Solution:
#   def restoreIpAddresses(self, s):
#     ret = []
#     for a in range(1, 4):
#       for b in range(1, 4):
#         for c in range(1, 4):
#           d = len(s) - a - b - c
#           """
#           Last number must use all remaining digits. Check;
#           1. The size of the last number is valid
#           2. Every number uses 1 digit for 0 and is less than 255 if using 3 digits
#           """
#           if (1 <= d <= 3 and
#             (1 == a or '0' != s[0        ]) and (a != 3 or s[         :a        ] <= "255") and
#             (1 == b or '0' != s[a        ]) and (b != 3 or s[a        :a + b    ] <= "255") and
#             (1 == c or '0' != s[a + b    ]) and (c != 3 or s[a + b    :a + b + c] <= "255") and
#             (1 == d or '0' != s[a + b + c]) and (d != 3 or s[a + b + c:         ] <= "255")):
#             ret.append('.'.join([s[0:a], s[a:a + b], s[a + b:a + b + c], s[a + b + c:]]))
#     return ret

class Solution:
  def restoreIpAddresses(self, s):
    ret = []
    for a in range(1, 4):
      for b in range(1, 4):
        for c in range(1, 4):
          d = len(s) - a - b - c
          """
          Last number must use all remaining digits. Check;
          1. The size of the last number is valid
          2. Every number uses 1 digit for 0 and is less than 255 if using 3 digits
          """
          if (1 <= d <= 3 and
            (1 == a or ('0' != s[0        ] and int(s[         :a        ]) <= 255)) and
            (1 == b or ('0' != s[a        ] and int(s[a        :a + b    ]) <= 255)) and
            (1 == c or ('0' != s[a + b    ] and int(s[a + b    :a + b + c]) <= 255)) and
            (1 == d or ('0' != s[a + b + c] and int(s[a + b + c:         ]) <= 255)))  :
            ret.append('.'.join([s[0:a], s[a:a + b], s[a + b:a + b + c], s[a + b + c:]]))
    return ret

