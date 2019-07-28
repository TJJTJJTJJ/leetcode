#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (34.90%)
# Total Accepted:    321.9K
# Total Submissions: 915.5K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# method 1 对区间排序，然后进行合并，如果end>start,则合并
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals = sorted(intervals, key=lambda x:x.start)
        new_intervals = list()
        for val in intervals:
            if not new_intervals or new_intervals[-1].end < val.start:
                new_intervals.append(val)
            else:
                new_intervals[-1].end=max(new_intervals[-1].end, val.end)
        return new_intervals

# method 2 直接对start和end进行排序，思路是最后的结果中，前一个的end一定小于后一个的start
# 算法复杂度差不多，难以证明正确性，
# 我们换个角度，实际上，对于[1,4],[2,3]和[1,3],[2,4]两种区间合并后没有区别，原因是start=[1,2],end=[3,4]
# 画在坐标轴上就是 . .  * *，这个点与星的匹配不重要，而是顺序比较重要，可以转化成第一个点和第一个星匹配
# 第二个点和第二个星匹配，那么从前到后依次遍历，j记录新区间的开始，i记录新区间的结束，所以i应该满足start[i+1]>end[i]



