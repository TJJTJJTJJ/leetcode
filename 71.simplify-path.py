#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (28.18%)
# Total Accepted:    144.7K
# Total Submissions: 510K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it. Or in other
# words, convert it to the canonical path.
# 
# In a UNIX-style file system, a period . refers to the current directory.
# Furthermore, a double period .. moves the directory up a level. For more
# information, see: Absolute path vs relative path in Linux/Unix
# 
# Note that the returned canonical path must always begin with a slash /, and
# there must be only a single slash / between two directory names. The last
# directory name (if it exists) must not end with a trailing /. Also, the
# canonical path must be the shortest string representing the absolute
# path.
# 
# 
# 
# Example 1:
# 
# 
# Input: "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory
# name.
# 
# 
# Example 2:
# 
# 
# Input: "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the
# root level is the highest level you can go.
# 
# 
# Example 3:
# 
# 
# Input: "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced
# by a single one.
# 
# 
# Example 4:
# 
# 
# Input: "/a/./b/../../c/"
# Output: "/c"
# 
# 
# Example 5:
# 
# 
# Input: "/a/../../b/../c//.//"
# Output: "/c"
# 
# 
# Example 6:
# 
# 
# Input: "/a//b////c/d//././/.."
# Output: "/a/b/c"
# 
# 
# method 1 利用split直接过滤'/'
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         import re
#         path_list = re.split(r'[/]', path)
#         stack = list()
#         for sub_path in path_list:
#             if sub_path == '':
#                 continue
#             stack.append('/')
#             if sub_path == '.':
#                 stack.pop()
#             elif sub_path == '..':
#                 stack.pop()
#                 if stack:
#                     stack.pop()
#                     stack.pop()
#             else:
#                 stack.append(sub_path)
#         if not stack:
#             stack.append('/')
#         res = ''.join(stack)
#         return res

# method 2 简化的 method 1
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         import re
#         path_list = re.split(r'[/]', path)
#         print(path_list)
#         stack = list()
#         for sub_path in path_list:
#             if sub_path == '..' and stack:
#                 stack.pop()
#             elif sub_path in ['', '.', '..']:
#                 continue
#             else:
#                 stack.append(sub_path)
#         print(stack)
#         if stack:
#             res = '/'+'/'.join(stack)
#         else:
#             res = '/'
#         return res
        
# method 3 继续简化 method 2
class Solution:
    def simplifyPath(self, path: str) -> str:
        import re
        stack = list()
        path_list = [ p  for p in re.split(r'/', path) if p not in ['', '.']]
        for sub_path in path_list:
            if sub_path=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(sub_path)
        res = '/'+'/'.join(stack)

        return res


