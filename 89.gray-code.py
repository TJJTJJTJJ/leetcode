#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (44.99%)
# Total Accepted:    130.6K
# Total Submissions: 287.8K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
# 
# Example 1:
# 
# 
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
# 
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 
# 
# Example 2:
# 
# 
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
# A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 =
# 1.
# Therefore, for n = 0 the gray code sequence is [0].
# 
# 
# method 1, 假设f(n-1)得到的是gray list[a,b,c]，那么对每个元素，以首尾加[0,1]或者[1,0]的顺序,即[0+a,1+a,1+b,0+b,0+c,1+c,1+d,0+d]
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         if n == 0:
#             return [0]
#         if n == 1:
#             return [0, 1]
#         res = list()
#         ad_val = 0
#         for val in self.grayCode(n-1):
#             if ad_val==0:
#                 res.extend([val, val+2**(n-1)])
#                 ad_val = (ad_val+1)%2
#             else:
#                 res.extend([val+2**(n-1), val])
#                 ad_val = (ad_val+1)%2
#         return res

# method 2
# 这个思路更奇特，对于f(n-1)=[a,b,c,d]，满足前半部分的首位为0，后半部分的首位为1，并且a,d和bc只是首位不一样
# part1是首位加0，即[0+a,0+b,0+c,0+d]，得到前半部分首位为0
# part2是前半部分首位和第二位加11，即[11+a, 11+b]，此时首位和第二位都为1
# part3是后半部分首位加1，即[1+c, 1+d]，此时首位和第二位也都为1
# 后半部分由part2和part3组成，首位为0
# 并且可以的简单的证明，
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         if n == 0:
#             return [0]
#         if n == 1:
#             return [0, 1]
#         part1 = self.grayCode(n-1)
#         part2 = [i + 3 * pow(2, n-2) for i in part1[:len(part1)//2]]
#         part3 = [i + pow(2, n-2) for i in part1[len(part1)//2:]]
#         return part1 + part2 + part3  

# method 3 graycode 又称格雷码，反正就是各种重要
# 格雷码有两种通用的构造方法
# 镜射排列：生成二进制格雷码方式2：n位元的格雷码可以从n-1位元的格雷码以上下镜射后加上新位元的方式快速的得到
# 二进制转换: G[i] = B[i]^B[i+1]，其中B[n]=0，即B和G的首位相同
# B[i]=G[i]^B[i+1]
# 可以证明，两个得到的graycode是一样的，证明太啰嗦，就不证明了，纯粹的硬推就行
# G[i] = B[i]^B[i+1] <==> G = B^(B>>1)
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [i^(i>>1) for i in range(2**n)]
        return res
# 镜面对称
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [2**i+x for x in res[::-1]]
        return res
