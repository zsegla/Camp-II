# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/



class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        kth = 1
        k -= 1

        while k > 0:

            lower, upper = kth, kth + 1  
            count = 0

            while lower <= n: 
                count += min(upper, n + 1) - lower
                lower *= 10
                upper *= 10

            if count <= k:  # count numbers do not reach k
                k -= count  # use all count numbers
                kth += 1  # increment start point for next range
            else:
                k -= 1     # use kth
                kth *= 10  # next range start

        return kth
