https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0        
        max_xor = 0    

        for bit in range(31, -1, -1):          

            mask |= (1 << bit)                 
            prefixes = {mask & num for num in nums}
            target = max_xor | (1 << bit)      

            for prefix in prefixes:             
                if prefix ^ target in prefixes:
                    max_xor = target
                    break

        return max_xor
