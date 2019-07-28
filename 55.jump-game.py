#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (31.37%)
# Total Accepted:    245.9K
# Total Submissions: 780.2K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# method 1
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         index_tf = dict()
#         nums_len = len(nums)
#         def canJump_index(index):
#             if index>=nums_len-1:
#                 return True
#             if nums[index]==0 or (not index_tf.get(index, True)):
#                 return False
#             for val in range(1, nums[index]+1):
#                 if not index_tf.get(index, True):
#                     return False
#                 if canJump_index(index+val):
#                     return True
#             index_pre = index
#             while index_pre>-1 and index-index_pre>=nums[index_pre]-nums[index]:
#                 index_tf[index_pre]=False
#                 index_pre-=1
#             return False
#         return canJump_index(0)

# method 2 先找到0
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         index_0 = [True]*len(nums)
#         for index, val in enumerate(nums):
#             if val == 0 and index != (len(nums)-1):
#                 index_0[index]=False
#         index = 0
#         while index_0[0] and index<len(index_0):
#             if not index_0[index]:
#                 index_pre = index-1
#                 while index_pre>-1 and index-index_pre>=nums[index_pre]-nums[index]:
#                     index_0[index_pre]=False
#                     index_pre-=1
#             index+=1 
#         return index_0[0]

# method 3 牛客网的一个线性方法，牛逼牛逼，需要分析下思路
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        index = 0
        while index<=reach and index<len(nums):
            reach = max(index+nums[index], reach)
            index+=1
        res = reach>=(len(nums)-1)
        return res
# 是否能跳出去关键不在于找到这样一条路径，而是是否会陷在陷阱里。
# 陷阱的判断：一个是找到0然后向前判断，但是需要进行二次判断
# 第二种方法就是网友的这种方法，直接向前走，记录从index=0以最大步伐开始走可以抵达的最远位置
# 看看最大步伐能否陷入陷阱中，如果最大步伐落入陷阱中，那么其他路径肯定落入陷阱中

# method 4 牛客网的solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i]>=lastPos:
                lastPos = i
        return lastPos==0
# 这个方法从后往前遍历，因为不陷入陷阱具有传递性，即如果当前位置j不陷入陷阱，那么位置i(i可以达到j)也不陷入陷阱
# 此时对于i而言，需要判断i+1, i+2, ..., i+nums[i]中如果有一个成功T，那么i就是成功T的
# 原则上讲，需要判断nums[i]次，但是实际上并不需要，因为只是想知道T是否在这些范围内，而不需要知道T具体的位置
# 所以可以用last_T记录i+1，i+2, ...中T出现的最左边的位置，用于判断即可。

