# https://leetcode.com/problems/partition-equal-subset-sum/



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False

        nums.sort(reverse = True)               # try largest nums first
        target = sum_nums // 2

        subset_sum = [True] + [False] * target

        for num in nums:
            for i in range(target - 1, -1, -1): # backwards so cannot use same num repeatedly
                if subset_sum[i] and i + num <= target:
                    if i + num == target:       # early return, solution found
                        return True
                    subset_sum[i + num] = True  # mark this value

        return False
