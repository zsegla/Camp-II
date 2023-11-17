# https://leetcode.com/problems/distinct-subsequences/



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev_subsequences = [1 for _ in range(len(s) + 1)]  
        for r in range(1, len(t) + 1):                        
            subsequences = [0 for _ in range(len(s) + 1)]

            for c in range(r, len(s) + 1):                    
                subsequences[c] = subsequences[c - 1]        
                if s[c - 1] == t[r - 1]:                     
                    subsequences[c] += prev_subsequences[c - 1]
            prev_subsequences = subsequences

        return prev_subsequences[-1]
